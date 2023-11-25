import turtle as t
import random as rd

# Set up the screen
t.bgcolor('black')
t.title('Snake Game')
t.setup(width=600, height=600)
t.tracer(0)

# Snake head
snake_head = t.Turtle()
snake_head.shape('square')
snake_head.color('green')
snake_head.penup()
snake_head.speed(0)
snake_head.goto(0, 0)

# Snake food
food = t.Turtle()
food.shape('circle')
food.color('red')
food.penup()
food.speed(0)
food.goto(0, 100)

# Snake body segments
segments = []

# Score
score = 0

# Functions
def go_up():
    if snake_head.direction != 'down':
        snake_head.direction = 'up'

def go_down():
    if snake_head.direction != 'up':
        snake_head.direction = 'down'

def go_left():
    if snake_head.direction != 'right':
        snake_head.direction = 'left'

def go_right():
    if snake_head.direction != 'left':
        snake_head.direction = 'right'

def move():
    if snake_head.direction == 'up':
        y = snake_head.ycor()
        snake_head.sety(y + 20)

    if snake_head.direction == 'down':
        y = snake_head.ycor()
        snake_head.sety(y - 20)

    if snake_head.direction == 'left':
        x = snake_head.xcor()
        snake_head.setx(x - 20)

    if snake_head.direction == 'right':
        x = snake_head.xcor()
        snake_head.setx(x + 20)

# Keyboard bindings
t.listen()
t.onkey(go_up, 'w')
t.onkey(go_down, 's')
t.onkey(go_left, 'a')
t.onkey(go_right, 'd')

# Main game loop
while True:
    t.update()

    # Check for a collision with the border
    if (
        snake_head.xcor() > 290
        or snake_head.xcor() < -290
        or snake_head.ycor() > 290
        or snake_head.ycor() < -290
    ):
        t.goto(0, 0)
        t.write('Game Over', align='center', font=('Arial', 24, 'normal'))
        t.update()
        t.delay(2000)
        t.clear()
        snake_head.goto(0, 0)
        snake_head.direction = 'Stop'

    # Check for a collision with the food
    if snake_head.distance(food) < 20:
        # Move the food to a random location
        x = rd.randint(-270, 270)
        y = rd.randint(-270, 270)
        food.goto(x, y)

        # Add a segment to the snake
        new_segment = t.Turtle()
        new_segment.shape('square')
        new_segment.color('green')
        new_segment.penup()
        segments.append(new_segment)

        # Increase the score
        score += 10

    # Move the end segments first in reverse order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = snake_head.xcor()
        y = snake_head.ycor()
        segments[0].goto(x, y)

    # Call the move function
    move()

    # Check for head collisions with the body segments
    for segment in segments:
        if snake_head.distance(segment) < 20:
            t.goto(0, 0)
            t.write('Game Over', align='center', font=('Arial', 24, 'normal'))
            t.update()
            t.delay(2000)
            t.clear()
            snake_head.goto(0, 0)
            snake_head.direction = 'Stop'

    # Update the score display
    t.clear()
    t.goto(0, 260)
    t.write(f'Score: {score}', align='center', font=('Arial', 24, 'normal'))
