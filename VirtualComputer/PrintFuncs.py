def print_byte_pairs(bool_list: list):
    for i in bool_list:
        if i:
            print(1, end="")
        else:
            print(0, end="")
    print()


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
    print()


def print_4_depth(bool_list: list):
    for mem in bool_list:
        for item in mem:
            print_2_depth(item)
    print()
