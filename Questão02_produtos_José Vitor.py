# Questão 02 - Cadastro e Validação de Produtos

def cadastrar_produto(produtos, nome, preco):
    produtos[nome] = preco

def exibir_produtos(produtos):
    print("\n=== PRODUTOS CADASTRADOS ===")
    if not produtos:
        print("Nenhum produto cadastrado.")
        return
    for nome, preco in produtos.items():
        print(f"{nome}: R$ {preco:.2f}")

def main():
    produtos = {}
    continuar = "s"

    while continuar == "s":
        nome = input("Nome do produto: ").strip()
        if nome == "":
            print("O nome não pode ficar vazio!\n")
            continue

        try:
            preco = float(input("Preço: R$ ").replace(",", "."))
        except ValueError:
            print("Preço inválido! Digite um número.\n")
            continue
            
        if preco <= 0:
            print("O preço deve ser maior que zero!\n")
            continue

        cadastrar_produto(produtos, nome, preco)
        print("Produto cadastrado com sucesso!\n")

        continuar = input("Deseja cadastrar outro produto? (s/n): ").strip().lower()
        print()

    exibir_produtos(produtos)

main()
