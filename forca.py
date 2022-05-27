import random
from unidecode import unidecode


def jogar():

    apresentacao()

    palavra_secreta = escolhe_palavra()

    acertos = esconde_palavra(palavra_secreta)  # muda as letras não acertadas para _
    print(acertos)

    # Inicializando variáveis
    acertou = False
    enforcou = False
    erros = 0

    while not acertou and not enforcou:
        chute = tentativa()
        if chute in palavra_secreta:
            marcar_acertos(palavra_secreta, chute, acertos)
        else:
            erros += 1

        print(acertos)
        acertou = "_" not in acertos
        print("Número de erros: ", erros)
        enforcou = erros == 6

    if acertou:
        print("Você ganhou!")
    else:
        print("A palavra era:", palavra_secreta)
        print("Você perdeu!")


def apresentacao():
    print("Bem-vinde ao jogo da forca!")
    print("A palavra foi escolhida aleatoriamente e seu limite de erros é 6!")
    print("Valendo!")


def escolhe_palavra():
    with open("palavras.txt") as arquivo:
        lista_palavras = arquivo.readlines()
        lista_palavras = [unidecode(palavra).strip() for palavra in lista_palavras]
    palavra = lista_palavras[random.randrange(0, len(lista_palavras))].upper()
    return palavra


def esconde_palavra(palavra):
    return ["_" for letra in palavra]


def tentativa():
    chute = input("Tente uma letra: ").strip().upper()
    return chute


def marcar_acertos(palavra_secreta, chute, acertos):
    index = 0
    for letra in palavra_secreta:
        if chute == letra:
            acertos[index] = chute
        index += 1


if __name__ == "__main__":
    jogar()
