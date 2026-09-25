# Questão 10 - Sistema Integrado de Análise de Dados

estudantes = []
NOTA_APROVACAO = 7.0

# preciso estudar isso aq melhor depois !!!!!!!
def cadastrar_estudante():
    nome = input("Nome do estudante: ").strip()
    if nome == "":
        print("O nome não pode ficar vazio!")
        return
    try:
        nota = float(input("Nota: ").replace(",", "."))
    except ValueError:
        print("Nota inválida!")
        return
    if nota < 0 or nota > 10:
        print("A nota deve estar entre 0 e 10!")
        return

    estudantes.append({"nome": nome, "nota": nota})
    print("Estudante cadastrado!")

def calcular_media():
    if not estudantes:
        return None
    soma = 0  # acumulador
    for estudante in estudantes:
        soma += estudante["nota"]
    return soma / len(estudantes)

def maior_nota():
    if not estudantes:
        return None
    melhor = estudantes[0]
    for estudante in estudantes:
        if estudante["nota"] > melhor["nota"]:
            melhor = estudante
    return melhor

def listar_aprovados():
    aprovados = []
    for estudante in estudantes:
        if estudante["nota"] >= NOTA_APROVACAO:
            aprovados.append(estudante)
    return aprovados

def main():
    opcao = ""
    while opcao != "5":
        print("\n1 - Cadastrar estudante")
        print("2 - Exibir média da turma")
        print("3 - Exibir estudante com maior nota")
        print("4 - Listar aprovados")
        print("5 - Sair")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_estudante()
        elif opcao == "2":
            media = calcular_media()
            if media is None:
                print("Nenhum estudante cadastrado.")
            else:
                print(f"Média da turma: {media:.2f}")
        elif opcao == "3":
            melhor = maior_nota()
            if melhor is None:
                print("Nenhum estudante cadastrado.")
            else:
                print(f"Maior nota: {melhor['nome']} ({melhor['nota']:.1f})")
        elif opcao == "4":
            aprovados = listar_aprovados()
            if not aprovados:
                print("Nenhum estudante aprovado.")
            else:
                print("=== APROVADOS ===")
                for estudante in aprovados:
                    print(f"{estudante['nome']}: {estudante['nota']:.1f}")
        elif opcao == "5":
            print("Encerrando o sistema...")
        else:
            print("Opção inválida!")

main()
