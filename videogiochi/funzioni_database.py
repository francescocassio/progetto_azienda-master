import mysql.connector
from mysql.connector import Error
def create_connection(nome_db):
    connection = None
    try:
        connection = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            database=nome_db)
        print("Connection to DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

def create_database(nome_db, drop = False):
    try:
        connection = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            )
        mycursor = connection.cursor()

        if drop:
            mycursor.execute(f"DROP DATABASE IF EXISTS {nome_db}")
            print(f"eliminato db {nome_db}")

        mycursor.execute(f"CREATE DATABASE {nome_db}")
        print(f"creato db {nome_db}")

    except Error as e:
        print(f"The error '{e}' occurred")

def esegui_query(query, nome_db):
    #creiamo la connessione al db
    connessione = create_connection(nome_db)

    #creiamo un cursore per navigare nel db
    cursor = connessione.cursor()

    try:
        cursor.execute(query)
        connessione.commit() #committiamo i risultati
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")
    finally:
        cursor.close()
        connessione.close()

def esegui_query_param(query, param, nome_db):
    #creiamo la connessione al db
    connessione = create_connection(nome_db)

    #creiamo un cursore per navigare nel db
    cursor = connessione.cursor()

    try:
        cursor.execute(query, param)
        connessione.commit() #committiamo i risultati
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")
    finally:
        cursor.close()
        connessione.close()


def esegui_query_select(query, nome_db):
    #creiamo la connessione al db
    connessione = create_connection(nome_db)

    #creiamo un cursore per navigare nel db
    cursor = connessione.cursor()

    try:
        cursor.execute(query)
        result = cursor.fetchall()

        return result
    except Error as e:
        print(f"The error '{e}' occurred")
    finally:
        cursor.close()
        connessione.close()

def esegui_query_select_param(query, param, nome_db):
    #creiamo la connessione al db
    connessione = create_connection(nome_db)

    #creiamo un cursore per navigare nel db
    cursor = connessione.cursor()

    try:
        cursor.execute(query, param)
        result = cursor.fetchall()

        return result
    except Error as e:
        print(f"The error '{e}' occurred")
    finally:
        cursor.close()
        connessione.close()