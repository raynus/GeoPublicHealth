# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'density.ui'
#
# Created: Wed Oct 21 14:51:30 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Density(object):
    def setupUi(self, Density):
        Density.setObjectName(_fromUtf8("Density"))
        Density.resize(651, 748)
        self.verticalLayout = QtGui.QVBoxLayout(Density)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.messageBar = gui.QgsMessageBar(Density)
        self.messageBar.setObjectName(_fromUtf8("messageBar"))
        self.verticalLayout.addWidget(self.messageBar)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_4 = QtGui.QLabel(Density)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_4)
        self.comboBox_incidence_pointLayer = QtGui.QComboBox(Density)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_incidence_pointLayer.sizePolicy().hasHeightForWidth())
        self.comboBox_incidence_pointLayer.setSizePolicy(sizePolicy)
        self.comboBox_incidence_pointLayer.setObjectName(_fromUtf8("comboBox_incidence_pointLayer"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.comboBox_incidence_pointLayer)
        self.label = QtGui.QLabel(Density)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label)
        self.comboBox_incidence_adminLayer = QtGui.QComboBox(Density)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_incidence_adminLayer.sizePolicy().hasHeightForWidth())
        self.comboBox_incidence_adminLayer.setSizePolicy(sizePolicy)
        self.comboBox_incidence_adminLayer.setObjectName(_fromUtf8("comboBox_incidence_adminLayer"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.comboBox_incidence_adminLayer)
        self.label_3 = QtGui.QLabel(Density)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_incidence_columnName = QtGui.QLineEdit(Density)
        self.lineEdit_incidence_columnName.setText(_fromUtf8("density"))
        self.lineEdit_incidence_columnName.setObjectName(_fromUtf8("lineEdit_incidence_columnName"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.lineEdit_incidence_columnName)
        self.label_2 = QtGui.QLabel(Density)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_2)
        self.comboBox_incidence_ratio = QtGui.QComboBox(Density)
        self.comboBox_incidence_ratio.setEditable(True)
        self.comboBox_incidence_ratio.setObjectName(_fromUtf8("comboBox_incidence_ratio"))
        self.comboBox_incidence_ratio.addItem(_fromUtf8(""))
        self.comboBox_incidence_ratio.addItem(_fromUtf8(""))
        self.comboBox_incidence_ratio.addItem(_fromUtf8(""))
        self.comboBox_incidence_ratio.addItem(_fromUtf8(""))
        self.comboBox_incidence_ratio.addItem(_fromUtf8(""))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.comboBox_incidence_ratio)
        self.checkBox_addNbIntersections = QtGui.QCheckBox(Density)
        self.checkBox_addNbIntersections.setObjectName(_fromUtf8("checkBox_addNbIntersections"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.checkBox_addNbIntersections)
        self.label_7 = QtGui.QLabel(Density)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.LabelRole, self.label_7)
        self.label_8 = QtGui.QLabel(Density)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.FieldRole, self.label_8)
        self.checkBox_incidence_runStats = QtGui.QCheckBox(Density)
        self.checkBox_incidence_runStats.setChecked(True)
        self.checkBox_incidence_runStats.setObjectName(_fromUtf8("checkBox_incidence_runStats"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.checkBox_incidence_runStats)
        self.verticalLayout.addLayout(self.formLayout)
        self.symbology = gui.QgsCollapsibleGroupBox(Density)
        self.symbology.setCheckable(True)
        self.symbology.setCollapsed(False)
        self.symbology.setObjectName(_fromUtf8("symbology"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.symbology)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_9 = QtGui.QLabel(self.symbology)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_3.addWidget(self.label_9)
        self.color_low_value = gui.QgsColorButtonV2(self.symbology)
        self.color_low_value.setColor(QtGui.QColor(255, 246, 246))
        self.color_low_value.setObjectName(_fromUtf8("color_low_value"))
        self.horizontalLayout_3.addWidget(self.color_low_value)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.label_10 = QtGui.QLabel(self.symbology)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout_3.addWidget(self.label_10)
        self.color_high_value = gui.QgsColorButtonV2(self.symbology)
        self.color_high_value.setColor(QtGui.QColor(202, 33, 36))
        self.color_high_value.setObjectName(_fromUtf8("color_high_value"))
        self.horizontalLayout_3.addWidget(self.color_high_value)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_11 = QtGui.QLabel(self.symbology)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout_4.addWidget(self.label_11)
        self.spinBox_classes = QtGui.QSpinBox(self.symbology)
        self.spinBox_classes.setMinimum(1)
        self.spinBox_classes.setProperty("value", 5)
        self.spinBox_classes.setObjectName(_fromUtf8("spinBox_classes"))
        self.horizontalLayout_4.addWidget(self.spinBox_classes)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.label_12 = QtGui.QLabel(self.symbology)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.horizontalLayout_4.addWidget(self.label_12)
        self.cbx_mode = QtGui.QComboBox(self.symbology)
        self.cbx_mode.setObjectName(_fromUtf8("cbx_mode"))
        self.horizontalLayout_4.addWidget(self.cbx_mode)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.verticalLayout.addWidget(self.symbology)
        self.button_box_ok = QtGui.QDialogButtonBox(Density)
        self.button_box_ok.setOrientation(QtCore.Qt.Horizontal)
        self.button_box_ok.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.button_box_ok.setObjectName(_fromUtf8("button_box_ok"))
        self.verticalLayout.addWidget(self.button_box_ok)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.tableWidget = QtGui.QTableWidget(Density)
        self.tableWidget.setMinimumSize(QtCore.QSize(200, 0))
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.verticalHeader().setVisible(False)
        self.horizontalLayout_2.addWidget(self.tableWidget)
        self.layout_plot = QtGui.QVBoxLayout()
        self.layout_plot.setObjectName(_fromUtf8("layout_plot"))
        self.horizontalLayout_2.addLayout(self.layout_plot)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Density)
        self.comboBox_incidence_ratio.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(Density)

    def retranslateUi(self, Density):
        Density.setWindowTitle(_translate("Density", "Density", None))
        self.label_4.setText(_translate("Density", "Case layer", None))
        self.label.setText(_translate("Density", "Layer for aggregation", None))
        self.label_3.setText(_translate("Density", "New column", None))
        self.label_2.setText(_translate("Density", "Ratio", None))
        self.comboBox_incidence_ratio.setItemText(0, _translate("Density", "10", None))
        self.comboBox_incidence_ratio.setItemText(1, _translate("Density", "100", None))
        self.comboBox_incidence_ratio.setItemText(2, _translate("Density", "1 000", None))
        self.comboBox_incidence_ratio.setItemText(3, _translate("Density", "10 000", None))
        self.comboBox_incidence_ratio.setItemText(4, _translate("Density", "100 000", None))
        self.checkBox_addNbIntersections.setToolTip(_translate("Density", "Add the number of cases per unit to the attribute table", None))
        self.checkBox_addNbIntersections.setText(_translate("Density", "Add the number of cases per unit to the attribute table", None))
        self.label_7.setText(_translate("Density", "<html><head/><body><p><span style=\" font-style:italic;\">Density =</span></p></body></html>", None))
        self.label_8.setText(_translate("Density", "<html><head/><body><p><span style=\" font-style:italic;\">number of cases / area * ratio</span></p></body></html>", None))
        self.checkBox_incidence_runStats.setText(_translate("Density", "Calculate statistics", None))
        self.symbology.setTitle(_translate("Density", "Add a symbology", None))
        self.label_9.setText(_translate("Density", "Low incidence", None))
        self.label_10.setText(_translate("Density", "High incidence", None))
        self.label_11.setText(_translate("Density", "Classes", None))
        self.label_12.setText(_translate("Density", "Mode", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Density", "Parameter", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Density", "Value", None))

from qgis import gui
