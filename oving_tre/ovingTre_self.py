
#!/usr/bin/python3

from sys import stdin
from itertools import repeat


def merge(decks):
    # SKRIV DIN KODE HER
    #print(decks)
    lista = [0,1,2,3,4,5,6,7,8]
    for element in decks:
        #print(element)
        for e in element:
            tall = e[0]
            #print(tall)
            lista[tall-1] = e[1]
    return ("".join(lista))



def main():
    # Read input.
    decks = []
    for line in stdin:
        (index, csv) = line.strip().split(':')
        deck = list(zip(map(int, csv.split(',')), repeat(index)))
        decks.append(deck)
    # Merge the decks and print result.
    print(merge(decks))


if __name__ == "__main__":
    main()
