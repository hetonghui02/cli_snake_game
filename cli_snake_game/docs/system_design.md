## Implementation approach
We will use Pygame, an open-source library for making video games in Python. The game logic will be implemented in a Game class, which will handle the game loop, user input, and game over conditions. The Snake and Food classes will be responsible for their respective functionalities. The game will be rendered in a terminal window using characters to represent the snake, food, and borders. The game speed will be controlled to ensure smooth and responsive gameplay.

## Python package name
```python
"cli_snake_game"
```

## File list
```python
[
    "main.py",
    "game.py",
    "snake.py",
    "food.py"
]
```

## Data structures and interface definitions
```mermaid
classDiagram
    class Main{
        +main()
    }
    class Game{
        +int score
        +bool game_over
        +start_game()
        +end_game()
        +update_game()
        +draw_game()
    }
    class Snake{
        +list body
        +str direction
        +move()
        +grow()
        +check_collision()
    }
    class Food{
        +tuple position
        +generate()
    }
    Main -- Game: starts >
    Game "1" -- "1" Snake: controls >
    Game "1" -- "1" Food: controls >
```

## Program call flow
```mermaid
sequenceDiagram
    participant M as Main
    participant G as Game
    participant S as Snake
    participant F as Food
    M->>G: start_game()
    loop game loop
        G->>S: move()
        G->>S: check_collision()
        G->>F: generate()
        G->>G: update_game()
        G->>G: draw_game()
    end
    G->>M: end_game()
```

## Anything UNCLEAR
The requirement is clear to me.