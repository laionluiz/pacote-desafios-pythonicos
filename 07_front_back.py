"""
07. front_back

Considere dividir uma string em duas metades.
Caso o comprimento seja par, a metade da frente e de trás tem o mesmo tamanho.
Caso o comprimento seja impar, o caracter extra fica na metade da frente.

Exemplo: 'abcde', a metade da frente é 'abc' e a de trás é 'de'.

Finalmente, dadas duas strings a e b, retorne uma string na forma:
a-frente + b-frente + a-trás + b-trás
"""
def front_back(a, b):
    # +++ SUA SOLUÇÃO 1 +++
    # Basic Pythonist
    # a_frente, b_frente = a[:(len(a)//2)+1 if len(a)%2!=0 else ((len(a)//2))], \
    #                      b[:(len(b)//2)+1 if len(b)%2!=0 else ((len(b)//2))]
    # a_tras, b_tras = a[(len(a)//2)+1 if len(a)%2!=0 else ((len(a)//2)):], \
    #                  b[(len(b)//2)+1 if len(b)%2!=0 else ((len(b)//2)):]
    # return a_frente + b_frente + a_tras + b_tras

    # +++ SUA SOLUÇÃO 2 +++
    # Pythonist cleaned and documented
    pos_char_odd_a = (len(a)//2)+1
    pos_char_odd_b = (len(b)//2)+1
    pos_char_even_a = (len(a)//2)
    pos_char_even_b = (len(b)//2)
    is_len_a_odd = len(a)%2!=0
    is_len_b_odd = len(b)%2!=0
    a_frente, b_frente = a[:pos_char_odd_a if is_len_a_odd else pos_char_even_a], \
                         b[:pos_char_odd_b if is_len_b_odd else pos_char_even_b]
    a_tras, b_tras = a[pos_char_odd_a if is_len_a_odd else pos_char_even_a:], \
                     b[pos_char_odd_b if is_len_b_odd else pos_char_even_b:]
    return a_frente + b_frente + a_tras + b_tras

# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---

def test(f, in_, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(*in_)

    if out == expected:
        sign = '✅'
        info = ''
    else:
        sign = '❌'
        info = f'e o correto é {expected!r}'

    print(f'{sign} {f.__name__}{in_!r} retornou {out!r} {info}')


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(front_back, ('abcd', 'xy'), 'abxcdy')
    test(front_back, ('abcde', 'xyz'), 'abcxydez')
    test(front_back, ('Kitten', 'Donut'), 'KitDontenut')
