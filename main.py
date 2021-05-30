import turtle
import random

turtles = []
colors = ["gold", "orange", "violet", "blue", "darkgreen"]

print("Once the turtles are lined up, press the 'Up' arrow to start the race.")
understand = input("Press any key if you understand: ")

print("\nYou can choose from 2-4 turtles.")
while True:
    turtle_amount = int(input("How many turtles would you like?: "))
    if 2 <= turtle_amount <= 4:
        break
    print("You must choose between 2-4 turtles.")

finish_line = turtle.Turtle()
finish_line.width(5)
finish_line.penup()
finish_line.setposition(-350, 275)
finish_line.pendown()
finish_line.forward(650)

for x in range(0, turtle_amount):
    new_turtle = turtle.Turtle()
    new_turtle.color(random.choice(colors))
    new_turtle.shape("turtle")
    new_turtle.left(90)
    turtles.append(new_turtle)

position_x = -250
position_y = -250

for existing_turtle in turtles:
    existing_turtle.penup()
    existing_turtle.setposition(position_x, position_y)
    position_x += 150
    existing_turtle.pendown()


def move(current_turtle):
    current_turtle.forward(random.randint(25, 100))


def start_race():
    race_over = False
    while True:
        if race_over:
            break

        for turtle in turtles:
            if turtle.ycor() < 275:
                move(turtle)
            if turtle.ycor() >= 275:
                winner = turtles.index(turtle)
                print("The winner is turtle ", winner + 1, "!")
                race_over = True
                break


turtle.listen()
turtle.onkey(start_race, "Up")

turtle.mainloop()
