import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width, screen_height = 640, 480
screen = pygame.display.set_mode((screen_width, screen_height))

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Shape properties
circle_pos = [screen_width // 2, screen_height // 2]  # Starting position at the center of the axes
circle_radius = 20
movement_vector = [5, 2]  # Movement direction and speed
is_moving = False  # Control the movement of the circle

# Function to draw axes
def draw_axes():
    # Draw X axis
    pygame.draw.line(screen, BLACK, (0, screen_height // 2), (screen_width, screen_height // 2))
    # Draw Y axis
    pygame.draw.line(screen, BLACK, (screen_width // 2, 0), (screen_width // 2, screen_height))
    # Markers for axes
    for x in range(0, screen_width, 20):
        pygame.draw.line(screen, BLACK, (x, screen_height // 2 - 5), (x, screen_height // 2 + 5))
    for y in range(0, screen_height, 20):
        pygame.draw.line(screen, BLACK, (screen_width // 2 - 5, y), (screen_width // 2 + 5, y))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and not is_moving:
                is_moving = True
            elif event.key == pygame.K_RETURN and is_moving:
                is_moving = False

    if is_moving:
        # Update the circle's position
        circle_pos[0] += movement_vector[0]
        circle_pos[1] += movement_vector[1]

        # Boundary collision detection and response
        if circle_pos[0] + circle_radius >= screen_width or circle_pos[0] - circle_radius <= 0:
            movement_vector[0] = -movement_vector[0]
        if circle_pos[1] + circle_radius >= screen_height or circle_pos[1] - circle_radius <= 0:
            movement_vector[1] = -movement_vector[1]

    print(f"Posicao: x={circle_pos[0]}, y={circle_pos[1]}")

    # Fill the screen with white
    screen.fill(WHITE)

    # Draw the axes
    draw_axes()

    # Draw the circle
    pygame.draw.circle(screen, BLUE, circle_pos, circle_radius)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
