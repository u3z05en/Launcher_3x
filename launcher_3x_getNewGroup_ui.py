# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'launcher_3x_getNewGroup.ui'
#
# Created: Sat May 11 19:03:48 2013
#      by: PyQt4 UI code generator 4.9.6
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

class Ui_getNewGroup(object):
    def setupUi(self, getNewGroup):
        getNewGroup.setObjectName(_fromUtf8("getNewGroup"))
        getNewGroup.resize(188, 381)
        getNewGroup.setMaximumSize(QtCore.QSize(188, 16777215))
        self.gridLayout = QtGui.QGridLayout(getNewGroup)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.button_cancel = QtGui.QPushButton(getNewGroup)
        self.button_cancel.setObjectName(_fromUtf8("button_cancel"))
        self.gridLayout.addWidget(self.button_cancel, 2, 2, 1, 1)
        self.button_ok = QtGui.QPushButton(getNewGroup)
        self.button_ok.setObjectName(_fromUtf8("button_ok"))
        self.gridLayout.addWidget(self.button_ok, 2, 1, 1, 1)
        self.label = QtGui.QLabel(getNewGroup)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        self.treeWidget_groups = QtGui.QTreeWidget(getNewGroup)
        self.treeWidget_groups.setObjectName(_fromUtf8("treeWidget_groups"))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(10)
        self.treeWidget_groups.headerItem().setFont(0, font)
        self.gridLayout.addWidget(self.treeWidget_groups, 1, 0, 1, 3)

        self.retranslateUi(getNewGroup)
        QtCore.QMetaObject.connectSlotsByName(getNewGroup)
        getNewGroup.setTabOrder(self.button_ok, self.button_cancel)

    def retranslateUi(self, getNewGroup):
        getNewGroup.setWindowTitle(_translate("getNewGroup", "Copy to Group", None))
        self.button_cancel.setText(_translate("getNewGroup", "Cancel", None))
        self.button_ok.setText(_translate("getNewGroup", "Copy", None))
        self.label.setText(_translate("getNewGroup", "<html><head/><body><p><span style=\" font-size:10pt;\">Which group am I copying to?</span></p></body></html>", None))
        self.treeWidget_groups.headerItem().setText(0, _translate("getNewGroup", "Groups", None))


class getNewGroup(QtGui.QWidget, Ui_getNewGroup):
    def __init__(self, parent=None, f=QtCore.Qt.WindowFlags()):
        QtGui.QWidget.__init__(self, parent, f)

        self.setupUi(self)

