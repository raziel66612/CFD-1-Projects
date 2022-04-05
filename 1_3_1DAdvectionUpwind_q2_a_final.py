import numpy as np
import matplotlib.pyplot as plt

TTime = 1
N_t = 1000
dt = TTime / N_t
L = 2.0
N = 101
dx = L / (N - 1)

x = np.linspace(0, L, N)
t = np.linspace(0, TTime, N_t)
u = np.zeros((N_t, N))

p= -1                                                                      #Direction of initial condition - Positive or negative
u[0] = [2*p if 1/dx+1 <= i < 1.5/dx+1 else 1*p for i in range(N)]          #Initial Condition

# ------------------------ Advection equation for both positive as well as negative direction-------------
if sum(u[0]) < 0:                 #for Negative initial velocity condition
    for i in range(N_t - 1):
        u[i+1] = u[i] - u[i] * dt/dx * ( np.roll(u[i], -1) - u[i])
else:
    for i in range(N_t - 1):       #for positive initial velocity condition
        u[i+1] = u[i] - u[i] * dt/dx * (u[i] - np.roll(u[i], 1))

fig, (ax1,ax2) = plt.subplots(1,2)

ax1.plot(x,u[0,:])
ax1.set_xlabel("x")
ax1.set_ylabel("u-velocity")
ax1.set_title("Initial condition, t=0")

ax2.plot(x,u[-1,:])
ax2.set_xlabel("x")
ax2.set_ylabel("u-velocity")

ax2.set_title("Final Time")
plt.savefig('Q2b')

fig.tight_layout()
plt.show()

