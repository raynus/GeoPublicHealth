# coding=utf-8

from builtins import object
from abc import ABCMeta, abstractmethod
from qgis.core import QgsRasterLayer, QgsVectorLayer, Qgis
from GeoPublicHealth.src.core.tools import tr
from future.utils import with_metaclass


class DataStore(with_metaclass(ABCMeta, object)):
    """
    DataStore

    .. versionadded:: 4.0
    """

    def __init__(self, uri):
        """
        Constructor for the DataStore.

        The datastore can be used in three different ways :
        - a PostGIS connection
        - a folder to store a shapefile
        - a geopackage file.

        We may add more datastores in the future.

        In a datastore, we should be able to save many layers.

        :param uri: The URI using a QFileInfo, QgsDataSourceURI or the path.
        :type uri: QDir, QFileInfo, QgsDataSourceURI, str

        .. versionadded:: 4.0
        """
        self._uri = uri
        self._index = 1
        self._use_index = False

    @property
    def use_index(self):
        """Return if we use an index to add the layer name.

        :return: If we use an index.
        :rtype: bool
        """
        return self._use_index

    @use_index.setter
    def use_index(self, index):
        """Setter if we use an index when we add a layer to the datastore.

        :param index: A boolean if we use an index.
        :type index: bool
        """
        self._use_index = index

    @property
    def uri(self):
        """Return the URI of the datastore. It's not a layer URI.

        :return: The URI.
        :rtype: QgsDataSourceURI, str

        .. versionadded:: 4.0
        """
        return self._uri

    def add_layer(self, layer, layer_name):
        """Add a layer to the datastore.

        :param layer: The layer to add.
        :type layer: QgsMapLayer

        :param layer_name: The name of the layer in the datastore.
        :type layer_name: str

        :returns: A two-tuple. The first element will be True if we could add
            the layer to the datastore. The second element will be the layer
            name which has been used or the error message.
        :rtype: (bool, str)

        .. versionadded:: 4.0
        """
        if self._use_index:
            layer_name = '%s-%s' % (self._index, layer_name)
            self._index += 1

        if self.layer_uri(layer_name):
            return False, tr('The layer already exists in the datastore.')

        if isinstance(layer, QgsRasterLayer):
            result = self._add_raster_layer(layer, layer_name)
        else:
            if layer.wkbType() == Qgis.WKBNoGeometry:
                result = self._add_tabular_layer(layer, layer_name)
            else:
                result = self._add_vector_layer(layer, layer_name)

        return result

    def layer(self, layer_name):
        """Get QGIS layer.

        :param layer_name: The name of the layer to fetch.
        :type layer_name: str

        :return: The QGIS layer.
        :rtype: QgsMapLayer

        .. versionadded:: 4.0
        """
        uri = self.layer_uri(layer_name)
        layer = QgsVectorLayer(uri, layer_name, 'ogr')
        if not layer.isValid():
            layer = QgsRasterLayer(uri, layer_name)
            if not layer.isValid():
                return False

        return layer

    @abstractmethod
    def is_writable(self):
        """Check if the URI is writable.

        :return: If it's writable or not.
        :rtype: bool

        .. versionadded:: 4.0
        """
        raise NotImplementedError

    @abstractmethod
    def supports_rasters(self):
        """Check if we can support raster in the datastore.

        :return: If it's writable or not.
        :rtype: bool

        .. versionadded:: 4.0
        """
        raise NotImplementedError

    @abstractmethod
    def layers(self):
        """Return a list of layers available.

        :return: List of layers available in the datastore.
        :rtype: list

        .. versionadded:: 4.0
        """
        raise NotImplementedError

    @abstractmethod
    def layer_uri(self, layer_name):
        """Get layer URI.

        :param layer_name: The name of the layer to fetch.
        :type layer_name: str

        :return: The URI of the layer.
        :rtype: QgsDataSourceURI, str

        .. versionadded:: 4.0
        """
        raise NotImplementedError

    @abstractmethod
    def _add_raster_layer(self, raster_layer, layer_name):
        """Add a raster layer to the database.

        :param raster_layer: The layer to add.
        :type raster_layer: QgsVectorLayer

        :param layer_name: The name of the layer in the datastore.
        :type layer_name: str

        :returns: A two-tuple. The first element will be True if we could add
            the layer to the datastore. The second element will be the layer
            name which has been used or the error message.
        :rtype: (bool, str)

        .. versionadded:: 4.0
        """
        raise NotImplementedError

    @abstractmethod
    def _add_vector_layer(self, vector_layer, layer_name):
        """Add a vector layer to the database.

        :param vector_layer: The layer to add.
        :type vector_layer: QgsVectorLayer

        :param layer_name: The name of the layer in the datastore.
        :type layer_name: str

        :returns: A two-tuple. The first element will be True if we could add
            the layer to the datastore. The second element will be the layer
            name which has been used or the error message.
        :rtype: (bool, str)

        .. versionadded:: 4.0
        """
        raise NotImplementedError

    @abstractmethod
    def _add_tabular_layer(self, tabular_layer, layer_name):
        """Add a vector layer to the database.

        :param tabular_layer: The layer to add.
        :type tabular_layer: QgsVectorLayer

        :param layer_name: The name of the layer in the datastore.
        :type layer_name: str

        :returns: A two-tuple. The first element will be True if we could add
            the layer to the datastore. The second element will be the layer
            name which has been used or the error message.
        :rtype: (bool, str)

        .. versionadded:: 4.0
        """
        raise NotImplementedError
