import math
import random
N = 1000000
N_T = 0
for i in range(N):
  x = random.random()*2 - 1
  y = random.random()*2 - 1

  x2 = x**2
  y2 = y**2

  if(math.sqrt(x2 + y2)<=1):
    N_T += 1
pi = (N_T/N)*4 
print(pi)