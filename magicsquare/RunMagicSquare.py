from MagicSquare import create_magic_square, is_magic_square
import numpy as np
from numpy import int16

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
