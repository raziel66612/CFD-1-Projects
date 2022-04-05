import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm



import time
start_time = time.time()


TTime = 0.5
N_t = 300
dt = TTime / N_t
L = 2.0
N = 101
dx = L / (N - 1)
dy = L / (N - 1)

x = np.linspace(0, L, N)
y = np.linspace(0, L, N)
t = np.linspace(0, TTime, N_t)
u = np.ones(((N_t, N, N)))
v = np.ones(((N_t, N, N)))

#--------------------Initialization
u[0,int(0.5/dx+1) : int(1/dx+1),int(0.5/dx+1) : int(1/dx+1)] = 2
v[0,int(0.5/dx+1) : int(1/dx+1),int(0.5/dx+1) : int(1/dx+1)] = 2



#----------------------------Method 1 : Optimized first-Order Upwind Advection Code------------------------------------------------------

for i in range(N_t - 1):
    u[i+1] = u[i] - u[i] * dt/dx * (u[i] - np.roll(u[i], 1,axis=0)) - v[i] * dt/dy * (u[i] - np.roll(u[i], 1,axis=1))
    v[i+1] = v[i] - u[i] * dt/dx * (v[i] - np.roll(v[i], 1,axis=0)) - v[i] * dt/dy * (v[i] - np.roll(v[i], 1,axis=1))
    
# --------------------------Method 2 : Conventional Code first-Order Upwind Advection (Not efficient)---------------------------------

# for tt in range(N_t-1):
#     for i in range(N-1):
#         for j in range(N-1):
#             u[tt+1,i,j]= u[tt,i,j] - (dt/dx)*u[tt,i,j]*(u[tt,i,j]-u[tt,i-1,j]) - (dt/dy)*v[tt,i,j]*(u[tt,i,j]-u[tt,i,j-1])
#             v[tt+1,i,j]= v[tt,i,j] - (dt/dx)*u[tt,i,j]*(v[tt,i,j]-v[tt,i-1,j]) - (dt/dy)*v[tt,i,j]*(v[tt,i,j]-v[tt,i,j-1])



#---------------------------------------Plot Single Graph------------------------------------------------------------------------------
# plt.plot(x,u[-1,50])

# X, Y = np.meshgrid(x, y)
# fig, ax = plt.subplots(subplot_kw={"projection":"3d"})
# surf = ax.plot_surface(X, Y, u[-1])
# surf = ax.plot_surface(X, Y, u[-1])
# plt.show()
# ---------------------------------------Plot multiple 3D subplot ---------------------------------------------------------------------

X, Y = np.meshgrid(x, y)
fig = plt.figure()
ax = fig.add_subplot(1,2,1,projection='3d')
# surf = ax.plot_surface(X, Y, u[-1],cmap=cm.coolwarm)
surf = ax.plot_surface(X, Y, u[-1],cmap="jet")
ax.set_xlabel('x-coordinate')
ax.set_ylabel('y-coordinate')
ax.set_zlabel('U velocity')
ax.set_xlim(0,2)
ax.set_ylim(0,2)
ax.set_zlim(1,2)

ax = fig.add_subplot(1,2,2,projection='3d')
ax.plot_surface(X,Y,v[-1],cmap=cm.twilight_shifted)
ax.set_xlabel('x-coordinate')
ax.set_ylabel('y-coordinate')
ax.set_zlabel('V velocity')
ax.set_xlim(0,2)
ax.set_ylim(0,2)
ax.set_zlim(1,2)
plt.show()



print("--- %s seconds ---" % (time.time() - start_time))