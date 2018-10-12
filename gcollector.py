#this program was made to automate the process of cleaning up your downloads folder
#Written in Python 3.7
#SageDark

import os
import glob

path = 'C:\\Users\\USER\\Downloads'

#get the number of files in the directory
onlyfiles = next(os.walk(path))[2]
print (len(onlyfiles))

#get a list with all filenames
filenames = glob.glob(path + "\\*")

def get_date(filename):
    lastmodified = os.path.getmtime(path + '\\' + filename)
    return lastmodified


for files in range(len(onlyfiles)):
    print (filenames[files])
