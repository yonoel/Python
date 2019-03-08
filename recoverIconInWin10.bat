taskkill /f /im explorer.exe

reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Icons" /v 29 /d "C:\Windows\system32\imageres.dll,154" /t reg_sz /f

reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Icons" /v 29 /d "C:\Windows\system32\imageres.dll,154" /t reg_sz /f

reg add "HKEY_CLASSES_ROOT\lnkfile" /v IsShortcut /t reg_sz /f

reg add "HEKY_CLASSES_ROOT\piffile" /v IsShortcut /t reg_sz /f

start explorer

taskkill /f /im explorer.exe

reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Icons" /v 29 /d "C:\Windows\system32\imageres.dll,154" /t reg_sz /f

reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Icons" /v 29 /d "C:\Windows\system32\imageres.dll,154" /t reg_sz /f

reg add "HKEY_CLASSES_ROOT\lnkfile" /v IsShortcut /t reg_sz /f

reg add "HEKY_CLASSES_ROOT\piffile" /v IsShortcut /t reg_sz /f

start explorer