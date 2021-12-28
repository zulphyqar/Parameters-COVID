import matplotlib.pyplot as plt
import numpy as np

ndays = 300
dt = 1 # time step in days
N = 38928346

I = np.zeros(ndays) #infected
t = np.arange(ndays)*dt+1
I[0] = 4

for i in range(ndays-1):
  if 0<i<21 :
        R = 1.16
        D = 0
  elif 20<i<40:
        R = 1.075
        D = 10
  elif 39<i<106 :
        R = 1.105
        D = 128
  elif 105<i<235:
        R = 1.07
        D = 70
  elif 234<i<301:
        R = 1.02
        D = 13

  I[i+1] = dt*(R*N*I[i])/(N+(R-1+D)*I[i])

print(t)
print(I)

fig = plt.figure(1); fig.clf()
plt.plot(t,I,'g', label='Infected')
fig.legend(); plt.xlabel('Days'); plt.ylabel('Infected Population')
