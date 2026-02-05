import datetime
import mysql.connector
conn = mysql.connector.connect(
    user="root",
    password="",
    host="localhost",
    database="azienda_generation")


def inserisci_fattura():
    cursor = conn.cursor()
    cursor.execute("SELECT MAX(id_fattura) FROM fattura")
    risultato = cursor.fetchone()
    id_massimo = risultato[0]
    id_fattura = (id_massimo if id_massimo is not None else 0) + 1 #AIUTO GEMINI (calcolo se id è nullo perchè 0 fatture, lo trasforma in 0)
    destinatario = input("Inserisci il destinatario: ").strip()
    bsvenduto = input("Inserisci il bene servizio venduto: ").strip()
    importo = float(input("Inserisci l'importo: "))
    if not destinatario or not bsvenduto:
        print("Errore: Destinatario o Servizio mancanti. Operazione annullata.")
        return

    if not importo.replace('.', '', 1).isdigit():
        print("Errore: L'importo deve essere un numero valido.")
        return
    iva = importo * 0.22
    imponibile = importo - iva
    data_fattura = datetime.date.today()
    dati = (id_fattura,destinatario,bsvenduto,importo,iva,imponibile,data_fattura)
    q_inserisci_fattura = f"""
    INSERT INTO fattura (id_fattura,destinatario, bene_servizio_venduto, importo, iva, imponibile, data_fattura)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(q_inserisci_fattura, dati)
    conn.commit()
    print("Complimenti, fattura inserita!")


def mostra_fatture():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM fattura")

    print("--- ELENCO FATTURE ---")

    for f in cursor:
        print(f[0], "|", f[1], "|", f[2], "|", f[3], "|", f[4], "€ | IVA:", f[5], "| Imp:", f[6], "| del:", f[7])

    cursor.close()