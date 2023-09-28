import numpy as np
import math

def sinc(x):
    if x == 0:
        return 1
    else:
        return np.sin(np.pi * x) / (np.pi * x)

def I(theta, d, lambd, I0):
    return I0 * (sinc(d * lambd * np.sin(theta) / np.pi))**2

I0 = float(input("Enter the value of I0: "))
lambd = float(input("Enter the value of lambda: "))
d = float(input("Enter the value of d: "))

theta_min = 0
theta_max = np.pi/2
num_points = 100
theta_array = np.linspace(theta_min, theta_max, num_points)
I_array = [I(theta, d, lambd, I0) for theta in theta_array]

with open("diffraction_data.txt", "w") as file:
    file.write("Theta (radians)   Intensity\n")
    for theta, intensity in zip(theta_array, I_array):
        file.write("{:.2f} {:.2f}\n".format(theta, intensity))

#values of θ and I are  written to a text file named diffraction_data.txt in a tabular format.
