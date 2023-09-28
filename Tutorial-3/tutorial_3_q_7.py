import numpy as np
import matplotlib.pyplot as plt

kB = 1.38e-23

def E(T, Tc):
    return 3.52 * kB * T * (1 - (T / Tc))**0.5

Tc = input("Enter Tc value: ")
Tc = float(Tc)

T = np.linspace(0, Tc, 1000)
E_T = E(T, Tc)

plt.plot(T, E_T)
plt.xlabel("Temperature (T)")
plt.ylabel("Energy Gap (E)")
plt.title("Energy Gap vs. Temperature")
plt.show()
