import csv
from tqdm import tqdm
import time

def carica_dati_da_csv():
    inizio = time.perf_counter()
    for i in tqdm(range(500)):
        with open("vgsales.csv", "r", encoding="utf-8") as f:
            lettore_csv = csv.reader(f)

            somma_anni = 0

            #saltiamo la prima riga
            header = next(lettore_csv)

            vg_validi = 0

            for riga in lettore_csv:
                if riga[3] != 'N/A':
                    somma_anni += int(riga[3])
                    vg_validi += 1

            # print(somma_anni)
            # print(somma_anni / vg_validi)
    fine = time.perf_counter()
    tempo_trascorso = fine - inizio

    print(f"Tempo impiegato: {tempo_trascorso:.6f} secondi")

def carica_dati_da_csv_diz():
    inizio = time.perf_counter()
    for i in tqdm(range(500)):
        with open("vgsales.csv", "r", encoding="utf-8") as f:
            lettore_csv = csv.DictReader(f)
            somma_anni = 0
            vg_validi = 0
            for riga in lettore_csv:
                if riga['Year'] != 'N/A':
                    somma_anni += int(riga['Year'])
                    vg_validi += 1

                #stampare la somma degli anni
            # print(somma_anni)
            # print(somma_anni / vg_validi)
    fine = time.perf_counter()
    tempo_trascorso = fine - inizio

    print(f"Tempo impiegato: {tempo_trascorso:.6f} secondi")


carica_dati_da_csv()
carica_dati_da_csv_diz()