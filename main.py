def menu_principal():
    print("===== Menu Principal =====")
    print ("1- Cadastrar Residente")
    print ("2- Listar Residentes")
    print ("3- Buscar Residente")
    print ("4- Sair")
    return input("Escolha a opção numérica: ").strip()

def main():
    lista_idosos = [] 
    while True:
        opcao = menu_principal()
        if opcao == "1":
            cadastrar_idoso(lista_idosos)
        elif opcao == "2":
            listar_idosos(lista_idosos)   
        elif opcao == "3":
            print("Buscar")
        elif opcao == "4":
            print("Saindo")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()        



def cadastrar_idoso (lista_idosos):
    nome = input(" Digite  nome do paciente: ").strip()
    idade = int(input("Digite a idade do paciente: "))
    quarto = int(input("Digite o quarto do paciente: "))

    idoso ={
        "nome": nome,
        "idade": idade,
        "quarto": quarto

    }
    lista_idosos.append(idoso)
    

def listar_idosos(lista_idosos):
    if not lista_idosos:
        print("A lista esta vazia....")
        return
    for idoso in lista_idosos:
        print("-" * 30)
        print (f"Paciente:{idoso['nome']} \n idade:{idoso['idade']} \n Quarto:{ idoso['quarto']}")
