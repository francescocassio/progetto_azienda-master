from funzioni_services import inserisci_fattura, mostra_fatture

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
                inserisci_fattura()
            elif opzione == 2:
                mostra_fatture()
            elif opzione == 0:
                break
            else:
                print("Opzione non valida")
        except ValueError:
            print("Campo non accettato")
        except EOFError:
            print("WTF? CTRL + d ma cosa combini")
            break
        except:
            print("Errore critico, non so perché sei qui")

if __name__ == '__main__':
    scelta()