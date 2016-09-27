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
        #print(node.posi)
    return toppNode

def bygg2(ordliste):
    root = Node()
    for ord in ordliste:
        node = root
        bygg_inner(ord[0], node, ord[1])

        #node.posi.append(ord[1])
        #print(node.posi)

    return root
def lagePosisjoner(node, posisjon):
    node.posi.append(posisjon)
    print(node.posi)

def bygg_inner(ord, node, posisjon):
    word = ord[0]
    bokstav = ord[0]
    #tall += 1
    #print(posisjon)
    if bokstav not in node.barn:
        node.barn[bokstav] = Node()


    if word[1:]:
        bygg_inner(word[1:], node.barn[bokstav], posisjon)


def posisjoner(ord, indeks, root):
    #print(node)

    if indeks >= len(ord):
        posi = root.posi
        #print(posi)
    elif ord[indeks] == "?":
        #print("lol")
        posi = []
        for barn in root.barn.values():
            posi += posisjoner(ord, indeks + 1, barn)
    elif ord[indeks] in root.barn:
        #print("lol")
        posi = posisjoner(ord, indeks + 1, root.barn[ord[indeks]])
    else:
        posi = []
    #rint(posi)
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
        root = bygg2(ordliste)

        for sokeord in stdin:
            sokeord = sokeord.strip()
            print("%s:" % sokeord, end='')
            posi = posisjoner(sokeord, 0, root)
            posi.sort()
            for p in posi:
                print(" %s" % p, end='')
            print()
    except:
        traceback.print_exc(file=stderr)


if __name__ == "__main__":
    main()