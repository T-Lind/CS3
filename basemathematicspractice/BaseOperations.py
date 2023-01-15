hex_to_dec_table = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "A": 10, "B": 11,
                    "C": 12, "D": 13, "E": 14, "F": 15}

def bin_to_hex(number: str, hex_nums=128) -> str:
    bin_number = int(number)
    temp = 0
    mult = 1

    cnt = 1

    hexNum = ["0"] * hex_nums

    i = 0
    while bin_number > 0:
        if i > hex_nums:
            raise IndexError(f"Needed more than {hex_nums} hex hums to convert 0b{number} to hex")

        remainder = bin_number % 10
        temp = temp + (remainder * mult)

        if cnt % 4 == 0:
            if temp < 10:
                hexNum[i] = chr(temp + 48)
            else:
                hexNum[i] = chr(temp + 55)

            mult = 1
            temp = 0
            cnt = 1
            i += 1

        else:
            mult *= 2
            cnt = cnt + 1
        bin_number = int(bin_number / 10)

    if cnt != 1:
        hexNum[i] = chr(temp + 48)

    if cnt == 1:
        i -= 1

    ret_str = ""

    while i >= 0:
        ret_str += hexNum[i]
        i -= 1
    return ret_str

def hex_to_dec(hex_number: str) -> str:
    result: int = 0
    size = len(hex_number) - 1

    for character in hex_number:
        result = result + hex_to_dec_table[character] * 16 ** size
        size -= 1

    return str(result)

def add_bin(num1: str, num2: str) -> str:
    ret_str = ''
    carry = 0

    for i in range(max(len(num1), len(num2)) - 1, -1, -1):
        remainder = carry
        remainder += 1 if int(num1[i]) else 0
        remainder += 1 if int(num2[i]) else 0
        ret_str = ('1' if remainder % 2 == 1 else '0') + ret_str

        carry = 0 if remainder <= 1 else 1

    if carry != 0:
        ret_str = '1' + ret_str

    return ret_str.zfill(max(len(num1), len(num2)))

inv_table = {"0": "1", "1": "0"}

def _inv_bits(num: str) -> str:
    num_inv = ""
    for character in num:
        num_inv += inv_table[character]
    return num_inv

def sub_bin(num1, num2):
    max_len = len(num1)

    result = ''
    temp = 0
    for i in range(max_len -1, -1, -1):
        num = int(num1[i]) - int(num2[i]) - temp
        if num % 2 == 1:
            result = '1' + result
        else:
            result = '0' + result

        if num < 0:
            temp = 1
        else:
            temp = 0

    if temp != 0:
        result = "01" + result

    if int(result) == 0:
        result = 0

    return result
