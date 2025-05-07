import numpy as np
import matplotlib.pyplot as plt

# EQUATION CREDIT: https://journals.asm.org/doi/10.1128/aem.71.12.7920-7926.2005
# " dN/dt = rN {1 -(N/Nmax)m}{1 -(Nmin/N)n} (equation 3) 
# Here, we will denote equation 3 as model III. Model III can describe 
# sigmoidal curves with various curvatures during the deceleration phase 
# compared to model II. With a larger m, the curvature of the deceleration 
# phase with model III becomes smaller. "
# ** Model applied to E. coli grown in LB broth. **

# Hyperparameters
duration = 24 # (hours)
logN0 = 3.8 # Initial population (log)
logN_max = 10.1 # Max population (log)
logN_min = 0 # Min population (log)

milk_adj = 0.25 # Milk adjustment factor

RT_r = 1.05 # Growth rate (RT)
RT_m = 0.58 # Curvature (RT)
RT_n = 3.3 # Adjustment factor (RT)

FR_r = 0.2 # Growth rate (FR)
FR_m = 0.42 # Curvature (FR)
FR_n = 3.3 # Adjustment factor (FR)

# Plot data
time = [] # Time (hours)
LB_rt = [] # CFU (room temp in LB)
rt = [] # CFU (room temp in MILK)
hs = [] # CFU (heat shock in MILK)
fr = [] # CFU (refrigeration in MILK)

# Setup initial CFUs
LB_rt_cfu = logN0
rt_cfu = logN0
hs_cfu = logN0 * 0.2
fr_cfu = logN0

# Loop over duration
for i in range(duration):
    # Append most recent values
    LB_rt.append(LB_rt_cfu)
    rt.append(rt_cfu)
    hs.append(hs_cfu)
    fr.append(fr_cfu)
    time.append(i)

    # Obtain most recent CFU values
    LB_RT_N = LB_rt[-1]
    RT_N = rt[-1]
    HS_N = hs[-1]
    FR_N = fr[-1]

    # Obtain new rate differentials
    LB_RT_dn_dt = RT_r * LB_RT_N * (1 - (RT_m * LB_RT_N / logN_max) * (1 - (RT_n * logN_min / LB_RT_N)))
    RT_dn_dt = (RT_r * milk_adj) * RT_N * (1 - (RT_m * RT_N / logN_max) * (1 - (RT_n * logN_min / RT_N)))
    HS_dn_dt = (RT_r * milk_adj) * HS_N * (1 - (RT_m * HS_N / logN_max) * (1 - (RT_n * logN_min / HS_N)))
    FR_dn_dt = (FR_r * milk_adj) * FR_N * (1 - (FR_m * FR_N / logN_max) * (1 - (FR_n * logN_min / FR_N)))

    # Calculate new CFUs
    LB_rt_cfu += LB_RT_dn_dt
    rt_cfu += RT_dn_dt
    hs_cfu += HS_dn_dt
    fr_cfu += FR_dn_dt

# Plot results
tfont = {'fontname':'Times', 'fontsize':18}
afont = {'fontname':'Times', 'fontsize':14}
plt.plot(time, LB_rt, color = 'gold', label = '(LB) Room temperature')
plt.plot(time, rt, color = 'limegreen', label = '(Milk) Room temperature')
plt.plot(time, hs, color = 'tomato', label = '(Milk) Heat shock')
plt.plot(time, fr, color = 'cornflowerblue', label = '(Milk) Refrigeration')

plt.xlabel("Time (hrs)", **afont)
plt.ylabel("log CFU", **afont)
plt.title("log CFU of E. coli Over Time in Different Conditions", **tfont)
plt.legend()

plt.show()