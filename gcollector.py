# This program was made to automate the process of cleaning up
#  your downloads folder
# Written in Python 3.7
# SageDark

import os
import glob
import os.path
import time

path = 'C:\\Users\\contr\\Downloads'
# timestamp equivalent to 31 days
timediff = 2592000

# get the number of files in the directory
onlyfiles = next(os.walk(path))[2]
print(len(onlyfiles))

# get a list with all filenames
filenames = glob.glob(path + "\\*")
modifiedFiles = 0
for files in range(len(onlyfiles)):
        if (time.time()) - os.path.getmtime(filenames[files]) > timediff:
            modifiedFiles += 1
            print(filenames[files])
print('Out of ' + str(len(onlyfiles)) + ' files, ' + str(modifiedFiles) + ' are older than 31 days.')


def get_date(filename):
    lastmodified = os.path.getmtime(path + '\\' + filename)
    print(lastmodified)
    return lastmodified


# get_date(filenames)
