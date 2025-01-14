"""
02. both_ends

Dada uma string s, retorne uma string feita com os dois primeiros
e os dois ultimos caracteres da string original.
Exemplo: 'spring' retorna 'spng'. Entretanto, se o tamanho da string
for menor que 2, retorne uma string vazia.
"""

def both_ends(s):
    # +++ SUA SOLUÇÃO 1 +++
    # Pythonic way
    # return s[:2]+s[-2:] if len(s) >= 2 else ''

    # +++ SUA SOLUÇÃO 2 +++
    # Old School way
    i = 0
    new_s = ''
    total_size = len(s)
    last_item = total_size - 1
    penultimate_item = last_item -1

    if total_size == 2:
        new_s = s*2
    elif total_size == 3:
        new_s = s[0]+s[1]+s[1]+s[2]
    else:
        while i < total_size:
            if i in (0, 1, penultimate_item, last_item):
                new_s += s[i]
            i += 1

    return new_s if total_size >= 2 else ''

# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---

def test(f, in_, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(in_)

    if out == expected:
        sign = '✅'
        info = ''
    else:
        sign = '❌'
        info = f'e o correto é {expected!r}'

    print(f'{sign} {f.__name__}({in_!r}) retornou {out!r} {info}')


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(both_ends, 'spring', 'spng')
    test(both_ends, 'Hello', 'Helo')
    test(both_ends, 'a', '')
    test(both_ends, 'xyz', 'xyyz')
    test(both_ends, 'xy', 'xyxy')
    test(both_ends, 'xyyyyyyyy', 'xyyy')
    test(both_ends, 'laion', 'laon')
