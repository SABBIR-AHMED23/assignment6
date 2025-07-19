import math
# Given values
S0=19   # Current stock price
K=20    # Strike price
C=1     # Call price
r=0.03  # Risk-free rate
T=4/12  # Time in years (4 months)
# Calculate put price using Put-Call Parity
P=C - S0 + K * math.exp(-r * T)

print(f"The price of the European put option is: ${P:.4f}")
