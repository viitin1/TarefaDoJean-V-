# Questão 04 - Sistema de Notas dos Estudantes

QUANTIDADE_NOTAS = 3

def calcular_media(notas):
    return sum(notas) / len(notas)

def definir_situacao(media):
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"

def ler_nota(numero):
    while True:
        try:
            nota = float(input(f"  Nota {numero}: ").replace(",", "."))
            if 0 <= nota <= 10:
                return nota
            print("  A nota deve estar entre 0 e 10!")
        except ValueError:
            print("  Valor inválido! Digite um número.")

def main():
    estudantes = {} #verificar isso aq depois
    continuar = "s"

    while continuar == "s":
        nome = input("Nome do estudante: ").strip()
        if nome == "":
            print("O nome não pode ficar vazio!\n")
            continue

        notas = []
        contador = 1
        while contador <= QUANTIDADE_NOTAS:
            notas.append(ler_nota(contador))
            contador += 1

        estudantes[nome] = notas
        continuar = input("\nCadastrar outro estudante? (s/n): ").strip().lower()
        print()

    print("=== RESULTADO FINAL ===")
    for nome, notas in estudantes.items():
        media = calcular_media(notas)
        print(f"Nome: {nome} | Média: {media:.2f} | Situação: {definir_situacao(media)}")

main()
