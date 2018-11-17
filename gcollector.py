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


# function that gets the modification date
# of the file and calculates how  many days ago it was modified
def get_date(filename):
    lastmodified = (time.time()) - os.path.getmtime(filenames[files])
    return lastmodified


def remove_file(filename):
    os.remove(filename)
    print(filename + ' removed.')


# get a list with all filenames
filenames = glob.glob(path + "\\*")
modifiedFiles = 0
for files in range(len(onlyfiles)):
        if get_date(filenames[files]) > timediff:
            modifiedFiles += 1
            remove_file(filenames[files])
print('Out of ' + str(len(onlyfiles)) + ' files, ' + str(modifiedFiles) + ' are older than 31 days.')
