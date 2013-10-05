# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'launcher_3x_changelog.ui'
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

class Ui_changeLog(object):
    def setupUi(self, changeLog):
        changeLog.setObjectName(_fromUtf8("changeLog"))
        changeLog.setWindowModality(QtCore.Qt.WindowModal)
        changeLog.setEnabled(True)
        changeLog.resize(614, 597)
        changeLog.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        changeLog.setMouseTracking(True)
        changeLog.setFocusPolicy(QtCore.Qt.StrongFocus)
        changeLog.setSizeGripEnabled(True)
        changeLog.setModal(True)
        self.gridLayout = QtGui.QGridLayout(changeLog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.textEdit = QtGui.QTextEdit(changeLog)
        self.textEdit.setMouseTracking(True)
        self.textEdit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.textEdit.setAcceptDrops(False)
        self.textEdit.setUndoRedoEnabled(False)
        self.textEdit.setReadOnly(True)
        self.textEdit.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.gridLayout.addWidget(self.textEdit, 0, 0, 1, 2)

        self.retranslateUi(changeLog)
        QtCore.QMetaObject.connectSlotsByName(changeLog)

    def retranslateUi(self, changeLog):
        changeLog.setWindowTitle(_translate("changeLog", "Launcher_3x Change Log", None))
        self.textEdit.setHtml(_translate("changeLog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">3.1.2</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-style:italic;\">Features</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- GUI updates everywhere. Minimalist approach. Hidden main menu. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- Reverted back to original one-handed item selection method. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-style:italic;\">Bug Fixes</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- Small change to launch logic. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- Installer/Uninstaller fixes. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-style:italic;\">Known Bugs</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- The \'Save\' button is a little sensitive and will appear sometimes even if no item re-ordering has taken place. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- Warning! Some Java based applications will start but may behave strangely. If this happens, start the application normally. </span></p>\n"
"<p style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">3.1.1</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-style:italic;\">Features</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- Find/Replace tool added. Very crude, case sensitive over the whole DB! </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-style:italic;\">Bug Fixes</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- Fixed error with launching an invalid application. </span></p>\n"
"<p style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">3.1.0</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-style:italic;\">Features</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- Qt updated to version 4.8.4 via PyQt. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- Database storage is now working properly. All characters are accepted. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:80px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- This means less launch failures. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:80px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- This means direct copy/paste from any known shortcut will work. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:80px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- Paths containing &quot;?&quot; will NO LONGER WORK. Replace all ? with &quot;. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- Entire app is now a &quot;Dialog&quot; type window. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:80px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- This means no icon in the &quot;Running Applications&quot; bar. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:80px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- This also means \'Always on Top\' is on permenantly. Menu item removed. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- Tray Icon code has been cleaned up/improved. New item added for minimisation. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- Text changed in various places. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- Numerous GUI changes. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- Double Clicking a single app will launch it! </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- Selection mode has changed! Either drag a selection or use Ctrl &amp; Shift for multiples. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- Mouse tracking enabled. Improved application focus control. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- Center text elide enabled on path. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-style:italic;\">Bug Fixes</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- Launch code improvements for all platforms as well as specific windows updates. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- Path renaming was broken for special characters. All paths launch correctly including &quot;&quot; </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- Window focus on resume now working as it should. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- Esc &amp; CtrlQ shortcuts were broken for popup windows. Now working. </span></p>\n"
"<p style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">3.0.0</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-style:italic;\">Features</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- Improved icons and more of them. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- Can now edit the path of launchers, not just the name. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- Linux integration testing. Some features don\'t work in Linux and are disabled </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">   including &quot;Start at boot&quot;, &quot;Hide on Focus Loss&quot;, &quot;Keyboard Shortcuts&quot; </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- Code clean up. Database abstraction moved to seperate file. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- utf8 converted strings everywhere. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- SVG support. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- Various small text changes. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-style:italic;\">Bug Fixes</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- Import/Export error handling. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- Linux launch code improvements including setsid forking. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- Cancelling a \'Duplicate\' action now works as it should. </span></p>\n"
"<p style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">2.4.0</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-style:italic;\">Features</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- &quot;Hide on Focus Loss&quot; menu option added! Off by default. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- &quot;Wipe All Data&quot; menu option added. Backup database first! </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- Win+A replaced by Caps+Caps and RCtrl+RCtrl </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- Keyboard shortcuts now Hide </span><span style=\" font-size:8pt; font-style:italic;\">and </span><span style=\" font-size:8pt;\">Restore the app window. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- Keyboard shortcut menu option added. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- New &quot;Copy To&quot; dialog for duplicating entries. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- Separator implementation. Paths with only \'-\'s will not execute e.g. ------- </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- A few icons updated. Separator has its own icon. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- Path Executable Examples added to \'path\' popup. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- Opacity Controller added to menu. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- Enter key can now launch item/s. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- Add new Launcher entry order reversed (Path -&gt; Name) </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-style:italic;\">Bug Fixes</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- MAJOR code rework. Duplicate Names supported. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- MAJOR code rework. Much simpler, all major functions rewritten. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- Fixed popup window parenting for all popups. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- Code cleanup and variable clarity, fewer classes. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- Simpler Hide/Show code. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- Window Flag alignment on all windows. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- Add Launcher location positioning fixed. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- Path Dialog cancel and close behaviour fixed. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- Keyboard shortcut timing implemented. 0.1-0.6s activation window. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- Keyboard shortcut activation bugs ironed out. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- Window Hide timing implemented. 0.3s restriction. </span></p>\n"
"<p style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">2.3.3</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-style:italic;\">Bug Fixes</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- Import/Export affected by keyboard detection system no longer. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- Import/Export now ignores selection of the current database. </span></p>\n"
"<p style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">2.3.2</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-style:italic;\">Bug Fixes</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- Key press detection works properly. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- Tray mouse click activation works properly. </span></p>\n"
"<p style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">2.3.1</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-style:italic;\">Features</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- Fixed the launch code. Now simpler and more robust. &quot; &quot; not needed for multiple arguments. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- &quot;Esc&quot; key now minimises the window to taskbar. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- &quot;Win+a&quot; bring the windows up from taskbar. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- &quot;Ctrl+q&quot; exits the program. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- Change Log text is now selectable. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- 2 Icon Changes </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- Now installs as a multi-file application rather than a single executable. </span></p>\n"
"<p style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">2.3.0</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-style:italic;\">Features</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- Added database import and export.  </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- Added &quot;Change Log&quot; menu item for displaying this list. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- A few font and colour changes. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- Code cleanup. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-style:italic;\">Bug Fixes</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- Duplicating an item with only 1 group present wasn\'t handled correctly. </span></p>\n"
"<p style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">2.2.0</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-style:italic;\">Features</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- Reworked \'App Path\' Dialog </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- Now checks to see if the app exists when adding - still can add duplicates though </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- Improved launch logic (only excludes &quot; in paths now) </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- Launch failure checks. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- Added \'Start at Boot\' functionality (uses the registry) </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- Changed menu names. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- Better OS detection &amp; integration </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- Changed \'About\' info. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- Uses %appdata% for storage. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- Packaged in a simple installer. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-style:italic;\">Bug Fixes</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- Deleting multiple items with the same name did not work.</span></p></body></html>", None))


class changeLog(QtGui.QDialog, Ui_changeLog):
    def __init__(self, parent=None, f=QtCore.Qt.WindowFlags()):
        QtGui.QDialog.__init__(self, parent, f)

        self.setupUi(self)

