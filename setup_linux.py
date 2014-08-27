#!/bin/bash
#Instalando python virtualenv
sudo apt-get install python-virtualenv

#Criando um novo virtualenv com python3
virtualenv --no-site-packages --distribute -p /usr/bin/python3 venv/

#Acessando o ambiente
source venv/bin/activate

#Instalando dependencias
pip install -r requirements.txt
