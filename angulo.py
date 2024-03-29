import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width, screen_height = 640, 480
screen = pygame.display.set_mode((screen_width, screen_height))

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Initial vector setup
origin = (screen_width // 2, screen_height // 2)  # Origin point
fixed_vec = (100, 0)  # Fixed vector (relative to origin)
movable_vec_angle = 0  # Angle for movable vector in degrees

# Function to draw vectors
def draw_vector(color, start, end):
    pygame.draw.line(screen, color, start, (start[0] + end[0], start[1] + end[1]), 5)

# Rotate vector by angle
def rotate_vector(angle_degrees):
    angle_radians = math.radians(angle_degrees)
    x = math.cos(angle_radians) * fixed_vec[0] - math.sin(angle_radians) * fixed_vec[1]
    y = math.sin(angle_radians) * fixed_vec[0] + math.cos(angle_radians) * fixed_vec[1]
    return (x, y)

# Calculate the dot product
def dot_product(v1, v2):
    return v1[0] * v2[0] + v1[1] * v2[1]

# Calculate the magnitude of a vector
def magnitude(v):
    return math.sqrt(v[0] ** 2 + v[1] ** 2)

# Calculate the angle between two vectors in degrees
def angle_between(v1, v2):
    dot_prod = dot_product(v1, v2)
    mag_v1 = magnitude(v1)
    mag_v2 = magnitude(v2)
    cos_angle = dot_prod / (mag_v1 * mag_v2)
    cos_angle = max(min(cos_angle, 1), -1)  # Avoid precision errors
    angle = math.acos(cos_angle)
    return math.degrees(angle)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                movable_vec_angle -= 5  # Rotate left
            elif event.key == pygame.K_RIGHT:
                movable_vec_angle += 5  # Rotate right

    # Rotate movable vector
    movable_vec = rotate_vector(movable_vec_angle)

    # Print vector positions
    print(f"Fixed Vector: {fixed_vec}, Movable Vector: {movable_vec}")

    # Fill the screen with white
    screen.fill(WHITE)

    # Draw vectors
    draw_vector(RED, origin, fixed_vec)
    draw_vector(GREEN, origin, movable_vec)

    # Calculate and display the dot product and angle
    dot_prod = dot_product(fixed_vec, movable_vec)
    angle = angle_between(fixed_vec, movable_vec)
    font = pygame.font.SysFont(None, 24)
    text_surf = font.render(f"Dot Product: {dot_prod}, Angle: {angle:.2f} degrees", True, BLACK)
    screen.blit(text_surf, (20, 20))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()