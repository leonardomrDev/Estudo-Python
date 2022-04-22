import random
import time

def jogar():
    print("Início do Jogo da Forca!!")
    time.sleep(0.5)
    print("\n")

    #secretas_comida = {}
    palavra_secreta = "BANANA"
    enforcou = False
    acertou = False
    index = 0
    letras_corretas = ["_", "_", "_", "_", "_", "_"]
    letras_faltando = str(letras_corretas.count('_'))

    while not enforcou and not acertou:
        chute = input("Qual letra deseja tentar?: ").strip()
        #palavra_secreta.find(chute)
        for letra in palavra_secreta:
            if chute.upper() == letra:
                print(f"A letra {letra} está na {index}ª posição da palavra secreta!")
                letras_corretas[index] = letra
                #print(f'Ainda faltam {letras_faltando} letras!')
            index = index + 1
            print(f'Ainda faltam {letras_faltando}')
        print("Jogando...")
        print(letras_corretas)
        print("Fim de Jogo!! Obrigado por Jogar!")

if __name__ == "__main__":
    jogar()
