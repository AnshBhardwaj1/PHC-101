import numpy as np

# Create a 2D array
a = np.array([[1, 2], [3,4], [8,6], [5,6], [5,9], [3,6], [5,7], [5,1], [5,2], [3,6]])

# Save the array to a .dat file
np.savetxt('expt.dat', a)

# Load data from expt.dat file
data = np.loadtxt("expt.dat")
C = data[:,0]
V = data[:,1]

# Calculate Q and E using given relationships
Q = C * V
E = 0.5 * C * V**2

# Save results in ce.out file
results = np.column_stack((C, V, Q, E))
np.savetxt("ce.out", results, delimiter='\t', fmt='%.6f')
