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
    return list


if __name__ == '__main__':
    print(f22("0xd139a832"))
    print(f22("0x6afb6fe4"))
