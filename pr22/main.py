# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def hexToBin(my_hexdata):
    scale = 16  ## equals to hexadecimal
    num_of_bits = 8
    return bin(int(my_hexdata, scale))[2:].zfill(num_of_bits)


    #24-14
    #29-25
    #31
    #30
    #13-0

if __name__ == '__main__':
    print(hexToBin("d1391832"))
