# encoding: utf-8


# WORKING BUT DOES NOT HANDLE FILES WITH PARENTHESE CHARACTERS AND SPACES


# 🔵 Create a web server that automatically converts the python files that a user uploads and sends it back to them.
# 🔴 Add Mac OS X alternative commands
# 🔴 Add Windows version of script
# 🔴 Pull programmer quotes from the web for loading animation (requires requests module)
# 🟢 Add multi-file upload
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
import uuid
import shlex
import shutil
import random
import itertools
import threading
import subprocess
import tkinter as tk
from time import sleep
from tkinter.filedialog import askopenfilenames



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
    return re.sub(r'[\\/*?:"<>|()!@#$%^&`~ ]', "_", filename)


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




def sanitize_and_rename_file(file_path):



    # Extract the directory and file name from the file path
    directory, filename = os.path.split(file_path)

    # If the original filename is empty, generate a unique filename
    if not filename:
        filename = f"untitled_{uuid.uuid4().hex}"

    # Remove invalid characters from the file name
    sanitized_filename = re.sub(r'[\\/*?:"<>|()!@#$%^&`~]', "", filename)

    # Check if the filename only contains '.py'
    if sanitized_filename.lower() == '.py':
        # Append a unique identifier

        #🔴CHANGE TO FILE HASH INSTEAD
        sanitized_filename = f"_{uuid.uuid4().hex}{sanitized_filename}"

    # Replace spaces with underscores
    sanitized_filename = shlex.quote(sanitized_filename.replace(" ", "_"))


    # Construct the new file path with the sanitized name
    new_file_path = os.path.join(directory, sanitized_filename)

    # Rename the file
    shutil.move(file_path, new_file_path)

    return new_file_path


def sanitize_and_rename_files(file_paths):
    sanitized_paths = []
    for file_path in file_paths:
        sanitized_path = sanitize_and_rename_file(file_path)
        sanitized_paths.append(sanitized_path)
    return sanitized_paths



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
    print("Select your Python (.py) script(s) of choice.\n")
    sleep(.3)

    # Open file selection dialog for multiple files
    filez = askopenfilenames()


    # Check if any files were selected
    if not filez:
        os.system('cls' if os.name == 'nt' else 'clear')
        print_colored_text(logo, 34)
        print_colored_text("\u26A0 No files selected. Exiting...", 33)
        sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        sys.exit(1)

    # Check if the selected files have .py extensions
    for file_selection in filez:
        while not file_selection.endswith('.py'):
            print_colored_text("\u2717 {0} is not a .py file. Try again...".format(file_selection), 31)
            filez = askopenfilenames()
            file_selection = filez[0]

    os.system('cls' if os.name == 'nt' else 'clear')
    print_colored_text(logo, 34)
    print_colored_text("\u2713 Files selected:\n{0}\n\n".format('\n'.join(filez).replace(" ", "\\ ")), 32)

    # Start animation thread
    t.start()

    # Sanitize and rename selected files and output files
    sanitized_file_paths = sanitize_and_rename_files(filez)


    output_files = []

    # Iterate over sanitized files and generate unique output files and shell script paths
    for selected_file in sanitized_file_paths:
        output_file = os.path.splitext(os.path.basename(selected_file))[0]

        if '\\/*?:"<>|()!@#$%^&`~ ' in output_file:
            print_colored_text("\n \u26A0 Invalid characters detected. Sanitizing file name...", 33)
        output_file = sanitize_filename(output_file)

        output_files.append(output_file)

    # Iterate over sanitized files and their corresponding output_files
    for selected_file, output_file in zip(sanitized_file_paths, output_files):
        # Calling cython3 to convert to python script to Cython
        # Build a unique shell script containing the commands used to compile each Python script
        # Generate the Cython C file explicitly
        
        escaped_output_file = output_file.replace(" ", "\\ ")
        escaped_selected_file = selected_file.replace(" ", "\\ ")

        cython_command = f'cython3 "{selected_file}" --embed'

        # Set PYTHONLIBVER dynamically
        PYTHONLIBVER = f'''python$(python3 -c "import sys; print('.'.join(map(str, sys.version_info[:2])))")$(python3-config --abiflags)'''

        # Corrected gcc command
        gcc_command = f'gcc -Os $(python3-config --includes) "{selected_file}" -o "{output_file}" $(python3-config --ldflags) -l{PYTHONLIBVER}'

        # Combine the commands into a shell script
        sh_builder = f'''#!/bin/sh

        {cython_command.replace(selected_file, escaped_selected_file)}
        {gcc_command.replace(output_file, escaped_output_file).replace('.py', '.c')}
        '''


        # Open a shell file in write mode
        sh_file_path = os.path.join(os.path.dirname(__file__), f'gcc_shell_{output_file}.sh')
     
        with open(sh_file_path, 'w') as file:
            print_colored_text(f"\n\u26A0 Executing compilation script for {selected_file}...\n\n", 33)
            # Write content to the file, wrapping file paths in double-quotes
            file.write(sh_builder)
            subprocess.call(['chmod', '+x', sh_file_path])

        # Execute the shell script then remove it and the Cython file
        try:
            result = subprocess.run([sh_file_path], check=True, capture_output=True, text=True)
            os.remove(sh_file_path)  # Remove the unique shell script
            os.remove(selected_file.replace('.py', '.c'))
            # os.system('cls' if os.name == 'nt' else 'clear')
            done = True

            # ...

        except subprocess.CalledProcessError as e:
            # os.remove(sh_file_path)  # Remove the unique shell script
            # os.remove(selected_file.replace('.py', '.c'))
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
