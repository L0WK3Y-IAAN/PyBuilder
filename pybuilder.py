# 🔵 Create a web server that automatically converts the python files that a user uploads and sends it back to them.
# 🔴 Add Mac OS X alternative commands
# 🔴 Add Windows version of script
# 🔴 Pull programmer quotes from the web for loading animation (requires requests module)
# 🟢 Add input sanitization to file_selection and output strings
# 🟢 Fix script so it reads directories and output names with spaces 
# 🟢 Add package check function that installs needed packages (cython, gcc, tkinter)
# 🟡 Make pip requirements file for packages that aren't installed (Package check function may need to be altered)
# 🟡 Add backwards compatibility for older python versions (Might not need if doing a package check)

'''
🔵 - Top priority
🟢 - Completed and working as intended
🟡 - May not need at the moment or feature is subject to change
🔴 - Not implemented yet
'''


'''
 __         ______   __       __  __    __   ______   __      __ 
/  |       /      \ /  |  _  /  |/  |  /  | /      \ /  \    /  |
$$ |      /$$$$$$  |$$ | / \ $$ |$$ | /$$/ /$$$$$$  |$$  \  /$$/ 
$$ |      $$$  \$$ |$$ |/$  \$$ |$$ |/$$/  $$ ___$$ | $$  \/$$/  
$$ |      $$$$  $$ |$$ /$$$  $$ |$$  $$<     /   $$<   $$  $$/   
$$ |      $$ $$ $$ |$$ $$/$$ $$ |$$$$$  \   _$$$$$  |   $$$$/    
$$ |_____ $$ \$$$$ |$$$$/  $$$$ |$$ |$$  \ /  \__$$ |    $$ |    
$$       |$$   $$$/ $$$/    $$$ |$$ | $$  |$$    $$/     $$ |    
$$$$$$$$/  $$$$$$/  $$/      $$/ $$/   $$/  $$$$$$/      $$/     
                                                                 
                                                                 
                                                                  
                                                               
####################################################
#                                                  #   
#   PyBuilder aims to automate the conversion of   #
#   Python scripts to ELF or EXE binaries using    #   
#   Cython3 and GCC. Currently this script only    #
#   to ELF. Stay tuned for updates :)              #
#                                                  #   
####################################################                                                            
                                                      
Follow me on Github!:
https://github.com/L0WK3Y-IAAN
'''

import os
import re
import sys
import shlex
import random
import itertools
import threading
import subprocess
import tkinter as tk
from time import sleep
from tkinter.filedialog import askopenfilename



# Last modification


logo='''
\n\n
_____       _           _ _     _           
|  __ \     | |         (_) |   | |          
| |__) |   _| |__  _   _ _| | __| | ___ _ __ 
|  ___/ | | | '_ \| | | | | |/ _` |/ _ \ '__|
| |   | |_| | |_) | |_| | | | (_| |  __/ |   
|_|    \__, |_.__/ \__,_|_|_|\__,_|\___|_|   
        __/ |                                
       |____/      
\u2728 Follow me on Github!:
\u2728 https://github.com/L0WK3Y-IAAN                                   
'''

done = False
log_file_path = 'compilation_log.txt'

def sanitize_filename(filename):
    return re.sub(r'[\\/*?:"<>|]', "", filename)


def animate():

    quotes = ['\u2615 Coffee break!', '\u2615 Time for a cup of Joe!']
    quote_to_display = random.choice(quotes)
    sys.stdout.write('\r{0}'.format(quote_to_display))


    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\r{0}'.format(c))
        sys.stdout.flush()
        sleep(0.1)


t = threading.Thread(target=animate)

# Color terminal text
def print_colored_text(text, color_code):
    print(f"\033[{color_code}m{text}\033[0m")
    return




# Check for required modules and commands 
modules = ['tkinter', 'cython']
software_names = ["cython3", "gcc", "pip"]
commands = [f"{name} --version" for name in software_names]
clear_cmd = 'cls' if os.name == 'nt' else 'clear'
os.system(clear_cmd)


def check_module(module):
    try:
        __import__(module)
        print_colored_text(f"\u2713 {module} Found!", 32)
    except ImportError or ModuleNotFoundError:
        print_colored_text(f"\u2717 {module} Not Found", 31)

def print_system_status(command, software_name):
    installation_command = f"sudo apt-get install {software_name.lower()}"
    package_installation_command = f"pip install {software_name.lower()}"

    try:
        subprocess.check_output(command, shell=True)
        print_colored_text(f"\u2713 {software_name} is installed!", 32)
    except subprocess.CalledProcessError:
        os.system(clear_cmd)
        print_colored_text(f"\u2717 Command '{command}' not found.", 31)
        print_colored_text(f"\u26A0 Installing '{software_name}'... ", 33)
        sleep(1)
        subprocess.call(installation_command, shell=True)
        subprocess.call(package_installation_command, shell=True)

def check_system_status():
    for module in modules:
        check_module(module)
    for command, software_name in zip(commands, software_names):
        print_system_status(command, software_name)

check_system_status()





try:
    # Clear screen
    os.system('cls' if os.name == 'nt' else 'clear')
    print_colored_text(logo, 34)
    print_colored_text("\u26A0 Opening file dialog...", 33)
    print("Select your Python (.py) script of choice.\n")
    sleep(1)


    # Open file selection dialog
    file_selection = askopenfilename()
    
    


    # Check if a file was selected
    if not file_selection:
        os.system('cls' if os.name == 'nt' else 'clear')
        print_colored_text(logo, 34)
        print_colored_text("\u26A0 No file selected. Exiting...", 33)
        sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        sys.exit(1)



    # Check if the selected file has a .py extension
    while not file_selection.endswith('.py'):
        print_colored_text("\u2717 {0} is not a .py file. Try again...".format(file_selection), 31)  
        file_selection = askopenfilename()
        


    os.system('cls' if os.name == 'nt' else 'clear')
    print_colored_text(logo, 34)
    print_colored_text("\u2713 File selected: {0}\n\n".format(file_selection), 32)
    
    output_file = input("Enter the name you would like for the output file: ")
    
    while output_file == "":
        os.system('cls' if os.name == 'nt' else 'clear')

        print_colored_text(logo, 34)
        print_colored_text("\u2713 File selected: {0}\n\n".format(file_selection), 32)

        print_colored_text("\u2717 You entered: {0}\n\n".format("No name detected. Please try again..."), 31)
        output_file = input("Enter the name you would like for the output file: ")

    
    print_colored_text("\u26A0 You entered: {0}\n\n".format(output_file), 33)

    if '\\/*?:"<>|' in output_file:
        print_colored_text("\n \u26A0 Invalid characters detected. Sanatizing file name...", 33)
    output_file = sanitize_filename(output_file)
        

    # Calling cython3 to convert to python script to Cython


    ### CURRENTLY BROKEN
    #Builds a shell script containing the commands used to compile the python script
    sh_builder='''#!/bin/sh
    
    cython3 {0} --embed

    # Set PYTHONLIBVER dynamically
    PYTHONLIBVER=python$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')$(python3-config --abiflags)

    # Execute the command
    gcc -Os $(python3-config --includes) {1} -o {2} $(python3-config --ldflags) -l$PYTHONLIBVER
    '''.format(shlex.quote(file_selection), shlex.quote(file_selection.replace('.py', '.c')), shlex.quote(output_file))

    # Open a shell file in write mode
    sh_file_path = os.path.join(os.path.dirname(__file__), 'gcc_shell.sh')  # Replace with the desired file path

    with open(sh_file_path, 'w') as file:
        print_colored_text("\u26A0 Executing compliation script...\n\n", 33)
        # Write content to the file
        file.write(sh_builder)
        subprocess.call(['chmod', '+x', sh_file_path])


    # Start loading thread
    t.start()
    



    # Execute the shell script then remove it and the Cython file
    try:
        result = subprocess.run([sh_file_path], check=True, capture_output=True, text=True)
        os.remove('gcc_shell.sh')
        os.remove(file_selection.replace('.py', '.c'))
        os.system('cls' if os.name == 'nt' else 'clear')

        if result.returncode != 0:
            print_colored_text("Error Occured: {0}".format(result.stderr), 31)

        # Write the result of the terminal to a log file
        with open(log_file_path, 'w') as log_file:
            log_file.write(f"Return Code: {result.returncode}\n")
            log_file.write("\n=== Standard Output ===\n")
            log_file.write(result.stdout)
            log_file.write("\n=== Standard Error ===\n")
            log_file.write(result.stderr)

        print_colored_text(logo, 34)
        print_colored_text("\u2713 Python compilation succeeded!", 32)
        print_colored_text("\u2713 Output File: {0}".format(os.path.join(os.path.dirname(__file__), output_file)), 32)
        done = True
        subprocess.call(["xdg-open", "{0}".format(os.path.join(os.path.dirname(__file__)))])

    except subprocess.CalledProcessError as e:
        os.remove('gcc_shell.sh')
        os.remove(file_selection.replace('.py', '.c'))
        print_colored_text(f"Command failed with return code {e.returncode}", 31)
        with open(log_file_path, 'w') as log_file:
            log_file.write(f"Return Code: {e.returncode}\n")
            log_file.write("\n=== Standard Output ===\n")
            log_file.write(e.stdout)
            log_file.write("\n=== Standard Error ===\n")
            log_file.write(e.stderr)
        done = True
        sys.exit(1)

# except KeyboardInterrupt:
except KeyboardInterrupt:
    os.system('cls' if os.name == 'nt' else 'clear')
    print_colored_text(logo, 34)
    done = True
    print_colored_text('Program Terminated...Exiting. \n \n', 31)

    sleep(1.3)

    os.system('cls' if os.name == 'nt' else 'clear')
    sys.exit(1)
