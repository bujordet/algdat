#!/usr/bin/python3

from sys import stdin, stderr
import traceback


class Node:
    def __init__(self):
        self.barn = {}
        self.posi = []


def bygg(ordliste):
    toppNode = Node()
    for (ord, posisjon) in ordliste:
        node = toppNode
        for bokstav in ord:
            if not bokstav in node.barn:
                node.barn[bokstav] = Node()
            node = node.barn[bokstav]
        node.posi.append(posisjon)
    return toppNode

def bygg2(ordliste, root):
    for ord in ordliste:
        bygg_inner(ord[0], root)
    return root

def bygg_inner(word, node):
    bokstav = word[0]
    if bokstav not in node.barn:
        node.barn[bokstav] = Node()
    if word[1:]:
        bygg_inner(word[1:], node.barn[bokstav])

def posisjoner(ord, indeks, node):

    if indeks >= len(ord):
        posi = node.posi
    elif ord[indeks] == "?":
        posi = []
        for barn in node.barn.values():
            posi += posisjoner(ord, indeks + 1, barn)
    elif ord[indeks] in node.barn:
        posi = posisjoner(ord, indeks + 1, node.barn[ord[indeks]])
    else:
        posi = []
    return posi

def main():
    try:
        ord = stdin.readline().split()
        ordliste = []
        pos = 0
        for o in ord:
            ordliste.append((o, pos))
            pos += len(o) + 1
        toppnode = bygg(ordliste)
        root = bygg2(ordliste, Node())

        for sokeord in stdin:
            sokeord = sokeord.strip()
            print("%s:" % sokeord, end='')
            posi = posisjoner(sokeord, 0, toppnode)
            posi.sort()
            for p in posi:
                print(" %s" % p, end='')
            print()
    except:
        traceback.print_exc(file=stderr)


if __name__ == "__main__":
    main()