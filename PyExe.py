#PyExe 1.1 - By: Wangthunder
#CC BY-NC 4.0: Non Commercial Use - With Attribution
#Updated: 9-28-24

import subprocess
import os

def get_input(prompt, options=None, blank_allowed=False):
    user_input = input(prompt)
    if options and user_input not in options:
        print(f"Invalid option. Please choose from {options}")
        return get_input(prompt, options, blank_allowed)
    elif not user_input and blank_allowed:
        return os.getcwd()  # Return the current directory if input is blank
    elif not user_input:
        print("Input is required. Please try again.")
        return get_input(prompt, options, blank_allowed)
    return user_input
    
def read_upx_directory():
    try:
        with open('directories.txt', 'r') as file:
            return file.readline().strip()  # Checks first line
    except FileNotFoundError:
        return None

def save_upx_directory(directory):
    with open('directories.txt', 'w') as file:
        file.write(directory)


print("Package a Python script as an EXE with UPX compression.")
print("---------------------------")
print("Example with no console, upx compression, one file, and additional icons: pyinstaller --onefile --windowed --upx-dir path_to_upx --add-data \"E_PA.ico; \" --add-data \"trashcan_icon.png;.\" EPA.py")
print("---------------------------")
print("Other arguments: --windowed _will not open the python console window when running the exe_, --clean _will clear existing PyExe cache/install files before building_ OTHER: pyinstaller --help will provide a list of commands.")
print("---------------------------")

# Packaging type
packaging_type = get_input("Do you want to package as one EXE (f)ile, or one (d)irectory? (f/d): ", ["f", "d"])
pyinstaller_arg = "--onefile" if packaging_type == "f" else "--onedir"

# UPX directory
upx_directory = read_upx_directory()

if upx_directory:
    upx_change = get_input(f"WT- My Directory is: C:\\Programming\\UPX-EXE-Compressor | Current UPX directory is '{upx_directory}'. Change it? (y/n): ", ["y", "n"])
    if upx_change == "y":
        upx_directory = input(f"Please enter new directory for UPX. It will use the default directory located here otherwise[['{upx_directory}']]: ")
        save_upx_directory(upx_directory)
else:
    upx_directory = input("Enter new UPX directory: ")
    save_upx_directory(upx_directory)

upx_dir = f"--upx-dir \"{upx_directory}\""

# Script location
script_location = input("Location of Python script: ")
script_path = "\"" + (script_location) + "\""

# Finished EXE location
get_outputpath = get_input("Enter the output location for the EXE. If no output path is entered, it will use the current path in this terminal: ", blank_allowed=True)
if get_outputpath:
    outputpath = "--distpath \"" + (get_outputpath) + "\""

# Windowed Argument
window_arg = get_input("Do you want to use the --window argument? This will hide the console window that normally pops up when you run the exe. (y)es or (n)o: ", ["y", "n"])
window_pref = "--windowed" if window_arg == "y" else ""

# Construct command
command = f"pyinstaller {pyinstaller_arg} {window_pref} {upx_dir} {outputpath} {script_path}"
print(f"Here is your command: {command}")

# Run command
run_command_prompt = get_input("Would you like to run this command now? (y/n): ", ["y", "n"])
if run_command_prompt == "y":
    try:
        subprocess.run(command, check=True, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

