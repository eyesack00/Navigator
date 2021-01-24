import os

os.system("cd ~")
choose = input("Would you like to replace the code?")
if choose:
    os.system("cd home/pi/Desktop")
    os.system("rm -r Reader")
    os.system("git clone https://github.com/eyesack00/Reader")
os.system("cd home/pi/Desktop/Reader")
os.system("python3 LoadRead.py")
