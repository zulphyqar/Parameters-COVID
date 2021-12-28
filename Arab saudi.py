import matplotlib.pyplot as plt
import numpy as np

ndays = 302
dt = 1 # time step in days
N = 34813871

I = np.zeros(ndays) #infected
t = np.arange(ndays)*dt
I[0] = 5

for i in range(ndays-1):
  if 0<i<12 :
        R = 1.35
        D = 0
  elif 11<i<60:
        R = 1.15
        D = 150
  elif 59<i<216 :
        R = 1.048
        D = 5
  elif 215<i<303:
        R = 1.052
        D = 5

  I[i+1] = (R*N*I[i])/(N+(R-1+D)*I[i])

fig = plt.figure(1); fig.clf()
plt.plot(t,I,'g', label='Infected')
fig.legend(); plt.xlabel('Days'); plt.ylabel('Infected Population')
