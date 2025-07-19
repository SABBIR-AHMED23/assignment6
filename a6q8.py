import numpy as np
import pandas as pd
from math import log,sqrt,exp
from scipy.stats import norm

# Black-Scholes formula for European Call and Put
def bs_price(S,K,r,T,sigma,option_type='call'):
    d1=(log(S/K)+(r+0.5*sigma**2)*T)/(sigma*sqrt(T))
    d2=d1-sigma*sqrt(T)
    if option_type=='call':
        return S*norm.cdf(d1)-K*exp(-r*T)*norm.cdf(d2)
    else:
        return K*exp(-r*T)*norm.cdf(-d2)-S*norm.cdf(-d1)
# Parameters
S0=32
r=0.05
sigma=0.30
# Strike Prices and Times
K1,K2,K3=25,30,35
T_short=0.5 # 6 months
T_long=1.0  # 1 year

# Compute option prices
call_25_6m=bs_price(S0,K1,r,T_short,sigma,'call')
call_30_6m=bs_price(S0,K2,r,T_short,sigma,'call')
put_25_6m=bs_price(S0,K1,r,T_short,sigma,'put')
put_30_6m=bs_price(S0,K2,r,T_short,sigma,'put')

call_25_1y=bs_price(S0,K1,r,T_long,sigma,'call')
call_30_1y=bs_price(S0,K2,r,T_long,sigma,'call')
call_35_1y=bs_price(S0,K3,r,T_long,sigma,'call')

put_25_1y=bs_price(S0,K1,r,T_long,sigma,'put')
put_30_1y=bs_price(S0,K2,r,T_long,sigma,'put')
put_35_1y=bs_price(S0,K3,r,T_long,sigma,'put')
call_35_6m=bs_price(S0,K3,r,T_short,sigma,'call')

# Display option prices
print("Option Prices:")
print(f"{'Call(25,6m)':<12}: {call_25_6m:.4f}, {'Call(30,6m)':<12}: {call_30_6m:.4f}")
print(f"{'Put(25,6m)':<12}: {put_25_6m:.4f}, {'Put(30,6m)':<12}: {put_30_6m:.4f}")
print(f"{'Call(25,1y)':<12}: {call_25_1y:.4f}, {'Call(30,1y)':<12}: {call_30_1y:.4f}, {'Call(35,1y)':<12}: {call_35_1y:.4f}")
print(f"{'Put(25,1y)':<12}: {put_25_1y:.4f}, {'Put(30,1y)':<12}: {put_30_1y:.4f}, {'Put(35,1y)':<12}: {put_35_1y:.4f}")

# Create stock price range for payoff calculations
S_range=np.arange(10,50,1)
# Strategy functions
def bull_call_spread(S,K1,K2,premium1,premium2):
    payoff=np.maximum(S-K1,0)-np.maximum(S-K2,0)
    cost=premium1-premium2
    return payoff-cost

def bear_put_spread(S,K1,K2,premium1,premium2):
    payoff=np.maximum(K2-S,0)-np.maximum(K1-S,0)
    cost=premium1-premium2
    return payoff-cost

def butterfly_call(S,K1,K2,K3,p1,p2,p3):
    payoff=np.maximum(S-K1,0)-2*np.maximum(S-K2,0)+np.maximum(S-K3,0)
    cost=p1-2*p2+p3
    return payoff-cost

def butterfly_put(S,K1,K2,K3,p1,p2,p3):
    payoff=np.maximum(K1-S,0)-2*np.maximum(K2-S,0)+np.maximum(K3-S,0)
    cost=p1-2*p2+p3
    return payoff-cost

def straddle(S,K,call_premium,put_premium):
    payoff=np.maximum(S-K,0)+np.maximum(K-S,0)
    cost=call_premium+put_premium
    return payoff-cost

def strangle(S,K1,K2,call_premium,put_premium):
    payoff=np.maximum(S-K2,0)+np.maximum(K1-S,0)
    cost=call_premium+put_premium
    return payoff-cost

# Calculate profit tables
bull=bull_call_spread(S_range,25,30,call_25_6m,call_30_6m)
bear=bear_put_spread(S_range,25,30,put_25_6m,put_30_6m)
butterfly_c=butterfly_call(S_range,25,30,35,call_25_1y,call_30_1y,call_35_1y)
butterfly_p=butterfly_put(S_range,25,30,35,put_25_1y,put_30_1y,put_35_1y)
straddle_profit=straddle(S_range,30,call_30_6m,put_30_6m)
strangle_profit=strangle(S_range,25,35,call_35_6m,put_25_6m)  # Strangle K1=25(put), K2=35(call)

# Create tables
df=pd.DataFrame({
    'Stock Price': S_range,
    'Bull Call Spread': bull,
    'Bear Put Spread': bear,
    'Butterfly Call': butterfly_c,
    'Butterfly Put': butterfly_p,
    'Straddle': straddle_profit,
    'Strangle': strangle_profit
})
print("\nProfit Table:")
print(df.head(15))