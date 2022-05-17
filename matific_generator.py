import pandas as pd
import datetime
import fuzzywuzzy as fz
from fuzzywuzzy import process
import re
from unicodedata import normalize
from sys import argv



#Funciones
tipo = lambda x, a: 'SI' if (x == f"{a}") else 'NO'


def formatString(x):
    return x.title().replace(".", "").replace('"', "").replace(",", "").rstrip().lstrip()

## Formateo de Eliminacion de acentos
def formatNorm(s):
    s = re.sub(r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+", r"\1",normalize("NFD", s), 0, re.I)
    return normalize('NFC', s)

def genFecha(a):
    currentDateTime = datetime.datetime.now()
    date = datetime.date.today()
    gradoAnos={'1':'7','2':'8','3':'9','4':'10','5':'11','6':'12','8':'13'}
    for key in gradoAnos:
        if key==str(a):
            x=gradoAnos[key]
    ano=date.year-int(x)
    return f"01/01/{ano}"

def genIADoc(x):
    aprox=process.extractOne(x,setDoc)
    print (aprox)
    return aprox[0]
def genIAPais(x):
    aprox=process.extractOne(x,setPais)
    print (aprox)
    return aprox[0]

## Diccionarios
setDoc=['Certificado de Nac',"Oficina","Cedula de Identidad"]
setPais=['Paraguay','Argentina','Documento Extranjero']
gradoAnos={'1':'6','2':'7','3':'8','4':'9','5':'10','6':'11','8':'12'}
Paises = {'PY': 'Paraguay', 'AR': 'Argentina', 'DE': 'Documento Extranjero'}
Nacionalidades = {'Paraguaya': 'PY', 'Afghanistan': 'AF',
                  'Albania': 'AL',
                  'Algeria': 'DZ',
                  'American Samoa': 'AS',
                  'Andorra': 'AD',
                  'Angola': 'AO',
                  'Anguilla': 'AI',
                  'Antarctica': 'AQ',
                  'Antigua and Barbuda': 'AG',
                  'Argentina': 'AR',
                  'Armenia': 'AM',
                  'Aruba': 'AW',
                  'Australia': 'AU',
                  'Austria': 'AT',
                  'Azerbaijan': 'AZ',
                  'Bahamas': 'BS',
                  'Bahrain': 'BH',
                  'Bangladesh': 'BD',
                  'Barbados': 'BB',
                  'Belarus': 'BY',
                  'Belgium': 'BE',
                  'Belize': 'BZ',
                  'Benin': 'BJ',
                  'Bermuda': 'BM',
                  'Bhutan': 'BT',
                  'Bolivia, Plurinational State of': 'BO',
                  'Bonaire, Sint Eustatius and Saba': 'BQ',
                  'Bosnia and Herzegovina': 'BA',
                  'Botswana': 'BW',
                  'Bouvet Island': 'BV',
                  'Brazil': 'BR',
                  'British Indian Ocean Territory': 'IO',
                  'Brunei Darussalam': 'BN',
                  'Bulgaria': 'BG',
                  'Burkina Faso': 'BF',
                  'Burundi': 'BI',
                  'Cambodia': 'KH',
                  'Cameroon': 'CM',
                  'Canada': 'CA',
                  'Cape Verde': 'CV',
                  'Cayman Islands': 'KY',
                  'Central African Republic': 'CF',
                  'Chad': 'TD',
                  'Chile': 'CL',
                  'China': 'CN',
                  'Christmas Island': 'CX',
                  'Cocos (Keeling) Islands': 'CC',
                  'Colombia': 'CO',
                  'Comoros': 'KM',
                  'Congo': 'CG',
                  'Congo, the Democratic Republic of the': 'CD',
                  'Cook Islands': 'CK',
                  'Costa Rica': 'CR',
                  'Country name': 'Code',
                  'Croatia': 'HR',
                  'Cuba': 'CU',
                  'Curaçao': 'CW',
                  'Cyprus': 'CY',
                  'Czech Republic': 'CZ',
                  "Côte d'Ivoire": 'CI',
                  'Denmark': 'DK',
                  'Djibouti': 'DJ',
                  'Dominica': 'DM',
                  'Dominican Republic': 'DO',
                  'Ecuador': 'EC',
                  'Egypt': 'EG',
                  'El Salvador': 'SV',
                  'Equatorial Guinea': 'GQ',
                  'Eritrea': 'ER',
                  'Estonia': 'EE',
                  'Ethiopia': 'ET',
                  'Falkland Islands (Malvinas)': 'FK',
                  'Faroe Islands': 'FO',
                  'Fiji': 'FJ',
                  'Finland': 'FI',
                  'France': 'FR',
                  'French Guiana': 'GF',
                  'French Polynesia': 'PF',
                  'French Southern Territories': 'TF',
                  'Gabon': 'GA',
                  'Gambia': 'GM',
                  'Georgia': 'GE',
                  'Germany': 'DE',
                  'Ghana': 'GH',
                  'Gibraltar': 'GI',
                  'Greece': 'GR',
                  'Greenland': 'GL',
                  'Grenada': 'GD',
                  'Guadeloupe': 'GP',
                  'Guam': 'GU',
                  'Guatemala': 'GT',
                  'Guernsey': 'GG',
                  'Guinea': 'GN',
                  'Guinea-Bissau': 'GW',
                  'Guyana': 'GY',
                  'Haiti': 'HT',
                  'Heard Island and McDonald Islands': 'HM',
                  'Holy See (Vatican City State)': 'VA',
                  'Honduras': 'HN',
                  'Hong Kong': 'HK',
                  'Hungary': 'HU',
                  'ISO 3166-2:GB': '(.uk)',
                  'Iceland': 'IS',
                  'India': 'IN',
                  'Indonesia': 'ID',
                  'Iran, Islamic Republic of': 'IR',
                  'Iraq': 'IQ',
                  'Ireland': 'IE',
                  'Isle of Man': 'IM',
                  'Israel': 'IL',
                  'Italy': 'IT',
                  'Jamaica': 'JM',
                  'Japan': 'JP',
                  'Jersey': 'JE',
                  'Jordan': 'JO',
                  'Kazakhstan': 'KZ',
                  'Kenya': 'KE',
                  'Kiribati': 'KI',
                  "Korea, Democratic People's Republic of": 'KP',
                  'Korea, Republic of': 'KR',
                  'Kuwait': 'KW',
                  'Kyrgyzstan': 'KG',
                  "Lao People's Democratic Republic": 'LA',
                  'Latvia': 'LV',
                  'Lebanon': 'LB',
                  'Lesotho': 'LS',
                  'Liberia': 'LR',
                  'Libya': 'LY',
                  'Liechtenstein': 'LI',
                  'Lithuania': 'LT',
                  'Luxembourg': 'LU',
                  'Macao': 'MO',
                  'Macedonia, the former Yugoslav Republic of': 'MK',
                  'Madagascar': 'MG',
                  'Malawi': 'MW',
                  'Malaysia': 'MY',
                  'Maldives': 'MV',
                  'Mali': 'ML',
                  'Malta': 'MT',
                  'Marshall Islands': 'MH',
                  'Martinique': 'MQ',
                  'Mauritania': 'MR',
                  'Mauritius': 'MU',
                  'Mayotte': 'YT',
                  'Mexico': 'MX',
                  'Micronesia, Federated States of': 'FM',
                  'Moldova, Republic of': 'MD',
                  'Monaco': 'MC',
                  'Mongolia': 'MN',
                  'Montenegro': 'ME',
                  'Montserrat': 'MS',
                  'Morocco': 'MA',
                  'Mozambique': 'MZ',
                  'Myanmar': 'MM',
                  'Namibia': 'NA',
                  'Nauru': 'NR',
                  'Nepal': 'NP',
                  'Netherlands': 'NL',
                  'New Caledonia': 'NC',
                  'New Zealand': 'NZ',
                  'Nicaragua': 'NI',
                  'Niger': 'NE',
                  'Nigeria': 'NG',
                  'Niue': 'NU',
                  'Norfolk Island': 'NF',
                  'Northern Mariana Islands': 'MP',
                  'Norway': 'NO',
                  'Oman': 'OM',
                  'Pakistan': 'PK',
                  'Palau': 'PW',
                  'Palestine, State of': 'PS',
                  'Panama': 'PA',
                  'Papua New Guinea': 'PG',
                  'Paraguay': 'PY',
                  'Peru': 'PE',
                  'Philippines': 'PH',
                  'Pitcairn': 'PN',
                  'Poland': 'PL',
                  'Portugal': 'PT',
                  'Puerto Rico': 'PR',
                  'Qatar': 'QA',
                  'Romania': 'RO',
                  'Russian Federation': 'RU',
                  'Rwanda': 'RW',
                  'Réunion': 'RE',
                  'Saint Barthélemy': 'BL',
                  'Saint Helena, Ascension and Tristan da Cunha': 'SH',
                  'Saint Kitts and Nevis': 'KN',
                  'Saint Lucia': 'LC',
                  'Saint Martin (French part)': 'MF',
                  'Saint Pierre and Miquelon': 'PM',
                  'Saint Vincent and the Grenadines': 'VC',
                  'Samoa': 'WS',
                  'San Marino': 'SM',
                  'Sao Tome and Principe': 'ST',
                  'Saudi Arabia': 'SA',
                  'Senegal': 'SN',
                  'Serbia': 'RS',
                  'Seychelles': 'SC',
                  'Sierra Leone': 'SL',
                  'Singapore': 'SG',
                  'Sint Maarten (Dutch part)': 'SX',
                  'Slovakia': 'SK',
                  'Slovenia': 'SI',
                  'Solomon Islands': 'SB',
                  'Somalia': 'SO',
                  'South Africa': 'ZA',
                  'South Georgia and the South Sandwich Islands': 'GS',
                  'South Sudan': 'SS',
                  'Spain': 'ES',
                  'Sri Lanka': 'LK',
                  'Sudan': 'SD',
                  'Suriname': 'SR',
                  'Svalbard and Jan Mayen': 'SJ',
                  'Swaziland': 'SZ',
                  'Sweden': 'SE',
                  'Switzerland': 'CH',
                  'Syrian Arab Republic': 'SY',
                  'Taiwan, Province of China': 'TW',
                  'Tajikistan': 'TJ',
                  'Tanzania, United Republic of': 'TZ',
                  'Thailand': 'TH',
                  'Timor-Leste': 'TL',
                  'Togo': 'TG',
                  'Tokelau': 'TK',
                  'Tonga': 'TO',
                  'Trinidad and Tobago': 'TT',
                  'Tunisia': 'TN',
                  'Turkey': 'TR',
                  'Turkmenistan': 'TM',
                  'Turks and Caicos Islands': 'TC',
                  'Tuvalu': 'TV',
                  'Uganda': 'UG',
                  'Ukraine': 'UA',
                  'United Arab Emirates': 'AE',
                  'United Kingdom': 'GB',
                  'United States': 'US',
                  'United States Minor Outlying Islands': 'UM',
                  'Uruguay': 'UY',
                  'Uzbekistan': 'UZ',
                  'Vanuatu': 'VU',
                  'Venezuela, Bolivarian Republic of': 'VE',
                  'Viet Nam': 'VN',
                  'Virgin Islands, British': 'VG',
                  'Virgin Islands, U.S.': 'VI',
                  'Wallis and Futuna': 'WF',
                  'Western Sahara': 'EH',
                  'Yemen': 'YE',
                  'Zambia': 'ZM',
                  'Zimbabwe': 'ZW',
                  'Åland Islands': 'AX'}
tipoDoc = {'Certificado de Nac': 'Matific', 'Cedula de Identidad': 'CI','Oficina':"Matific"}
Grados = {'1': "1ero", '2': "2do", '3': "3ro", '4': "4to", '5': "5to", '6': "6to", '7': "7mo"}
Documentos = {'DE': 'Documento Extranjero', 'CI': 'Cédula de Identidad'}

def op(archivo):
    df = pd.read_excel(archivo)
    Escuela = formatString(str(df['Nombre de la institución'][0]))
    Grado = df['Grado'][0]
    Turno = df['Turno'][0]
    Seccion = df['Sección'][0]
    Tipo = df['Tipo de Institución '][0]
    # print(Escuela,Grado,Turno,Seccion,Tipo)

    df1 = df.iloc[9:, 1:]
    df1 = df1.reset_index(drop=True)
    df1.columns = [
        'Nacionalidad',
        'Tipo de documento',
        'Nro de doc.',
        'Correo electrónico',
        'Nombre',
        'Apellido',
        'F. Nacimiento',
        'Sexo',
        'Rol',
        'Tiene discapacidad']

## Eliminar las filas que no tengan nombres y apellido
    df1=df1.dropna(subset=['Nombre', 'Apellido'], axis=0)
    df1['F. Nacimiento'] = df1['F. Nacimiento'].fillna(genFecha(Grado))

    ## Archivo CSV de Matific
    data = {"Nacionalidad": df1["Nacionalidad"].astype(str).apply(formatNorm).apply(genIAPais),
            'Tipo de documento': df1["Tipo de documento"].astype(str).apply(formatNorm).apply(formatString).apply(genIADoc),
            'Nro de doc.': df1["Nro de doc."].astype(str).apply(formatString),
            'Correo electrónico': df1["Correo electrónico"],
            "Nombre": df1["Nombre"].astype(str).apply(formatString),
            "Apellido": df1["Apellido"].astype(str).apply(formatString),
            "Contrasena": "Meta2022",
            'F. Nacimiento': df1['F. Nacimiento'],
            'Pertenezco a una institución pública': tipo(Tipo, "Pública"),
            'Pertenezco a una institución Subvencionada': tipo(Tipo, "Subvencionada"),
            'Pertenezco a una institución Privada': tipo(Tipo, "Privada"),
            'Sexo': df1['Sexo'],
            'Rol': df1['Rol'],
            'Tiene discapacidad': df1['Tiene discapacidad'],
            }
    df2 = pd.DataFrame(data)
#Reemplazo segun diccionarios
    # df2["Nacionalidad"] = df2["Nacionalidad"].astype(str)
    df2 = df2.replace({'Nacionalidad': Nacionalidades})
    df2 = df2.replace({'Tipo de documento': tipoDoc})
#Formateo de Fechas
    df2['F. Nacimiento']=pd.to_datetime(df2['F. Nacimiento']).dt.strftime('%d/%m/%Y')

# Set Documentos

## Set de nombres matific User
    for index, row in df2.iterrows():
        if not df2["Nro de doc."][index].isdigit():
            df2["Tipo de documento"][index] = "Matific"

        if df2["Tipo de documento"][index] == "Matific":
            # print(df2["Nombre"][index] + " " + df2["Apellido"][index])
            df2["Nro de doc."][index] = df2["Nombre"][index].split()[0] + df2["Apellido"][index].split()[0]


    ## Archivo TODOS
    data = {"Nacionalidad": df2["Nacionalidad"],
            'Tipo de documento': df2["Tipo de documento"],
            'Nro de doc.': df2["Nro de doc."],
            "Contrasena": "Meta2022",
            "Nombre": df2["Nombre"],
            "Apellido": df2["Apellido"],
            'Escuela': Escuela,
            'F. Nacimiento': df2['F. Nacimiento'],
            'Sexo': df1['Sexo'],
            'Grade': Grado,
            'Tiene discapacidad': df1['Tiene discapacidad'],
            'Pertenezco a una institución pública': tipo(Tipo, "Pública"),
            'Pertenezco a una institución Subvencionada': tipo(Tipo, "Subvencionada"),
            'Pertenezco a una institución Privada': tipo(Tipo, "Privada"),
            }
    df3 = pd.DataFrame(data)
    df3 = df3.replace({'Nacionalidad': Paises})
    df3 = df3.replace({'Tipo de documento': Documentos})
    df3["Grade"] = df3["Grade"].astype(str)
    df3 = df3.replace({'Grade': Grados})

# Nombre del Archivo
    fichero = str(Grado) +"_"+ str(Seccion)+"_" + str(Escuela)
    df3.to_excel(f"{fichero}.xlsx", index=False)
    df2.to_csv(f"{fichero}.csv", index=False)


if __name__ =="__main__":
    script, archivo = argv
    try:
        op(archivo)
        # print(f"\nLISTO -> {archivo}")
    except Exception as ex:
        print(f"\nFALLA -> {archivo}")
        print(ex)
