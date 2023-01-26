# Lab 1:
numerical_english = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
                     "ten": 10}

# Lab 2:
numerical_roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000, " ": 0}

# Lab 3:

# Different test cases
inputs = ["V I I", "X X", "C D M", "L"]
for entry in inputs:
    print(f"\"{entry}\" in roman numerals converts to {sum(numerical_roman[character] for character in entry)}")
