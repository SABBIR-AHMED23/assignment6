import math
# Given data
S0=40     # Initial stock price
r=0.10    # Risk-free rate
T=1       # Time to maturity

# (a) Forward price and initial value
F0=S0*math.exp(r*T)
initial_value=0

print("(a)")
print(f"Forward price (F0): {F0:.2f}")
print(f"Initial value of forward contract: {initial_value:.2f}")

# (b) Six months later
t=0.5         # 6 months
St=45         # Stock price at t = 0.5
Ft=St*math.exp(r*(T-t))  # New forward price
# Value of original forward contract
ft=St-F0*math.exp(-r*(T-t))

print("\n(b)")
print(f"New forward price (Ft): {Ft:.2f}")
print(f"Value of original forward contract (ft): {ft:.2f}")