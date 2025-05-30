import numpy as np
import math
import matplotlib.pyplot as plt

# EQUATION CREDIT: https://journals.asm.org/doi/10.1128/aem.71.12.7920-7926.2005
# " dN/dt = rN {1 -(N/Nmax)^m}{1 -(Nmin/N)^n} (equation 3) 
# Here, we will denote equation 3 as model III. Model III can describe 
# sigmoidal curves with various curvatures during the deceleration phase 
# compared to model II. With a larger m, the curvature of the deceleration 
# phase with model III becomes smaller. "
# ** Model applied to E. coli grown in LB broth. **

# Hyperparameters
duration = 24 # (hours)
N0 = 10**3.8 # Initial population
N_max = 10**10.1 # Max population
N_min = 10**1 # Min population

milk_adj = 1/6 # Milk adjustment factor (20 min in LB / 120 min in skim milk) doubling time

RT_r = 1.05 # Growth rate (RT)
RT_m = 0.58 # Curvature (RT)
RT_n = 3.3 # Adjustment factor (RT)

FR_r = 0.2 # Growth rate (FR)
FR_m = 0.42 # Curvature (FR)
FR_n = 3.3 # Adjustment factor (FR)

# Plot data
time = [] # Time (hours)
LB_rt = [] # log CFU (room temp in LB)
rt = [] # log CFU (room temp in MILK)
hs = [] # log CFU (heat shock in MILK)
fr = [] # log CFU (refrigeration in MILK)

# Setup initial CFUs
LB_rt_cfu = N0
rt_cfu = N0
hs_cfu = N0 * 0.2
fr_cfu = N0

# Loop over duration
for i in range(duration):
    # Append log of most recent values
    LB_rt.append(math.log10(LB_rt_cfu))
    rt.append(math.log10(rt_cfu))
    hs.append(math.log10(hs_cfu))
    fr.append(math.log10(fr_cfu))
    time.append(i)

    # Obtain most recent CFU values
    LB_RT_N = LB_rt_cfu
    RT_N = rt_cfu
    HS_N = hs_cfu
    FR_N = fr_cfu

    # Obtain new rate differentials
    LB_RT_dn_dt = RT_r * LB_RT_N * (1 - (LB_RT_N / N_max)**RT_m) * (1 - (N_min / LB_RT_N)**RT_n)
    RT_dn_dt = (RT_r * milk_adj) * RT_N * (1 - (RT_N / N_max)**RT_m) * (1 - (N_min / RT_N)**RT_n)
    HS_dn_dt = (RT_r * milk_adj) * HS_N * (1 - (HS_N / N_max)**RT_m) * (1 - (N_min / HS_N)**RT_n)
    FR_dn_dt = (FR_r * milk_adj) * FR_N * (1 - (FR_N / N_max)**FR_m) * (1 - (N_min / FR_N)**FR_n)

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
plt.ylabel("log[CFU]", **afont)
plt.title("Predicted log[CFU] of E. coli over 24 hours in different conditions", **tfont)
plt.legend()

plt.show()