import math

# Given values
face_value = 100
coupon_rate = 0.08
annual_coupon = face_value * coupon_rate
y_initial = 0.11  # 11% continuously compounded
y_new = 0.108     # 10.8%
T = 5

# (a) Bond price at 11%
def bond_price(yield_rate):
    price = 0
    for t in range(1, T + 1):
        price += annual_coupon * math.exp(-yield_rate * t)
    price += face_value * math.exp(-yield_rate * T)
    return price

price_initial = bond_price(y_initial)

# (b) Duration
def bond_duration(yield_rate):
    weighted_sum = 0
    price = bond_price(yield_rate)
    for t in range(1, T + 1):
        cf = annual_coupon if t < T else annual_coupon + face_value
        pv = cf * math.exp(-yield_rate * t)
        weighted_sum += t * pv
    return weighted_sum / price

duration = bond_duration(y_initial)

# (c) Price change estimate using duration
delta_y = y_new - y_initial
price_change_estimate = -duration * delta_y * price_initial
estimated_new_price = price_initial + price_change_estimate

# (d) Recalculate price at 10.8%
price_new = bond_price(y_new)

# Print results
print(f"(a) Bond Price at 11%: {price_initial:.4f}")
print(f"(b) Duration: {duration:.4f} years")
print(f"(c) Estimated Price Change: {price_change_estimate:.4f}")
print(f"    Estimated New Price: {estimated_new_price:.4f}")
print(f"(d) Actual New Price at 10.8%: {price_new:.4f}")
print(f"Difference between estimate and actual: {abs(price_new - estimated_new_price):.4f}")