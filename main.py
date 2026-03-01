def menu_principal():
    print("===== Menu Principal =====")
    print ("1- Cadastrar Residente")
    print ("2- Listar Residentes")
    print ("3- Buscar Residente")
    print ("4- Sair")
    return input("Escolha a opção numérica: ").strip()

def main(): 
    while True:
        opcao = menu_principal()
        if opcao == "1":
            print ("Cadastrar")
        elif opcao == "2":
            print("Listar")    
        elif opcao == "3":
            print("Buscar")
        elif opcao == "4":
            print("Saindo")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()        