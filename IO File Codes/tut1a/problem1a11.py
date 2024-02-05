import numpy as np
import matplotlib.pyplot as plt
q_0 = 0.001
q_max = 0.001
c = 0.001
R = 1000
t = []
for i in range(1000):
  t.append(i*0.01)
q_dis = []
for i in range(1000):
  q_dis.append(q_0 * (np.exp(-t[i]/(R*c))))

for i in range(1000):
  plt.plot(t[:i+1] , q_dis[: i + 1] )
  plt.pause(0.01)
q_char = []
for i in range(100):
  
  q_char.append(q_max*(1 - (np.exp(-t[i]/(R*c)))))
for i in range(1000):
  plt.clf()
  plt.plot(t[:i+1] , q_char[: i + 1] )
  plt.pause(0.01)
plt.show()
