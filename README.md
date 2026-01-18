# Project-20---Snake-Game-Part-1

Snake Game – Part 1 (Movement & Controls)

This project is part of my 100 Days of Code (Python) journey and represents the first step in building the classic Snake game using Turtle graphics.

At this stage, the focus is on snake creation, movement logic, and keyboard interaction.

**Project Overview**

This version of the Snake game includes:

A game window with controlled refresh rate

A snake composed of multiple segments

Smooth forward movement

Keyboard-based direction control

Manual game loop timing

There is no food, scoring, or collision logic yet — those are added in later stages.

**Why this project exists**

This project was designed to practice:

Object-oriented programming with classes

Separating game logic across multiple files

Controlling animation speed manually

Understanding how movement chains work

Managing keyboard input in a game loop

It lays the foundation for a full-featured Snake game.

**What I learned**

How to manage multiple Turtle objects as a single entity

How to move objects relative to each other

Why screen.tracer() improves animation performance

How to prevent invalid movement (e.g. reversing direction)

How to structure game logic incrementally

**How the code works (high level)**

The screen is created and configured.

A Snake object initializes its body segments.

Keyboard keys are mapped to direction controls.

The game loop:

Updates the screen

Waits based on game speed

Moves the snake forward

The game ends after a fixed number of cycles.

**Project File Structure**

├── main.py        # Game loop, screen setup, and controls

├── snake.py      # Snake class and movement logic

**Current Limitations (by design)**

No food or growth logic

No wall or self-collision detection

No scoring system

No game-over screen

These limitations are intentional and addressed in later parts.

**This project demonstrates:**

Clean separation of responsibilities

Intentional use of constants for readability

Incremental game development

Solid object-oriented foundations
