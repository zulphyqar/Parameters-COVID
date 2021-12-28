import matplotlib.pyplot as plt
import numpy as np

ndays = 306
dt = 1 # time step in days
N = 1380004385

I = np.zeros(ndays) #infected
t = np.arange(ndays)*dt+1
I[0] = 3

for i in range(ndays-1):
  if 0<i<88 :
        R = 1.12
        D = 230
  elif 87<i<128:
        R = 1.09
        D = 110
  elif 127<i<247 :
        R = 1.04
        D = 6
  elif 246<i<307:
        R = 1.038
        D = 5

  I[i+1] = (R*N*I[i])/(N+(R-1+D)*I[i])


fig = plt.figure(1); fig.clf()
plt.plot(t,I,'g', label='Infected')
fig.legend(); plt.xlabel('Days'); plt.ylabel('Infected Population')
