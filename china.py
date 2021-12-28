import matplotlib.pyplot as plt
import numpy as np

ndays = 365
dt = 1 # time step in days
N = 1439323776

I = np.zeros(ndays) #infected
t = np.arange(ndays)*dt+1
I[0] = 27

for i in range(ndays-1):
  if 0<i<21 :
        R = 1.23
        D = 0
  elif 20<i<120:
        R = 1.22
        D = 4030
  elif 119<i<203 :
        R = 1.22
        D = 3760
  elif 202<i<225:
        R = 1.22
        D = 3565
  elif 224<i<366:
        R = 1.22
        D = 3505

  I[i+1] = (R*N*I[i])/(N+(R-1+D)*I[i])


fig = plt.figure(1); fig.clf()
plt.plot(t,I,'g', label='Infected')
fig.legend(); plt.xlabel('Days'); plt.ylabel('Infected Population')
