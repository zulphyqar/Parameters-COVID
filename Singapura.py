import matplotlib.pyplot as plt
import numpy as np

ndays = 344
dt = 1 # time step in days
N = 5850342

I = np.zeros(ndays) #infected
t = np.arange(ndays)*dt
I[0] = 1

for i in range(ndays-1):
  if 0<i<75 :
        R = 1.11
        D = 5
  elif 74<i<118:
        R = 1.11
        D = 18
  elif 117<i<179 :
        R = 1.049
        D = 6
  elif 178<i<345:
        R = 1.0605
        D = 6

  I[i+1] = (R*N*I[i])/(N+(R-1+D)*I[i])


fig = plt.figure(1); fig.clf()
plt.plot(t,I,'g', label='Infected')
fig.legend(); plt.xlabel('Days'); plt.ylabel('Infected Population')
