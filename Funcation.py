import tkinter as tk
from tkinter import  ttk
import json
import datetime
from pprint import pprint
import time
import math
import csv


import pandas as pd

# Read the first sheet of the Excel file
df = pd.read_excel('Trail.xlsx')
print(df)

























def update_name_and_phone_number(name_of_the_csv):

    
    with open(name_of_the_csv, 'r') as file:
        reader = csv.reader(file)
        with open("DB_Main.json","r") as jsons:
            DB_main = json.load(jsons)
            for row in reader:
                pass#if DB_main[f"A{row[0][1:]}"]:
    
 

#update_name_and_phone_number("Untitled spreadsheet - Sheet1.csv")

# Code Depoy_1:

def Create_database_for_10000():
    DB = {}
    for i in range(9999):
        if i>999:
            DB[f"A{i}"]={"Status":"Close"}
        elif i>99:
            DB[f"A0{i}"]={"Status":"Close"}
        elif i>9:
            DB[f"A00{i}"]={"Status":"Close"}
        else:
            DB[f"A000{i}"]={"Status":"Close"}

    with open("DB_Main.json", "w") as creating_db:
        json.dump(DB, creating_db, indent=5, sort_keys=True)

#Create_database_for_10000()


