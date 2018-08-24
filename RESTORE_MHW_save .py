# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 10:55:01 2018

@author: Jotun
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 12:25:16 2018

@author: Thibaud
"""
#Importing necessary stuff
import shutil
import tkinter, tkinter.filedialog
root = tkinter.Tk()
root.withdraw()

#Get the backup save file from user
defaultPath="E:/SaveGames/MHW/" 
saveFile = tkinter.filedialog.askopenfilename(initialdir = defaultPath, title = "Please select save file to restore",filetypes = ())
if "SAVEDATA1000" in saveFile:
   print ("You chose {0} as your save file to restore".format(saveFile))

else:
   print ("Please select a valid save file")

#restore save into steam directory
defaultSteamPath="E:/Program Files (x86)/Steam/userdata/00000000/582010/remote"
savePath= tkinter.filedialog.askdirectory (parent= root, initialdir= defaultSteamPath, title= "Please select Steam directory to restore save file")
if len(savePath) > 0:
    print ("You chose {0} as your directory for backups".format(savePath))
    
else:
    print ("Please select a valid directory")

shutil.copy2 (saveFile, savePath)

