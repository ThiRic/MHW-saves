# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 12:25:16 2018

@author: Jotun
"""
#Importing necessary stuff
import os
import datetime
import shutil
import tkinter, tkinter.filedialog
root = tkinter.Tk()
root.withdraw()

#Get the back up desitnation directory from user
backupPath= tkinter.filedialog.askdirectory (parent= root, initialdir="/", title= "Please select directory for save backups")
if len(backupPath) > 0:
    print ("You chose {0} as your directory for backups".format(backupPath))
    
else:
    print ("Please select a valid directory")
    
now = datetime.datetime.now() #simplification for dirName
dirName= '{0}_{1}_{2}_{3}{4}'.format(now.day, now.month, now.year, now.hour, now.minute) #the name of the folder will be day_month_year_hourminute

try:
    # Create target Directory and all required directories in between
    os.makedirs("{0}/SaveGames/MHW/{1}".format(backupPath, dirName))
    print("Directory " , dirName ,  " created ") 

except FileExistsError:
    print("Directory " , dirName ,  " already exists")

#Get the original save file from user
defaultSteamPath="E:/Program Files (x86)/Steam/userdata/00000000/582010/remote"

saveFile = tkinter.filedialog.askopenfilename(initialdir = defaultSteamPath, title = "Please select save file to back up",filetypes = ())
if "SAVEDATA1000" in saveFile:
   print ("You chose {0} as your save file to back up".format(saveFile))

else:
   print ("Please select a valid save file")

shutil.copy2 (saveFile, "{0}/SaveGames/MHW/{1}".format(backupPath, dirName))



