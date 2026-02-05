# from funzioni_services import inserisci_fattura, mostra_fatture

def menu():
    #permette di salvare le fatture dopo averne chiesto i campi da riempire
    print("1) Salva fattura")

    #mostra tutte le fatture nel db
    print("2) Mostra fatture")

    print("0) Termina")

def scelta():
    while True:
        menu()
        try:
            opzione = int(input("Scelta: "))

            if opzione == 1:
                pass
                # inserisci_fattura()
            elif opzione == 2:
                pass
                # mostra_fatture()
            elif opzione == 0:
                break
            else:
                print("Opzione non valida")
        except ValueError:
            print("Campo non accettato")
        except EOFError:
            print("Errore imprevisto, contatta l'ammistrazione, chiusura del progrmma")
            break

if __name__ == '__main__':
    scelta()