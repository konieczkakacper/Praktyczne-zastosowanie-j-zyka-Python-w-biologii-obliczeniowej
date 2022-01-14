1.
Napisz program, który znajduje w pliku tekstowym zadany ciąg znaków (wyrażenie regularne wprowadzone z linii poleceń) i zlicza liczbę jego wystąpień.
Jakiego wyrażenia użyjesz do wyszukania liczb pięciocyfrowych? Jakiego wyrażenia użyjesz do znalezienia ciągów złożonych z A i dowolnego znaku innego niż x,y lub z?
Jakiego wyrażenia użyjesz do sprawdzenia, czy łańcuch jest złożony z samych spacji?

Zobacz: https://docs.python.org/3/library/re.html

import re

with open('human.txt', 'r')as myfile:
    data = myfile.read()

    piecio = re.finditer(r'\b\d{5}\b', data)
    lista_piecio = list(piecio)

    ciagAidowolny =  re.finditer(r'[^xyz]', data) # A.+ a i jeden lub więcej dowolnych znaków
    lista_dowolny = list(ciagAidowolny)

    samespac = re.finditer(r'\s+[^ \n]',data)
    lista_spac = list(samespac)

    print(f'Liczba wystąpień liczb 5 cyfrowych: {len(lista_piecio)}')
    print(f'Liczba wystąpień dowolnych znaków z wyjątkiem x, y, z: {len(lista_dowolny)}')
    print(f'Liczba wystąpień spacji:{len(lista_spac)}')

2.
Napisz program, który cyfry zamieni na słowa tj. zamiast 1 umieści w tekście „jeden” itd.
def num_to_word(num):
    word_num = {"0": "zero", "00": "", "1": "One", "2": "Two", "3": "Three", "4": "Four", "5": "Five", "6": "Six",
                "7": "Seven", "8": "eight", "9": "Nine", "01": "One", "02": "Two", "03": "Three", "04": "Four",
                "05": "Five", "06": "Six", "07": "Seven", "08": "eight", "09": "Nine", "10": "Ten", "11": "Eleven",
                "12": "Twelve", "13": "Thirteen", "14": "Fourteen", "15": "Fifteen", "17": "Seventeen",
                "18": "Eighteen", "19": "Nineteen", "20": "Twenty", "30": "Thirty", "40": "Forty", "50": "Fifty",
                "60": "Sixty", "70": "seventy", "80": "eighty", "90": "ninety"}
    keys = []
    for k in word_num.keys():
        keys.append(k)

    if len(num) == 1: # dł == 1
        return (word_num[num[0]]) # zwraca 1 indeks wprowadzonej liczby

    elif len(num) == 2: #dł == 2
        number = 0
        for k in keys:
            if k == num[0] + num[1]:
                number += 1
        if number == 1:
            return (word_num[num[0] + num[1]])
        else:
            return (word_num[str(int(num[0]) * 10)] + " " + word_num[num[1]])

    elif len(num) == 3: #dł == 3
        number = 0
        for k in keys:
            if k == num[1] + num[2]:
                number += 1
        if number == 1:
            return (word_num[num[0]] + " Hundred " + word_num[num[1] + num[2]])
        else:
            return (word_num[num[0]] + " Hundred " + word_num[str(int(num[1]) * 10)] + " " + word_num[num[2]])

    elif len(num) == 4: #dl == 4
        number = 0
        for k in keys:
            if k == num[2] + num[3]:
                number += 1
        if number == 1:
            if num[1] == '0':
                return (word_num[num[0]] + " Thousand " + word_num[num[2] + num[3]])
            else:
                return (word_num[num[0]] + " Thousand " + word_num[num[1]] + " Hundred " + word_num[num[2] + num[3]])

        else:
            if num[1] == '0':
                return (word_num[num[0]] + " Thousand " + word_num[str(int(num[2]) * 10)] + " " + word_num[num[3]])
            else:
                return (word_num[num[0]] + " Thousand " + word_num[num[1]] + " Hundred " + word_num[
                    str(int(num[2]) * 10)] + " " + word_num[num[3]])

    elif len(num) == 5: #dł == 5
        number = 0
        d = 0
        for k in keys:
            if k == num[3] + num[4]:
                number += 1
        for k in keys:
            if k == num[0] + num[1]:
                d += 1
        if d == 1:
            val = word_num[num[0] + num[1]]
        else:
            val = word_num[str(int(num[0]) * 10)] + " " + word_num[num[1]]

        if number == 1:
            if num[1] == '0':
                return (val + " Thousand " + word_num[num[3] + num[4]])
            else:
                return (val + " Thousand " + word_num[num[2]] + " Hundred " + word_num[num[3] + num[4]])

        else:
            if num[1] == '0':
                return (val + " Thousand " + word_num[str(int(num[3]) * 10)] + " " + word_num[num[4]])
            else:
                return (val + " Thousand " + word_num[num[2]] + " Hundred " + word_num[str(int(num[3]) * 10)] + " " +
                        word_num[num[4]])


num = [str(d) for d in input("Wprowadź numer o maksymalnej długości 5 cyfr: ")]
print(num_to_word(num).upper())

3.
Napisz program, który wyszykuje powtórzenia słów i ujmuje blok powtórzonych słów w nawiasy kwadratowe.
W tym celu zapoznaj się z mechanizmem odwołania wstecznego (ang. backreference). Poszukaj o tym informacji w dokumentacji Pythona: https://docs.python.org/3/howto/regex.html (szukaj słowa backreference)
Przykład działania:
Wejście: To jest tekst tekst tekst bardzo wazny i i istotny wrecz wrecz niezastapiony tekst

Wyjście: To jest [tekst tekst tekst] bardzo wazny [i i] istotny [wrecz wrecz] niezastapiony tekst

4.
Zmodyfikuj powyższy program tak, by usuwał powtórzenia (Możesz wykorzystać do tego „named capture groups”).

Przykład działania:

Wejście: To jest tekst tekst tekst bardzo wazny i i istotny wrecz wrecz niezastapiony tekst Wyjście: To jest tekst bardzo wazny i istotny wrecz niezastapiony tekst

5.
Zobacz przykłady wykorzystania wyrażeń regularnych do analizy sekwencji DNA:
https://towardsdatascience.com/using-regular-expression-in-genetics-with-python-175e2b9395c2

Spróbuj przetestować wybrane wyrażenia na dowolnej sekwencji DNA.
# Alternation and Character Groups
import re

seq = 'AAGCTTTGGGGAGGCACACTCCTTTGGGGATGTAAGTGTAATTTTGCTTCCCTGATTTTCATCTTTTATTTG GGGCC TGGAAAATTAATAAAGCAGACTTTCCCCCATGTTT'
if re.search('GG(G|C)CC', seq):
    print('Restriction enzyme found!')
