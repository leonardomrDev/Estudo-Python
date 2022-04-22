import adivinhacao
import forca

import time

def escolha_jogo():
    print("###################################")
    print("######## O QUE JOGAREMOS ? ########")
    print("###################################")

    print("\n")
    time.sleep(0.8)
    print(" PARA JOGARMOS O JOGO DA ADIVINHAÇÃO (1)")
    time.sleep(0.5)
    print(" PARA JOGARMOS O JOGO DA FORCA (2)")
    time.sleep(0.5)
    print("\n")

    jogo = int(input(" Qual será?: "))
    if jogo == 1:
        print("\n")
        print("ESCOLHIDO O JOGO DA ADIVINHAÇÃO!")
        time.sleep(0.7)
        adivinhacao.jogar()
        print("\n")
    elif jogo == 2:
        print("\n")
        print("ESCOLHIDO O JOGO DA FORCA!")
        time.sleep(0.7)
        forca.jogar()
        print("\n")
    else:
        print("Por gentileza, escolha um valor válido.")

if __name__ == "__main__":
    escolha_jogo()