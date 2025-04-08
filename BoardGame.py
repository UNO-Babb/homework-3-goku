import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Game settings
WIDTH, HEIGHT = 600, 400  # Size of the window
FPS = 30  # Frames per second for smooth animation

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Way Game")

# Font for displaying text
font = pygame.font.SysFont(None, 36)

# Questions for each character
goku_questions = [
    {"question": "What’s Goku’s signature move?", "answer": "kamehameha"},
    {"question": "What planet is Goku from?", "answer": "vegeta"}
]

vegeta_questions = [
    {"question": "Who is Vegeta’s rival?", "answer": "goku"},
    {"question": "What’s Vegeta’s royal title?", "answer": "prince"}
]

# Function to draw text on the screen
def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

# Function to draw the game path
def draw_path(position):
    for i in range(10):  # Draw the 10 blocks of the path
        color = GREEN if i != position else RED  # The player’s position is red
        pygame.draw.rect(screen, color, (50 + i * 50, HEIGHT // 2, 40, 40))

# Function for character selection
def character_select():
    selecting = True
    selected_image = None
    selected_questions = []
    while selecting:
        screen.fill(WHITE)
        draw_text("Select Your Fighter", font, BLACK, WIDTH // 2 - 130, HEIGHT // 2 - 100)
        draw_text("Press 1 for Goku", font, GREEN, WIDTH // 2 - 100, HEIGHT // 2 - 50)
        draw_text("Press 2 for Vegeta", font, GREEN, WIDTH // 2 - 100, HEIGHT // 2)

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    selected_image = pygame.image.load('goku-png-20.png')
                    selected_questions = goku_questions
                    selecting = False
                elif event.key == pygame.K_2:
                    selected_image = pygame.image.load('vegeta.png')
                    selected_questions = vegeta_questions
                    selecting = False
    return selected_image, selected_questions

# Game loop
def game_loop():
    position = 0
    score = 0
    player_name = "Player 1"
    player_image, current_questions = character_select()

    # Game loop
    running = True
    while running:
        screen.fill(WHITE)  # Fill the screen with white background

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Display player info
        draw_text(f"Position: {position}", font, BLACK, 20, 20)
        draw_text(f"Score: {score}", font, BLACK, 20, 60)

        # Draw the "Snake Way" path and the player character
        draw_text("Snake Way", font, GREEN, WIDTH // 2 - 100, HEIGHT // 2 - 100)
        draw_path(position)

        # Draw player image at the current position (replace rectangle with the player image)
        screen.blit(player_image, (50 + position * 50, HEIGHT // 2))  # Draw player image

        # Handle user input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:  # Move forward when the space bar is pressed
            question = current_questions[position % len(current_questions)]
            user_answer = input(f"{question['question']} ").lower().strip()
            if user_answer == question['answer']:
                position += 1
                score += 10
            else:
                draw_text("Wrong answer!", font, RED, WIDTH // 2 - 100, HEIGHT // 2 + 60)
                pygame.display.update()
                pygame.time.wait(1000)

            if position >= 10:  # End the game if the player reaches the end
                draw_text("You Win!", font, GREEN, WIDTH // 2 - 70, HEIGHT // 2 + 60)
                pygame.display.update()
                pygame.time.wait(2000)  # Wait for 2 seconds before quitting
                running = False

        # Update the display
        pygame.display.update()
        pygame.time.Clock().tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    game_loop()
