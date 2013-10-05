#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Manages a database of groups of applications and launches them individually or as groups.
Copyright (c) 2013 u3z05en
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

-> v1.0 - June-14-2012 - u3z05en - Script created, tracked in Git.
"""

import os, sys, platform, subprocess, logging, codecs, ctypes, datetime, shutil, time
from re import split, sub, findall, search
from PyQt4 import QtCore, QtGui
from launcher_3x_db import DbCursor
from launcher_3x_ui import Ui_window_main
from launcher_3x_getpath_ui import Ui_getPath
from launcher_3x_changelog_ui import Ui_changeLog
from launcher_3x_getNewGroup_ui import Ui_getNewGroup
from launcher_3x_findreplace_ui import Ui_findReplace
try:
    f8 = QtCore.QString.fromUtf8
except AttributeError:
    f8 = lambda s: s
try:
    import pyHook
except:
    pass

APPNAME = 'Launcher_3x'
APPVERSION = 'v3.1.2'

class MainW(QtGui.QMainWindow):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create(f8('cleanlooks')))
        if PLATFORM[0] == 'Windows':
            self.setWindowFlags(QtCore.Qt.Tool | QtCore.Qt.WindowStaysOnTopHint)
            self.keyHook = pyHook.HookManager()
            self.keyHook.KeyDown = self.keyPress
            self.keyHook.HookKeyboard()
            self.keyArray = []
        else:
            os.setsid()
        self.ui = Ui_window_main()
        self.ui.setupUi(self)
        self.ui.slider_opacity.hide()
        self.ui.lcd_opacity.hide()
        self.ui.label_opacity.hide()
        self.ui.menuBar.hide()
        self.ui.treeview_applist.installEventFilter(self)
        self.escKey = QtGui.QShortcut(QtGui.QKeySequence(f8("Esc")), self, self.hide)
        self.ctrlQ = QtGui.QShortcut(QtGui.QKeySequence(f8("Ctrl+q")), self, self.windowLeave)
        self.setup()
        self.initDB()
        self.mainWindow = QtGui.QApplication.activeWindow()
        # SLOT GLOBAL
        QtCore.QObject.connect(Application, QtCore.SIGNAL(f8("focusChanged(QWidget *, QWidget *)")), self.focusChanged)
        QtCore.QObject.connect(self.ui.slider_opacity, QtCore.SIGNAL("valueChanged(int)"), self.opacityChange)
        # SLOTS DOUBLE CLICK
        self.ui.treeview_applist.doubleClicked.connect(self.launchItem)
        # SLOTS BUTTONS
        QtCore.QObject.connect(self.ui.button_launch, QtCore.SIGNAL(f8("clicked()")), self.launchItem)
        QtCore.QObject.connect(self.ui.button_selectall, QtCore.SIGNAL(f8("clicked()")), self.selectAll)
        QtCore.QObject.connect(self.ui.button_selectnone, QtCore.SIGNAL(f8("released()")), self.selectNone)
        QtCore.QObject.connect(self.ui.button_invert, QtCore.SIGNAL(f8("clicked()")), self.selectInvert)
        QtCore.QObject.connect(self.ui.button_addapp, QtCore.SIGNAL(f8("clicked()")), self.addApp)
        QtCore.QObject.connect(self.ui.button_addgroup, QtCore.SIGNAL(f8("clicked()")), self.addGroup)
        QtCore.QObject.connect(self.ui.button_saveedits, QtCore.SIGNAL(f8("clicked()")), self.saveState)
        # SLOTS MENUS
        QtCore.QObject.connect(self.ui.menu_importdatabase, QtCore.SIGNAL(f8("triggered()")), self.importDatabase)
        QtCore.QObject.connect(self.ui.menu_exportdatabase, QtCore.SIGNAL(f8("triggered()")), self.exportDatabase)
        QtCore.QObject.connect(self.ui.menu_selectallbydefault, QtCore.SIGNAL(f8("triggered()")), self.saveSelectAll)
        QtCore.QObject.connect(self.ui.menu_savewindowsize, QtCore.SIGNAL(f8("triggered()")), self.saveWindowSize)
        QtCore.QObject.connect(self.ui.menu_startatboot, QtCore.SIGNAL(f8("triggered()")), self.startAtBoot)
        QtCore.QObject.connect(self.ui.menu_setwindowopacity, QtCore.SIGNAL(f8("triggered()")), self.showOpacity)
        QtCore.QObject.connect(self.ui.menu_findreplace, QtCore.SIGNAL(f8("triggered()")), self.findReplace)
        QtCore.QObject.connect(self.ui.menu_dbdesign, QtCore.SIGNAL(f8("triggered()")), self.showSchema)
        QtCore.QObject.connect(self.ui.menu_exit, QtCore.SIGNAL(f8("triggered()")), self.windowLeave)
        QtCore.QObject.connect(self.ui.menu_hideonfocusloss, QtCore.SIGNAL(f8("triggered()")), self.hideOnFocusLoss)
        QtCore.QObject.connect(self.ui.menu_enablekeyboardshortcut, QtCore.SIGNAL(f8("triggered()")), self.keyboardShortcut)
        QtCore.QObject.connect(self.ui.menu_about, QtCore.SIGNAL(f8("triggered()")), self.about)
        QtCore.QObject.connect(self.ui.menu_whatsnew, QtCore.SIGNAL(f8("triggered()")), self.showChangeLog)
        QtCore.QObject.connect(self.ui.menu_wipealldata, QtCore.SIGNAL(f8("triggered()")), self.wipeData)
        QtCore.QObject.connect(self.ui.menu_aboutqt, QtCore.SIGNAL(f8("triggered()")), self.aboutQT)
        # SLOTS TREES
        QtCore.QObject.connect(self.ui.treeview_grouplist, QtCore.SIGNAL(f8("itemClicked(QTreeWidgetItem*,int)")), self.groupClicked)
        QtCore.QObject.connect(self.ui.treeview_applist, QtCore.SIGNAL(f8("itemClicked(QTreeWidgetItem*,int)")), self.appClicked)
        QtCore.QObject.connect(self.ui.treeview_applist, QtCore.SIGNAL(f8("itemEntered(QTreeWidgetItem*,int)")), self.appClicked)
        QtCore.QObject.connect(self.ui.treeview_grouplist, QtCore.SIGNAL(f8("itemEntered(QTreeWidgetItem*,int)")), self.stateChanged)
        QtCore.QObject.connect(self.ui.treeview_applist, QtCore.SIGNAL(f8("itemEntered(QTreeWidgetItem*,int)")), self.stateChanged)
        # SLOTS TRAY
        QtCore.QObject.connect(self.trayIcon, QtCore.SIGNAL(f8("activated(QSystemTrayIcon::ActivationReason)")), self.trayControl)
        # ACTIONS
        launchAll = QtGui.QAction(f8("Launch All"), self.ui.treeview_grouplist); launchAll.triggered.connect(self.launchAll)
        launchAll.setIcon(QtGui.QIcon(f8(':/launchall.svg'))); self.ui.treeview_grouplist.addAction(launchAll)
        renameGroup = QtGui.QAction(f8("Rename"), self.ui.treeview_grouplist); renameGroup.triggered.connect(self.renameGroup)
        renameGroup.setIcon(QtGui.QIcon(f8(':/utilities-terminal.svg'))); self.ui.treeview_grouplist.addAction(renameGroup)
        deleteGroup = QtGui.QAction(f8("Delete Group"), self.ui.treeview_grouplist); deleteGroup.triggered.connect(self.deleteGroup)
        deleteGroup.setIcon(QtGui.QIcon(f8(':/deleteeverywhere.png'))); self.ui.treeview_grouplist.addAction(deleteGroup)
        launchApp = QtGui.QAction(f8("Launch"), self.ui.treeview_applist); launchApp.triggered.connect(self.launchItem)
        launchApp.setIcon(QtGui.QIcon(f8(':/launcher.png'))); self.ui.treeview_applist.addAction(launchApp)
        invertApp = QtGui.QAction(f8("Invert Selection"), self.ui.treeview_applist); invertApp.triggered.connect(self.selectInvert)
        invertApp.setIcon(QtGui.QIcon(f8(':/inverse.png'))); self.ui.treeview_applist.addAction(invertApp)
        copyApp = QtGui.QAction(f8("Copy to Group"), self.ui.treeview_applist); copyApp.triggered.connect(self.copyApp)
        copyApp.setIcon(QtGui.QIcon(f8(':/teamviewer.svg'))); self.ui.treeview_applist.addAction(copyApp)
        renameApp = QtGui.QAction(f8("Edit Name"), self.ui.treeview_applist); renameApp.triggered.connect(self.renameApp)
        renameApp.setIcon(QtGui.QIcon(f8(':/utilities-terminal.svg'))); self.ui.treeview_applist.addAction(renameApp)
        changePath = QtGui.QAction(f8("Edit Path"), self.ui.treeview_applist); changePath.triggered.connect(self.changePath)
        changePath.setIcon(QtGui.QIcon(f8(':/utilities-terminal.svg'))); self.ui.treeview_applist.addAction(changePath)
        deleteApp = QtGui.QAction(f8("Delete Here"), self.ui.treeview_applist); deleteApp.triggered.connect(self.deleteApp)
        deleteApp.setIcon(QtGui.QIcon(f8(':/deletehere.png'))); self.ui.treeview_applist.addAction(deleteApp)
        deleteAppAll = QtGui.QAction(f8("Delete Everywhere"), self.ui.treeview_applist); deleteAppAll.triggered.connect(self.deleteAppAll)
        deleteAppAll.setIcon(QtGui.QIcon(f8(':/deleteeverywhere.png'))); self.ui.treeview_applist.addAction(deleteAppAll)

    def setup(self):
        msg = BASE_NAME + ' Initiated';log_this(msg.center(45, '-'), 'info')
        # PID PROCESSING
        if os.path.isfile(PID_FILE) == True:
            old_instance = open(PID_FILE).readlines()[0].strip()
            if int(old_instance) != PID_NUM:
                os.remove(PID_FILE)
                try:
                    os.kill(int(old_instance), 9)
                    log_this('Old PID file found and killed. Old PID: ' + old_instance + ' Current PID: ' + str(PID_NUM), 'warn')
                except:
                    log_this('Old PID file found, process was not running. Old PID: ' + old_instance + ' Cur PID: ' + str(PID_NUM), 'warn')
            else:
                log_this('PID file contains current PID, something is very wrong!', 'crit')
                leave_now(1)
        pid_gate = open(PID_FILE, 'wb')
        pid_gate.write(str(PID_NUM))
        pid_gate.close()
        # PREFERENCES
        self.hideTime = time.time()
        self.key1Time = self.hideTime
        self.regRunPath = QtCore.QSettings(REG_RUN, QtCore.QSettings.NativeFormat)
        if os.path.isfile(VAR_FILE):
            for line in open(VAR_FILE):
                if search(r'^geometry', line):
                    ws = split(r',', split(r'=', line)[1].strip())
                    self.setGeometry(QtCore.QRect(int(ws[0]), int(ws[1]), int(ws[2]), int(ws[3])))
                if search(r'^select_all_by_default', line):
                    if str(split(r'=', line)[1].strip()) == 'Yes':
                        self.ui.menu_selectallbydefault.setChecked(True)
                    else:
                        self.ui.menu_selectallbydefault.setChecked(False)
                if search(r'^start_at_boot', line):
                    if str(split(r'=', line)[1].strip()) == 'Yes':
                        self.ui.menu_startatboot.setChecked(True)
                    else:
                        self.ui.menu_startatboot.setChecked(False)
                    self.startAtBoot()
                if search(r'^hide_on_focus_loss', line):
                    if str(split(r'=', line)[1].strip()) == 'Yes':
                        self.ui.menu_hideonfocusloss.setChecked(True)
                    else:
                        self.ui.menu_hideonfocusloss.setChecked(False)
                    self.hideOnFocusLoss()
                if search(r'^enable_keyboard_shortcut', line):
                    if str(split(r'=', line)[1].strip()) == 'Yes':
                        self.ui.menu_enablekeyboardshortcut.setChecked(True)
                    else:
                        self.ui.menu_enablekeyboardshortcut.setChecked(False)
                    self.keyboardShortcut()
                if search(r'^window_opacity', line):
                    Opacity = float(split(r'=', line)[1].strip())
                    self.ui.slider_opacity.setValue(Opacity)
                    self.setWindowOpacity(Opacity / 100)
        else:
            rfile = codecs.open(VAR_FILE, 'w', 'utf-8')
            rfile.write(unicode("select_all_by_default=Yes\n"))
            rfile.write(unicode("start_at_boot=No\n"))
            rfile.write(unicode("hide_on_focus_loss=No\n"))
            rfile.write(unicode("enable_keyboard_shortcut=No\n"))
            rfile.write(unicode("window_opacity=100\n"))
            rfile.write(unicode("geometry=210,259,490,316\n"))
            rfile.close()
            self.startAtBoot()
            self.hideOnFocusLoss()
            self.keyboardShortcut()
        # PLATFORM SPECIFIC GUI CONTROLS
        if PLATFORM[0] == 'Windows':
            pass
        else:
            self.ui.menu_hideonfocusloss.setVisible(False)
            self.ui.menu_enablekeyboardshortcut.setVisible(False)
            self.ui.menu_startatboot.setVisible(False)

        # ICONS, FONTS, ACTIONS
        self.setWindowTitle(APPNAME + '  ' + APPVERSION)
        self.setWindowIcon(QtGui.QIcon(':/launcher.png'))
        self.font = QtGui.QFont()
        self.font.setFamily('Segoe UI')
        self.createTrayIcon()

    def shortCutKeysOn(self):
        self.trayIcon.show()
        self.escKey.setEnabled(True)
        self.ctrlQ.setEnabled(True)

    def shortCutKeysOff(self):
        self.trayIcon.hide()
        self.escKey.setEnabled(False)
        self.ctrlQ.setEnabled(False)

    def eventFilter(self, watched, event):
        if event.type() == QtCore.QEvent.KeyPress:
            if event.matches(QtGui.QKeySequence.InsertParagraphSeparator):
                if watched.objectName() == 'treeview_applist':
                    self.launchItem()
                return True
        return False

    def opacityChange(self):
        self.setWindowOpacity(float(self.ui.slider_opacity.value()) / 100)

    def findReplace(self):
        findReplace = FindReplace(self.app_db, parent = self)
        self.trayIcon.hide()
        findReplace.exec_()
        self.trayIcon.show()
        self.loadLinks()

    def showOpacity(self):
        self.ui.slider_opacity.show()
        self.ui.lcd_opacity.show()
        self.ui.label_opacity.show()
        if not self.ui.button_saveedits.isEnabled():
            self.ui.button_saveedits.setEnabled(True)
            self.ui.button_saveedits.setStyleSheet('color: #FF0000;')

    def keyPress(self, event):
        if QtGui.QApplication.activeModalWidget() == None:
                Now = time.time(); diff = Now - self.key1Time
                if diff > 0.6:
                    self.keyArray = []
                print event.KeyID
                if event.KeyID == 91 or event.KeyID == 163 or len(self.keyArray) == 1:
                    self.keyArray.append(event.KeyID)
                    if len(self.keyArray) == 2:
                        if self.keyArray[1] == 91 or self.keyArray[1] == 163:
                            if diff < 0.6 and diff > 0.1:
                                self.trayControl(2)
                        self.keyArray = []
                    else:
                        self.key1Time = time.time()

    def focusChanged(self, old, new):
        if not self.isHidden():
            if QtGui.QApplication.activeModalWidget() == None:
                if QtGui.QApplication.activeWindow() == None:
                    if self.autoHide == True:
                        self.trayControl(2)
                        self.shortCutKeysOn()

    # TREEVIEW CONTROL
    def loadLinks(self):
        self.Links = self.app_db.getTable('itemgroup_has_item')
        self.loadGroups()

    def loadGroups(self):
        if not self.ui.slider_opacity.isHidden():
            self.ui.slider_opacity.hide();self.ui.lcd_opacity.hide()
            self.ui.label_opacity.hide()
        self.ui.treeview_grouplist.clear()
        self.Groups = self.app_db.getTable('itemgroup')  # [ID, NAME, SEQ, DATE]
        self.Groups = sorted(self.Groups, key = lambda i:i[2])  # Sorts by the 2nd element in each item
        for index in range(len(self.Groups)):
            item = QtGui.QTreeWidgetItem(self.ui.treeview_grouplist)
            item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
            self.font.setPointSize(13); item.setFont(0, self.font)
            item.setIcon(0, QtGui.QIcon(':/folder.png'))
            item.setText(0, self.Groups[index][1])
            item.setText(1, str(self.Groups[index][0]))
        try:
            self.setWindowTitle(APPNAME + '  ' + APPVERSION + '    "%s"' % self.currentGroup[1])
        except:
            self.currentGroup = [self.Groups[0][0], self.Groups[0][1]]
            self.setWindowTitle(APPNAME + '  ' + APPVERSION + '    "%s"' % self.currentGroup[1])
        self.ui.treeview_grouplist
        self.loadApps()

    def loadApps(self):
        try:
            self.appMax = max(self.app_db.getTable('item'))[0]
        except:
            self.appMax = 0
        self.ui.treeview_applist.clear()
        self.Apps = self.app_db.getApps(self.currentGroup[0])  # [SEQ, NAME, PATH, ID]
        self.Apps = sorted(self.Apps)
        for index in range(len(self.Apps)):
            item = QtGui.QTreeWidgetItem(self.ui.treeview_applist)
            item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
            brush = QtGui.QBrush(QtGui.QColor(112, 112, 112));item.setForeground(1, brush)
            self.font.setPointSize(11); item.setFont(0, self.font)
            self.font.setPointSize(7); item.setFont(1, self.font)
            if not search(r'^-*$', self.Apps[index][2]):
                item.setIcon(0, QtGui.QIcon(':/app.png'))
            else:
                item.setIcon(0, QtGui.QIcon(':/separator.png'))
            item.setText(0, self.Apps[index][1])
            item.setText(1, self.Apps[index][2]); item.setText(2, str(self.Apps[index][3]))
        self.ui.treeview_applist.resizeColumnToContents(0)
        self.ui.button_saveedits.setEnabled(False)
        self.ui.button_saveedits.setStyleSheet('color: #FFFFFF;')
        if self.ui.menu_selectallbydefault.isChecked():
            self.selectAll()
        self.update(); self.repaint()

    # BUTTON SLOT CONTROL
    def addApp(self):
        self.shortCutKeysOff()
        Path = GetPath(parent = self)
        path = Path.getPath()
        self.shortCutKeysOn()
        if path:
            app, appok = QtGui.QInputDialog.getText(self, 'Launcher Title', 'What should this Launcher be called?')
            if app and appok:
                app = sub(r'"', '', sub(r'[ ]{2,}', ' ', str(app)).strip())
                path = sub(r'[ ]{2,}', ' ', str(path)).strip()
                reply = QtGui.QMessageBox.Yes
                if self.app_db.findApp(path):
                    reply = QtGui.QMessageBox.information(self, 'Launcher Exists', 'This Launcher already exists. Proceed?', QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
                if reply == QtGui.QMessageBox.Yes:
                    self.app_db.add_app(self.appMax + 1, app, path, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                    self.app_db.add_app_link(self.appMax + 1, self.currentGroup[0], len(self.Apps))
                    self.app_db.commit()
                    self.loadLinks()

    def deleteApp(self):
        reply = QtGui.QMessageBox.critical(self, 'Delete Item from List', 'Are you sure?', QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            if self.ui.treeview_applist.selectedIndexes() == []:
                self.ui.treeview_applist.currentItem().setSelected(True)
            curList = self.ui.treeview_applist.findItems('', QtCore.Qt.MatchContains)
            for index in range(len(curList)):
                if curList[index].isSelected():
                    ciID = int(curList[index].text(2))
                    for index2 in range(len(self.Links)):
                        if self.Links[index2][1] == self.currentGroup[0]:
                            if self.Links[index2][0] == ciID:
                                self.app_db.deleteSingleAppLink(self.currentGroup[0], ciID)
            self.app_db.commit()
            self.loadLinks()
            allApps = self.app_db.getAllApps()
            for index in range(len(allApps)):
                found = False
                for index2 in range(len(self.Links)):
                    if int(allApps[index][0]) == int(self.Links[index2][0]):
                        found = True
                if found == False:
                    self.app_db.deleteApp(allApps[index][0])
            self.app_db.commit()

    def deleteAppAll(self):
        reply = QtGui.QMessageBox.critical(self, 'Delete Item Everywhere', 'Are you sure?\nThis will remove ALL instances from the database!', QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            if self.ui.treeview_applist.selectedIndexes() == []:
                self.ui.treeview_applist.currentItem().setSelected(True)
            curList = self.ui.treeview_applist.findItems('', QtCore.Qt.MatchContains)
            for index in range(len(curList)):
                if curList[index].isSelected():
                    ciID = int(curList[index].text(2))
                    self.app_db.deleteApp(ciID)
                    self.app_db.deleteAllAppLinks(ciID)
            self.app_db.commit()
            self.loadLinks()

    def copyApp(self):
        if self.ui.treeview_applist.selectedIndexes() == []:
            itemsToCopy = [self.ui.treeview_applist.currentItem()]
        else:
            itemsToCopy = self.ui.treeview_applist.selectedItems()
        gAddList = []
        for item in self.ui.treeview_grouplist.findItems('', QtCore.Qt.MatchContains):
            if int(item.text(1)) != self.currentGroup[0]:
                gAddList.append([item.text(0), item.text(1)])
        if not gAddList == []:
            ng = GetNewGroup(gAddList, parent = self)
            newGroup = ng.getGroup()
            if newGroup != None:
                for item in itemsToCopy:
                    try:
                        self.app_db.add_app_link(int(item.text(2)), str(newGroup[1]), 0)
                    except:
                        pass
                self.currentGroup = [int(newGroup[1]), str(newGroup[0])]
        else:
            QtGui.QMessageBox.information(self, 'No Other Groups', 'There are no other groups to duplicate to.', QtGui.QMessageBox.Ok)
        self.app_db.commit()
        self.loadLinks()

    def renameApp(self):
        app, appok = QtGui.QInputDialog.getText(self, 'Rename Launcher', 'What should this Launcher be called?'.center(75), QtGui.QLineEdit.Normal, self.ui.treeview_applist.currentItem().text(0))
        if app and appok:
            for index in range(len(self.Apps)):
                if int(self.ui.treeview_applist.currentItem().text(2)) == self.Apps[index][3]:
                    self.app_db.renameApp(app, self.Apps[index][3])
            self.app_db.commit()
            self.loadLinks()

    def changePath(self):
        path, pathok = QtGui.QInputDialog.getText(self, 'Change Path', 'What should the new path be?'.center(155), QtGui.QLineEdit.Normal, self.ui.treeview_applist.currentItem().text(1))
        if path and pathok:
            for index in range(len(self.Apps)):
                if int(self.ui.treeview_applist.currentItem().text(2)) == self.Apps[index][3]:
                    self.app_db.changePath(path, self.Apps[index][3])
            self.app_db.commit()
            self.loadLinks()

    def addGroup(self):
        group, qok = QtGui.QInputDialog.getText(self, 'Group Name', "What's your new group called?")
        group = str(group)
        if qok:
            newIndex = max(self.Groups)[0] + 1
            self.app_db.add_group(newIndex, group, len(self.Groups), datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            self.Groups.append((newIndex, group, len(self.Groups), datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
            self.app_db.commit()
            self.currentGroup = [newIndex, group]
            self.loadGroups()

    def deleteGroup(self):
        reply = QtGui.QMessageBox.critical(self, 'Delete Group', 'Are you sure you want to delete this group?\n\n  ' + self.currentGroup[1], QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            self.app_db.deleteGroup(self.currentGroup[0])
            self.app_db.deleteGroupLink(self.currentGroup[0])
            self.app_db.commit()
            self.loadLinks()
            allApps = self.app_db.getAllApps()
            for index in range(len(allApps)):
                found = False
                for index2 in range(len(self.Links)):
                    if int(allApps[index][0]) == int(self.Links[index2][0]):
                        found = True
                if found == False:
                    self.app_db.deleteApp(allApps[index][0])
            self.app_db.commit()
            if self.Groups == []:
                self.app_db.shutdown()
                del self.app_db
                os.remove(DB_FILE)
                leave_now(0)
            self.loadLinks()

    def renameGroup(self):
        group, appok = QtGui.QInputDialog.getText(self, 'Group', 'What do you want to rename this Group to?', QtGui.QLineEdit.Normal, self.currentGroup[1])
        if group and appok:
            self.app_db.renameGroup(str(group), self.currentGroup[0])
            self.app_db.commit()
            self.currentGroup = [self.currentGroup[0], str(group)]
            self.loadGroups()

    def saveSelectAll(self):
        if self.ui.menu_selectallbydefault.isChecked():
            oldstate = 'No'; newstate = 'Yes'
        else:
            oldstate = 'Yes'; newstate = 'No'
        old = "select_all_by_default=%s" % oldstate
        new = "select_all_by_default=%s" % newstate
        data = codecs.open(VAR_FILE, 'r', 'utf-8').read()
        rfile = codecs.open(VAR_FILE, 'w', 'utf-8')
        rfile.write(unicode(sub(old, new, data)))
        rfile.close()
        self.loadLinks()

    def saveWindowSize(self):
        newGeo = sub(r' ', '', findall(r'\(.*\)$', str(self.geometry()))[0].strip(' \(\)\''))
        old = "geometry=.*"
        new = "geometry=%s" % newGeo
        data = codecs.open(VAR_FILE, 'r', 'utf-8').read()
        rfile = codecs.open(VAR_FILE, 'w', 'utf-8')
        rfile.write(unicode(sub(old, new, data)))
        rfile.close()

    def selectAll(self):
        for item in self.ui.treeview_applist.findItems('', QtCore.Qt.MatchContains):
            item.setSelected(True)
            item.setBackgroundColor(0, QtGui.QColor(228, 240, 255)); item.setBackgroundColor(1, QtGui.QColor(228, 240, 255))

    def selectNone(self):
        for item in self.ui.treeview_applist.findItems('', QtCore.Qt.MatchContains):
            item.setSelected(False)
            item.setBackgroundColor(0, QtGui.QColor(255, 255, 255)); item.setBackgroundColor(1, QtGui.QColor(255, 255, 255))

    def selectInvert(self):
        for item in self.ui.treeview_applist.findItems('', QtCore.Qt.MatchContains):
            if item.isSelected():
                item.setSelected(False)
                item.setBackgroundColor(0, QtGui.QColor(255, 255, 255)); item.setBackgroundColor(1, QtGui.QColor(255, 255, 255))
            else:
                item.setSelected(True)
                item.setBackgroundColor(0, QtGui.QColor(228, 240, 255)); item.setBackgroundColor(1, QtGui.QColor(228, 240, 255))

    def launchAll(self):
        self.ui.treeview_applist.selectAll()
        self.launchItem()

    def launchItem(self):
        try:
            self.ui.treeview_applist.currentItem().setSelected(True)
        except:
            pass
        if not self.ui.treeview_applist.selectedIndexes() == []:
                self.hide()
                for item in self.ui.treeview_applist.findItems('', QtCore.Qt.MatchContains):
                    if item.isSelected():
                        cmd = str(item.text(1))
                        if PLATFORM[0] == 'Windows':
                            if not search(r'^-*$', cmd):
                                try:
                                    subprocess.Popen(cmd)
                                except:
                                    self.show()
                                    QtGui.QMessageBox.warning(self, 'Launch Failed', 'Something went wrong, check the path.', QtGui.QMessageBox.Ok)
                        else:
                            if not search(r'^-*$', cmd):
                                try:
                                    subprocess.Popen(cmd, shell = True)
                                except:
                                    self.show()
                                    QtGui.QMessageBox.warning(self, 'Launch Failed', 'Something went wrong, check the path.', QtGui.QMessageBox.Ok)
        self.loadLinks()
        self.selectNone()

    # TREE SLOT CONTROL
    def appClicked(self):
        for item in self.ui.treeview_applist.findItems('', QtCore.Qt.MatchContains):
            item.setBackgroundColor(0, QtGui.QColor(255, 255, 255))
            item.setBackgroundColor(1, QtGui.QColor(255, 255, 255))

    def stateChanged(self):
        if not self.ui.button_saveedits.isEnabled():
            self.ui.button_saveedits.setEnabled(True)
            self.ui.button_saveedits.setStyleSheet('color: #FF0000;')

    def groupClicked(self):
        curList = self.ui.treeview_grouplist.findItems('', QtCore.Qt.MatchContains)
        for index in range(len(curList)):
            if curList[index].isSelected():
                self.currentGroup = [int(curList[index].text(1)), str(curList[index].text(0))]
                break
        self.loadGroups()

    # MENU CONTROL
    def about(self):
        self.trayIcon.hide()
        QtGui.QMessageBox.about(self, APPNAME + ', version ' + APPVERSION, """<html><h3><strong>Copyright (c) 2013 u3z05en@gmail.com</strong></h3><p><span style="font-family:arial,helvetica,sans-serif"><span style="font-size:10px">Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the &#39;Software&#39;), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions: The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software. THE SOFTWARE IS PROVIDED &#39;AS IS&#39;, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.</span></span></p><h3><strong>Overview</strong></h3><p><span style="font-size:11px"><span style="font-family:arial,helvetica,sans-serif">This application is a group based application launcher written using PyQt. The application uses a simple n:m database to store applications and groups and the links between them. Applications duplicated across multiple groups are the same database instance. It has been tested to work on Windows and Linux.</span></span></p><h3><strong>Shortcuts</strong></h3><p><span style="font-size:11px"><span style="font-family:courier new,courier,monospace">Ctrl+Click: &nbsp; Multiple apps for launching.<br />Shift+Click: &nbsp;Multiple contiguous apps for launching.<br />Caps+Caps: &nbsp; &nbsp;Minimise &amp; Restore the window.<br />RCtrl+RCtrl: &nbsp;Same as above.<br />Esc: &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;Minimise the window to the tray.<br />Ctrl+Q: &nbsp; &nbsp; &nbsp; Exit the application.</span></span></p></html>""")
        self.trayIcon.show()

    def aboutQT(self):
        self.trayIcon.hide()
        QtGui.qApp.aboutQt()
        self.trayIcon.show()

    def showChangeLog(self):
        changeLog = ShowChangeLog(self)
        self.shortCutKeysOff()
        changeLog.exec_()
        self.shortCutKeysOn()

    def showSchema(self):
        self.schema = QtGui.QDialog()
        self.schema.setModal(True)
        self.schema.setWindowFlags(self.windowFlags())
        self.schema.setWindowTitle(APPNAME + '  ' + APPVERSION + ' Database Schema')
        self.schema.setWindowIcon(QtGui.QIcon(':/database.png'))
        self.schema.setStyleSheet('image: url(:dbschema.png);')
        self.schema.setMinimumSize(575, 394)
        self.schema.setMaximumSize(575, 394)
        self.schema.showNormal()
        self.schema.activateWindow()

    def startAtBoot(self):
        if self.ui.menu_startatboot.isChecked():
            oldstate = 'No'; newstate = 'Yes'
            self.regRunPath.setValue('Launcher_3x', sys.argv[0])
        else:
            oldstate = 'Yes'; newstate = 'No'
            self.regRunPath.remove('Launcher_3x')
        old = "start_at_boot=%s" % oldstate
        new = "start_at_boot=%s" % newstate
        data = codecs.open(VAR_FILE, 'r', 'utf-8').read()
        rfile = codecs.open(VAR_FILE, 'w', 'utf-8')
        rfile.write(unicode(sub(old, new, data)))
        rfile.close()

    def hideOnFocusLoss(self):
        if self.ui.menu_hideonfocusloss.isChecked():
            oldstate = 'No'; newstate = 'Yes'
            self.autoHide = True
        else:
            oldstate = 'Yes'; newstate = 'No'
            self.autoHide = False
        old = "hide_on_focus_loss=%s" % oldstate
        new = "hide_on_focus_loss=%s" % newstate
        data = codecs.open(VAR_FILE, 'r', 'utf-8').read()
        rfile = codecs.open(VAR_FILE, 'w', 'utf-8')
        rfile.write(unicode(sub(old, new, data)))
        rfile.close()

    def keyboardShortcut(self):
        self.repaint()
        if self.ui.menu_enablekeyboardshortcut.isChecked():
            oldstate = 'No'; newstate = 'Yes'
            if PLATFORM[0] == 'Windows':
                self.keyHook.HookKeyboard()
        else:
            oldstate = 'Yes'; newstate = 'No'
            if PLATFORM[0] == 'Windows':
                self.keyHook.UnhookKeyboard()
        old = "enable_keyboard_shortcut=%s" % oldstate
        new = "enable_keyboard_shortcut=%s" % newstate
        data = codecs.open(VAR_FILE, 'r', 'utf-8').read()
        rfile = codecs.open(VAR_FILE, 'w', 'utf-8')
        rfile.write(unicode(sub(old, new, data)))
        rfile.close()

    def importDatabase(self):
        self.trayIcon.hide()
        self.hide()
        if PLATFORM[0] == 'Windows':
            newBase = QtGui.QFileDialog.getOpenFileName(self, 'Find Database to Import', 'C:\\', 'Sqlite (*.sqlite);;All Files (*)')
        else:
            newBase = QtGui.QFileDialog.getOpenFileName(self, 'Find Database to Import', '', 'Sqlite (*.sqlite);;All Files (*)')
        if not newBase == '' and not os.path.abspath(str(newBase)) == os.path.abspath(DB_FILE):
            reply = QtGui.QMessageBox.critical(self, 'Import New Data', 'Are you sure? You will loose the current database.', QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
            if reply == QtGui.QMessageBox.Yes:
                self.app_db.shutdown()
                del self.app_db
                try:
                    shutil.copy(newBase, DB_FILE)
                except:
                    QtGui.QMessageBox.critical(self, 'Import Error', 'Something went wrong, check access permissions.', QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
                self.app_db = DbCursor(DB_FILE)
                self.loadLinks()
        self.show()
        self.trayIcon.show()

    def exportDatabase(self):
        self.trayIcon.hide()
        self.hide()
        self.app_db.commit()
        if PLATFORM[0] == 'Windows':
            newBase = QtGui.QFileDialog.getSaveFileName(self, 'Database Backup Location', 'C:\\', 'Sqlite (*.sqlite);;All Files (*)')
        else:
            newBase = QtGui.QFileDialog.getSaveFileName(self, 'Database Backup Location', '', 'Sqlite (*.sqlite);;All Files (*)')
        if not newBase == '' and not os.path.abspath(str(newBase)) == os.path.abspath(DB_FILE):
            try:
                shutil.copy(DB_FILE, newBase)
            except:
                QtGui.QMessageBox.critical(self, 'Export Error', 'Something went wrong, check access permissions.', QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
        self.show()
        self.trayIcon.show()

    def wipeData(self):
        reply = QtGui.QMessageBox.critical(self, 'WARNING!', 'Are you sure?\nYou will loose all data and the application will be closed!', QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            self.app_db.shutdown()
            del self.app_db
            os.remove(DB_FILE)
            os.remove(VAR_FILE)
            log_this('Application Wiped!!', 'crit')
            self.trayIcon.hide()
            leave_now(0)

    # DATABASE CONTROL
    def initDB(self):
        if not os.path.isfile(DB_FILE):
            if PLATFORM[0] == 'Windows':
                self.keyHook.UnhookKeyboard()
            self.hide()
            self.app_db = DbCursor(DB_FILE)
            group, qok = QtGui.QInputDialog.getText(self, 'Group Name', 'What will your first Launch Group be called?: ')
            self.currentGroup = [1, str(group)]
            if qok:
                self.app_db.build()
                self.app_db.add_group(1, self.currentGroup[1], 0, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                self.app_db.commit()
            else:
                self.app_db.shutdown()
                del self.app_db
                os.remove(DB_FILE)
                self.trayIcon.hide()
                leave_now(0)
        else:
            self.app_db = DbCursor(DB_FILE)
        if PLATFORM[0] == 'Windows':
            self.keyboardShortcut()
        self.loadLinks()

    def saveState(self):
        self.repaint()
        # OPACITY
        if not self.ui.slider_opacity.isHidden():
            self.ui.slider_opacity.hide()
            self.ui.lcd_opacity.hide()
            self.ui.label_opacity.hide()
            old = "window_opacity=.*"
            new = "window_opacity=%s" % self.ui.slider_opacity.value()
            data = codecs.open(VAR_FILE, 'r', 'utf-8').read()
            rfile = codecs.open(VAR_FILE, 'w', 'utf-8')
            rfile.write(unicode(sub(old, new, data)))
            rfile.close()
        # TREEVIEWS
        groupChanged = False; appChanged = False
        # GROUPS
        curList = self.ui.treeview_grouplist.findItems('', QtCore.Qt.MatchContains)
        for index in range(len(self.Groups)):
            if int(curList[index].text(1)) != self.Groups[index][0]:
                groupChanged = True
                break
        if groupChanged:
            self.app_db.deleteAllRows('itemgroup')
            for index in range(len(curList)):
                for index2 in range(len(self.Groups)):
                    if int(curList[index].text(1)) == self.Groups[index2][0]:
                        self.app_db.add_group(self.Groups[index2][0], self.Groups[index2][1], index, self.Groups[index2][3])
            self.app_db.commit()
        # APPS
        curList = self.ui.treeview_applist.findItems('', QtCore.Qt.MatchContains)
        for index in range(len(curList)):
            if int(curList[index].text(2)) != self.Apps[index][3]:
                appChanged = True
                break
        if appChanged:
            self.app_db.deleteGroupLink(self.currentGroup[0])
            for index in range(len(curList)):
                for index2 in range(len(self.Apps)):
                    if int(curList[index].text(2)) == self.Apps[index2][3]:
                        self.app_db.add_app_link(self.Apps[index2][3], self.currentGroup[0], index)
            self.app_db.commit()
        self.ui.button_saveedits.setEnabled(False)
        self.ui.button_saveedits.setStyleSheet('color: #FFFFFF;')
        if groupChanged or appChanged:
            self.loadLinks()

    # TRAY CONTROL
    def createTrayIcon(self):
        self.trayActions()
        self.trayIconMenu = QtGui.QMenu(self)
        self.trayIconMenu.addAction(self.restoreAction)
        self.trayIconMenu.addAction(self.minimizeAction)
        self.trayIconMenu.addSeparator()
        self.trayIconMenu.addAction(self.quitAction)
        self.trayIcon = QtGui.QSystemTrayIcon(self)
        if self.trayIcon.isSystemTrayAvailable():
            self.trayIcon.setContextMenu(self.trayIconMenu)
            self.trayIcon.setIcon(QtGui.QIcon(':/launcher.png'))
            self.trayIcon.show()

    def trayActions(self):
        self.restoreAction = QtGui.QAction("&Activate", self,
                triggered = self.showNormal)
        self.quitAction = QtGui.QAction("&Quit", self,
                triggered = self.windowLeave)
        self.minimizeAction = QtGui.QAction("Mi&nimize", self,
                triggered = self.hide)
        self.restoreAction.setIcon(QtGui.QIcon(':/ccsm.svg'))
        self.quitAction.setIcon(QtGui.QIcon(':/start-here.svg'))
        self.minimizeAction.setIcon(QtGui.QIcon(':/teamviewer.svg'))

    def trayControl(self, event):
        event = int(event)
        if event == 2 or event == 3 or event == 4:  # 1=RIGHT, 2=DOUBLE, 3=LEFT, 4=MIDDLE
            if self.isHidden():
                if time.time() - self.hideTime > 0.3:
                    self.show()
                    self.activateWindow()
            else:
                self.hideTime = time.time()
                self.hide()

    # BUILT IN CONTROLS
    def closeEvent(self, event):
        self.hide()
        event.ignore()

    def windowLeave(self):
        self.repaint()
        self.trayIcon.hide()
        self.app_db.shutdown()
        leave_now(0)

class FindReplace(Ui_findReplace, QtGui.QDialog):
    def __init__(self, app_db, parent):
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_findReplace()
        self.ui.setupUi(self)
        self.setWindowFlags(launch_GUI.windowFlags())
        self.app_db = app_db
        self.activateWindow()
        self.ui.fr_ok.clicked.connect(self.run)

    def run(self):
        if self.ui.fr_type.currentIndex() == 1:
            self.app_db.fr_appname(self.ui.fr_find.text(), self.ui.fr_replace.text())
        if self.ui.fr_type.currentIndex() == 0:
            self.app_db.fr_apppath(self.ui.fr_find.text(), self.ui.fr_replace.text())
        if self.ui.fr_type.currentIndex() == 2:
            self.app_db.fr_groupname(self.ui.fr_find.text(), self.ui.fr_replace.text())
        self.app_db.commit()
        self.accept()

class ShowChangeLog(Ui_changeLog, QtGui.QDialog):
    def __init__(self, parent):
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_changeLog()
        self.ui.setupUi(self)
        self.setWindowFlags(launch_GUI.windowFlags())
        self.setWindowIcon(QtGui.QIcon(':/launcher.png'))
        self.activateWindow()

class GetNewGroup(Ui_getNewGroup, QtGui.QDialog):
    def __init__(self, addList, parent):
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_getNewGroup()
        self.ui.setupUi(self)
        self.font = QtGui.QFont()
        for index in range(len(addList)):
            item = QtGui.QTreeWidgetItem(self.ui.treeWidget_groups)
            item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
            brush = QtGui.QBrush(QtGui.QColor(112, 112, 112));item.setForeground(1, brush)
            self.font.setPointSize(9); item.setFont(0, self.font); item.setIcon(0, QtGui.QIcon(':/folder.png'))
            item.setText(0, addList[index][0]); item.setText(1, addList[index][1])
        self.ui.treeWidget_groups.resizeColumnToContents(0)
        QtCore.QObject.connect(self.ui.button_ok, QtCore.SIGNAL("clicked()"), self.copy)
        QtCore.QObject.connect(self.ui.button_cancel, QtCore.SIGNAL("clicked()"), self.shutdown)

    def getGroup(self):
        self.results = []
        self.exec_()
        if not self.results == []:
            return self.results

    def copy(self):
        self.results = [self.ui.treeWidget_groups.currentItem().text(0), self.ui.treeWidget_groups.currentItem().text(1)]
        self.accept()

    def shutdown(self):
        self.close()

class GetPath(Ui_getPath, QtGui.QDialog):
    def __init__(self, parent):
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_getPath()
        self.ui.setupUi(self)
        self.setWindowFlags(launch_GUI.windowFlags())
        if PLATFORM[0] == 'Linux':
            self.setGeometry(parent.x(), parent.y(), self.width(), self.height())
        self.setWindowIcon(QtGui.QIcon(':/launcher.png'))
        self.ui.tabWidget_examples.hide()
        self.ui.gridLayout.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.activateWindow()
        QtCore.QObject.connect(self.ui.button_examples, QtCore.SIGNAL("clicked()"), self.showEG)
        QtCore.QObject.connect(self.ui.button_ok, QtCore.SIGNAL("clicked()"), self.accept)
        QtCore.QObject.connect(self.ui.button_locate, QtCore.SIGNAL("clicked()"), self.locate)
        QtCore.QObject.connect(self.ui.pushButton_1, QtCore.SIGNAL("clicked()"), self.setText1)
        QtCore.QObject.connect(self.ui.pushButton_2, QtCore.SIGNAL("clicked()"), self.setText2)
        QtCore.QObject.connect(self.ui.pushButton_3, QtCore.SIGNAL("clicked()"), self.setText3)
        QtCore.QObject.connect(self.ui.pushButton_4, QtCore.SIGNAL("clicked()"), self.setText4)
        QtCore.QObject.connect(self.ui.pushButton_5, QtCore.SIGNAL("clicked()"), self.setText5)
        QtCore.QObject.connect(self.ui.pushButton_01, QtCore.SIGNAL("clicked()"), self.setText6)
        QtCore.QObject.connect(self.ui.pushButton_02, QtCore.SIGNAL("clicked()"), self.setText7)
        QtCore.QObject.connect(self.ui.pushButton_03, QtCore.SIGNAL("clicked()"), self.setText8)
        QtCore.QObject.connect(self.ui.pushButton_04, QtCore.SIGNAL("clicked()"), self.setText9)
        QtCore.QObject.connect(self.ui.pushButton_05, QtCore.SIGNAL("clicked()"), self.setText10)
        QtCore.QObject.connect(self.ui.pushButton_06, QtCore.SIGNAL("clicked()"), self.setText11)

    def showEG(self):
        if not self.ui.tabWidget_examples.isVisible():
            self.ui.tabWidget_examples.setVisible(True)
        else:
            self.ui.tabWidget_examples.setVisible(False)
        if PLATFORM[0] == 'Windows':
            self.ui.tabWidget_examples.setCurrentIndex(0)
        elif PLATFORM[0] == 'Linux':
            self.ui.tabWidget_examples.setCurrentIndex(1)
        else:
            self.ui.tabWidget_examples.setCurrentIndex(2)

    def setText1(self):
        self.ui.edit_path.setText(r'C:\windows\notepad.exe C:\Windows\System32\drivers\etc\hosts')
    def setText2(self):
        self.ui.edit_path.setText(r'control netconnections')
    def setText3(self):
        self.ui.edit_path.setText(r'Shutdown.exe -s -t 00')
    def setText4(self):
        self.ui.edit_path.setText(r'java -jar "java_file.jar"')
    def setText5(self):
        self.ui.edit_path.setText(r'control.exe mouse')
    def setText6(self):
        self.ui.edit_path.setText(r'libreoffice --writer')
    def setText7(self):
        self.ui.edit_path.setText(r'gnome-terminal --working-directory /home')
    def setText8(self):
        self.ui.edit_path.setText(r'gnome-system-monitor')
    def setText9(self):
        self.ui.edit_path.setText(r'/opt/google/chrome/google-chrome')
    def setText10(self):
        self.ui.edit_path.setText(r'baobab')
    def setText11(self):
        self.ui.edit_path.setText(r'sudo halt')

    def locate(self):
        self.ui.edit_path.setText(QtGui.QFileDialog.getOpenFileName(self, 'Find Launch File', 'C:\\', 'Executables (*.exe and *.msi and *.sh and *.py and *.bat);;All Files (*)'))

    def getPath(self):
        self.exec_()
        return self.ui.edit_path.text()

    def closeEvent(self, event):
        self.ui.edit_path.setText('')
        event.accept()

def log_this(log_string, severity):
    """Log a string. Sevs: debug, info, warn, crit"""
    logging.info(log_string)
    print log_string

def leave_now(exit_code):
    """Exit procedures"""
    if exit_code == 0:
        os.remove(PID_FILE)
    msg = BASE_NAME + ' Exited (' + str(exit_code) + ')'
    log_this(msg.center(45, '-'), 'info')
    logging.shutdown()
    sys.exit(exit_code)

if __name__ == '__main__':
    # GLOBALS
    PLATFORM = split(r'-', platform.platform())
    BASE_DIR = os.path.dirname(os.path.realpath(__file__))
    BASE_NAME = split(r'\..*$', os.path.basename(os.path.realpath(__file__)))[0]
    if PLATFORM[0] == 'Windows':
        APPDATA = os.path.join(os.environ['APPDATA'], BASE_NAME)
    else:
        APPDATA = os.path.join(os.environ['HOME'], '.Launcher_3x')
    if not os.path.isdir(APPDATA):
            os.mkdir(APPDATA)
    PID_NUM = os.getpid()
    PID_FILE = os.path.join(APPDATA, '.pid')
    VAR_FILE = os.path.join(APPDATA, 'preferences')
    LOG_FILE = os.path.join(APPDATA, BASE_NAME + '.log')
    DB_FILE = os.path.join(APPDATA, BASE_NAME + '.sqlite')
    REG_RUN = 'HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run'
    logging.basicConfig(filename = LOG_FILE, format = '%(asctime)s,%(name)s,%(levelname)s,%(message)s', datefmt = '%d/%m/%Y,%H:%M:%S', level = logging.DEBUG)
    if PLATFORM[0] + PLATFORM[1] == 'Windows7':
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('u3z05en.Launcher_3x')

    # START GUI
    os.chdir(BASE_DIR)
    Application = QtGui.QApplication(sys.argv)
    launch_GUI = MainW()
    launch_GUI.show()
    sys.exit(Application.exec_())
