__author__ = "Morten Bujordet"

from sys import stdin

Inf = 1000000000


def min_coins_greedy(coins, value, ant):
    largest = 0
    for element in coins:
        if element > largest and element <= value:
            largest = element
    if value > 0:
        value -= largest
        ant += 1
        ant = min_coins_greedy(coins, value, ant)
    return ant


def min_coins_dynamic(coins, value, ant):
    print(value, ant)
    largest = 0
    for element in coins:
        if (element > largest and element <= value):
            largest = element
    #print(coins, value ,largest)

    if (value > 0):
        #coins.remove(largest)
        value = value - largest
        ant = min_coins_dynamic(coins, value, ant+1)
    return ant


def can_use_greedy(coins):
    # bare returner False her hvis du ikke klarer aa finne ut
    # hva som er kriteriet for at den graadige algoritmen skal fungere
    # SKRIV DIN KODE HER
    return False

coins = []
for c in stdin.readline().split():
    coins.append(int(c))
coins.sort()
coins.reverse()
method = stdin.readline().strip()
if method == "graadig" or (method == "velg" and can_use_greedy(coins)):
    for line in stdin:
        print(min_coins_greedy(coins, int(line), 0))
else:
    for line in stdin:
        print(min_coins_dynamic(coins, int(line), 0))
