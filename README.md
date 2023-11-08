# Windows Program Lock

The Windows Program Lock allowes to restrict the use of a program by time. 
This app aims at supporting **digital wellbeing** by restricting the use of entertainment apps.

The use of a program is prevented if you have spent a certain amount of time with the program and/or at certain clock times of the day.
This can be individually configured for each weekday.
If the amount of time allowed is exceeded or if the usage is not allowed at the current clock time, the program is closed.
A check if the program is running is executed every minute (can be configured).

*Note: Currently, this is a very basic app without a graphical user interface for configuration.*

## Requirements
- requires python 3
- install python dependencies with 
  
```shell
pip install -r requirements.txt
```

## Setup
**1. Configuration**
- change the configuration in `src\settings.py`. The variables are already filled with example configurations. Just replace them and adapt it to your needs.
  - configure which program should be controlled. Example:
    ```python
    # the program that is to be locked
    PROGRAM="steam.exe" 
    ```
  - configure the times in which it is allowed to use the program:
    - edit the allowed timespans in the `ALLOWED_TIME` dictionary.  
    Example configuration:
    ```python
        # define when the program is allowed to run.
        "ALLOWED_TIME": {
            "Monday": ("00:00", "00:00"), # the program use is not allowed on Monday    
            "Tuesday": ("19:30", "22:15"), # allowed from 19:30 -to 22:15
            "Wednesday": ("19:30", "22:15"), 
            "Tuesday": ("19:30", "22:15"),
            "Friday": ("14:30", "23:59"),
            "Saturday": ("00:00", "23:59"), # allowed for the whole day
            "Sunday": ("00:00", "23:59"), 
        },
    ```
    - edit the maximum times spent with the program in the `MAX_ALLOWED_MINUTES` dictionary. Example configuration:
    ```python
        # define how long the program is allowed to run (in minutes)
    "MAX_ALLOWED_MINUTES": {
        "Monday": 0, # the program use is not allowed on Monday
        "Tuesday": 24*60, # the program is allowed to run 24 hours
        "Wednesday": 24*60,
        "Tuesday": 24*60,
        "Friday": 24*60,
        "Saturday": 3*60, # the program is allowed to run max. 3 hours
        "Sunday": 180 # the program is allowed to run max. 3 hours
      },
    ```

**2. Installation**
- create executable (.exe file) - this command will create an executable `dist\programlock.exe`: 
```shell
python -m PyInstaller --windowed --onefile src\programlock.py
```
- create a shortcut to the .exe file
  - right-click on `py-program-lock\dist\programlock.exe` and select "create shortcut"
  - rename the shortcut file as you wish, e.g. `ProgramLock`
- move your shortcut file to the Windows autostart folder: 
  - Windows + R
  - enter: `shell:startup` -> autostart folder is opened automatically
  - copy-paste the file to the autostart folder
- restart the computer for activation of the autostart programlock app

## Change configuration
Change your configuration in the source files as described above and create a new .exe file. After a restart, the new configuration is applied.

## Deinstallation
Delete the programlock shortcut file in the Windows autostart folder.

## Limitations

- Currently, there is no GUI for configurations.
- Currently, only one program can be controlled (with one .exe).
