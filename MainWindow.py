# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(1028, 782)
        self.gridLayout = QtWidgets.QGridLayout(mainWindow)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox_3 = QtWidgets.QGroupBox(mainWindow)
        self.groupBox_3.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.open_btn = QtWidgets.QPushButton(self.groupBox_3)
        self.open_btn.setObjectName("open_btn")
        self.horizontalLayout.addWidget(self.open_btn)
        self.save_btn = QtWidgets.QPushButton(self.groupBox_3)
        self.save_btn.setObjectName("save_btn")
        self.horizontalLayout.addWidget(self.save_btn)
        self.gridLayout_6.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.name_checkBox = QtWidgets.QCheckBox(self.groupBox_3)
        self.name_checkBox.setChecked(True)
        self.name_checkBox.setObjectName("name_checkBox")
        self.gridLayout_4.addWidget(self.name_checkBox, 0, 0, 1, 1)
        self.size_checkBox = QtWidgets.QCheckBox(self.groupBox_3)
        self.size_checkBox.setObjectName("size_checkBox")
        self.gridLayout_4.addWidget(self.size_checkBox, 1, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_4.addWidget(self.lineEdit, 0, 2, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_3, 1, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(mainWindow)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout_5.addWidget(self.label_3, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setObjectName("label")
        self.gridLayout_5.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout_5.addWidget(self.label_2, 2, 0, 1, 1)
        self.wdith_spinBox = QtWidgets.QSpinBox(self.groupBox_2)
        self.wdith_spinBox.setMaximum(9999999)
        self.wdith_spinBox.setProperty("value", 512)
        self.wdith_spinBox.setObjectName("wdith_spinBox")
        self.gridLayout_5.addWidget(self.wdith_spinBox, 0, 1, 1, 1)
        self.height_spinBox = QtWidgets.QSpinBox(self.groupBox_2)
        self.height_spinBox.setMaximum(999999)
        self.height_spinBox.setProperty("value", 1024)
        self.height_spinBox.setObjectName("height_spinBox")
        self.gridLayout_5.addWidget(self.height_spinBox, 2, 1, 1, 1)
        self.frame_spixBox = QtWidgets.QSpinBox(self.groupBox_2)
        self.frame_spixBox.setMaximum(999999)
        self.frame_spixBox.setProperty("value", 1)
        self.frame_spixBox.setObjectName("frame_spixBox")
        self.gridLayout_5.addWidget(self.frame_spixBox, 3, 1, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_2, 0, 0, 1, 3)
        self.convert_btn = QtWidgets.QPushButton(self.groupBox)
        self.convert_btn.setObjectName("convert_btn")
        self.gridLayout_3.addWidget(self.convert_btn, 1, 2, 1, 1)
        self.file_btn = QtWidgets.QPushButton(self.groupBox)
        self.file_btn.setObjectName("file_btn")
        self.gridLayout_3.addWidget(self.file_btn, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "OctTool"))
        self.groupBox_3.setTitle(_translate("mainWindow", "copy file"))
        self.open_btn.setText(_translate("mainWindow", "open"))
        self.save_btn.setText(_translate("mainWindow", "save"))
        self.name_checkBox.setText(_translate("mainWindow", "select by name"))
        self.size_checkBox.setText(_translate("mainWindow", "select by file size"))
        self.groupBox.setTitle(_translate("mainWindow", "convert bin to image"))
        self.groupBox_2.setTitle(_translate("mainWindow", "custom size"))
        self.label_3.setText(_translate("mainWindow", "frame:"))
        self.label.setText(_translate("mainWindow", "width:"))
        self.label_2.setText(_translate("mainWindow", "height:"))
        self.convert_btn.setText(_translate("mainWindow", "convert"))
        self.file_btn.setText(_translate("mainWindow", "file"))
