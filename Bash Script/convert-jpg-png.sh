#! /bin/bash 
# Seleção de Interpretador

#CAMINHO_IMAGENS=~Estudo Python/Bash Script/imagens-livros

#convert ~/imagens-livros/$1.jpg ~/imagens-livros/$1.png
#convert $CAMINHO_IMAGENS/$2.jpg $CAMINHO_IMAGENS/$2.png

# awk -F # utilizado para especificar um campo delimitador do parâmetro de texto passado.
# rm *.png

image_conversion(){
       
    cd ~/Estudo Python/Bash Script/imagens-livros

    if [! -d png]
        then mkdir png
    fi

    for image in *.jpg
    do
        convert_image=$(ls $image | awk -F. '{print $1}'
        convert $convert_image.jpg png/$convert_image.png
    done
}

image_conversion 2> erros_conversao.txt

echo $convert_image

if [$? -eq 0]
    then
        echo "Realizado com sucesso a conversão!"
    else
        echo "Houve uma falha no processo!"
fi


# bash convert-jpg-png.sh
