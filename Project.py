import pygame
import random
import heapq
import sys

# Initialize Pygame
pygame.init()

# Constants
CELL_SIZE = 20
GRID_WIDTH = 30
GRID_HEIGHT = 30
SCREEN_WIDTH = CELL_SIZE * GRID_WIDTH
SCREEN_HEIGHT = CELL_SIZE * GRID_HEIGHT
FPS = 10  # Will increase after eating

# Colors "in RGB"
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
LIGHT_GREEN = (144, 238, 144)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
GRAY = (100, 100, 100)

# Directions
DIRS = {
    "UP": (0, -1),
    "DOWN": (0, 1),
    "LEFT": (-1, 0),
    "RIGHT": (1, 0),
}

# Sound effects
EAT_SOUND = pygame.mixer.Sound("eat.wav")
GAMEOVER_SOUND = pygame.mixer.Sound("gameover.wav")

class SnakeGame:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Snake Game with AI (Pygame)")
        self.clock = pygame.time.Clock()
        
        self.snake = [(5, 5)]
        self.food = self.place_food()
        self.direction = "RIGHT"
        self.running = True
        self.score = 0
        self.fps = FPS
        
        self.walls = self.generate_walls()

    def generate_walls(self):
        walls = set()
        for _ in range(30):  # Number of wall blocks
            wall = (random.randint(0, GRID_WIDTH-1), random.randint(0, GRID_HEIGHT-1))
            if wall not in self.snake:
                walls.add(wall)
        return walls

    def place_food(self):
        while True:
            food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
            if food not in self.snake:
                return food

    def move(self):
        if self.direction in DIRS:
            dx, dy = DIRS[self.direction]
            new_head = (self.snake[0][0] + dx, self.snake[0][1] + dy)
            
            # Collision checks
            if (not 0 <= new_head[0] < GRID_WIDTH or
                not 0 <= new_head[1] < GRID_HEIGHT or
                new_head in self.snake or
                new_head in self.walls):
                self.running = False
                return
            
            self.snake = [new_head] + self.snake
            if new_head == self.food:
                EAT_SOUND.play()
                self.food = self.place_food()
                self.score += 1
                self.fps += 0.5  # Speed up!
            else:
                self.snake.pop()

    def draw_cell(self, position, color):
        x, y = position
        rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(self.screen, color, rect)

    def draw(self):
        # Filling screen with Black
        self.screen.fill(BLACK)

        # Draw walls
        for wall in self.walls:
            self.draw_cell(wall, GRAY)

        # Draw food
        self.draw_cell(self.food, RED)

        # Draw snake
        for idx, cell in enumerate(self.snake):
            color = GREEN if idx == 0 else LIGHT_GREEN
            self.draw_cell(cell, color)

        # Draw score
        font = pygame.font.SysFont(None, 24)
        score_text = font.render(f"Score: {self.score}", True, WHITE)
        self.screen.blit(score_text, (5, 5))
        
        pygame.display.flip()

    def game_over(self):
        GAMEOVER_SOUND.play()
        pygame.time.wait(500)  # Short pause for sound
        font = pygame.font.SysFont(None, 48)
        text = font.render(f"Game Over! Score: {self.score}", True, WHITE)
        rect = text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
        self.screen.blit(text, rect)
        pygame.display.flip()
        pygame.time.wait(3000)
        pygame.quit()
        sys.exit()

    def heuristic(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def find_path(self):
        start = self.snake[0]
        goal = self.food
        open_set = []
        heapq.heappush(open_set, (0 + self.heuristic(start, goal), 0, start, [start]))
        closed_set = set()

        while open_set:
            est_total_cost, cost_so_far, current, path = heapq.heappop(open_set)
            
            if current == goal:
                return path
            
            if current in closed_set:
                continue
            closed_set.add(current)

            for dx, dy in DIRS.values():
                neighbor = (current[0] + dx, current[1] + dy)
                if (0 <= neighbor[0] < GRID_WIDTH and
                    0 <= neighbor[1] < GRID_HEIGHT and
                    neighbor not in self.snake and
                    neighbor not in self.walls and
                    neighbor not in closed_set):
                    
                    heapq.heappush(open_set, (
                        cost_so_far + 1 + self.heuristic(neighbor, goal),
                        cost_so_far + 1,
                        neighbor,
                        path + [neighbor]
                    ))
        return None

    def update(self):
        path = self.find_path()
        if path and len(path) > 1:
            next_cell = path[1]
            dx = next_cell[0] - self.snake[0][0]
            dy = next_cell[1] - self.snake[0][1]
            for dir_name, (dir_dx, dir_dy) in DIRS.items():
                if (dx, dy) == (dir_dx, dir_dy):
                    self.direction = dir_name
                    break

        self.move()

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            self.update()
            self.draw()
            self.clock.tick(self.fps)

        self.game_over()

# Main
if __name__ == "__main__":
    game = SnakeGame()
    game.run()