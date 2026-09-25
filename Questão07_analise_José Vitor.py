# Questão 07 - Análise de Texto

def analisar_texto(texto):
    letras = 0
    numeros = 0
    espacos = 0

    i = 0
    while i < len(texto):
        caractere = texto[i]
        if caractere.isalpha():
            letras += 1
        elif caractere.isdigit():
            numeros += 1
        elif caractere == " ":
            espacos += 1
        i += 1

    return {
        "caracteres": len(texto),
        "letras": letras,
        "numeros": numeros,
        "espacos": espacos,
        "palavras": len(texto.split()),
    }

def main():
    texto = input("Digite uma frase: ")
    resultado = analisar_texto(texto)

    print("\n=== ANÁLISE DO TEXTO ===")
    print(f"Quantidade total de caracteres: {resultado['caracteres']}")
    print(f"Quantidade de letras: {resultado['letras']}")
    print(f"Quantidade de números: {resultado['numeros']}")
    print(f"Quantidade de espaços: {resultado['espacos']}")
    print(f"Quantidade de palavras: {resultado['palavras']}")

main()
