def cvt_int(*int_list):
    return (bool(val) for val in int_list)


def print_hex(bool_list):
    str_val = ""
    for i in bool_list:
        str_val += str(int(i))
    val = str_val.encode('ascii')
    num = int(val, 2)
    hex_num = hex(num)
    print(hex_num)


def print_hex_long(bool_list: list):
    try:
        if type(bool_list[0]) == bool:
            print_hex(bool_list)
            return
    except Exception as e:
        raise IndexError("Tried to get an index from a boolean!")

    for small_list in bool_list:
        print_hex_long(small_list)


def print_depth(bool_list: list):
    for j in bool_list:
        if j:
            print(1, end="")
        else:
            print(0, end="")


def print_2_depth(bool_list: list):
    for i in range(len(bool_list) - 1, -1, -1):
        for j in bool_list[i]:
            if j:
                print(1, end="")
            else:
                print(0, end="")
        print(" ", end="")
    print()


def print_3_depth(bool_list: list):
    for mem in bool_list:
        print_2_depth(mem)


def print_4_depth(bool_list: list):
    for mem in bool_list:
        for item in mem:
            print_2_depth(item)
    print()


def print_5_depth(bool_list: list):
    for mem in bool_list:
        for item in mem:
            print_3_depth(item)
    print()
