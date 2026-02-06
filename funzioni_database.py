import mysql.connector
from mysql.connector import Error
def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            database="azienda_generation")
        print("Connection to DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

def esegui_query(query):
    #creiamo la connessione al db
    connessione = create_connection()

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

def esegui_query_param(query, param):
    #creiamo la connessione al db
    connessione = create_connection()

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


def esegui_query_select(query):
    #creiamo la connessione al db
    connessione = create_connection()

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

def esegui_query_select_param(query, param):
    #creiamo la connessione al db
    connessione = create_connection()

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