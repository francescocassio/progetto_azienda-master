from funzioni_supporto import scelta
from funzioni_database import esegui_query_select, esegui_query_select_param


#permettere all'utente di inserire una nuova fattura, stando MOLTO attenti agli id sequenziali e
#a tutto ciò che non deve essere NULL. Inoltre pensate se riuscite ad inserire alcuni dei campi in
#automatico (imponibile, data, ecc)

#commento a caso test

#questo programma per funzionare necessita di un db chiamato azienda_generation e che mysql sia attivo

def main():
    username = input("Inserisci username: ")
    psw = input("Inserisci password: ")

    q = f"select * from utente where username = %s and psw = %s;"
    dati = (username, psw)

    print(q)
    ris = esegui_query_select_param(q, dati)

    print(ris)

    print("ciao cecilia")

    print("mondo")



    # scelta()

if __name__ == "__main__":
    main()
