# ABOUT THIS PROJECT

This project involves the creation of a Python Trojan keylogger. A BAT file or its compiled executable file serves as the Trojan, connecting to the attacker's Django web server (hosted on their system). Once executed on the victim's system,the Trojan installs two malicious Python scripts. The first script captures keystrokes and saves them in a text file, while the second script periodically sends the text file to the attacker's machine and checks if the attacker machine is online. If the attacker machine is offline the scripts will be deleted. After transmission, both scripts automatically delete themselves along with the text file to minimize suspicion

NOTE - It's important to note that if the victim shuts down their system, the connection to the attacker will be lost, and the scripts will not self-delete, potentially leaving behind scripts containing the public IP address of the attacker's system.

# CLONING REPOSITORY AND SETUP

-> Open terminal in required directory and enter following commands

git clone <repository_url>
cd <project_directory>
pip install pipenv
pipenv shell
pipenv install -r requirements.txt
python manage.py makemigrations
python manage.py migrate

# USING THIS PROJECT

-> Open the project in you preferred text editor and start the server using the following command in terminal.

python manage.py runserver

-> The .bat file

A .bat file is there in the keylogger directory of the project which you can send to the victim to connect to your system. The .bat file connect to the attacker machine when the victim will open the .bat file and perform series of task. You can try giving icon to the .bat file

By default, an image will open as soon as the victim opens the .bat file to avoid suspicion. However, you can customize it as needed to further avoid suspicion or compile it to an executable (.exe) file using a BAT to EXE converter and give it a suitable icon.

NOTE - Note that .exe files are more likely to be flagged by antivirus software, so consider obfuscating it to minimize detection.