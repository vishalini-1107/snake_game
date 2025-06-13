import turtle
import random
import time


screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Simple Snake Game")
screen.tracer(0) 


head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head_direction = "stop"  


food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)


score = 0
high_score = 0

score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))


segments = []


def go_up():
    global head_direction
    if head_direction != "down":
        head_direction = "up"

def go_down():
    global head_direction
    if head_direction != "up":
        head_direction = "down"

def go_left():
    global head_direction
    if head_direction != "right":
        head_direction = "left"

def go_right():
    global head_direction
    if head_direction != "left":
        head_direction = "right"

def move():
    if head_direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    elif head_direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    elif head_direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    elif head_direction == "right":
        x = head.xcor()
        head.setx(x + 20)


screen.listen()
screen.onkeyrelease(go_up, "Up")
screen.onkeyrelease(go_down, "Down")
screen.onkeyrelease(go_left, "Left")
screen.onkeyrelease(go_right, "Right")


while True:
    screen.update()

   
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head_direction = "stop"

        
        for segment in segments:
            segment.clear() 
            segment.hideturtle() 
        segments.clear() 

        score = 0
        score_display.clear()
        score_display.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

    
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x, y)


   
    if head.distance(food) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x, y)

       
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

       
        score += 10
        if score > high_score:
            high_score = score
        score_display.clear()
        score_display.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

    
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

   
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head_direction = "stop"

            
            for seg in segments:
                seg.clear()
                seg.hideturtle()
            segments.clear()

            score = 0
            score_display.clear()
            score_display.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

            
            x = random.randint(-280, 280)
            y = random.randint(-280, 280)
            food.goto(x, y)

    time.sleep(0.1)

