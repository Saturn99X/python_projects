import pygame
import random
import time
import heapq

# Initialize pygame
pygame.init()

# Constants for the game
WIDTH, HEIGHT = 800, 800
ROWS, COLS = 20, 20
CELL_SIZE = WIDTH // COLS

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Create the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Generator and Solver")

# Clock for controlling FPS
clock = pygame.time.Clock()

# Define directions for maze generation
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# Function to create the grid
def create_grid():
    grid = []
    for row in range(ROWS):
        grid.append([1] * COLS)  # 1 means a wall, 0 means a path
    return grid

# Function to draw the grid
def draw_grid(grid):
    for row in range(ROWS):
        for col in range(COLS):
            color = WHITE if grid[row][col] == 0 else BLACK
            pygame.draw.rect(screen, color, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# Depth-First Search to generate a random maze
def generate_maze(grid):
    def dfs(x, y):
        grid[x][y] = 0
        random.shuffle(DIRECTIONS)
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx * 2, y + dy * 2
            if 0 <= nx < ROWS and 0 <= ny < COLS and grid[nx][ny] == 1:
                grid[x + dx][y + dy] = 0
                draw_grid(grid)
                pygame.display.update()
                time.sleep(0.05)
                dfs(nx, ny)

    start_x, start_y = 0, 0
    dfs(start_x, start_y)

# Heuristic function for A* (Manhattan distance)
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# A* Algorithm to solve the maze
def a_star(grid, start, goal):
    open_list = []
    heapq.heappush(open_list, (0, start))
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}

    while open_list:
        _, current = heapq.heappop(open_list)
        if current == goal:
            return reconstruct_path(came_from, current)

        for dx, dy in DIRECTIONS:
            neighbor = (current[0] + dx, current[1] + dy)
            if 0 <= neighbor[0] < ROWS and 0 <= neighbor[1] < COLS and grid[neighbor[0]][neighbor[1]] == 0:
                tentative_g_score = g_score[current] + 1
                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = g_score[neighbor] + heuristic(neighbor, goal)
                    heapq.heappush(open_list, (f_score[neighbor], neighbor))

    return None  # No path found

# Function to reconstruct the path from A* algorithm
def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path

# Function to draw the solution path
def draw_path(path):
    for position in path:
        pygame.draw.rect(screen, GREEN, (position[1] * CELL_SIZE, position[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        pygame.display.update()
        time.sleep(0.1)

# Main loop
def main():
    grid = create_grid()
    generate_maze(grid)

    # Start and goal positions
    start = (0, 0)
    goal = (ROWS - 1, COLS - 1)

    # Solve the maze using A*
    path = a_star(grid, start, goal)

    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Draw the maze and the path if found
        draw_grid(grid)
        if path:
            draw_path(path)

        pygame.display.update()
        clock.tick(60)

    pygame.quit()

# Run the game
if __name__ == "__main__":
    main()