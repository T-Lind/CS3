import numpy as np
from numpy import int16


def is_magic_square(square):
    """
    Determine if an array is a magic square or not
    :param square: the np.ndarray object to reference
    :return: a boolean of if it is a magic square
    """
    sums = np.concatenate((np.sum(square, axis=0, dtype=int16),  # Sum along rows
                           np.sum(square, axis=1, dtype=int16),  # Sum along columns
                           [sum(np.diagonal(square))],  # Main diagonal 1
                           [sum(np.diagonal(np.flipud(square)))]))  # Main diagonal 2
    return np.all(sums == sums[0])  # Check and see if all items in the sums array are equal to each other


def create_magic_square(square_size) -> np.ndarray:
    # Does not work with odd numbers per lab specifications
    assert square_size % 2 != 0

    square = np.zeros(shape=[square_size, square_size], dtype=int16)

    r = square_size - 1
    c = square_size // 2

    # Loop through array
    num = 1
    while num <= (square_size ** 2):
        if c == -1 and r == square_size:
            r = square_size - 2
            c = 0
        else:
            if r == square_size:
                r = 0
            if c < 0:
                c = square_size - 1

        if square[int(c)][int(r)]:
            r = r - 2
            c = c + 1
            continue
        else:
            square[int(c)][int(r)] = num
            num = num + 1

        r = r + 1
        c = c - 1

    return square


if __name__ == "__main__":
    print("MAGIC NUMER LAB PART 1:")
    square_size = int(input("Enter an integer size for the magic square to be read:"))

    square = np.zeros(shape=[square_size, square_size], dtype=int16)

    for r in range(square_size):
        for c in range(square_size):
            square[r][c] = int(input("Enter an integer value:"))
    print(f"The provided square is a magic square: {is_magic_square(square)}\n\n")


    print("MAGIC NUMER LAB PART 2:")
    print("Generated square 3x3:")
    generated_square = create_magic_square(3)
    print(generated_square)
    print(f"The generated square is a magic square: {is_magic_square(generated_square)}")

    print("Generated square 5x5:")
    generated_square = create_magic_square(5)
    print(generated_square)
    print(f"The generated square is a magic square: {is_magic_square(generated_square)}")
