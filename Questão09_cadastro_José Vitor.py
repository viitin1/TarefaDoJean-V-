# Questão 09 - Sistema de Cadastro de Clientes

def cadastrar_cliente(clientes):
    nome = input("Nome: ").strip()
    email = input("E-mail: ").strip()
    telefone = input("Telefone: ").strip()

    if nome == "":
        print("O nome é obrigatório!")
        return

    clientes.append({"nome": nome, "email": email, "telefone": telefone})
    print("Cliente cadastrado com sucesso!")

def exibir_cliente(cliente):
    print(f"Nome: {cliente['nome']} | E-mail: {cliente['email']} | Telefone: {cliente['telefone']}")

def pesquisar_cliente(clientes):
    busca = input("Digite o nome para pesquisar: ").strip().lower()
    encontrou = False

    for cliente in clientes:
        if busca in cliente["nome"].lower():
            exibir_cliente(cliente)
            encontrou = True

    if not encontrou:
        print("Nenhum cliente encontrado.")

def listar_clientes(clientes):
    if not clientes:
        print("Nenhum cliente cadastrado.")
        return
    print("\n=== CLIENTES ===")
    for cliente in clientes:
        exibir_cliente(cliente)

def main():
    clientes = []
    opcao = ""

    while opcao != "4":
        print("\n1 - Cadastrar cliente")
        print("2 - Pesquisar cliente pelo nome")
        print("3 - Listar todos os clientes")
        print("4 - Encerrar o programa")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_cliente(clientes)
        elif opcao == "2":
            pesquisar_cliente(clientes)
        elif opcao == "3":
            listar_clientes(clientes)
        elif opcao == "4":
            print("Programa encerrado.")
        else:
            print("Opção inválida!")

main()
