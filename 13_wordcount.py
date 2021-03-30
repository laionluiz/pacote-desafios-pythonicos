"""
13. wordcount

Este desafio é um programa que conta palavras de um arquivo qualquer de duas
formas diferentes.

A. Lista todas as palavras por ordem alfabética indicando suas ocorrências.

Ou seja...

Dado um arquivo letras.txt contendo as palavras: A a C c c B b b B
Quando você executa o programa: python wordcount.py --count letras.txt
Ele deve imprimir todas as palavras em ordem alfabética seguidas
do número de ocorrências.

Por exemplo:

$ python wordcount.py --count letras.txt
a 2
b 4
c 3

B. Lista as 20 palavras mais frequêntes indicando suas ocorrências.

Ou seja...

Dado um arquivo letras.txt contendo as palavras: A a C c c B b b B
Quando você executa o programa: python wordcount.py --topcount letras.txt
Ele deve imprimir as 20 palavras mais frequêntes seguidas
do número de ocorrências, em ordem crescente de ocorrências.

Por exemplo:

$ python wordcount.py --topcount letras.txt
b 4
c 3
a 2

Abaixo já existe um esqueleto do programa para você preencher.

Você encontrará a função main() chama as funções print_words() e
print_top() de acordo com o parâmetro --count ou --topcount.

Seu trabalho é implementar as funções print_words() e depois print_top().

Dicas:
* Armazene todas as palavras em caixa baixa, assim, as palavras 'A' e 'a'
  contam como a mesma palavra.
* Use str.split() (sem parêmatros) para fazer separar as palavras.
* Não construa todo o programade uma vez. Faça por partes executando
e conferindo cada etapa do seu progresso.
"""

import sys
import collections
from operator import itemgetter, attrgetter

dict = {'a': 0, 'b': 0, 'c': 0}

# +++ SUA SOLUÇÃO +++
# Defina as funções print_words(filename) e print_top(filename).
def content(ordered_list):
    #Basic Loop with print
    # for l, qtd in ordered_list:
    #     print(l, qtd)

    #solution without print
    # l = []
    # for w, qtd in ordered_list:
    #     l.append(f'{w} {qtd}')
    #
    # return '\n'.join(l)

    #List Comprehension
    return '\n'.join([f'{w} {qtd}' for w, qtd in ordered_list])


def work_file(filename):
    #Read file
    f = open(filename, 'r')
    data = f.read()
    f.close()

    #Split the file
    words = data.lower().split()

    #Count ocurrencies
    counter = collections.Counter(words)

    #return a dict like k/v
    return counter

def print_words(filename):
    # Sol 1 - Old fashion a,b,c only
    '''
    f = open(filename, 'r')
    data = f.read()
    f.close()

    words = data.split()
    cont_a = 0
    cont_b = 0
    cont_c = 0
    for w in words:
        if w[0].lower() == 'a':
            cont_a += 1
        elif w[0].lower() == 'b':
            cont_b += 1
        elif w[0].lower() == 'c':
            cont_c += 1

    print('a', cont_a, '\nb', cont_b, '\nc', cont_c)
    '''
    # Sol 2 - Pythonist - collections + sorted
    ordered_list = sorted(work_file(filename).items())
    return ordered_list


def print_top(filename):
    ordered_list = sorted(work_file(filename), reverse=True, key=lambda t: t[-1])
    return ordered_list[:20]


# A função abaixo chama print_words() ou print_top() de acordo com os
# parêtros do programa.
def main():
    if len(sys.argv) != 3:
        print('Utilização: ./13_wordcount.py {--count | --topcount} file')
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    if option == '--count':
        print(content(print_words(filename)))
    elif option == '--topcount':
        print(content(print_top(filename)))
    else:
        print('unknown option: ' + option)
        sys.exit(1)


if __name__ == '__main__':
    main()
