# Windows Program Lock

The Windows Program Lock allowes to restrict the use of a program by time. 
This app aims at supporting **digital wellbeing** by restricting the use of entertainment apps.

The use of a program is prevented if you have spent a certain amount of time with the program and/or at certain clock times of the day.
This can be individually configured for each weekday.
If the amount of time allowed is exceeded or if the usage is not allowed at the current clock time, the program is closed.
A check if the program is running is executed every five minutes (can be configured).

Note: Currently, this is a very basic app without a graphical user interface for configuration. 

## Requirements
- requires python 3
- install python dependencies with 
  
```shell
pip install -r requirements.txt
```

## Setup
**1. Configuration**
- change the configuration in `src\settings.py`: 
  - configure times in which it is allowed to use the programm in `time_settings.py`:
  - edit the timespans in the `ALLOWED_TIME` dictionary
  - edit the maximum times spent with the program in the `MAX_ALLOWED_MINUTES` dictionary

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
Change your configuration in the source files and create a new .exe file.
After a restart, the new configuration is applied.

## Deinstallation
Delete the .exe file in the Windows autostart folder.
