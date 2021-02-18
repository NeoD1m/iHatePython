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


def listMyList(list=[[], []]):
    for i in range(len(list)):
        print("\n")
        for j in range(len(list[i])):
            print(list[i][j], end=" ")


def f23(list=[[]]):
    for i in range(len(list)):  # Удаляем None
        while None in list[i]:
            list[i].remove(None)

    for i in range(len(list) - 1):  # Удаляем пустые строки
        if not list[i]:
            list.remove(list[i])

    for i in range(len(list)):  # Удаляем дубликаты
        for j in range(len(list[i]) - 1):
            if list[i].count(list[i][j]) > 1:
                list[i].remove(list[i][j])

    for i in range(len(list)):  # Удаляем @mail.ru и меняем - на /
        for j in range(len(list[i]) - 1):
            if "@" in list[i][j]:
                list[i][j] = list[i][j].split("@", 1)[0]
            if "-" in list[i][j]:
                list[i][j] = list[i][j].replace("-", "/")

    for i in range(len(list)):  # Выделяем фамилию в отдельную клетку
        for j in range(len(list[i])):
            if "!" in list[i][j]:
                list[i].append(list[i][j].split("!", 1)[1])
                list[i][j + 1] = list[i][j + 1].split(" ", 1)[0]

    for i in range(len(list)):  # Меняем фамилию и проценты местами
        for j in range(len(list[i]) - 1):
            if "!" in list[i][j]:
                temp = list[i][j + 1]
                list[i][j + 1] = list[i][j]
                list[i][j] = temp

    for i in range(len(list)):  # Переводим числа в проценты
        for j in range(len(list[i])):
            if "!" in list[i][j]:
                list[i][j] = list[i][j].split("!", 1)[0]
                list[i][j] = str(int(round(float(list[i][j]), 2) * 100)) + "%"

    # listMyList([*zip(*list)])
    return [*zip(*list)]


if __name__ == '__main__':
    f23([["besizak60@rambler.ru", None, "besizak60@rambler.ru", "2002-04-12", "0.899!Бесицак Федор"],
         [None, None, None, None, None],
         ["nocman35@yandex.ru", None, "nocman35@yandex.ru", "2002-01-27", "0.729!Ночман Артур"],
         ["gordej5@rambler.ru", None, "gordej5@rambler.ru", " 1999-10-10", "0.560!Гибов Гордей"]
         ])
    f23([["vasilij45@gmail.com", None, "vasilij45@gmail.com", "2000-01-05", "0.759!Видко Василий"],
         [None, None, None, None, None],
         ["cizli81@yahoo.com", None, "cizli81@yahoo.com", "2004-12-13", "0.650!Чицли Павел"],
         ["sebinman97@yahoo.com", None, "sebinman97@yahoo.com", "2003-04-08", "0.440!Шебинман Марк"],
         ["vladimir77@mail.ru", None, "vladimir77@mail.ru", "2002-08-23", "0.520!Мовигко Владимир"],
         ])
