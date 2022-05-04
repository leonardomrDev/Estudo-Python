#! /bin/bash 
# Seleção de Interpretador

CAMINHO_IMAGENS=~Estudo Python/Bash Script/imagens-livros

#convert ~/imagens-livros/$1.jpg ~/imagens-livros/$1.png
#convert $CAMINHO_IMAGENS/$2.jpg $CAMINHO_IMAGENS/$2.png

for imagem in $@

do
    convert $CAMINHO_IMAGENS/$imagem.jpg $CAMINHO_IMAGENS/$imagem.png
    

