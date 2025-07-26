import numpy as np
import matplotlib.pyplot as plt
# Parameters
S0=484         # initial index level
K=480          # strike price
T=2/12         # time to maturity (in years)
r=0.10         # risk-free interest rate
q=0.03         # dividend yield
sigma=0.25     # volatility
N=4            # number of steps
dt=T/N         # time per step

# Binomial parameters
u=np.exp(sigma*np.sqrt(dt))
d=1/u
p=(np.exp((r-q)*dt)-d)/(u-d)
discount=np.exp(-r*dt)

# Trees
asset_tree=[]
option_tree=[]

# Asset prices
for i in range(N+1):
    level=[]
    for j in range(i+1):
        S=S0*(u**j)*(d**(i-j))
        level.append(S)
    asset_tree.append(level)

# Option values at maturity
last_level=[max(K-s,0) for s in asset_tree[-1]]
option_tree.append(last_level)

# Backward induction for American Put
for i in reversed(range(N)):
    level=[]
    for j in range(i+1):
        hold=discount*(p*option_tree[0][j+1]+(1-p)*option_tree[0][j])
        exercise=K-asset_tree[i][j]
        level.append(max(hold, exercise))
    option_tree.insert(0, level)

# Plotting the tree
fig,ax=plt.subplots(figsize=(12,7))
ax.set_title("Binomial Tree: American Put Option", fontsize=14)
ax.axis("off")

# Coordinates for plotting
positions={}  # (i, j): (x, y)
x_spacing=2
y_spacing=1.8

for i in range(N+1):
    for j in range(i+1):
        x=i*x_spacing
        y=j*y_spacing
        positions[(i,j)]=(x,y)
        S=asset_tree[i][j]
        V=option_tree[i][j]
        ax.text(x,y,f"S={S:.1f}\nV={V:.2f}", ha='center', va='center',
                bbox=dict(boxstyle='round,pad=0.3', fc='lightyellow', ec='black'))

# Draw arrows between nodes
for i in range(N):
    for j in range(i+1):
        x1,y1=positions[(i,j)]
        x2u,y2u=positions[(i+1,j+1)]
        x2d,y2d=positions[(i+1,j)]
        ax.plot([x1,x2u],[y1,y2u],'gray')
        ax.plot([x1,x2d],[y1,y2d],'gray')

plt.tight_layout()
plt.show()