; Сенарий сгенерирован Мастер сценария Inno Setup.
; СМОТРИТЕ В ДОКУМЕНТАЦИИ СВЕДЕНИЯ О СОЗДАНИИ ФАЙЛОВ СЦЕНАРИЯ INNO SETUP!

[Setup]
; Примечание: Значение AppId уникально идентифицирует приложение.
; Не используйте то же значение AppId в установщиках для других приложений.
; (Чтобы создать новый идентификатор GUID, нажмите Сервис | Генерировать GUID в интегрированной среде разработки).
AppId={{F1A043FB-AA9E-4F40-879B-274DE8067861}
AppName=Temperature Converter
AppVersion=почти бета
;AppVerName=Temperature Converter почти бета
AppPublisher=Mikhin Andrei`s Inc.
AppPublisherURL=http://www.vk.com/mikhinandrei
AppSupportURL=http://www.vk.com/mikhinandrei
AppUpdatesURL=http://www.vk.com/mikhinandrei
DefaultDirName={pf}\Temperature Converter
DefaultGroupName=Temperature Converter
AllowNoIcons=yes
OutputDir=C:\Users\Admin\Desktop\Проекты\Сетапы\Converter
OutputBaseFilename=setup
SetupIconFile=C:\Users\Admin\Desktop\Проекты\Python\Converter\_-1_jpg.ico
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
; Примечание: Не используйте "Flags: ignoreversion" для любых общих системных файлов

[Icons]
Name: "{group}\Temperature Converter"; Filename: "{app}\Converter.exe"
Name: "{commondesktop}\Temperature Converter"; Filename: "{app}\Converter.exe"; Tasks: desktopicon
Name: "{userappdata}\Microsoft\Internet Explorer\Quick Launch\Temperature Converter"; Filename: "{app}\Converter.exe"; Tasks: quicklaunchicon

[Run]
Filename: "{app}\Converter.exe"; Description: "{cm:LaunchProgram,Temperature Converter}"; Flags: nowait postinstall skipifsilent

