from matplotlib import pyplot as plt
from matplotlib import colors
import numpy as np


class Map:
    def __init__(self):
        self.grid = np.array(([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
                              [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1],
                              [0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
                              [0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
                              [1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                              [1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0],
                              [1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1],
                              [0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0]))

        self.grid[21][10] = 2  # Starting location of player
        self.display(self.grid)

    def update(self, direction):
        loc = self.getLoc()
        oldLoc = loc

        sendUpdate = 1
        if direction == 'w':
            # newRow = int(loc[0]) - 1  # Could be used to make location an integer
            newRow = loc[0] - 1
            newCol = loc[1]
            if self.grid[newRow, newCol] == 0:
                # Wall
                newRow = loc[0]
                sendUpdate = 0

        elif direction == 'a':
            newRow = loc[0]
            newCol = loc[1] - 1
            if self.grid[newRow, newCol] == 0:
                # Wall
                newCol = loc[1]
                sendUpdate = 0

        elif direction == 's':
            newRow = loc[0] + 1
            newCol = loc[1]
            if self.grid[newRow, newCol] == 0:
                # Wall
                newRow = loc[0]
                sendUpdate = 0

        elif direction == 'd':
            newRow = loc[0]
            newCol = loc[1] + 1
            if self.grid[newRow, newCol] == 0:
                # Wall
                newCol = loc[1]
                sendUpdate = 0

        else:
            print('Invalid entree')
            newRow = loc[0]
            newCol = loc[1]
            sendUpdate = 0

        self.grid[newRow, newCol] = 2  # Update location
        if sendUpdate:
            print('Replaced old location with blank')
            self.grid[oldLoc[0], oldLoc[1]] = 1  # Replace old location

        self.display(self.grid)
        return

    def getLoc(self):
        self.searchMatrix(self.grid)
        return np.where(self.grid == 2)

    def searchMatrix(self, mat):
        rows = len(mat[:, 1])
        for row in range(rows):
            idx = np.where(mat[row] == 2)
            if not idx == []:
                return row, idx[0]

    # TODO: Figure out how to stop making a new figure (update existing one) for every new update
    def display(self, grid):
        self.cmap = colors.ListedColormap(['Black', 'White', 'Blue'])
        self.fig = plt.figure(figsize=(6, 6))
        plt.pcolor(self.grid[::-1], cmap=self.cmap, edgecolors='k', linewidths=3)
        plt.show()
        return

    def viewChests(self):
        pass