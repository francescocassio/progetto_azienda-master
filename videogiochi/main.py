# creare il database
    # creare la/e tabella/e necessaria
        # creare la connessione al db
        # creare il cursore
    # inserire i dati all'interno del db
        # -> aprire il csv
        # -> iterarlo
        # -> inserire i dati estratti da ciascuna riga

from funzioni_database import create_database, esegui_query
from script_sql import crea_tabella_videogiochi
from caricamento import caricamento_dati

if __name__ == '__main__':
    create_database("database_videogiochi", drop = True)

    #creare la tabella videogiochi nel db
    esegui_query(crea_tabella_videogiochi, "database_videogiochi", "creata tabella vg")

    #carico i dati dal csv nel db
    caricamento_dati("database_videogiochi")

    print("fine del programma")


