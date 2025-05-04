import numpy as np
import matplotlib.pyplot as plt

# Hyperparameters
init_OD = 20
max_OD = 200
duration = 24 # (hours)

# Plot data
X = [] # Time (hours)
Y = [] # OD600

curr_OD = init_OD

for i in range(duration):
    Y.append(curr_OD)
    X.append(i)
    curr_OD += 10



plt.plot(X, Y)
plt.xlabel("Time (hrs)")
plt.ylabel("OD600")
plt.title("OD600 Over Time")
plt.show()