import random
from collections import namedtuple

from colorama import init, Fore

# Create a basic object with row and column member data
from Player import Player


class Maze:
    def __init__(self, height, width):
        """
        Create a maze given a height and width of the maze
        :param height: The height of the maze in rows
        :param width: The width of the row in columns
        """
        self.height = height
        self.width = width

        self.maze = []
        self.wall = '█'
        self.cell = ' '
        self.unvisited = 'u'
        self.end = '▢'
        self.trodden = '△'

        self.player = Player(-1, -1)

        # Define the ending coordinates

        self.end_r = -1
        self.end_c = -1

        init()

    def printMaze(self):
        """
        Print the maze, given an input maze
        :param maze: the input maze
        """
        print()
        for i in range(0, self.height):
            for j in range(0, self.width):
                if self.maze[i][j] == self.wall:
                    print(Fore.GREEN + str(self.maze[i][j]), end=" ")
                elif self.maze[i][j] == self.end:
                    print(Fore.RED + str(self.maze[i][j]), end=" ")
                else:
                    print(Fore.BLUE + str(self.maze[i][j]), end=" ")

            print()
        print('\n\n')

    def surroundingCells(self, rand_wall):
        s_cells = 0
        if self.maze[rand_wall[0] - 1][rand_wall[1]] == self.cell:
            s_cells += 1
        if self.maze[rand_wall[0] + 1][rand_wall[1]] == self.cell:
            s_cells += 1
        if self.maze[rand_wall[0]][rand_wall[1] - 1] == self.cell:
            s_cells += 1
        if self.maze[rand_wall[0]][rand_wall[1] + 1] == self.cell:
            s_cells += 1

        return s_cells

    def is_maze_complete(self):
        """
        See if the maze is complete
        :return: A boolean state of whether the maze is complete or not
        """
        if self.player.r == self.end_r and self.player.c == self.end_c:
            return True
        return False

    def check_cell_open(self, r, c):
        if r >= len(self.maze) or c >= len(self.maze[0]):
            return False

        if self.maze[r][c] == self.wall:
            return False
        return True

    def get_maze_options(self):
        # Stores right, above, left, below order
        option_states = [
            self.check_cell_open(self.player.r, self.player.c + 1),
            self.check_cell_open(self.player.r - 1, self.player.c),
            self.check_cell_open(self.player.r, self.player.c - 1),
            self.check_cell_open(self.player.r + 1, self.player.c)]

        return option_states

    def move_up(self):
        if self.get_maze_options()[1] is True:
            self.trodden = '△'
            self.maze[self.player.r][self.player.c] = self.cell
            self.player.r -= 1
            self.set_trodden()

    def move_down(self):
        if self.get_maze_options()[3] is True:
            self.trodden = '▽'
            self.maze[self.player.r][self.player.c] = self.cell
            self.player.r += 1
            self.set_trodden()

    def move_left(self):
        if self.get_maze_options()[2] is True:
            self.trodden = '◁'
            self.maze[self.player.r][self.player.c] = self.cell
            self.player.c -= 1
            self.set_trodden()

    def move_right(self):
        self.trodden = '▷'
        if self.get_maze_options()[0] is True:
            self.maze[self.player.r][self.player.c] = self.cell
            self.player.c += 1
            self.set_trodden()

    def set_trodden(self):
        self.maze[self.player.r][self.player.c] = self.trodden

    def create_maze(self):
        """
        Create the cells in the maze, randomly
        :return: nothing, prints to the screen
        """
        # Denote all cells as unvisited
        for i in range(0, self.height):
            line = []
            for j in range(0, self.width):
                line.append(self.unvisited)
            self.maze.append(line)

        # Randomize starting point and set it a cell
        starting_height = int(random.random() * self.height)
        starting_width = int(random.random() * self.width)
        if starting_height == 0:
            starting_height += 1
        if starting_height == self.height - 1:
            starting_height -= 1
        if starting_width == 0:
            starting_width += 1
        if starting_width == self.width - 1:
            starting_width -= 1

        # Mark it as cell and add surrounding walls to the list
        self.maze[starting_height][starting_width] = self.cell
        walls = [[starting_height - 1, starting_width], [starting_height, starting_width - 1],
                 [starting_height, starting_width + 1], [starting_height + 1, starting_width]]

        # Denote walls in maze
        self.maze[starting_height - 1][starting_width] = self.wall
        self.maze[starting_height][starting_width - 1] = self.wall
        self.maze[starting_height][starting_width + 1] = self.wall
        self.maze[starting_height + 1][starting_width] = self.wall

        while walls:
            # Pick a random wall
            rand_wall = walls[int(random.random() * len(walls)) - 1]

            # Check if it is a left wall
            if rand_wall[1] != 0:
                if self.maze[rand_wall[0]][rand_wall[1] - 1] == self.unvisited and self.maze[rand_wall[0]][
                    rand_wall[1] + 1] == self.cell:
                    # Find the number of surrounding cells
                    s_cells = self.surroundingCells(rand_wall)

                    if s_cells < 2:
                        # Denote the new path
                        self.maze[rand_wall[0]][rand_wall[1]] = self.cell

                        # Mark the new walls
                        # Upper cell
                        if rand_wall[0] != 0:
                            if self.maze[rand_wall[0] - 1][rand_wall[1]] != self.cell:
                                self.maze[rand_wall[0] - 1][rand_wall[1]] = self.wall
                            if [rand_wall[0] - 1, rand_wall[1]] not in walls:
                                walls.append([rand_wall[0] - 1, rand_wall[1]])

                        # Bottom cell
                        if rand_wall[0] != self.height - 1:
                            if self.maze[rand_wall[0] + 1][rand_wall[1]] != self.cell:
                                self.maze[rand_wall[0] + 1][rand_wall[1]] = self.wall
                            if [rand_wall[0] + 1, rand_wall[1]] not in walls:
                                walls.append([rand_wall[0] + 1, rand_wall[1]])

                        # Leftmost cell
                        if rand_wall[1] != 0:
                            if self.maze[rand_wall[0]][rand_wall[1] - 1] != self.cell:
                                self.maze[rand_wall[0]][rand_wall[1] - 1] = self.wall
                            if [rand_wall[0], rand_wall[1] - 1] not in walls:
                                walls.append([rand_wall[0], rand_wall[1] - 1])

                    # Delete wall
                    for wall in walls:
                        if wall[0] == rand_wall[0] and wall[1] == rand_wall[1]:
                            walls.remove(wall)

                    continue

            # Check if it is an upper wall
            if rand_wall[0] != 0:
                if self.maze[rand_wall[0] - 1][rand_wall[1]] == self.unvisited and self.maze[rand_wall[0] + 1][
                    rand_wall[1]] == self.cell:

                    s_cells = self.surroundingCells(rand_wall)
                    if s_cells < 2:
                        # Denote the new path
                        self.maze[rand_wall[0]][rand_wall[1]] = self.cell

                        # Mark the new walls
                        # Upper cell
                        if rand_wall[0] != 0:
                            if self.maze[rand_wall[0] - 1][rand_wall[1]] != self.cell:
                                self.maze[rand_wall[0] - 1][rand_wall[1]] = self.wall
                            if [rand_wall[0] - 1, rand_wall[1]] not in walls:
                                walls.append([rand_wall[0] - 1, rand_wall[1]])

                        # Leftmost cell
                        if rand_wall[1] != 0:
                            if self.maze[rand_wall[0]][rand_wall[1] - 1] != self.cell:
                                self.maze[rand_wall[0]][rand_wall[1] - 1] = self.wall
                            if [rand_wall[0], rand_wall[1] - 1] not in walls:
                                walls.append([rand_wall[0], rand_wall[1] - 1])

                        # Rightmost cell
                        if rand_wall[1] != self.width - 1:
                            if self.maze[rand_wall[0]][rand_wall[1] + 1] != self.cell:
                                self.maze[rand_wall[0]][rand_wall[1] + 1] = self.wall
                            if [rand_wall[0], rand_wall[1] + 1] not in walls:
                                walls.append([rand_wall[0], rand_wall[1] + 1])

                    # Delete wall
                    for wall in walls:
                        if wall[0] == rand_wall[0] and wall[1] == rand_wall[1]:
                            walls.remove(wall)

                    continue

            # Check the bottom wall
            if rand_wall[0] != self.height - 1:
                if self.maze[rand_wall[0] + 1][rand_wall[1]] == self.unvisited and self.maze[rand_wall[0] - 1][
                    rand_wall[1]] == self.cell:

                    s_cells = self.surroundingCells(rand_wall)
                    if s_cells < 2:
                        # Denote the new path
                        self.maze[rand_wall[0]][rand_wall[1]] = self.cell

                        # Mark the new walls
                        if rand_wall[0] != self.height - 1:
                            if self.maze[rand_wall[0] + 1][rand_wall[1]] != self.cell:
                                self.maze[rand_wall[0] + 1][rand_wall[1]] = self.wall
                            if [rand_wall[0] + 1, rand_wall[1]] not in walls:
                                walls.append([rand_wall[0] + 1, rand_wall[1]])
                        if rand_wall[1] != 0:
                            if self.maze[rand_wall[0]][rand_wall[1] - 1] != self.cell:
                                self.maze[rand_wall[0]][rand_wall[1] - 1] = self.wall
                            if [rand_wall[0], rand_wall[1] - 1] not in walls:
                                walls.append([rand_wall[0], rand_wall[1] - 1])
                        if rand_wall[1] != self.width - 1:
                            if self.maze[rand_wall[0]][rand_wall[1] + 1] != self.cell:
                                self.maze[rand_wall[0]][rand_wall[1] + 1] = self.wall
                            if [rand_wall[0], rand_wall[1] + 1] not in walls:
                                walls.append([rand_wall[0], rand_wall[1] + 1])

                    # Delete wall
                    for wall in walls:
                        if wall[0] == rand_wall[0] and wall[1] == rand_wall[1]:
                            walls.remove(wall)

                    continue

            # Check the right wall
            if rand_wall[1] != self.width - 1:
                if self.maze[rand_wall[0]][rand_wall[1] + 1] == self.unvisited and self.maze[rand_wall[0]][
                    rand_wall[1] - 1] == self.cell:

                    s_cells = self.surroundingCells(rand_wall)
                    if s_cells < 2:
                        # Denote the new path
                        self.maze[rand_wall[0]][rand_wall[1]] = self.cell

                        # Mark the new walls
                        if rand_wall[1] != self.width - 1:
                            if self.maze[rand_wall[0]][rand_wall[1] + 1] != self.cell:
                                self.maze[rand_wall[0]][rand_wall[1] + 1] = self.wall
                            if [rand_wall[0], rand_wall[1] + 1] not in walls:
                                walls.append([rand_wall[0], rand_wall[1] + 1])
                        if rand_wall[0] != self.height - 1:
                            if self.maze[rand_wall[0] + 1][rand_wall[1]] != self.cell:
                                self.maze[rand_wall[0] + 1][rand_wall[1]] = self.wall
                            if [rand_wall[0] + 1, rand_wall[1]] not in walls:
                                walls.append([rand_wall[0] + 1, rand_wall[1]])
                        if rand_wall[0] != 0:
                            if self.maze[rand_wall[0] - 1][rand_wall[1]] != self.cell:
                                self.maze[rand_wall[0] - 1][rand_wall[1]] = self.wall
                            if [rand_wall[0] - 1, rand_wall[1]] not in walls:
                                walls.append([rand_wall[0] - 1, rand_wall[1]])

                    # Delete wall
                    for wall in walls:
                        if wall[0] == rand_wall[0] and wall[1] == rand_wall[1]:
                            walls.remove(wall)

                    continue

            # Delete the wall from the list anyway
            for wall in walls:
                if wall[0] == rand_wall[0] and wall[1] == rand_wall[1]:
                    walls.remove(wall)

        # Mark the remaining unvisited cells as walls
        for i in range(0, self.height):
            for j in range(0, self.width):
                if self.maze[i][j] == self.unvisited:
                    self.maze[i][j] = self.wall

        # Set entrance and exit
        for i in range(0, self.width):
            if self.maze[1][i] == self.cell:
                self.maze[0][i] = self.end
                self.end_r = 0
                self.end_c = i
                break

        for i in range(self.width - 1, 0, -1):
            if self.maze[self.height - 2][i] == self.cell:
                self.maze[self.height - 1][i] = self.trodden
                self.player.r = self.height - 1
                self.player.c = i
                break


        # Print final maze
        self.printMaze()
