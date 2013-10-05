#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, subprocess

os.chdir('S:\Documents\Miscleaneous\Programming_Scripting\Python_Scripts\Launcher_3x')

subprocess.Popen('C:\Python27\Lib\site-packages\PyQt4\pyrcc4.exe launcher_3x.qrc > launcher_3x_rc.py', shell = True)

subprocess.Popen('C:\Python27\Lib\site-packages\PyQt4\pyuic4.bat -w launcher_3x.ui > launcher_3x_ui.py', shell = True)

subprocess.Popen('C:\Python27\Lib\site-packages\PyQt4\pyuic4.bat -w launcher_3x_getpath.ui > launcher_3x_getpath_ui.py', shell = True)

subprocess.Popen('C:\Python27\Lib\site-packages\PyQt4\pyuic4.bat -w launcher_3x_changelog.ui > launcher_3x_changelog_ui.py', shell = True)

subprocess.Popen('C:\Python27\Lib\site-packages\PyQt4\pyuic4.bat -w launcher_3x_getNewGroup.ui > launcher_3x_getNewGroup_ui.py', shell = True)

subprocess.Popen('C:\Python27\Lib\site-packages\PyQt4\pyuic4.bat -w launcher_3x_findreplace.ui > launcher_3x_findreplace_ui.py', shell = True)

# subprocess.Popen('C:\Python27\python.exe make_build.py bdist --format=msi', shell = True)
