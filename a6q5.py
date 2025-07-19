import numpy as np
import matplotlib.pyplot as plt
K=150 # Strike Price
premium=5 # Option premium
S=np.linspace(100,200,100) # Spot price range
# Payoff and Profit calculations
# Long Call
long_call_payoff=np.maximum(S-K,0)
long_call_profit=long_call_payoff-premium
# Short Call
short_call_payoff=-long_call_payoff
short_call_profit=short_call_payoff+premium
# Long Put
long_put_payoff=np.maximum(K-S,0)
long_put_profit=long_put_payoff-premium
# Short Put
short_put_payoff= -long_put_payoff
short_put_profit=short_put_payoff+premium
# Plotting all in subplots
fig,axs=plt.subplots(2,2,figsize=(10,6))
fig.suptitle('Payoff and Profit Diagrams for Options (K=$150, Premium=$5)',fontsize=14)
# Titles for each subplot
titles=['Long Call','Short Call','Long Put','Short Put']
payoffs=[long_call_payoff, short_call_payoff, long_put_payoff, short_put_payoff]
profits=[long_call_profit, short_call_profit, long_put_profit, short_put_profit]
# Plot each
for ax, title, payoff, profit in zip(axs.flat, titles, payoffs, profits):
    ax.axhline(0, color='black', linewidth=1)
    ax.axvline(K, color='red', linestyle='--', label=f'Strike Price (K={K})')
    ax.plot(S, payoff, '--', color='blue', label='Payoff')
    ax.plot(S, profit, color='green', label='Profit')
    ax.set_title(title)
    ax.set_xlabel('Spot Price ($)')
    ax.set_ylabel('Value ($)')
    ax.legend()
    ax.grid()

plt.tight_layout()
plt.show()