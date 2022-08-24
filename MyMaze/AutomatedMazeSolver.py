from Maze import Maze

my_maze = Maze(5, 5)
my_maze.create_maze()

while True:
    my_maze.printMaze()

    if my_maze.is_maze_complete():
        print("Congratulations! You beat the maze!")
        break

    char_input = input("Enter w/a/s/d: ")

    if char_input == 'a':
        my_maze.move_left()

    elif char_input == 'd':
        my_maze.move_right()

    elif char_input == 'w':
        my_maze.move_up()

    elif char_input == 's':
        my_maze.move_down()

    else:
        break
