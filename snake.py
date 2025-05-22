
import turtle
import time
import random

# game settings
delay=0.1
score=0
high_score=0

# screen setup
wn = turtle.Screen()
wn.title("snake game by bushra")
wn.bgcolor("pink")
wn.setup(width=600,height=600)
wn.tracer(0)

#Snake head
head=turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("purple")
head.penup()
head.goto(0,0)
head.direction="stop"

# score display
pen=turtle.Turtle()
pen.speed=0
pen.color("black")
pen.shape("square")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("score=0 High Score=0",align="center",font=("courier",24,"normal"))

# snake body
def update_score():
    pen.clear()
    pen.write(f"score: {score},HighScore: {high_score}", align="center",font=("courier",24,"normal"))
update_score()


def go_up():
    if head.direction != "down":  
        head.direction = "up"

def go_down():
    if head.direction != "up":  
        head.direction = "down"

def go_left():
    if head.direction != "right":  
        head.direction = "left"

def go_right():
    if head.direction != "left":  
        head.direction = "right"

# Function to move the snake forward
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
    

# Keyboard controls
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# snake food
food=turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("yellow")
food.penup()
food.goto(0,100)
segments=[]


# main game loop



while True:
    wn.update()
    if head.xcor()>280 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
       time.sleep(1)
       head.goto(0,0)
       head.direction="stop"

       for segment in segments:
           segment.goto(1000,1000)
       segments.clear()  
       score=0
       delay=0
       update_score()
    
        

       
    if head.distance(food)<20:
        x=random.randint(-280,280)
        y=random.randint(-280,280)
        food.goto(x,y)
        
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("hotpink")
        new_segment.penup()
        segments.append(new_segment) 

        score+=10
        if score> high_score:
            high_score=score
        update_score()
       

    for i in range(len(segments)-1,0,-1):
        x=segments[i-1].xcor()
        y=segments[i-1].ycor()
        segments[i].goto(x,y)
    if len(segments)>0:
        x=head.xcor()
        y=head.ycor()
        segments[0].goto(x,y)

    move()
    for segment in segments:
        if segment.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction="stop"
            for segments in segments:
                segments.goto(1000,1000)
            score=0
            delay=0.1
            segments.clear()
            update_score()
            pen.clear()
            pen.write(f"score: {score},HighScore: {high_score}", align="center",font=("courier",24,"normal"))
    time.sleep(delay)
wn.mainloop()


# import turtle
# import time
# import random

# # Game settings
# delay = 0.1
# score = 0
# high_score = 0

# # Screen setup
# wn = turtle.Screen()
# wn.title("Snake Game by Bushra")
# wn.bgcolor("pink")
# wn.setup(width=600, height=600)
# wn.tracer(0)  # Turns off auto updates

# # Snake head
# head = turtle.Turtle()
# head.speed(0)
# head.shape("square")
# head.color("purple")
# head.penup()
# head.goto(0, 0)
# head.direction = "stop"

# # Score display
# pen = turtle.Turtle()
# pen.speed(0)
# pen.color("white")
# pen.penup()
# pen.hideturtle()
# pen.goto(0, 260)

# # Function to update the score display
# def update_score():
#     pen.clear()
#     pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

# update_score()  # Initial display

# # Movement functions
# def go_up():
#     if head.direction != "down":
#         head.direction = "up"

# def go_down():
#     if head.direction != "up":
#         head.direction = "down"

# def go_left():
#     if head.direction != "right":
#         head.direction = "left"

# def go_right():
#     if head.direction != "left":
#         head.direction = "right"

# # Function to move the snake
# def move():
#     if head.direction == "up":
#         y = head.ycor()
#         head.sety(y + 20)

#     if head.direction == "down":
#         y = head.ycor()
#         head.sety(y - 20)

#     if head.direction == "left":
#         x = head.xcor()
#         head.setx(x - 20)

#     if head.direction == "right":
#         x = head.xcor()
#         head.setx(x + 20)

# # Keyboard controls
# wn.listen()
# wn.onkeypress(go_up, "w")
# wn.onkeypress(go_down, "s")
# wn.onkeypress(go_left, "a")
# wn.onkeypress(go_right, "d")

# # Snake food
# food = turtle.Turtle()
# food.speed(0)
# food.shape("circle")
# food.color("red")
# food.penup()
# food.goto(0, 100)

# # Snake body
# segments = []

# # Main game loop
# def game_loop():
#     global score, high_score, delay

#     while True:
#         wn.update()  # Refresh the screen

#         # Check for border collision
#         if head.xcor() > 280 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
#             time.sleep(1)
#             head.goto(0, 0)
#             head.direction = "stop"

#             for segment in segments:
#                 segment.goto(1000, 1000)  # Move segments off-screen
#             segments.clear()
            
#             score = 0  # Reset the score
#             delay = 0.1
#             update_score()

#         # Check for food collision
#         if head.distance(food) < 20:
#             x = random.randint(-280, 280)
#             y = random.randint(-280, 280)
#             food.goto(x, y)

#             # Add a new segment to the snake
#             new_segment = turtle.Turtle()
#             new_segment.speed(0)
#             new_segment.shape("square")
#             new_segment.color("grey")
#             new_segment.penup()
#             segments.append(new_segment)

#             # Update score
#             score += 10
#             if score > high_score:
#                 high_score = score
#             update_score()

#         # Move the body segments
#         for i in range(len(segments) - 1, 0, -1):
#             x = segments[i - 1].xcor()
#             y = segments[i - 1].ycor()
#             segments[i].goto(x, y)

#         # Move the first segment to the head’s position
#         if len(segments) > 0:
#             x = head.xcor()
#             y = head.ycor()
#             segments[0].goto(x, y)

#         move()

#         # Check for self-collision
#         for segment in segments:
#             if segment.distance(head) < 20:
#                 time.sleep(1)
#                 head.goto(0, 0)
#                 head.direction = "stop"

#                 for segment in segments:
#                     segment.goto(1000, 1000)  # Move segments off-screen
#                 segments.clear()
                
#                 score = 0  # Reset the score
#                 delay = 0.1
#                 update_score()

#         time.sleep(delay)

# # Start the game loop
# game_loop()

# # Keep the window open
# wn.mainloop()
