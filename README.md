Galaxy Background
================

![Sample Background](https://github.com/dorian-adams/Nasa_Background/blob/master/screenshot.png)

Galaxy Background utilizes NASA's Photo of the Day API to set your Window's desktop background to the best photos in the galaxy. :rocket:

## Features
Utilizes:

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

## Relevant Docs and Info
* [ctypes](https://docs.python.org/3/library/ctypes.html)
* [SystemParametersInfoW function](https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-systemparametersinfow)
* [Apply Changes Permanently or Temporarily](https://devblogs.microsoft.com/oldnewthing/20160721-00/?p=93925)

## License
