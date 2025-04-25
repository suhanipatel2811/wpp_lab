import pandas as pd

# Given Series of asking prices and fair prices
asking_prices = pd.Series([15000, 20000, 18000, 25000, 22000])
fair_prices = pd.Series([16000, 21000, 17000, 24000, 23000])

# Identify good deals where asking price is less than fair price
good_deals = asking_prices < fair_prices

# Get the indices of the good deals
good_deal_indices = good_deals[good_deals].index.tolist()

# Display the result
print("Indices of good deals:", good_deal_indices)
