import pytest
import pygame
from unittest.mock import patch, MagicMock

from project import main, Snake, Food, Main, WIDTH, HEIGHT, CELL_SIZE, CELL_NUMBER



# Mock the necessary Pygame functions for testing
def mock_pygame_init():
    pass


def mock_pygame_quit():
    pass


def mock_pygame_display_set_mode(*args):
    pass


def mock_pygame_time_set_timer(*args):
    pass


def mock_pygame_event_get():
    return []


def mock_pygame_display_flip():
    pass


# Test the Snake class
def test_snake_init():
    snake = Snake()
    assert snake.direction == pygame.math.Vector2(0, -1)
    assert snake.new is False
    assert snake.body == [
        pygame.math.Vector2(10, 10),
        pygame.math.Vector2(10, 11),
        pygame.math.Vector2(10, 12),
    ]


# Test the Main class
def test_main_init():
    main = Main()
    assert isinstance(main.snake, Snake)
    assert isinstance(main.food, Food)
    assert main.gameover is False




# Test the Main.fail method
def test_end_game():
    main = Main()
    main.snake.body = [
        pygame.math.Vector2(-1, 0),
        pygame.math.Vector2(0, 0),
        pygame.math.Vector2(1, 0),
    ]  # Snake body forms a straight line to the left

    # Snake hits the left boundary
    main.snake.direction = pygame.math.Vector2(-1, 0)
    main.update_movement()
    assert main.gameover is True

    # Snake hits itself
    main.snake.direction = pygame.math.Vector2(0, 0)
    main.update_movement()
    assert main.gameover is True

    # Reset the snake position
    main.snake.body = [
        pygame.math.Vector2(0, 0),
        pygame.math.Vector2(1, 0),
        pygame.math.Vector2(2, 0),
    ]

    # Snake hits the right boundary
    main.snake.direction = pygame.math.Vector2(1, 0)
    main.update_movement()
    assert main.gameover is True

    # Snake hits the top boundary
    main.snake.direction = pygame.math.Vector2(0, -1)
    main.update_movement()
    assert main.gameover is True

    # Snake hits the bottom boundary
    main.snake.direction = pygame.math.Vector2(0, 1)
    main.update_movement()
    assert main.gameover is True


# Test the Food.randomize method
def test_start_game(mocker):
    food = Food()

    # Mock random.randint to always return 0
    mocker.patch("random.randint", return_value=0)

    food.randomize()
    assert food.pos == pygame.math.Vector2(0, 0)


# Ensure that the pygame.init and pygame.quit functions are mocked
@pytest.fixture(autouse=True)
def mock_pygame_init_quit(mocker):
    mocker.patch("pygame.init", side_effect=mock_pygame_init)
    mocker.patch("pygame.quit", side_effect=mock_pygame_quit)


# Ensure that the necessary Pygame functions are mocked
@pytest.fixture(autouse=True)
def mock_pygame_functions(mocker):
    mocker.patch("pygame.time.set_timer", side_effect=mock_pygame_time_set_timer)
    mocker.patch("pygame.event.get", side_effect=mock_pygame_event_get)


# Run all tests
if __name__ == "__main__":
    pytest.main()
