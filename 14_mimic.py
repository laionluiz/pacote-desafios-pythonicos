"""
14. mimic

Neste desafio você vai fazer um gerador de lero-lero.

É um programa que lê um arquivo, armazena a relação entre as palavras e
então gera um novo texto respeitando essas relações para imitar um
escritor de verdade.

Para isso você precisa:

A. Abrir o arquivo especificado via linha de comando.

B. Ler o conteúdo e separar as palavras obtendo uma lista de palavras.

C. Criar um dicionário de "imitação".

Nesse dicionário a chave será uma palavra e o valor será uma lista
contendo as palavras que aparecem no texto após a palavra usada na chave.

Por exemplo, suponha um arquivo com o conteúdo: A B C B A

O dicionário de imitação deve considerar que:
* a chave A contém uma lista com a palavra B
* a chave B contém uma lista com as palavras C e A
* a chave C contém uma lista com a palavra B

Além disso precisamos considerar que:
* a chave '' contém uma lista com a primeira palavra do arquivo
* a última palavra do arquivo contém uma lista com a palavra ''.

Com o dicionario imitador é bastante simples emitir aleatoriamente texto
que imita o original. Imprima uma palavra, depois veja quais palavras podem
vir a seguir e pegue uma aleatoriamente como a proxima palavra do texto.

Use a string vazia como a primeira palavra do texto para preparar as coisas.

Nota: o módulo padrão do python 'random' conta com o random.choice(list),
método que escolhe um elemento aleatório de uma lista não vazia.
"""

import random
import sys
from collections import defaultdict


def mimic_dict(filename):
    """Retorna o dicionario imitador mapeando cada palavra para a lista de
    palavras subsequentes."""
    # +++ SUA SOLUÇÃO +++
    with open(filename) as f:
        data = f.read()

    l_content = data.split()

    #Generate l_keys list
    #Solution 1
    # for k in l_content:
    #     if k not in l_keys:
    #         l_keys.append(k)

    #Soluion 2
    # l_keys = list(set(l_content))
    # possible_words = []

    #Generate lists of possible words
    # Solution 1
    # for key in l_keys:
    #     l = []
    #     for i, word in enumerate(l_content):
    #         if word == key and i != len(l_content)-1:
    #             l.append(l_content[i+1])
    #     possible_words.append(l)

    #Solution 3
    dict_words = defaultdict(list)
    dict_words[''] = l_content[0]
    dict_words[l_content[-1]] = ['']
    for key, word in zip(l_content, l_content[1:]):
        dict_words[key].append(word)

    # leros = dict(zip(l_keys, possible_words))

    # return leros

    return dict_words

def print_mimic(mimic_dict, word):
    """Dado o dicionario imitador e a palavra inicial, imprime texto de 200 palavras."""
    # +++ SUA SOLUÇÃO +++
    l_dict = mimic_dict.get(word)
    # print(f'Finding {word} in dict...')
    msg = []

    for i in range(0, 10):
        msg.append(random.choice(list(l_dict)))

    return ' '.join(msg)


# Chama mimic_dict() e print_mimic()
def main():
    if len(sys.argv) != 3:
        print('Utilização: ./14_mimic.py file-to-read word-to-generate')
        sys.exit(1)

    dict = mimic_dict(sys.argv[1])
    w = sys.argv[2]
    print(print_mimic(dict, w))

if __name__ == '__main__':
    main()
