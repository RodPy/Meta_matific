import subprocess
from os import listdir
import pandas as pd

# path="TEST"
path="."

def ls(ruta = '.'):
    return listdir(ruta)




for x in ls(path):
    df = pd.read_excel(f"{path}\{x}")
    if df.shape[1] > 11:
        print("redimensionar.. ")
        df=df.iloc[:,1:]
        aux=x[:-5]
        df.to_excel(f"{aux}.xlsx", index=False)
        val=f"{path}\{aux}"
        print(f"{x} LISTO ----> {val}")

# print (type(ls(path)))

for x in ls(path):
    subprocess.run(["python", "..\matific_generator.py", f"{path}\{x}"], shell=True)
#   subprocess.run(["python", "matific_generator.py", f"{path}\{x}"], shell=True)
#     subprocess.run(["python",".\matific_generator.py","TEST\op.xlsx"],shell=True)


# for i in range(0,2):
#     subprocess.call(['mkdir',f"{i}"],shell=True)

