from Maze import Maze
import copy

my_maze = Maze(5, 5)
my_maze.create_maze()
solve_steps = 0


def solve_maze(maze: Maze):
    global solve_steps

    maze_copy = copy.deepcopy(maze)

    print(maze_copy.player.r, maze_copy.player.c)

    # Check and see if the maze is complete
    if maze_copy.player.r is my_maze.end_r and maze_copy.player.c is my_maze.end_c:
        return maze_copy

    if maze_copy.count_options() <= 1 and solve_steps > 1:
        return

    states = maze_copy.get_maze_options()
    print(states)

    if solve_steps > 1 and maze_copy.in_dead_end() is not False:


    for i in range(len(states)):
        if states[i] is False:
            continue

        if i == 0:
            maze_copy.move_right()
            solve_maze(maze_copy)
        elif i == 1:
            maze_copy.move_up()
            solve_maze(maze_copy)
        elif i == 2:
            maze_copy.move_left()
            solve_maze(maze_copy)
        elif i == 3:
            maze_copy.move_down()
            solve_maze(maze_copy)
        else:
            raise IndexError(f"Improper index applied to the states object! in {__name__}")

    solve_steps += 1


solution = solve_maze(my_maze)
solution.print_maze()

print(f"Solved the maze in {solve_steps} steps!")
