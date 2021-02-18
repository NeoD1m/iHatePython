def f22(my_hexdata):
    scale = 16  # equals to hexadecimal
    num_of_bits = 8

    bit_list = []
    bit_list[:0] = bin(int(my_hexdata, scale))[2:].zfill(num_of_bits)

    while len(bit_list) < 32:
        bit_list.insert(0, "0")

    bit_list2 = []

    for i in range(6, 18, 1):  # B
        bit_list2.insert(i - 7, bit_list[i])

    for i in range(2, 6, 1):  # C
        bit_list2.insert(i + 9, bit_list[i])

    for i in range(0, 2, 1):  # ED
        bit_list2.insert(i + 16, bit_list[i])

    for i in range(18, 32, 1):  # A
        bit_list2.insert(i, bit_list[i])

    bitstring = ""
    for bits in bit_list2:
        bitstring += bits

    return hex(int(bitstring, 2))


def f21(list=[]):
    if 2010 in list:
        return 13
    elif 1995 in list:
        if 'c' in list:
            if 'pug' in list:
                return 5
            elif 'cuda' in list:
                return 6
        elif 'mako' in list:
            if 1967 in list:
                return 2
            elif 1996 in list:
                return 3
            elif 1960 in list:
                return 4
        elif 'lfe' in list:
            if 'pug' in list:
                return 0
            elif 'cuda' in list:
                return 1
    elif 2019 in list:
        if 'c' in list:
            return 12
        elif 'mako' in list:
            if 1967 in list:
                return 9
            elif 1996 in list:
                return 10
            elif 1960 in list:
                return 11
        elif 'lfe' in list:
            if 'pug' in list:
                return 7
            elif 'cuda' in list:
                return 8
    return list


if __name__ == '__main__':
    print(f21(['cuda', 'c', 1996, 1995]))
    print(f21(['pug', 'mako', 1967, 2010]))
    print(f21(['pug', 2019, 1967, 'mako']))
