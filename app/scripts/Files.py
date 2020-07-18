# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 23:12:35 2020

@author: SERGI
"""
from json import load, dump

class Files:

    def __init__(self):
        '''
        Returns
        -------
        None.

        '''
        pass
    
    def readConfig():
        with open("config.json", "r") as file:
            return load(file)
    
    def readJson(file_name):
        with open("./app/resources/"+file_name, "r") as file:
            return load(file)

    def writeJson(file_name, users_strikes):
        with open("./app/resources/"+file_name, "w") as file:
            dump(users_strikes, file)