import numpy as np
import matplotlib.pyplot as plt
K_call=45
K_put=40
call_premium=3
put_premium=4
total_premium=call_premium+put_premium
S = np.linspace(20, 70, 200) # Asset price range
# Payoff calculations
call_payoff=np.maximum(S-K_call,0)
put_payoff=np.maximum(K_put-S,0)
total_payoff=call_payoff+put_payoff
profit=total_payoff-total_premium
# Plotting
plt.figure(figsize=(10,6))
plt.axhline(0, color='black', linewidth=1)
plt.axvline(K_call, color='red', linestyle='--', label=f'Call Strike (Kc={K_call})')
plt.axvline(K_put, color='blue', linestyle='--', label=f'Put Strike (Kp={K_put})')

plt.plot(S, profit, color='green', linewidth=2, label='Profit')
plt.plot(S, total_payoff, color='orange', linestyle='--', label='Payoff')

plt.title('Profit Diagram for Long Strangle (Buy Call & Put)')
plt.xlabel('Asset Price at Expiration ($)')
plt.ylabel('Profit / Payoff ($)')
plt.legend()
plt.grid()
plt.show()