import csv
from funzioni_database import esegui_query_param
from tqdm import tqdm
def caricamento_dati(nome_db):
    with open("vgsales.csv", "r", encoding="utf-8") as f:
        lettore_csv = csv.DictReader(f)

        q = """INSERT INTO videogiochi(Rank,Name, Platform, Year_v, Genre, Publisher,
         NA_Sales, EU_Sales, JP_Sales, Other_Sales, Global_Sales) 
         VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

        #mi serve una tupla che contenga questi 11 %s
        #questsa tupla è diversa per ogni gioco che vado ad iterare

        for gioco in tqdm(lettore_csv):
            if gioco['Year'] == "N/A":
                anno = None
            else:
                anno = gioco['Year']

            if gioco['Publisher'] == "Unknown" or gioco['Publisher'] == "N/A":
                publisher = None
            else:
                publisher = gioco['Publisher']


            dati = (gioco['Rank'], gioco['Name'],gioco['Platform'],
                    anno,gioco['Genre'],publisher,
                    gioco['NA_Sales'],gioco['EU_Sales'],gioco['JP_Sales'],
                    gioco['Other_Sales'],gioco['Global_Sales'])

            esegui_query_param(q, dati, nome_db)
