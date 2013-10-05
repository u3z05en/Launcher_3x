; Launcher Setup Script

[Setup]
AppName=Launcher_3x
AppVersion=3.1.2
DefaultDirName={pf}\Launcher_3x
DefaultGroupName=Launcher_3x
UninstallDisplayIcon={app}\Launcher_3x.exe
Compression=lzma2
SolidCompression=yes
;OutputDir=userdocs:Inno Setup Examples Output

[Files]
Source: "S:\pyinstaller\Launcher_3x\dist\Launcher_3x\*"; DestDir: "{app}"
Source: "S:\pyinstaller\Launcher_3x\dist\Launcher_3x\include\*"; DestDir: "{app}\include\"
Source: "S:\pyinstaller\Launcher_3x\dist\Launcher_3x\qt4_plugins\codecs\*"; DestDir: "{app}\qt4_plugins\codecs\"
Source: "S:\pyinstaller\Launcher_3x\dist\Launcher_3x\qt4_plugins\graphicssystems\*"; DestDir: "{app}\qt4_plugins\graphicssystems\"
Source: "S:\pyinstaller\Launcher_3x\dist\Launcher_3x\qt4_plugins\iconengines\*"; DestDir: "{app}\qt4_plugins\iconengines\"
Source: "S:\pyinstaller\Launcher_3x\dist\Launcher_3x\qt4_plugins\imageformats\*"; DestDir: "{app}\qt4_plugins\imageformats\"

[Icons]
Name: "{group}\Launcher_3x"; Filename: "{app}\Launcher_3x.exe"
