import matplotlib.pyplot as plt
import numpy as np

ndays = 315
dt = 1 # time step in days
N = 60461826

I = np.zeros(ndays) #infected
t = np.arange(ndays)*dt+1
I[0] = 20

for i in range(ndays-1):
  if 0<i<34 :
        R = 1.36
        D = 270
  elif 35<i<169:
        R = 1.15
        D = 37
  elif 168<i<193 :
        R = 1.15
        D = 31
  elif 192<i<236:
        R = 1.15
        D = 29
  elif 235<i<316:
        R = 1.07
        D = 2

  I[i+1] = (R*N*I[i])/(N+(R-1+D)*I[i])


fig = plt.figure(1); fig.clf()
plt.plot(t,I,'g', label='Infected')
fig.legend(); plt.xlabel('Days'); plt.ylabel('Infected Population')
