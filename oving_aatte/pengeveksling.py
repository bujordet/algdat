__author__ = "Morten Bujordet"

from sys import stdin

Inf = float('inf')


def min_coins_greedy(coins, value):
    currentCoin = 0
    numCoins = 0
    while value > 0:
        if coins[currentCoin] <= value:
            value -= coins[currentCoin]
            numCoins += 1
        else:
            currentCoin += 1
    return numCoins


def min_coins_dynamic(coins, value):
    r = [Inf]*(value+1)
    s = []
    for element in coins:
        if element <= value:
            r[element] = 1
            s.append(element)
    for val in range(1, value+1):
        if r[val] != Inf:
            continue
        q = Inf
        for useful in s:
            if useful <= val:
                current = 1 + r[val - useful]
                if current < q:
                    q = current
        r[val] = q
    return r[value]


def can_use_greedy(coins):
    # bare returner False her hvis du ikke klarer aa finne ut
    # hva som er kriteriet for at den graadige algoritmen skal fungere
    # SKRIV DIN KODE HER
    for x in range(len(coins)-1):
        if coins[x] % coins[x + 1] != 0:
            return False
    return True

coins = []
for c in stdin.readline().split():
    coins.append(int(c))
coins.sort()
coins.reverse()
method = stdin.readline().strip()
if method == "graadig" or (method == "velg" and can_use_greedy(coins)):
    for line in stdin:
        print(min_coins_greedy(coins, int(line)))
else:
    for line in stdin:
        print(min_coins_dynamic(coins, int(line)))
