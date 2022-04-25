import time

def jogar():
    print("Início do Jogo da Forca!!")
    time.sleep(0.5)
    print("\n")
    print('Temas disponíveis: (1) Comidas e (2) Sem tema específico')
    print('\n')
    time.sleep(1)
    tema = int(input('Qual será o tema da partida?: '))
    match tema:
        case 1:
            open('comidas.txt', 'r')
            time.sleep(0.5)
            print('Jogaremos utilizando como base o tema de Comidas!')
        case 2:
            open('words.txt', 'r')
            time.sleep(0.5)
            print('Jogaremos utilizando nenhum tema específico!')
        case _:
            time.sleep(0.5)
            print('Escolha inválida!')
            time.sleep(0.5)
            print(f'Fechando o jogo! ({tema}) não é uma opção válida.')
            time.sleep(0.5)
            quit()
    palavra_secreta = "CACHORRO"
    enforcou = False
    acertou = False
    erros = 0
    letras_corretas = ['_' for i in palavra_secreta] # List Comprehension
    #letras_faltando = str(letras_corretas.count('_'))

    #for i in palavra_secreta:
     #   letras_corretas.append('_')

    while not enforcou and not acertou:
        chute = input("Qual letra deseja tentar?: ").strip().upper()
        #palavra_secreta.find(chute)
        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if chute == letra:
                    print(f"A letra {letra} está na {index}ª posição da palavra secreta!")
                    letras_corretas[index] = letra
                    #print(f'Ainda faltam {letras_faltando} letras!')
                index += 1 #index = index + 1
                #print(f'Ainda faltam {letras_faltando}')
        else:
            erros += 1
            print('\n')
            time.sleep(0.5)
            print(f'Errou! Você possui {6-erros} tentativas restante!')
            print('\n')
        enforcou = erros == 6
        acertou = '_' not in letras_corretas
        if acertou is True:
            time.sleep(0.6)
            print('Você venceu!')
            time.sleep(1)
            print(f'A Palavra Secreta era ({palavra_secreta})!')
            time.sleep(1)
            print('Fim de jogo! Obrigado por jogar!')
        elif enforcou is True:
            time.sleep(0.5)
            print('Você errou 6 vezes. Fim de jogo!')
            time.sleep(0.7)
            print(f'A palavra secreta era {palavra_secreta}!')
        print(letras_corretas)
if __name__ == "__main__":
    jogar()
