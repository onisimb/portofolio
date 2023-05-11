# Creating a function that takes a grid of # and -, where each hash (#) represents amine and each dash (-) represents a mine-free spot. 
# Returing a grid, where each dash is replaced by a digit, indicating the number of mines immediately adjacent to the spot
# Input grid
grid = [["-", "-", "-", "#", "#"],
        ["-", "#", "-", "-", "-"],
        ["-", "-", "#", "-", "-"],
        ["-", "#", "#", "-", "-"],
        ["-", "-", "-", "-", "-"]]

# Function counting the the mines surrounding the hash (_)
#I started by creating a new grid list which would store the mines result (Dashboard lecture task 15)
def count_mines(grid):
    rows, cols = len(grid), len(grid[0])
    new_grid_list = [[0] * cols for _ in range(rows)]

# This block will iterate over each element skipping over # (Lecture on 30th of March at time 58:06 min)
    for i, x in enumerate(grid):
        for j, y in enumerate(x):
            if y == "#":
                new_grid_list[i][j] = "#"
                continue

            # Below block will count the number of mines adjecent to the cell (_)     
            adj_mines_num = 0
            for dx, dy in [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]:
                adj_row_idx, adj_col_idx = i + dx, j + dy
                if 0 <= adj_row_idx < rows and 0 <= adj_col_idx < cols and grid[adj_row_idx][adj_col_idx] == "#":
                    adj_mines_num += 1
            new_grid_list[i][j] = str(adj_mines_num)
    return new_grid_list

new_grid = count_mines(grid)
print(new_grid)

# References:
# 1 - https://stackoverflow.com/questions/74976577/2d-list-minesweeper-task-python
# 2 - https://app.livestorm.co/hyperion-development/skills-bootcamp-cohort-4-data-science-lectures/live?s=233fe250-5110-46ee-ac1c-30f5b7cc3332#/qa - lecture from 30th of March 
# 3 - https://app.livestorm.co/hyperion-development/skills-bootcamp-cohort-4-data-science-lectures/live?s=fd5b5a63-11c2-441a-a3e5-5bb2572f0b85#/qa - lecture from 26th of MArch
# 4 - Video provided with the task 15 on the HyperionDev dashboard 