import numpy as np
import os
class Labyrinth:
    def __init__(self, rows, cols, start, goal, obstacles=[]):
        self.rows = rows
        self.cols = cols
        self.start = start
        self.goal = goal
        self.obstacles = obstacles
        self.grid = np.zeros((rows, cols))
        self.grid[start[0]][start[1]] = 1  # Start-Zelle
        self.grid[goal[0]][goal[1]] = 0.5  # Ziel-Zelle
        for obstacle in obstacles:
            self.grid[obstacle[0]][obstacle[1]] = -1  # Hindernis-Zellen

    def write_to_file(self, values, iteration):
        filename = 'iterations.txt'
        if iteration == 0:
            # Lösche die Datei, wenn es sich um die erste Iteration handelt.
            if os.path.exists(filename):
                os.remove(filename)

        with open(filename, 'a') as file:
            file.write(f"Iteration {iteration}:\n")
            for i in range(self.rows):
                for j in range(self.cols):
                    file.write(f"{values[i][j]:.2f}\t")
                file.write("\n")
            file.write("\n")

    def display(self, values=None, iteration=None):
        if iteration is not None:
            self.write_to_file(values, iteration)

        for i in range(self.rows):
            for j in range(self.cols):
                if values is not None:
                    print(f"{values[i][j]:.2f}\t", end="")
                else:
                    print(f"{int(self.grid[i][j])}\t", end="")
            print("\n")

    def get_possible_actions(self, row, col):
        actions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Unten, Oben, Rechts, Links
        possible_actions = []

        for action in actions:
            next_row, next_col = row + action[0], col + action[1]
            if 0 <= next_row < self.rows and 0 <= next_col < self.cols and self.grid[next_row][next_col] != -1:
                possible_actions.append(action)

        return possible_actions

    def get_next_position(self, row, col, action):
        return row + action[0], col + action[1]

# Rest des Codes bleibt unverändert
