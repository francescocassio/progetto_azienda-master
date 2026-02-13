# creare il database
    # creare la/e tabella/e necessaria
        # creare la connessione al db
        # creare il cursore
    # inserire i dati all'interno del db
        # -> aprire il csv
        # -> iterarlo
        # -> inserire i dati estratti da ciascuna riga

from funzioni_database import create_database

if __name__ == '__main__':
    create_database("prova999", drop = True)

    print("fine del programma")


