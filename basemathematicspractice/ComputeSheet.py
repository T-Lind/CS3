from BaseOperations import bin_to_hex, hex_to_dec, add_bin, sub_bin

def add_bin_nums(num1, num2):
    max_len = max(len(num1), len(num2))
    num1.zfill(max_len-len(num1))
    num2.zfill(max_len-len(num2))
    result = add_bin(num1, num2)
    hex_result = bin_to_hex(result)
    print(f" {num1}\n+{num2}\n{'-'*(max_len+1)}\n{result}(b2) or {hex_result}(b16) or {hex_to_dec(hex_result)}(b10)\n")

def sub_bin_nums(num1, num2):
    max_len = max(len(num1), len(num2))
    num1.zfill(max_len)
    num2.zfill(max_len)
    result = sub_bin(num1, num2)
    hex_result = bin_to_hex(result)
    print(
        f" {num1}\n-{num2}\n{'-' * (max_len + 1)}\n{result}(b2) or {hex_result}(b16) or {hex_to_dec(hex_result)}(b10)\n")

if __name__ == '__main__':
    print("ADDING BINARY NUMBERS WORKSHEET\n--------------")
    print("Solving row 2:\n")

    add_bin_nums("101101", "110010")
    add_bin_nums("101010", "110100")
    add_bin_nums("101001", "110101")
    add_bin_nums("100110", "110110")

    print("Solving row 5:\n")

    add_bin_nums("101001", "100101")
    add_bin_nums("100011", "101110")
    add_bin_nums("100010", "110000")
    add_bin_nums("101110", "110101")


    print("SUBTRACTING BINARY NUMBERS WORKSHEET\n--------------")
    print("Solving row 2:\n")

    sub_bin_nums("1000010", "0100001")

