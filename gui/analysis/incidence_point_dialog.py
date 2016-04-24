# -*- coding: utf-8 -*-
"""
/***************************************************************************

                                 GeoHealth
                                 A QGIS plugin

                              -------------------
        begin                : 2014-08-20
        copyright            : (C) 2014 by Etienne Trimaille
        email                : etienne@trimaille.eu
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

from GeoHealth.ui.analysis.incidence_with_point import Ui_IncidencePoint
from GeoHealth.gui.analysis.parent_incidence_density_dialog import IncidenceDensityDialog


class IncidencePointDialog(IncidenceDensityDialog, Ui_IncidencePoint):
    def __init__(self, parent=None):
        """Constructor."""
        IncidenceDensityDialog.__init__(self, parent)
        # noinspection PyArgumentList
        Ui_IncidencePoint.setupUi(self, self)

        self.use_area = False
        self.use_point_layer = True

        self.setup_ui()

    def run_stats(self):
        """Main function which do the process."""
        IncidenceDensityDialog.run_stats(self)
