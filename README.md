# PyEXE
A simple program to package Python files as a Windows executable using Pyinstaller with UPX compression.

Instructions:

**1)** Ensure that you have installed Pyinstaller:

   ```pip install -U pyinstaller```

**2)** Download either the standalone executable (which comes packaged with UPX) or the python script, whichever you prefer. If you use the python script, download UPX (https://github.com/upx/upx) and place it in the same directory as the script.

**3)** Run the program/script and follow the on screen prompts:

   **Packaging type:** Select either one file (a single executable) or one directory (a folder with dependancies and the executable separate.)
   **Script location:** Enter the location of the script you want to package. If the script is in the same directory as PyEXE, you can just hit enter.
   **Output location:** Enter the desired output location for the finished package. If you select none it will be placed in the same directory as PyEXE.
   **Additional Arguments:** Enter any additional Pyinstaller arguments (a list can be found at https://pyinstaller.org/en/stable/usage.html#options). For simple scripts, enter n for no additional arguments.
   **Display command:** After entering your parameters PyEXE will display your complete build command and give you the option to run command now. If you select yes, it will run the displayed command in the current console.


This program is *not* necessary to use either Pyinstaller or UPX. This is mostly helpful for people that are new to Python or are lazy ;) 
