import pygame
import os
import random
import sys

# Constants for game dimensions and settings
WIDTH = 800
HEIGHT = 800
FPS = 30
CELL_SIZE = 40
CELL_NUMBER = 20

# Define the Snake class, representing the player-controlled snake
class Snake:
    def __init__(self):
        # Initialize the snake's direction and body segments
        self.direction = pygame.math.Vector2(0, -1)
        self.new = False
        self.body = [
            pygame.math.Vector2(10, 10),
            pygame.math.Vector2(10, 11),
            pygame.math.Vector2(10, 12),
        ]
        
    # Move the snake based on its direction
    def move_snake(self):
        if self.new:
            body_copy = self.body[:]
        else:
            body_copy = self.body[:-1]
        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy[:]
        self.new = False

    # Draw the snake on the game screen
    def draw_snake(self):
        self.update_head_image()
        self.update_tail_image()
        for i, part in enumerate(self.body):
            part_rect = pygame.Rect(
                int(part.x * CELL_SIZE), int(part.y * CELL_SIZE), CELL_SIZE, CELL_SIZE
            )
        
            if i == 0 :
                screen.blit(self.head, part_rect)
            elif i == len(self.body) - 1:
                screen.blit(self.tail, part_rect)
            else:
                prev_part = self.body[i - 1] - part
                next_part = self.body[i + 1] - part

                if prev_part.x == next_part.x:
                    self.mid = body_vert
                elif prev_part.y == next_part.y:
                    self.mid = body_linear
                else:
                    if prev_part.x == -1 and next_part.y == -1 or prev_part.y == -1 and next_part.x == -1:
                        self.mid = corner_ul
                    if prev_part.x == -1 and next_part.y == 1 or prev_part.y == 1 and next_part.x == -1:
                        self.mid = corner_dl
                    if prev_part.x == 1 and next_part.y == -1 or prev_part.y == -1 and next_part.x == 1:
                        self.mid = corner_ur
                    if prev_part.x == 1 and next_part.y == 1 or prev_part.y == 1 and next_part.x == 1:
                        self.mid = corner_dr

                screen.blit(self.mid, part_rect)

    # Update the snake's head image based on its direction
    def update_head_image(self):
        relation = self.body[1] - self.body[0]
        if relation == pygame.math.Vector2(1, 0):
            self.head = head_right
        elif relation == pygame.math.Vector2(-1, 0):
            self.head = head_left
        elif relation == pygame.math.Vector2(0, 1):
            self.head = head_up
        elif relation == pygame.math.Vector2(0, -1):
            self.head = head_down

     # Update the snake's tail image based on the position of the last two body segments
    def update_tail_image(self):
        relation = self.body[-2] - self.body[-1]
        if relation == pygame.math.Vector2(1, 0):
            self.tail = tail_right
        elif relation == pygame.math.Vector2(-1, 0):
            self.tail = tail_left
        elif relation == pygame.math.Vector2(0, 1):
            self.tail = tail_down
        elif relation == pygame.math.Vector2(0, -1):
            self.tail = tail_up

    # Add a new body segment to the snake
    def add(self):
        self.new = True

# Define the Food class, representing the food that the snake can eat
class Food:
    def __init__(self):
        # Initialize the food's image and position
        self.image = food_image
        self.randomize()

    # Draw the food on the game screen
    def draw_food(self):
        food_rect = pygame.Rect(
            int(self.pos.x * CELL_SIZE),
            int(self.pos.y * CELL_SIZE),
            CELL_SIZE,
            CELL_SIZE,
        )
        screen.blit(self.image, food_rect)

    # Randomize the position of the food on the game grid
    def randomize(self):
        self.x = random.randint(0, CELL_NUMBER - 1)
        self.y = random.randint(0, CELL_NUMBER - 1)
        self.pos = pygame.math.Vector2(self.x, self.y)

# Define the Main class, representing the game itself
class Main:
    def __init__(self):
        # Initialize the snake, food, and gameover status
        self.snake = Snake()
        self.food = Food()
        self.gameover = False

    # Update the movement of the snake and check for collisions and game-over conditions
    def update_movement(self):
        self.snake.move_snake()
        self.colisions()
        self.fail()

    # Draw all game elements on the game screen
    def draw_elements(self):
        screen.blit(background, (0, 0))
        self.food.draw_food()
        self.snake.draw_snake()
        self.draw_score()

    # Check for collisions between the snake and the food
    def colisions(self):
        if self.snake.body[0] == self.food.pos:
            self.food.randomize()
            self.snake.add()
        for pos in self.snake.body:
            if self.food.pos == pos:
                self.food.randomize()

     # Check for game-over conditions, such as hitting the boundaries or self-collision
    def fail(self):
        if (
            self.snake.body[0].x < 0
            or self.snake.body[0].x > CELL_NUMBER - 1
            or self.snake.body[0].y < 0
            or self.snake.body[0].y > CELL_NUMBER - 1
        ):
            self.gameover = True

        for pos in self.snake.body[1:]:
            if self.snake.body[0] == pos:
                self.gameover = True

    # Draw the player's score on the game screen
    def draw_score(self):
        self.score = len(self.snake.body) - 3 
        score_surface_black = score_font.render(f"Score: {self.score}", False, (0, 0, 0))
        score_surface_white = score_font.render(f"Score: {self.score}", False, (255, 255, 255))
        screen.blit(score_surface_black, (23, 23))
        screen.blit(score_surface_white, (20, 20))

#Initializing the screen
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

#Opening all the assets
icon = pygame.image.load(os.path.join("Assets", "icon.png"))
background = pygame.image.load(os.path.join("Assets", "background.png"))
menu_background = pygame.image.load(os.path.join("Assets", "menu_backround.png"))
food_image = pygame.image.load(os.path.join("Assets", "food.png"))
play_button = pygame.image.load(os.path.join("Assets", "play_button.png"))
play_button_pressed = pygame.image.load(
    os.path.join("Assets", "play_button_pressed.png")
)
quit_button = pygame.image.load(os.path.join("Assets", "quit_button.png"))
quit_button_pressed = pygame.image.load(
    os.path.join("Assets", "quit_button_pressed.png")
)
retry_button = pygame.image.load(os.path.join("Assets", "retry_button.png"))
retry_button_pressed = pygame.image.load(
    os.path.join("Assets", "retry_button_pressed.png")
)

title = pygame.image.load(os.path.join("Assets", "title.png"))
over = pygame.image.load(os.path.join("Assets", "over.png"))

head_up = pygame.image.load(os.path.join("Assets", "head_up.png"))
head_down = pygame.image.load(os.path.join("Assets", "head_down.png"))
head_left = pygame.image.load(os.path.join("Assets", "head_left.png"))
head_right = pygame.image.load(os.path.join("Assets", "head_right.png"))

tail_up = pygame.image.load(os.path.join("Assets", "tail_up.png"))
tail_down = pygame.image.load(os.path.join("Assets", "tail_down.png"))
tail_left = pygame.image.load(os.path.join("Assets", "tail_left.png"))
tail_right = pygame.image.load(os.path.join("Assets", "tail_right.png"))

body_vert = pygame.image.load(os.path.join("Assets", "body_vert.png"))
body_linear = pygame.image.load(os.path.join("Assets", "body_linear.png"))

corner_ur = pygame.image.load(os.path.join("Assets", "corner_ur.png"))
corner_ul = pygame.image.load(os.path.join("Assets", "corner_ul.png"))
corner_dr = pygame.image.load(os.path.join("Assets", "corner_dr.png"))
corner_dl = pygame.image.load(os.path.join("Assets", "corner_dl.png"))

#Setting the Font of the score text
score_font = pygame.font.Font(os.path.join("Fonts", "PublicPixel-z84yD.ttf"), 25)

#Setting the caption and the icon of the game
pygame.display.set_caption("Snake Game")
pygame.display.set_icon(icon)


#Function for creating a button
def create_button(x, y, button, button_pressed, func):
    pos = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    screen.blit(button, (x, y))

    if pos[0] > x and pos[0] < x + 300 and pos[1] > y and pos[1] < y + 150:
        screen.blit(button_pressed, (x, y))
        if click[0] == 1:
            func()

#End Game screen
def end_game(score):
    run = True

    while run:
        screen.blit(menu_background, (0, 0))
        screen.blit(over, (WIDTH / 2 - 300, 50))

        score_surface_black = score_font.render(f"Your score was: {score}", False, (0, 0, 0))
        score_surface_white = score_font.render(f"Your score was: {score}", False, (255, 255, 255))
        screen.blit(score_surface_black, (188, 228))
        screen.blit(score_surface_white, (185, 225))

        create_button(
            WIDTH / 2 - 150,
            HEIGHT / 2 - 75,
            retry_button,
            retry_button_pressed,
            start_game,
        )
        create_button(
            WIDTH / 2 - 150, HEIGHT / 2 + 75, quit_button, quit_button_pressed, sys.exit
        )

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.display.update()

    pygame.quit()
    quit()

#Game Screen
def start_game():
    run = True
    main_game = Main()

    screen_update = pygame.USEREVENT
    pygame.time.set_timer(screen_update, 150)
    

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == screen_update:
                main_game.update_movement()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and main_game.snake.direction.y != 1:
                    main_game.snake.direction = pygame.math.Vector2(0, -1)
                if event.key == pygame.K_s and main_game.snake.direction.y != -1:
                    main_game.snake.direction = pygame.math.Vector2(0, 1)
                if event.key == pygame.K_d and main_game.snake.direction.x != -1:
                    main_game.snake.direction = pygame.math.Vector2(1, 0)
                if event.key == pygame.K_a and main_game.snake.direction.x != 1:
                    main_game.snake.direction = pygame.math.Vector2(-1, 0)
        if main_game.gameover:
            end_game(main_game.score)
        main_game.draw_elements()

        pygame.display.flip()

    pygame.quit()
    quit()

#Main menu screen
def main():
    run = True

    while run:
        screen.blit(menu_background, (0, 0))
        screen.blit(title, (WIDTH / 2 - 300, 50))
        create_button(
            WIDTH / 2 - 150,
            HEIGHT / 2 - 75,
            play_button,
            play_button_pressed,
            start_game,
        )
        create_button(
            WIDTH / 2 - 150, HEIGHT / 2 + 75, quit_button, quit_button_pressed, sys.exit
        )

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.display.update()

    pygame.quit()
    quit()

# Main game setup and initialization
if __name__ == "__main__":
    main()
