def minNumberOfCoinsForChange(n, denoms):
    mins = [float("inf")] * (n+1)
    mins[0] = 0

    for denom in denoms:
        for amount in range(denom, n+1):
            mins[amount] = min(mins[amount], 1 + mins[amount-denom])
    return mins[n] if mins[n] != float("inf") else -1
