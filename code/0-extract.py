# -*- coding: utf-8 -*-
"""
"Cross-Domain Topic Classification for Political Texts"
Moritz Osnabruegge, Elliott Ash, Massimo Morelli

This script extracts the files.
"""


import os
import zipfile


#Specify working directory
os.chdir("")

directory =  os.getcwd()

for file in os.listdir(directory):
    if zipfile.is_zipfile(file): 
        with zipfile.ZipFile(file) as item: 
           item.extractall()  

