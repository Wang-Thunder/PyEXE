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


print("PyExe by: Wangthunder")
print("Package a Python script as an EXE with UPX compression.")
print("This package includes UPX 4.2.1 (github.com/upx/upx)")
print("-----------------")
print("Follow the prompts to quickly and easily package your ")

# Packaging type
packaging_type = get_input("Do you want to package as one EXE (f)ile, or one (d)irectory? (f/d): ", ["f", "d"])
pyinstaller_arg = "--onefile" if packaging_type == "f" else "--onedir"

# UPX directory
#upx_dir = f"--upx-dir \ "
upx_exe_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "upx.exe")
upx_dir = f"--add-data \"{upx_exe_path};.\""


# Script location
script_location = input("Location of Python script. If script is in the same directory as this terminal, just enter the script name: ")

# Finished EXE location
get_outputpath = get_input("Enter the output location for the EXE. If no output path is entered, it will use the current path in this terminal: ", blank_allowed=True)
if get_outputpath:
    outputpath = "--distpath \"" + (get_outputpath) + "\""

# Additional arguments
arguments = get_input("Enter any additional pyinstaller arguments you may have (such as --paths to add another directory or --add-data (\"""src;dest""\") to include additional files.) If you are unsure or do not require additional arguments, just enter (n): ", blank_allowed=True)
add_arguments = "" if arguments == "n" else arguments

# Construct command
command = f"pyinstaller {pyinstaller_arg} {upx_dir} {script_location} {outputpath} {add_arguments}"
print(f"Here is your command: {command}")

# Run command
run_command_prompt = get_input("Would you like to run this command now? (y/n): ", ["y", "n"])
if run_command_prompt == "y":
    try:
        subprocess.run(command, check=True, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

