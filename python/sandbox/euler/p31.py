#given total of N cents, how many ways can 1 express N as a linear combination of coins in S


coins = [1, 2, 5, 10, 20, 50, 100, 200]
total = 200
ways = [1] + [0] * total

for coin in coins:
	for i in range(coin, total+1):
		ways[i] += ways[i - coin]
print(ways, ways[total])