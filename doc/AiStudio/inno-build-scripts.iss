; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

#define MyAppName "DocDemo"
#define MyAppVersion "1.5"
#define MyAppPublisher "Yijie, Inc."
#define MyAppURL "https://cn.bing.com"
#define MyAppExeName "DocDemo.exe"

[Setup]
; NOTE: The value of AppId uniquely identifies this application. Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{7291D2FC-4DB8-4A39-816C-486E3C1B0451}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
;AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName={autopf}\C:\Users\Admin\workspace\AiStudioDocs\sphinx-electron\DocDemo-win32-x64
DisableProgramGroupPage=yes
LicenseFile=C:\Users\Admin\workspace\AiStudioDocs\sphinx-electron\DocDemo-win32-x64\LICENSE
; Uncomment the following line to run in non administrative install mode (install for current user only.)
;PrivilegesRequired=lowest
OutputDir=C:\Users\Admin\workspace\AiStudioDocs\sphinx-electron
OutputBaseFilename=DocDemo-inno
SetupIconFile=C:\Users\Admin\workspace\AiStudioDocs\sphinx-electron\DocDemo-win32-x64\docdemon.ico
Compression=lzma
SolidCompression=yes
WizardStyle=modern

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "C:\Users\Admin\workspace\AiStudioDocs\sphinx-electron\DocDemo-win32-x64\{#MyAppExeName}"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Icons]
Name: "{autoprograms}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent
