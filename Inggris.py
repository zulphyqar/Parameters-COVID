import matplotlib.pyplot as plt
import numpy as np

ndays = 329
dt = 1 # time step in days
N = 67886011

I = np.zeros(ndays) #infected
t = np.arange(ndays)*dt+1
I[0] = 1

for i in range(ndays-1):
  if 0<i<66 :
        R = 1.17
        D = 80
  elif 65<i<143:
        R = 1.15
        D = 40
  elif 142<i<224 :
        R = 1.15
        D = 30
  elif 223<i<287:
        R = 1.03
        D = 0.5
  elif 286<i<330:
        R = 1.013
        D = 0

  I[i+1] = (R*N*I[i])/(N+(R-1+D)*I[i])
print(I)

fig = plt.figure(1); fig.clf()
plt.plot(t,I,'g', label='Infected')
fig.legend(); plt.xlabel('Days'); plt.ylabel('Infected Population')
