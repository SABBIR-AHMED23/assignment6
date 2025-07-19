import math
from scipy.stats import norm
# Given values
S0=30
K=29
r=0.05
sigma=0.25
T=4/12  # 4 months

# Black-Scholes formula for European Call and Put
def black_scholes(S,K,r,T,sigma):
    d1=(math.log(S/K)+(r+0.5*sigma**2)*T)/(sigma*math.sqrt(T))
    d2=d1-sigma*math.sqrt(T)
    call_price=S*norm.cdf(d1)-K*math.exp(-r*T)*norm.cdf(d2)
    put_price=K*math.exp(-r*T)*norm.cdf(-d2)-S*norm.cdf(-d1)
    return call_price, put_price
# Calculate prices
call_euro,put_euro=black_scholes(S0,K,r,T,sigma)

# American call on non-dividend stock = European call price
call_american=call_euro
# Check Put-Call Parity: C - P = S - K*e^(-rT)
lhs=call_euro-put_euro
rhs=S0-K*math.exp(-r*T)

print(f"European Call Price: {call_euro:.4f}")
print(f"American Call Price: {call_american:.4f}")
print(f"European Put Price: {put_euro:.4f}")
print("\nPut-Call Parity Check:")
print(f"LHS (C - P) = {lhs:.4f}, RHS (S0 - K*e^(-rT)) = {rhs:.4f}")
print("Parity holds?" , abs(lhs - rhs) < 1e-6)