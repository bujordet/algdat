#!/usr/bin/python3

__auther__ = "Morten Bujordet"

from sys import stdin


def sort_list(usortert):
    # NOTICE: The sorted list must be returned.
    # SKRIV DIN KODE HER
    sorted_list = []
    for a in usortert:
        #print(a)
        sorted_list.append(a)

    #print(usortert)
    for element in usortert:
        counter = 0
        for e in usortert:
            if e < element:
                counter += 1
        sorted_list[counter] = element


    #print(sorted_list)
    return sorted_list

def find(liste, lower, upper):
    # NOTICE: The result must be returned.
    # SKRIV DIN KODE HER
    #print(lower, upper)
    minlower = liste[0]
    minUpper = liste[-1]
    for e in range(len(liste)):
        if liste[e] > lower and e != 0:
            minlower = liste[e-1]
            break
    for e in range(len(liste)):
        if liste[e] > upper:
            minUpper = liste[e]
            break
    return [minlower,minUpper]


def main():
    input_list = []
    sorted_list = []
    for x in stdin.readline().split():
        input_list.append(int(x))
        sorted_list.append(int(x))

    for element in input_list:
        counter = 0
        for e in input_list:
            if e < element:
                counter += 1
        sorted_list[counter] = element
    #sorted_list = sort_list(input_list)

    for line in stdin:
        word = line.split()
        minimum = int(word[0])
        maximum = int(word[1])
        result = find(sorted_list, minimum, maximum)
        print(str(result[0]) + " " + str(result[1]))


if __name__ == "__main__":
    main()
