import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 600
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (135, 206, 250)
BLACK = (0, 0, 0)
BIRD_SIZE = 30
PIPE_WIDTH = 70
PIPE_HEIGHT = 500
PIPE_GAP = 150
GRAVITY = 0.5
JUMP_STRENGTH = -10
FPS = 30

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Load images
bird_image = pygame.Surface((BIRD_SIZE, BIRD_SIZE))
bird_image.fill(WHITE)
pipe_image = pygame.Surface((PIPE_WIDTH, PIPE_HEIGHT))
pipe_image.fill(GREEN)

# Bird class
class Bird:
    def __init__(self):
        self.x = WIDTH // 4
        self.y = HEIGHT // 2
        self.y_speed = 0

    def jump(self):
        self.y_speed = JUMP_STRENGTH

    def move(self):
        self.y_speed += GRAVITY
        self.y += self.y_speed

    def draw(self):
        screen.blit(bird_image, (self.x, self.y))

# Pipe class
class Pipe:
    def __init__(self):
        self.x = WIDTH
        self.height = random.randint(100, HEIGHT - PIPE_GAP - 100)
        self.passed = False

    def move(self):
        self.x -= 5

    def draw(self):
        screen.blit(pipe_image, (self.x, 0, PIPE_WIDTH, self.height))
        screen.blit(pipe_image, (self.x, self.height + PIPE_GAP, PIPE_WIDTH, HEIGHT - self.height - PIPE_GAP))

    def collide(self, bird):
        if (self.x < bird.x + BIRD_SIZE and
            self.x + PIPE_WIDTH > bird.x and
            (bird.y < self.height or bird.y + BIRD_SIZE > self.height + PIPE_GAP)):
            return True
        return False

# Game function
def game():
    bird = Bird()
    pipes = [Pipe()]
    score = 0
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 55)
    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.jump()

        # Move bird and pipes
        bird.move()
        for pipe in pipes:
            pipe.move()

        # Add new pipes
        if pipes[-1].x < WIDTH - 200:
            pipes.append(Pipe())

        # Remove off-screen pipes
        if pipes[0].x < -PIPE_WIDTH:
            pipes.pop(0)
            score += 1

        # Check collisions
        if (bird.y + BIRD_SIZE > HEIGHT or bird.y < 0 or
            any(pipe.collide(bird) for pipe in pipes)):
            game_over = True

        # Draw everything
        screen.fill(BLUE)
        for pipe in pipes:
            pipe.draw()
        bird.draw()

        # Display score
        score_text = font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(FPS)

    # Game over screen
    screen.fill(BLACK)
    game_over_text = font.render(f"Game Over! Your Score: {score}", True, WHITE)
    screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - game_over_text.get_height() // 2))
    pygame.display.flip()
    pygame.time.wait(3000)
    pygame.quit()

# Run the game
if __name__ == "__main__":
    game()
