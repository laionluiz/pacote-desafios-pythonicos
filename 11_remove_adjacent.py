"""
11. remove_adjacent

Dada uma lista de números, retorne uma lista onde todos elementos
adjacentes iguais são reduzidos a um único elemento.

Exemplo: [1, 2, 2, 3]
Irá retornar: [1, 2, 3]
"""

def remove_adjacent(nums):
    # # +++ SUA SOLUÇÃO 1 +++
    # # Classic way
    # new_nums = []
    # i = 0
    # while i < len(nums):
    #     if nums[i] not in new_nums:
    #         new_nums.append(nums[i])
    #     elif nums[i] != nums[i-1]:
    #         new_nums.append(nums[i])
    #     i += 1
    # return new_nums

    # +++ SUA SOLUÇÃO 2 +++
    # Classic way - II
    # new_nums = []
    # i = 0
    # while i < len(nums):
    #     if nums[i] not in new_nums or nums[i] != nums[i-1]:
    #         new_nums.append(nums[i])
    #     i += 1
    # return new_nums

    # # +++ SUA SOLUÇÃO 3 +++
    # # Basic Pythonist
    # new_nums = []
    # for i in range(len(nums)):
    #     if nums[i] not in new_nums or nums[i] != nums[i-1]:
    #         new_nums.append(nums[i])
    # return new_nums

    # +++ SUA SOLUÇÃO 4 +++
    # Basic Pythonist - Enumerate
    # new_nums = []
    # for i, n in enumerate(nums):
    #     if nums[i] not in new_nums or nums[i] != nums[i-1]:
    #         new_nums.append(nums[i])
    # return new_nums

    # +++ SUA SOLUÇÃO 5 +++
    # Basic Pythonist - Last position
    new_nums = []
    last_pos = ''
    for i in nums:
        if i != last_pos:
            new_nums.append(i)
        last_pos = i
    return new_nums


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
    test(remove_adjacent, [1, 2, 2, 3], [1, 2, 3])
    test(remove_adjacent, [2, 2, 3, 3, 3], [2, 3])
    test(remove_adjacent, [], [])
    test(remove_adjacent, [2, 2, 3, 3, 3, 2, 2], [2, 3, 2])
    test(remove_adjacent, [2, 2, 3, 3, 3, 2, 2, 1, 2, 7], [2, 3, 2, 1, 2, 7])
    test(remove_adjacent, [3, 3, 3, 2, 2, 1, 2, 7, 7, 7, 7], [3, 2, 1, 2, 7])
    test(remove_adjacent, [1, 1, 1, 1, 4, 1, 1], [1, 4, 1])