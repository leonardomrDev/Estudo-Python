import random
import time

def jogar():
    def escolha_tema():
        global palavras
        palavras = []
        print("\n")
        print('Temas disponíveis: (1) Alimentos e (2) Sem tema específico')
        print('\n')
        time.sleep(1)
        tema = int(input('Qual será o tema da partida?: '))
        match tema:
            case 1:
                alimentos = open('alimentos.txt', 'r')
                time.sleep(0.5)
                print('Jogaremos utilizando como base o tema de Alimentos!')
                for linha in alimentos:
                    palavras.append(linha.strip)
                alimentos.close()
            case 2:
                semtema = open('words.txt', 'r')
                time.sleep(0.5)
                print('Jogaremos utilizando nenhum tema específico!')
                for linha in semtema:
                    palavras.append(linha.strip())
                semtema.close()
            case _:
                time.sleep(0.5)
                print('Escolha inválida!')
                time.sleep(0.5)
                print(f'Fechando o jogo! ({tema}) não é uma opção válida.')
                time.sleep(0.5)
                quit()

    def palavra_segredo(palavras):
        global palavra_secreta
        palavra_secreta = palavras[random.randrange(0, len(palavras))]

    def tentativa(letras_corretas, palavra_secreta):
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

    def cond_vitoria(palavra_secreta):
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

    enforcou = False
    acertou = False
    erros = 0
    enforcou = erros == 6
    
    print("Início do Jogo da Forca!!")
    time.sleep(0.5)
    escolha_tema()
    letras_corretas = ['_' for i in palavra_secreta]
    acertou = '_' not in letras_corretas
    palavra_segredo(letras_corretas)
    tentativa(palavra_secreta, letras_corretas, erros, acertou, enforcou)
    cond_vitoria(acertou, palavra_secreta)
        
if __name__ == "__main__":
    jogar()
