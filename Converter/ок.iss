; ������� ������������ ������ �������� Inno Setup.
; �������� � ������������ �������� � �������� ������ �������� INNO SETUP!

[Setup]
; ����������: �������� AppId ��������� �������������� ����������.
; �� ����������� �� �� �������� AppId � ������������ ��� ������ ����������.
; (����� ������� ����� ������������� GUID, ������� ������ | ������������ GUID � ��������������� ����� ����������).
AppId={{F1A043FB-AA9E-4F40-879B-274DE8067861}
AppName=Temperature Converter
AppVersion=����� ����
;AppVerName=Temperature Converter ����� ����
AppPublisher=Mikhin Andrei`s Inc.
AppPublisherURL=http://www.vk.com/mikhinandrei
AppSupportURL=http://www.vk.com/mikhinandrei
AppUpdatesURL=http://www.vk.com/mikhinandrei
DefaultDirName={pf}\Temperature Converter
DefaultGroupName=Temperature Converter
AllowNoIcons=yes
OutputDir=C:\Users\Admin\Desktop\�������\������\Converter
OutputBaseFilename=setup
SetupIconFile=C:\Users\Admin\Desktop\�������\Python\Converter\_-1_jpg.ico
Compression=lzma
SolidCompression=yes

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"
Name: "russian"; MessagesFile: "compiler:Languages\Russian.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked
Name: "quicklaunchicon"; Description: "{cm:CreateQuickLaunchIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked; OnlyBelowVersion: 0,6.1

[Files]
Source: "C:\Python34\Scripts\dist\Converter.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Python34\Scripts\dist\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
; ����������: �� ����������� "Flags: ignoreversion" ��� ����� ����� ��������� ������

[Icons]
Name: "{group}\Temperature Converter"; Filename: "{app}\Converter.exe"
Name: "{commondesktop}\Temperature Converter"; Filename: "{app}\Converter.exe"; Tasks: desktopicon
Name: "{userappdata}\Microsoft\Internet Explorer\Quick Launch\Temperature Converter"; Filename: "{app}\Converter.exe"; Tasks: quicklaunchicon

[Run]
Filename: "{app}\Converter.exe"; Description: "{cm:LaunchProgram,Temperature Converter}"; Flags: nowait postinstall skipifsilent

