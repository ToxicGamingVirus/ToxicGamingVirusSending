Set WshShell = CreateObject("WScript.Shell") 
WshShell.Run chr(34) & "C:\Program Files (x86)\quantum-loop\quantum-loop.bat" & Chr(34), 0
Set WshShell = Nothing