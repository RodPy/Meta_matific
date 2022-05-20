import pandas as pd
from sys import argv
import os


script, archivo = argv


workbook = archivo

df_sheets = pd.ExcelFile(workbook , engine="openpyxl")

for elem in df_sheets.sheet_names:
    df = pd.read_excel(workbook, engine="openpyxl", sheet_name=elem)
    df.to_excel(f"{elem}.xlsx")