import numpy as np
import matplotlib.pyplot as plt

S0,K,r,q,sigma,T,N=484,480,0.1,0.03,0.25,2/12,4
dt=T/N
u=np.exp(sigma*np.sqrt(dt))
d=1/u
p=(np.exp((r-q)*dt)-d)/(u-d)

# Stock & option trees
S=[[S0*u**j*d**(i-j)for j in range(i+1)]for i in range(N+1)]
P=[[0]*(i+1)for i in range(N+1)]
P[-1]=[max(K-s,0)for s in S[-1]]

for i in range(N-1,-1,-1):
  for j in range(i+1):
    cont=np.exp(-r*dt)*(p*P[i+1][j+1]+(1-p)*P[i+1][j])
    P[i][j]=max(K-S[i][j],cont)

print("American put price:",P[0][0])

# --- Plot tree ---
for i in range(N):
  for j in range(i+1):
    plt.plot([i,i+1],[P[i][j],P[i+1][j]],'r-')
    plt.plot([i,i+1],[P[i][j],P[i+1][j+1]],'r-')
for i in range(N+1):
  for j,v in enumerate(P[i]):
    plt.scatter(i,v,c='r')
    plt.text(i,v,f"{v:.2f}",ha='center',fontsize=8)

plt.title("American Put Option Value Tree")
plt.show()