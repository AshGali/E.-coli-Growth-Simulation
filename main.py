import numpy as np
import matplotlib.pyplot as plt

# Hyperparameters
init_OD = 0
max_OD = 10
duration = 24 # (hours)

# Plot data
time = [] # Time (hours)
rt = [] # OD600 (room temp)
hs = [] # OD600 (heat shock)
fr = [] # OD600 (refrigeration)

# Setup initial OD600s
rt_OD = init_OD
hs_OD = init_OD
fr_OD = init_OD

# Loop over duration
for i in range(duration):
    rt.append(rt_OD)
    hs.append(hs_OD)
    fr.append(fr_OD)
    time.append(i)
    rt_OD += 0.05*i
    hs_OD += 0.02*i
    fr_OD += 0.005*i

# Plot results
plt.plot(time, rt, color = 'green', label = 'Room temperature')
plt.plot(time, hs, color = 'red', label = 'Heat shock')
plt.plot(time, fr, color = 'blue', label = 'Refrigeration')

plt.xlabel("Time (hrs)")
plt.ylabel("OD600")
plt.title("OD600 Over Time")

plt.show()