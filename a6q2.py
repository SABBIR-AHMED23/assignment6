import numpy as np
F = 100      # Face value
c = 0.08     # Coupon rate
y = 0.11     # Yield
n = 5        # Number of periods
# Cash flows
t = np.arange(1, n+1)
CF = np.full(n, c*F)
CF[-1] += F  # add principal to last cash flow

# Price and duration
P = np.sum(CF * np.exp(-y*t))
D = np.sum(t * CF * np.exp(-y*t)) / P

# Approximate price change for a small yield change
dy = -0.002
dP_approx= -P*D*dy

# Actual price change
y2 = 0.108
P2 = np.sum(CF * np.exp(-y2*t))
dP_actual = P2 - P

# Print results
print("Bond Price :", P)
print("Duration D:", D)
print("Approx. price change :", dP_approx)
print("Actual price change :", dP_actual)