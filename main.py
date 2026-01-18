# Day 20 – Snake Game (Part 1)
# This is the first stage of building the classic Snake game.
# At this stage, the focus is on screen setup, snake movement,
# and keyboard controls — without food or collision logic yet.

import turtle
import time
from snake import Snake

# Game speed expressed as a user-friendly integer (1 = slow, 10 = fast)
# This makes speed tuning easier without dealing directly with time values
GAME_SPEED = 5

# Convert the game speed into a delay time (in seconds)
# Higher speed results in shorter wait time between frames
wait_time = (11 - GAME_SPEED) / 30

# Screen setup for the game window
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.title("Unfinished Snake Game (Part 1)")
screen.bgcolor("black")

# Disable automatic screen refresh
# This allows manual control over when the screen updates
screen.tracer(0)

# Create the snake object
# The Snake class handles all logic related to the snake’s body and movement
snake = Snake()

# Keyboard control setup
# These bindings connect arrow keys to snake movement methods
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Temporary game loop limit
# Since there is no collision or game-over logic yet,
# the game ends after a fixed number of movement cycles
cycle = 0
while cycle < 50:
    # Manually refresh the screen after all movements are calculated
    screen.update()

    # Pause execution to control the game speed
    time.sleep(wait_time)

    # Move the snake forward by one step
    snake.move()

    cycle += 1

# Keep the window open until the user clicks
screen.exitonclick()
