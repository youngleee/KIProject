import numpy as np
from Labyrinth import Labyrinth
import os


class ValueIteration:
    def __init__(self, labyrinth, discount_factor=0.9, epsilon=0.01):
        self.labyrinth = labyrinth
        self.discount_factor = discount_factor
        self.epsilon = epsilon
        self.values = np.zeros((labyrinth.rows, labyrinth.cols))
        self.iterate()

    def bellman_equation(self, row, col):
        if self.labyrinth.grid[row][col] == -1:  # Hindernis
            return 0

        possible_actions = self.labyrinth.get_possible_actions(row, col)
        if not possible_actions:  # Wenn keine Aktionen möglich sind, bleibe an Ort und Stelle
            return self.values[row][col]

        # Berechne den Wert für jede mögliche Aktion
        action_values = []
        for action in possible_actions:
            next_row, next_col = self.labyrinth.get_next_position(row, col, action)
            reward = self.labyrinth.grid[next_row][next_col]
            next_value = self.values[next_row][next_col]
            action_values.append(reward + self.discount_factor * next_value)

        # Verwende die Bellman-Gleichung
        return max(action_values)

    def iterate(self):
        iteration = 0
        while True:
            delta = 0
            # Erstelle eine temporäre Matrix für die neuen Werte
            new_values = np.zeros((self.labyrinth.rows, self.labyrinth.cols))

            for i in range(self.labyrinth.rows):
                for j in range(self.labyrinth.cols):
                    new_values[i][j] = self.bellman_equation(i, j)
                    delta = max(delta, abs(new_values[i][j] - self.values[i][j]))

            # Aktualisiere die Werte nach jeder Iteration
            self.values = np.copy(new_values)

            # Anzeige und Speichern der Werte nach jeder Iteration
            self.labyrinth.display(values=self.values, iteration=iteration)
            iteration += 1

            if delta < self.epsilon:
                break

        # Abschließende Anzeige und Speichern der Werte
        self.labyrinth.display(values=self.values, iteration=iteration)

# Beispiel für die Value Iteration
labyrinth = Labyrinth(rows=5, cols=5, start=(0, 0), goal=(4, 4), obstacles=[(2, 1), (2, 2), (2, 3)])
vi = ValueIteration(labyrinth)

