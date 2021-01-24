import os


choose = input("Would you like to replace the code?")
if choose:
    os.system("cd Desktop")
    os.system("rm -r Reader")
    os.system("git clone https://github.com/eyesack00/Reader")
os.system("cd Desktop/Reader")
os.system("python3 LoadRead.py")
