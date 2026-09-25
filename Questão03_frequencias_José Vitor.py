# Questão 03 - Análise de Frequência de Palavras

def contar_palavras(frase):
    frase = frase.lower()
    palavras = frase.split()
    contagem = {}

    i = 0
    while i < len(palavras):
        palavra = palavras[i].strip(".,!?;:\"'()")
        if palavra != "":
            if palavra in contagem:
                contagem[palavra] += 1
            else:
                contagem[palavra] = 1
        i += 1

    return contagem

def main():
    frase = input("Digite uma frase: ")
    resultado = contar_palavras(frase)

    print("\nFrequência das palavras:")
    for palavra, quantidade in resultado.items():
        print(f"{palavra}: {quantidade}")

main()
