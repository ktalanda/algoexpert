def numberOfWaysToMakeChange(n, denoms):
    ways = [0] * (n + 1)
    ways[0] = 1

    for denom in denoms:
        for amount in range(denom, n+1):
            ways[amount] += ways[amount-denom]
    return ways[n]
