import turtle
import math

t = turtle.Turtle()
print("""The following values need to be entered:
                           1) C1 = x, y coordinates of the first circle(centre)  
                           2) C2 = x, y coordinates of the second circle(centre)
                           3) R1 = length of the radius of the first cicle
                           4) R2 = length of the radius of the second circle  """)

#Values input
x_1 = int(input("Enter the x coordinate of circle A:  "))
y_1 = int(input("Enter the y coordinate of circle A:  "))
r_1 = int(input("Enter the length of the radius of circle A:  "))

x_2 = int(input("Enter the x coordinate of circle B:  "))
y_2 = int(input("Enter the y coordinate of circle B:  "))
r_2 = int(input("Enter the length of the radius of circle B:  "))

#dist between the centres = sqrt((x1 - x2)^2 + (y1 - y2)^2)

C1C2 = math.sqrt((x_1 - x_2)^2 + (y_1 - y_2)^2)

if C1C2 == r_1 + r_2:
    print("Circle A and circle B are tangents to each other.")
elif C1C2 == 0:
    print("Circles A, B are co-centric.")
elif C1C2 < r_1 + r_2:
    print("Circles A, B intersect each other")
elif C1C2 > r_1 + r_2:
    print("The circles don't intersect.")

t.circle(r_1)
t.left(90)
t.penup()
t.forward(r_1)
t.right(90)
t.forward(C1C2)
t.pendown()
if C1C2 == 0:
    exit()
else:
    pass
t.circle(r_2)
turtle.exitonclick()
