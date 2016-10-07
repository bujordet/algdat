#!/usr/bin/python3

from sys import stdin
from string import ascii_lowercase as chars
from random import randint, choice
from operator import itemgetter
from collections import defaultdict

def counting(A, k):
    c = [0] * ( k + 1 )
    for i in A:
      c[i] += 1

    ndx = 0;
    for i in range(len(c)):
      while 0 < c[i]:
        A[ndx] = i
        ndx += 1
        c[i] -= 1
    #print(A)
    return A



def flexradix(A, d):
    # Du må mest sannsynlig lage egne hjelpefunksjoner for denne funksjonen for å løse oppgaven.
    # Funksjonen skal returnere listen A sortert.
    # SKRIV DIN KODE HER
    #print(A)
    dic2 = {'d': 4, 'b': 2, 'p': 16, 'e': 5, 'j': 10, 'k': 11, 'm': 13, 'y': 25, 'a': 1, 'g': 7, 'n': 14,'q': 17, 'w': 23, 'r': 18, 'l': 12, 'x': 24, 'i': 9, 'f': 6, 'c': 3, 'v': 22, 't': 20, 'u': 21, 's': 19,'o': 15, 'z': 26, 'h': 8}

    #print(k)
    counting_list = []
    ge = 0
    vente_liste = []

    while 0 < d:
        k = d
        a_videre = []
        for element in A:
            if (len(element) >= k):
                ##print(element)
                counting_list.append(dic2.get(element[k-1]))
                if (dic2.get(element[k-1]) > ge):
                    ge = dic2.get(element[k-1])
                vente_liste.append(element)
            else:
                a_videre.append(element)

        if (len(counting_list) > 1):
            counting_list = counting(counting_list, ge)
        vente_liste2 = [0] * (len(vente_liste))
        for i in counting_list:
            for x in vente_liste:
                if (dic2.get(x[k-1]) == i):
                    #print(x)
                    a_videre.append(x)
                    vente_liste.remove(x)
                    break
        print(a_videre)
        print(d)
        d -= 1

    return a_videre

def main():
    d = int(stdin.readline())
    strings = []
    for line in stdin:
        strings.append(line.rstrip())
    liste = flexradix(strings, d)
    print(liste)
    for string in liste:
        print(string)


if __name__ == "__main__":
    main()
