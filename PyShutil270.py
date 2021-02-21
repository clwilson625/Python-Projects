import glob
import os
import datetime
import shutil

# Have to import glob, this matches patterns/rules, import os, provides functions for interacting
# import datetime, manipulating dates and times, import shutil, used to copy files from
# a source file to a destination file

def GetFileList(path, type):
    '''
    Return a list of filename matching the given path and file type
    '''
    return glob.glob(path + "*" + type)

# This area shows where the Source Folder and Destination (Modified) Folders are located

originPath = 'C:/Users/aarons/Desktop/Source/'
destinationPath = 'C:/Users/aarons/Desktop/Modified/'
fileType = ".txt"

# Create list of text filenames in Origin folder
fileList = GetFileList(originPath, fileType)

for file in fileList:
    # Get last modified date and todays date - using getmtime
    modifyDate = datetime.datetime.fromtimestamp(os.path.getmtime(file))
    todaysDate = datetime.datetime.today()
    
    filePathList = file.split("\\") # Create a list from the filepath
    filename = filePathList[-1] # The last element is a the filename
    
    # If modified within last 24 hours, then copy to destination folder
    modifyDateLimit = modifyDate + datetime.timedelta(days=1)

    # If the file was edited less then 24 hours ago then copy it
    if modifyDateLimit > todaysDate:
        shutil.copy2(file, destinationPath + filename)


from tkinter import Tk
from tkinter.filedialog import askdirectory
path = askdirectory(title='Select Folder') # shows dialog box and return the path
print(path)




