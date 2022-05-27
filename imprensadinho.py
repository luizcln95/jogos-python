import random


def jogar():
    apresentacao()

    # Inicializando variáveis
    numero_secreto = random.randrange(1, 100)
    limite_inferior = 0
    limite_superior = 100

    while True:
        palpite = novo_palpite()
        if palpite <= limite_inferior or palpite >= limite_superior:
            numero_invalido(limite_inferior, limite_superior)
        elif palpite == numero_secreto:
            perdeu(numero_secreto)
            break
        else:  # palpite != numero_secreto
            if palpite < numero_secreto:
                limite_inferior = palpite
            else:  # palpite > numero_secreto
                limite_superior = palpite

            if limite_inferior == numero_secreto - 1 and limite_superior == numero_secreto + 1:
                imprensou(numero_secreto)
                break
            else:
                informa_novos_limites(limite_inferior, limite_superior)


def apresentacao():
    print("Bem-vinde ao jogo de imprensadinho!")
    print("Um número entre 0 e 100 foi escolhido aleatoriamente.")
    print("O objetivo é acertar seu antecessor e seu sucessor, ou seja, imprensá-lo!")
    print("Valendo!")


def novo_palpite():
    palpite = int(input("Digite um número: "))
    return palpite


def numero_invalido(limite_inferior, limite_superior):
    print("Número inválido.")
    print(f"O número secreto está entre {limite_inferior} e {limite_superior}.")


def perdeu(numero_secreto):
    print("VOCÊ PERDEU!!")
    print(f"O número secreto era exatamente {numero_secreto}!")


def imprensou(numero_secreto):
    print("IMPRENSOU!!")
    print(f"O número secreto era {numero_secreto}!")


def informa_novos_limites(limite_inferior, limite_superior):
    print(f"O número secreto está entre {limite_inferior} e {limite_superior}.")


if __name__ == "__main__":
    jogar()
