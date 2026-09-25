# Questão 08 - Menu de Sistema com Funções

tarefas = []

def adicionar_tarefa():
    tarefa = input("Digite a tarefa: ").strip()
    if tarefa == "":
        print("A tarefa não pode ficar vazia!")
        return
    tarefas.append(tarefa)
    print("Tarefa adicionada!")

def listar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return
    print("\n=== TAREFAS ===")
    for numero, tarefa in enumerate(tarefas, start=1):
        print(f"{numero}. {tarefa}")

def remover_tarefa():
    if not tarefas:
        print("Nenhuma tarefa para remover.")
        return
    listar_tarefas()
    try:
        numero = int(input("Número da tarefa a remover: "))
        if 1 <= numero <= len(tarefas):
            removida = tarefas.pop(numero - 1)
            print(f"Tarefa '{removida}' removida!")
        else:
            print("Número inválido!")
    except ValueError:
        print("Digite um número válido!")

def main():
    opcao = ""
    while opcao != "4":
        print("\n1 - Adicionar tarefa")
        print("2 - Listar tarefas")
        print("3 - Remover tarefa")
        print("4 - Sair")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            adicionar_tarefa()
        elif opcao == "2":
            listar_tarefas()
        elif opcao == "3":
            remover_tarefa()
        elif opcao == "4":
            print("Saindo do sistema...")
        else:
            print("Opção inválida!")

main()
