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
#   PyBuilder aims to automate the conversion of   #
#   Python scripts to ELF or EXE binaries using    #   
#   Cython3 and GCC. Currently this script only    #
#   to ELF. Stay tuned for updates :)              #
#                                                  #   
#                                                  #
####################################################                                                            
                                                      
Follow me on Github!:
https://github.com/L0WK3Y-IAAN
'''

import os
import sys
import subprocess
import itertools
import threading
import tkinter as tk
from time import sleep
from tkinter.filedialog import askopenfilename


logo='''
  _____       _           _ _     _           
 |  __ \     | |         (_) |   | |          
 | |__) |   _| |__  _   _ _| | __| | ___ _ __ 
 |  ___/ | | | '_ \| | | | | |/ _` |/ _ \ '__|
 | |   | |_| | |_) | |_| | | | (_| |  __/ |   
 |_|    \__, |_.__/ \__,_|_|_|\__,_|\___|_|   
         __/ |                                
        |___/      
\u2728 Follow me on Github!:
\u2728 https://github.com/L0WK3Y-IAAN                                   
'''

done = False
log_file_path = 'compilation_log.txt'


def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rloading ' + c)
        sys.stdout.flush()
        sleep(0.1)

t = threading.Thread(target=animate)

# Color terminal text
def print_colored_text(text, color_code):
    print(f"\033[{color_code}m{text}\033[0m")
    return


try:
    # Clear screen
    os.system('cls' if os.name == 'nt' else 'clear')
    print_colored_text(logo, 34)
    print("To get started press the enter key and a file dialog window will appear allow you to select your Python script of choice.\n")
    print_colored_text("Press Enter to continue...", 32)
    input("")


    # Open file selection dialog
    file_selection = askopenfilename()
    


    # Check if a file was selected
    if not file_selection:
        os.system('cls' if os.name == 'nt' else 'clear')
        print_colored_text(logo, 34)
        print_colored_text("No file selected. Exiting...", 33)
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

    
    print_colored_text("You entered: {0}\n\n".format(output_file), 33)

    # Calling cython3 to convert to python script to Cython
    t.start()
    subprocess.call(['cython3', file_selection, '--embed'])

    #Builds a shell script containing the commands used to compile the python script
    sh_builder='''#!/bin/sh

    # Set PYTHONLIBVER dynamically
    PYTHONLIBVER=python$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')$(python3-config --abiflags)

    # Execute the command
    gcc -Os $(python3-config --includes) {0} -o {1} $(python3-config --ldflags) -l$PYTHONLIBVER
    '''.format(file_selection.replace('.py', '.c'), output_file)

    # Open a shell file in write mode
    sh_file_path = os.path.join(os.path.dirname(__file__), 'gcc_shell.sh')  # Replace with the desired file path
    with open(sh_file_path, 'w') as file:
        print_colored_text("Executing compliation script...\n\n", 33)
        # Write content to the file
        file.write(sh_builder)
        subprocess.call(['chmod', '+x', sh_file_path])



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
        log_file.write(f"Return Code: {result.returncode}\n")
        log_file.write("\n=== Standard Output ===\n")
        log_file.write(result.stdout)
        log_file.write("\n=== Standard Error ===\n")
        log_file.write(result.stderr)
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