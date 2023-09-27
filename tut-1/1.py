#A rocket starts with a velocity u = 4 × 10 5 m/s and moves in a straight line with a net acceleration of a = 10 m/s 2 . Write a program to display the velocity (v) of the rocket at the following times (in minutes) t = 0, 5, 10, ..., 25. Hint: v = u + at.
u=4*10**5
a=10
for t in range(0,26,5):
    v=u+a*t
    print("Velocity at time ",t," is ",v)