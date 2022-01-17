# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
from PIL import Image



directory = 'C:/TEST/Cards/FF/Weapons'
#
#with os.scandir(directory) as files:
#    for file in files:

        
#        print(file)

files = os.listdir(directory)
sorted(files)
print(files)

for file in files:
    filewithpath = ('%s/%s') % (directory, file)
    img = Image.open(filewithpath)
#    img.show()
    wh = img.size
#    print(wh)
    img.crop((642, 70, 1824, 1976)).save(filewithpath)
#    img.crop((939, 2, 4951, 2740)).save(filewithpath)





