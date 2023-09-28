import numpy as np
import matplotlib.pyplot as plt

def runges(x):
    return 1/(1 + 25*x**2)

x = np.linspace(-1, 1, 11)
y = runges(x)

third_order = np.polyfit(x, y, 3)
third_interp = np.poly1d(third_order)
x_interp = np.linspace(-1, 1, 1000)
y_third = third_interp(x_interp)

seventh_order = np.polyfit(x, y, 7)
seventh_interp = np.poly1d(seventh_order)
y_seventh = seventh_interp(x_interp)

plt.plot(x_interp, y_third, 'r', label='Third order')
plt.plot(x_interp, y_seventh, 'g', label='Seventh order')
plt.plot(x, y, 'o', label='Nodes')
plt.legend()
plt.show()
