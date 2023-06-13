#!/bin/bash
echo "Iniciando geracao de dados..."
gcc ./models/bash/gpt.c -o executavel
./executavel
zip -r arquivo.zip ./models/bash/
