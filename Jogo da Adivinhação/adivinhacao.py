import random
import time

dificuldade = 0
tentativa = 0
def escolha_dificuldade(dificuldade):
    global numero_sorteado
    while dificuldade < 1:   
        dificuldade = int(input("Qual será a dificuldade? 1 - Fácil, 2 - Médio e 3 - Difícil: "))
    if dificuldade < 1:
        print("Por favor, escolha uma opção válida")
    elif dificuldade == 1:
        numero_sorteado = random.randint(1, 10)
        print(numero_sorteado)
    elif dificuldade == 2:
        numero_sorteado = random.randint(1,50)
        print(numero_sorteado)
    else:
        numero_sorteado = random.randint(1,100)
        print(numero_sorteado)
    return numero_sorteado
def jogada(numero_sorteado, tentativa):
    print(numero_sorteado)
    for i in range(1,4):
        tentativa = int(input("Qual o número sorteado?: "))
        if tentativa == numero_sorteado:
            print("Você acertou!")
            time.sleep(0.5)
            quit()
        elif tentativa < numero_sorteado:
            print("Não é isso... Pense mais alto...")
        elif tentativa > numero_sorteado:
            print("Não é isso... Talvez um valor menor?")
        else:
            print("Não foi dessa vez...")
            print("\n")
            time.sleep(0.5)
            print("Finalizando o jogo...")
            quit()


print("Bem vindo ao jogo da Adivinhação!")

time.sleep(0.5)
print("\n")

print("Iniciando o jogo!")

time.sleep(0.5)
print("\n")

escolha_dificuldade(dificuldade)
jogada(numero_sorteado, tentativa)

time.sleep(0.5)
print("\n")
print("Obrigado por jogar!")