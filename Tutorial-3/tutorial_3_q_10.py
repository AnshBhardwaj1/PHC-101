import numpy as np

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
