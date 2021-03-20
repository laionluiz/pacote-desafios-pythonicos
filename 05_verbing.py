"""
05. verbing

Dada uma string, se seu tamanho for pelo menos 3,
adicione 'ing' no seu fim, a menos que a string
já termine com 'ing', nesse caso adicione 'ly'.

Se o tamanho da string for menor que 3, não altere nada.

Retorne o resultado da string.
"""

def verbing(s):
    # +++ SUA SOLUÇÃO 1 +++
    # Basic Pythonist I
    # new_s = ''
    # new_s += s
    # new_s += ('ly' if new_s[-3:] == 'ing' else 'ing')
    # return new_s if len(s) > 3 else s

    # +++ SUA SOLUÇÃO 2 +++
    # Basic Pythonist II
    # cp_s = s
    # s += ('ly' if s[-3:] == 'ing' else 'ing')
    # return s if len(cp_s) > 3 else cp_s

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
    test(verbing, 'hail', 'hailing')
    test(verbing, 'swiming', 'swimingly')
    test(verbing, 'do', 'do')
    test(verbing, 'a', 'a')
    test(verbing, 'Laion', 'Laioning')
    test(verbing, 'Laioning', 'Laioningly')