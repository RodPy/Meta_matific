import pandas as pd
from sys import argv
import matific_generator as mg
import os


script, workbook = argv
## Path de carpeta
os.makedirs('Escuela', exist_ok=True)
df_sheets = pd.ExcelFile(workbook , engine="openpyxl")
i=0
for elem in df_sheets.sheet_names:
    i+=1
    df = pd.read_excel(workbook, engine="openpyxl", sheet_name=elem)
    df.to_excel(f"Escuela\{elem}.xlsx")
    print(f"Procesando {i} de "+str (len(df_sheets.sheet_names)))
