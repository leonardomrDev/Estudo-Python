#!/bin/bash
memory_processes(){
    if [ ! -d log ]
    then
        mkdir log
    fi

    processes=$(ps -e -o pid --sort -size | head -n 11 | grep [0-9])
    #$(ps -p 14009 -o comm=)

    for pid in $processes
    do
        process_name=$(ps -p $pid -o comm=)
        echo -n $(date +%F,%H:%M:%S) >> log/$process_name.log
        process_size=$(ps -p $pid -o size | grep [0-9])
        echo "$(bc <<< "scale=2;$tamanho_processo/1024") MB" >> log/$process_name.log
    done 
}

memory_processes()
if [ $? -eq 0 ]
then
    echo "Arquivos salvos com sucesso!"
else
    echo "Tivemos um problema ao salvar os arquivos"
fi




