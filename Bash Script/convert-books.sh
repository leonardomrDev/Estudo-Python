#!/bin/bash

image_conversion(){
    local caminho_imagem=$1
    local imagem_sem_extensao=$(ls $caminho_imagem | awk -F. '{print $1}')
    convert $imagem_sem_extensao.jpg $imagem_sem_extensao.png

}

varrer_diretorio(){
    
    cd $1
    #cd ~/Estudo Python/Bash Script/imagens-livros

    for arquivo in *
    do
        local caminho_arquivo=$(find ~/Estudo Python/Bash Script/imagens-livros -name $arquivo)
        #find ~/Estudo Python/Bash Script/imagens-livros -name $arquivo
        if [-d $caminho_arquivo]
        then
            varrer_diretorio $caminho_arquivo
        else
            convert_image $caminho_arquivo
        fi
    done
}

varrer_diretorio ~/Estudo Python/Bash Script/imagens-livros
if [$? -eq 0]
then
    echo "Conversão foi um sucesso!"
else
    echo "Houve um problema na conversão!"
fi

