import turtle as t
import random as rd
import time

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

# Snake body segments
segments = []

# Score
score = 0

# Bonus
bonus = t.Turtle()
bonus.shape('circle')
bonus.color('blue')
bonus.penup()
bonus.speed(0)
bonus.hideturtle()
bonus_time = 0

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
        time.sleep(2)
        t.clear()
        snake_head.goto(0, 0)
        snake_head.direction = 'Stop'
        segments.clear()
        score = 0

    # Check for a collision with the food
    if snake_head.distance(bonus) < 20:
        bonus.hideturtle()
        bonus_time = 0
        score += 20

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

    # Check for head collisions with the body segments
    for segment in segments:
        if snake_head.distance(segment) < 20:
            t.goto(0, 0)
            t.write('Game Over', align='center', font=('Arial', 24, 'normal'))
            t.update()
            time.sleep(2)
            t.clear()
            snake_head.goto(0, 0)
            snake_head.direction = 'Stop'
            segments.clear()
            score = 0

    # Update the score display
    t.goto(0, 260)
    t.write(f'Score: {score}', align='center', font=('Arial', 24, 'normal'))

    # Bonus appearance logic
    if bonus_time == 0 and rd.randint(1, 100) == 1:
        bonus.showturtle()
        x = rd.randint(-270, 270)
        y = rd.randint(-270, 270)
        bonus.goto(x, y)
        bonus_time = 300  # Bonus disappears after 15 seconds

    # Bonus countdown
    if bonus_time > 0:
        bonus_time -= 1

    # Move the bonus
    if bonus_time % 2 == 0:
        x = bonus.xcor()
        y = bonus.ycor()
        bonus.goto(x + 5, y + 5)

    # Call the move function
    move()
    time.sleep(0.05)
