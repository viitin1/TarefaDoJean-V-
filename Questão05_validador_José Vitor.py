# Questão 05 - Validador de Senha

def validar_senha(senha):
    if len(senha) < 8:
        return False

    tem_maiuscula = False
    tem_minuscula = False
    tem_numero = False

    i = 0
    while i < len(senha):
        caractere = senha[i]
        if caractere.isupper():
            tem_maiuscula = True
        elif caractere.islower():
            tem_minuscula = True
        elif caractere.isdigit():
            tem_numero = True
        i += 1

    return tem_maiuscula and tem_minuscula and tem_numero

def main():
    print("A senha deve ter:")
    print("- Pelo menos 8 caracteres")
    print("- Pelo menos uma letra maiúscula")
    print("- Pelo menos uma letra minúscula")
    print("- Pelo menos um número\n")

    senha = input("Digite uma senha: ")

    while not validar_senha(senha):
        print("Senha inválida! Tente novamente.\n")
        senha = input("Digite uma senha: ")

    print("\nSenha válida! Cadastrada com sucesso.")

main()
