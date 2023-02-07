import string

character_dict = dict()
for item in string.ascii_letters + string.digits + string.punctuation:
    character_dict[item] = 0


def count_symbols(string):
    print(f"Reading string \"{string}\":")
    copy_dict = character_dict.copy()
    for item in string.replace(" ", ""):
        copy_dict[item] += 1

    for key in copy_dict:
        if copy_dict.get(key) != 0:
            print(f"{key} count = {copy_dict.get(key)}")

    print()


def count_symbols_hist(string):
    print("char 1---5----10---15")
    copy_dict = character_dict.copy()
    for item in string.replace(" ", ""):
        copy_dict[item] += 1
    for key in copy_dict:
        if copy_dict.get(key) != 0:
            print(f"{key}    " + "*" * copy_dict.get(key))
    print()


print("LAB 1:")

count_symbols("a b c d e f g h i a c d e g h i h k")
count_symbols("1 2 3 4 5 6 1 2 3 4 5 1 3 1 2 3 4")
count_symbols("Y U I O Q W E R T Y")
count_symbols("4 T # @ ^ # # #")

print("LAB 2")
count_symbols_hist("a b c d e f g h i a c d e g h i h k")
count_symbols_hist("1 2 3 4 5 6 1 2 3 4 5 1 3 1 2 3 4")
count_symbols_hist("Y U I O Q W E R T Y")
count_symbols_hist("4 T # @ ^ # # #")
