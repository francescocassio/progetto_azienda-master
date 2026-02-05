import mysql.connector

def crea_tabella():
    conn = mysql.connector.connect(
        user="root",
        password="",
        host="localhost",
        database="azienda_generation")
    cursor = conn.cursor()

    q_crea_fatture = """
    create table fattura(
         id_fattura INT PRIMARY KEY,
         emittente VARCHAR(80) DEFAULT "Azienda Zurich" NOT NULL,
         destinatario VARCHAR(80) NOT NULL,
         bene_servizio_venduto VARCHAR(80) NOT NULL,
         importo DOUBLE NOT NULL,
         iva double NOT NULL,
         imponibile double NOT NULL,
         data_fattura DATE
     );
"""
    cursor.execute(q_crea_fatture)

    creazione_trigger_arrotonda_iva_imponibile = """
          DELIMITER $$
        
        CREATE TRIGGER arrotonda_fatture
        BEFORE INSERT ON fatture
        FOR EACH ROW
        BEGIN
            SET NEW.imponibile = ROUND(NEW.imponibile, 2);
            SET NEW.iva = ROUND(NEW.iva, 2);
        
            IF ROUND(NEW.imponibile + NEW.iva, 2) <> NEW.importo THEN
                SET NEW.importo = ROUND(NEW.imponibile + NEW.iva, 2);
            END IF;
        END$$
        
        DELIMITER ;
        """
    #aggiungo anche il trigger
    cursor.execute(creazione_trigger_arrotonda_iva_imponibile)



if __name__ == '__main__':
    try:
        crea_tabella()
        print("tabella creata con successo")
    except mysql.connector.errors.ProgrammingError:
        print("Tabella già esistente")