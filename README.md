# MHW-saves
Two very simple python 3 scripts to back up and restore a saved game for Monster Hunter World PC.

These scripts require Python 3, please install it before using these scripts.
You can download Python 3 at https://www.python.org/download/releases/3.0/

=====================================================================================

Back up your saves:

1) Open BACKUP_MHW_save.py with a text editor
2) Go to line 35 and change defaultPath from "E:/Program Files (x86)/Steam/userdata/00000000/582010/remote" to your own path (E: and the directory inside userdata, here referred to "00000000" will be different).
3) Save the script
4) Install Python 3.6.x (skip this step if you already have Python)
5) Open BACKUP_MHW_save.py with Python and follow the instructions

All the saves are stored within a directory with the name day_month_year_hourminute.


=====================================================================================

Restore a save file:

1) Open RESTORE_MHW_backup.py with a text editor
2) Go to line 21 and change defaultPath from "E:/SaveGames/MHW/" by default to your own path (the one generated by the previous script BACKUP_MHW_save.py).
3) Go to line 30 and change defaultSteamPath from "E:/Program Files (x86)/Steam/userdata/00000000/582010/remote" to your own path that you have already set at step 2) of BACKUP_MHW_save.py.
4) Save the script
5) Open RESTORE_MHW_backup.py with Python and follow the instructions

You do not have to edit the scripts with a text editor once you have changed the destination of your save and their original directory.
Just run BACKUP_MHW_save.py to back up a file and BACKUP_MHW_save.py to choose a file to restore. 
