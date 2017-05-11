prices = {
	'ACME':45.23,
	'APPLE':612.78,
	'IBM':205.55,
	'HPQ':37.12,
	'FB':10.75

}

min_prices = min(zip(prices.values(),prices.keys()))
max_prices = max(zip(prices.values(),prices.keys()))
prices_sorted = sorted(zip(prices.values(),prices.keys()))

print(min_prices)
print(max_prices)
print(prices_sorted)
print(min(prices.values()))
print(max(prices.values()))
