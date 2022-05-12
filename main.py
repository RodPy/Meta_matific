.pyimport pandas as pd
from sys import argv

#
script, archivo, archivo2 = argv

df = pd.read_csv(archivo)
# df = pd.read_csv("file.csv")
Grados = {'1': '1ero', '2': '2do', '3': '3ero', '4': "4to", '5': "5to", '6': "6to", '7': "7mo"}
Paises = {'PY': 'Paraguay', 'AR': 'Argentina'}
Documentos = {'DE': 'Documento Extranjero', 'CI': 'Cedula de Identidad'}
df2 = df.copy()
df2 = df2.replace({'Nacionalidad': Paises, 'Tipo de documento': Documentos})
df2 = df2.drop(columns=["Sexo", "Correo electrónico", 'F. Nacimiento', 'Pertenezco a una institución pública',
                        'Pertenezco a una institución Subvencionada', 'Pertenezco a una institución privada', 'Rol',
                        "Tiene discapacidad"])


df3 = pd.read_excel(archivo2)
data = {"Nacionalidad": df2["Nacionalidad"],
        'Tipo de documento': df2["Tipo de documento"],
        "Escuela": df3['Nombre de la institución'][0],
        "Nombre": df2["Nombre"],
        "Apellido": df2["Apellido"],
        "Contrasena": "Meta2022",
        'F. Nacimiento': df['F. Nacimiento'],
        'Sexo': df['Sexo'],
        'Grado': str(df3['Grado'][0]).strip(),
        'Tiene discapacidad': df['Tiene discapacidad'],
        }
df5 = pd.DataFrame(data)
df5 = df5.replace({'Grado': Grados})

fichero1=str(df5['Escuela'][0])+str(df5['Grado'][0])
df5.to_excel(f"Full_{fichero1}.xlsx", index=False)
df2.to_excel(f"{fichero1}.xlsx", index=False)
