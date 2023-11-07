# Windows Program Lock

## Requirements
- requires python 3
- install python dependencies with 
  
```shell
pip install -r requirements.txt
```

## Setup
**1. Configuration**
- configure program to lock in `src/programlock.py`: change .exe name in the variable `PROGRAM` to the program that you want to lock
- configure times in which it is allowed to use the programm in `time_settings.py`:
  - edit the timespans in the `ALLOWED_TIME` dictionary
  - do not remove a day entry from the dictionary
  - stay to the format of the example

**2. Installation**
- create executable: 
```shell
python -m PyInstaller --onefile src\programlock.py
```
- move the file `programlock.bat` to the Windows autostart folder: 
  - Windows + R
  - enter: `shell:startup` -> autostart folder is opened automatically
  - copy-paste the file to the autostart folder
- restart the computer for activation of the programlock app

## Change configuration
Change your configuration in the source files, create a new .exe file and replace the old .exe with the new one in the Windows autostart folder.

## Deinstallation
Delete the .exe file in the Windows autostart folder.
