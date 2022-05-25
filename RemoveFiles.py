from importlib.metadata import files
from logging import root
import time
import os
import shutil

path = input('Enter folder path here: ')
days = int(input('Enter number of days here: '))

seconds = days*24*60*60
print(seconds)

isExist = os.path.exists(path)
print(isExist)

if isExist:
   for root, dirs, files in os.walk(path):
       print(root)

       dirs[:] = [d for d in dirs if not d.startswith('.')]

       for dir in dirs:
           print(os.path.join(root, dir))

       for file in files:
           print(os.path.join(root, file))
           fileOrigin = os.stat(path).st_ctime
           print(fileOrigin)

           if fileOrigin > seconds:
               os.remove(file)

           else:
               print('File not removed')

else:
    print('Path not found')