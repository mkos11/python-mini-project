import turtle as t
import random as rd

# Set up the screen
t.bgcolor('lightgreen')
t.title('Snake Game')
t.setup(width=600, height=600)
t.tracer(0)

# Snake head
caterpillar = t.Turtle()
caterpillar.shape('square')
caterpillar.speed(0)
caterpillar.penup()
caterpillar.hideturtle()

# Leaf shape
leaf_shape = ((0, 0), (14, 2), (18, 6), (20, 20), (6, 18), (2, 14))
t.register_shape('leaf', leaf_shape)

# Leaf
leaf = t.Turtle()
leaf.shape('leaf')
leaf.color('darkgreen')
leaf.penup()
leaf.hideturtle()
leaf.speed()

# Text display
text_turtle = t.Turtle()
text_turtle.write('Press SPACE to start', align='center', font=('Arial', 18, 'bold'))
text_turtle.hideturtle()

# Score display
score_turtle = t.Turtle()
score_turtle.hideturtle()
score_turtle.speed(0)

# Functions
def outside_window():
    left_wall, right_wall = -t.window_width() / 2, t.window_width() / 2
    top_wall, bottom_wall = t.window_height() / 2, -t.window_height() / 2
    x, y = caterpillar.pos()
    return x < left_wall or x > right_wall or y > top_wall or y < bottom_wall

def game_over():
    caterpillar.color('red')
    leaf.color('red')
    t.penup()
    t.hideturtle()
    t.write('GAME OVER !', align='center', font=('Arial', 30, 'normal'))

def display_score(current_score):
    score_turtle.clear()
    score_turtle.penup()
    x, y = t.window_width() / 2 - 20, t.window_height() / 2 - 40
    score_turtle.setpos(x, y)
    score_turtle.write(f'Score: {current_score}', align='right', font=('Arial', 16, 'normal'))

def place_leaf():
    leaf.hideturtle()
    leaf.setx(rd.randint(-200, 200))
    leaf.sety(rd.randint(-200, 200))
    leaf.showturtle()

def start_game():
    global game_started
    if game_started:
        return
    game_started = True

    score = 0
    text_turtle.clear()

    caterpillar_speed, caterpillar_length = 2, 3
    caterpillar.shapesize(1, caterpillar_length, 1)
    caterpillar.showturtle()
    display_score(score)
    place_leaf()

    while True:
        caterpillar.forward(caterpillar_speed)
        if caterpillar.distance(leaf) < 20:
            place_leaf()
            caterpillar_length += 1
            caterpillar.shapesize(1, caterpillar_length, 1)
            caterpillar_speed += 1
            score += 10
            display_score(score)
        if outside_window():
            game_over()
            break

def move_up():
    caterpillar.setheading(90)

def move_down():
    caterpillar.setheading(270)

def move_left():
    caterpillar.setheading(180)

def move_right():
    caterpillar.setheading(0)

def restart_game():
    start_game()

# Keyboard bindings
t.onkey(start_game, 'space')
t.onkey(restart_game, 'Up')
t.onkey(move_up, 'Up')
t.onkey(move_right, 'Right')
t.onkey(move_down, 'Down')
t.onkey(move_left, 'Left')

# Main game loop
t.listen()
t.mainloop()
