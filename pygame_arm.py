import pygame
import math
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 1000
screen_height = 1000
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Arm Simulation')

# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Define segment properties
segment_amount = 4
segment_length = 100

tolerance = 1

# Define goal properties
goal_pos = pygame.Vector2(screen_width // 2, screen_height // 2)
pole_pos = pygame.Vector2(100, 100)

hue_offset = 0

# Define segment class
class Segment:
    def __init__(self, position):
        self.position = pygame.Vector2(position)

    def update_position(self, new_position):
        self.position = new_position

# Create segments
segments = [Segment((screen_width // 2, screen_height // 2))]  # Starting position
for _ in range(segment_amount):
    segments.append(Segment((0, 0)))

# Function to move segments backwards
def backwards(goal_pos, segments):
    segments[-1].update_position(goal_pos)
    for i in range(len(segments) - 2, -1, -1):
        direction = segments[i].position - segments[i + 1].position
        direction.scale_to_length(segment_length)
        segments[i].update_position(segments[i + 1].position + direction)

# Function to move segments forwards
def forwards(segments):
    segments[0].update_position(pygame.Vector2(screen_width // 2, screen_height // 2))
    for i in range(len(segments) - 1):
        direction = segments[i + 1].position - segments[i].position
        if segment_length != 0:
            direction.scale_to_length(segment_length)
        else:
            direction = pygame.Vector2(0, 0)
        segments[i + 1].update_position(segments[i].position + direction)

def pole_solve(segments):
    for i in range(len(segments)-1):
        r = (pole_pos - segments[i].position).length()
        l = segment_length/r
        segments[i+1].position = (1 - l) * segments[i].position + pygame.Vector2(l * pole_pos[0], l * pole_pos[1])

def solve(segments):
    d = (segments[1].position - goal_pos).length()
    if d > segment_length * segment_amount:
        for i in range(len(segments)-1):
            r = (goal_pos - segments[i].position).length()
            l = segment_length/r
            segments[i+1].position = segments[i+1].position.lerp((1 - l) * segments[i].position + l * goal_pos, 0.99)
    else:
        differ = (segments[-1].position - goal_pos).length()
        pole_solve(segments)
        for i in range(100):
            backwards(goal_pos, segments)
            forwards(segments)
            differ = (segments[-1].position - goal_pos).length()
    

def rainbow_rgb(i, segment_amount, hue_offset):
    # Calculate the hue value with offset
    hue = (i / segment_amount * 360 + hue_offset) % 360  # Map i to degrees (0-360) and add offset
    
    # Convert hue to RGB
    r = int(max(0, min(255, (1 + math.cos(math.radians(hue))) / 2 * 255)))
    g = int(max(0, min(255, (1 + math.cos(math.radians(hue - 120))) / 2 * 255)))
    b = int(max(0, min(255, (1 + math.cos(math.radians(hue - 240))) / 2 * 255)))
    
    return r, g, b

# Main game loop
running = True
last_time = pygame.time.get_ticks()
while running:
    current_time = pygame.time.get_ticks()
    delta_time = (current_time - last_time)
    last_time = current_time

    hue_offset += 1 * delta_time / 10.0  # Update hue offset

    screen.fill(WHITE)

    # Handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == MOUSEBUTTONDOWN:
            pole_pos = pygame.mouse.get_pos()

    # Update goal position based on mouse input
    goal_pos = pygame.Vector2(pygame.mouse.get_pos())

    
    # Update segment positions
    solve(segments)

    # Draw segments
    for i in range(len(segments) - 1):
        pygame.draw.line(screen, rainbow_rgb(i, segment_amount, hue_offset), segments[i].position, segments[i + 1].position, round((segment_amount-i)/(segment_amount/20))+20)
        pygame.draw.circle(screen, rainbow_rgb(i, segment_amount, hue_offset), segments[i].position, round((segment_amount-i)/(segment_amount/20))+10)
        pygame.draw.circle(screen, rainbow_rgb(i, segment_amount, hue_offset), segments[i+1].position, round((segment_amount-i)/(segment_amount/20))+10)

    # Draw goal
    pygame.draw.circle(screen, RED, pole_pos, 10)

    pygame.display.flip()

pygame.quit()
