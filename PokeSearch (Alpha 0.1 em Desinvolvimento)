import requests
import os
from colorama import Fore, init
init(autoreset=True)
os.system('title PokeSearch (Versão Alpha 0.1)'

def procurar(pokemon, informacoes): # Procura o Nome do Pokemon que você escolheu
    pokemon_format = pokemon.strip().lower()
    resposta = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_format}')
    if resposta.status_code == 200:
        dados = resposta.json()
        id_ = dados['id']
        experiencia_base = dados['base_experience']
        altura = dados['height'] + 'cm'
        habilidades = dados['abilities']['ability']['name']
    else:
        print(Fore.RED + f'Erro! Código de Status é {resposta.status_code}')

procurar('Pikachu')
