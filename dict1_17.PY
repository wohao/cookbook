prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
P1 = {key: value for key, value in prices.items() if value > 200}
print(P1)
tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
P2 = {key:value for key,value in prices.items() if key in tech_names}
print(P2)
P3 = dict((key,value) for key,value in prices.items() if value > 200)
print(P3)
P4 = {key :prices[key] for key in prices.keys() & tech_names}
print(P4)