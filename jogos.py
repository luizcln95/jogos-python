import imprensadinho
import forca


def executar():
    print("JOGOS DISPONÍVEIS:")
    print("(1) Imprensadinho  /  (2) Forca")
    jogo = int(input("Selecione o jogo que deseja jogar: "))

    if jogo == 1:
        imprensadinho.jogar()
    elif jogo == 2:
        forca.jogar()
    else:
        print("Jogo não encontrado.")


if __name__ == "__main__":
    executar()
