import requests
import os
from colorama import Fore, init
init(autoreset=True)
os.system('title PokeSearch (Versão Alpha 0.1)')

def procurar(pokemon): # Procura o Nome do Pokemon que você escolheu
    pokemon_format = pokemon.strip().lower()
    resposta = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_format}')
    if resposta.status_code == 200:
        dados = resposta.json()
        id_ = dados['id']
        experiencia_base = dados['base_experience']
        altura = dados['height']
        habilidade = [
            habilidade['ability']['name']
            for habilidade in dados['abilities']
            if not habilidade['is_hidden']
        ]

        return {
            'id': id_,
            'altura': altura,
            'experiencia_base': experiencia_base,
            'habilidade': habilidade
        }
    else:
        print(Fore.RED + f'Erro! Código de Status é {resposta.status_code}, Por Favor Contacte o Desinvolvedor!')

info = procurar('Pikachu')
print(info['id'])
print(info['altura'])
print(info['experiencia_base'])
print(info['habilidade'])
