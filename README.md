NASA Background
================

![Sample Background](https://github.com/dorian-adams/Nasa_Background/blob/master/screenshot.png)

NASA Background utilizes NASA's Photo of the Day API to automatically set your Window's wallpaper to the best photos in the galaxy. :rocket:

## Features
**Utilizes:**
* Python
    * ctypes
    * PIL
    * API get via requests
    * Windows API

Downloads NASA's Photo of the Day, based on the current date, along with the associated text description. Resizes the photo to your monitor's resolution, then appends the text description to the photo via PIL, and finally applies it as your desktop background.

## Getting Started
**Requirements:**
* Windows 7, 8, or 10
* Python 3.x
* PIL 9.x
* requests 2.x
* Note: the script must be run from a global Python environment, due to limitations with Window's API, otherwise changes to the background will be lost on reboot. 

## Installation
1. Download the script, `Nasa_Background.py`, to the directory of your choosing.
2. Get your personal API key at (https://api.nasa.gov/).
3. Setup your environment variable for your API key.
* Open your control panel.
* Navigate to System and Security and then select 'System'.
* Scroll down and select 'Advanced system settings'.
* Select 'Environment variables'.
* Create a new user variable.
* Variable name should be as follows: `NASA_API_KEY`
* Variable value: copy and paste the unique API key you created earlier here.
4. To have the script run automatically, perform the following:
* Open Windows Task Scheduler.
* Create Task
* Name the task whatever you prefer.
* Under 'configure for', select the OS you're running on.
* Select 'run with highest privileges.
* Now, navigate to the 'Triggers' tab and configure when you want the script to run. I recommend choosing 'At startup' from the drop-down menu and delay task for 1 minute, to give your internet time to fully boot.
* Next, navigate to the 'Actions' tab. Create a new action, 'start a program'.
* Program script: paste the full path to your global Python exe.
* Add arguments: paste the full path to the `Nasa_Background.py` script.

## Relevant Docs and Info
* [ctypes](https://docs.python.org/3/library/ctypes.html)
* [SystemParametersInfoW function](https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-systemparametersinfow)
* [Apply Changes Permanently or Temporarily](https://devblogs.microsoft.com/oldnewthing/20160721-00/?p=93925)

## License
