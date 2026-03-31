import pygame
import sys

# User input
WIDTH = int(input("Enter screen width: "))
HEIGHT = int(input("Enter screen height: "))
speed = int(input("Enter circle speed: "))
grid_size = int(input("Enter grid size (distance between lines): "))

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Animated Circle with Grid")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (100, 150, 255)
GRAY = (200, 200, 200)

x, y = WIDTH // 2, HEIGHT // 2
radius = 20

clock = pygame.time.Clock()

# Function to draw grid
def draw_grid():
    for i in range(0, WIDTH, grid_size):
        pygame.draw.line(screen, GRAY, (i, 0), (i, HEIGHT), 1)
    for j in range(0, HEIGHT, grid_size):
        pygame.draw.line(screen, GRAY, (0, j), (WIDTH, j), 1)

    # Axes
    pygame.draw.line(screen, BLACK, (0, HEIGHT//2), (WIDTH, HEIGHT//2), 2)
    pygame.draw.line(screen, BLACK, (WIDTH//2, 0), (WIDTH//2, HEIGHT), 2)

    # Labels
    font = pygame.font.SysFont(None, 24)
    x_label = font.render("X-axis", True, BLACK)
    y_label = font.render("Y-axis", True, BLACK)

    screen.blit(x_label, (WIDTH - 80, HEIGHT//2 + 10))
    screen.blit(y_label, (WIDTH//2 + 10, 10))

# Main loop
while True:
    screen.fill(WHITE)
    draw_grid()

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Key press handling
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed

    # Keep circle inside screen
    x = max(radius, min(WIDTH - radius, x))
    y = max(radius, min(HEIGHT - radius, y))

    pygame.draw.circle(screen, BLUE, (x, y), radius)

    pygame.display.flip()
    clock.tick(60)