import math
# Given data
F0=60       # Futures price
K=60        # Strike price
sigma=0.30  # Volatility
r=0.08      # Risk-free rate
T=0.5       # Time in years
n=2         # Steps
# Step size and factors
dt=T/n
u=math.exp(sigma*math.sqrt(dt))   # Up factor
d=1/u                             # Down factor
p=(math.exp(r*dt)-d)/(u-d)        # Risk-neutral probability
           
# Futures prices at nodes
Fuu=F0*u*u
Fud=F0*u*d
Fdd=F0*d*d
# Terminal payoffs
Cuu=max(Fuu-K,0)
Cud=max(Fud-K,0)
Cdd=max(Fdd-K,0)

# One step back
Cu=math.exp(-r*dt)*(p*Cuu+(1-p)*Cud)
Cd=math.exp(-r*dt)*(p*Cud+(1-p)*Cdd)
# Root value (European)
C0=math.exp(-r*dt)*(p*Cu+(1-p)*Cd)
# American check at node 1
Cu_early=max(F0*u-K,0)
Cd_early=max(F0*d-K,0)
early_exercise_possible=(Cu_early > Cu) or (Cd_early > Cd)

print(f"European Call Option Price: {C0:.4f}")
print(f"Early exercise for American Call? {'Yes' if early_exercise_possible else 'No'}")