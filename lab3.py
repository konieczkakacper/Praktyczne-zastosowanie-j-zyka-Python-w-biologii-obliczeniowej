# Listy (Lists)

## Zad. 1
Lista to uporządkowana sekwencja obiektów dowolnego typu.

```python
lst = []                       # Pusta lista
lst = list()                   # Pusta lista

lst = [1, 2, 3]                # Lista trzech liczb całkowitych
lst = ['John', 24, True]       # Lista trzech obiektów różnego typu
```

Utwórz listę dwuelementową, w której pierwszym elementem będzie liczba zmiennoprzecinkowa, a drugim elementem łańcuch znaków.
lst =[3.14, 'Pi number']

## Zad. 2
Listy, podobnie jak łańcuchy znaków, obsługują operator konkatenacji (`+`), powtórzenia (`*`), przynależności (`in`) oraz funkcję `len`.

Podaj wynik poniższych instrukcji.

```python
print([1, 2, 3] + [4, 5, 6])  # Konkatenacja --> [1, 2, 3, 4, 5, 6]
print([1, 2, 3] * 2)          # Powtórzenie --> [1, 2, 3, 1, 2, 3]
print(len([1, 2, 3]))         # Funkcja len --> 3
print(3 in [1, 2, 3])         # Przynależność --> True
print(3 not in [1, 2, 3])     # Przynależność --> False
```


## Zad. 3
Listy, podobnie jak łańcuchy znaków, obsługują indeksowanie i wycinki.

```python
lst = ['Python', 'C++', 'JavaScript']
print(lst[1])
print(lst[-1])
print(lst[0:2])
```

W brakujące miejsca (`_`) wpisz odpowiednie indeksy, aby wydobyć literę `h` z łańcucha `'Python'`.

```python
lst = ['Python', 'C++', 'JavaScript']
print(lst[0][3])
```

## Zad. 4
Listy, w odróżnieniu od łańuchów znaków, są obiektami **mutowalnymi**. Listy można więc modyfikować w miejscu (np. rozszerzać, zmniejszać lub zmieniać
ich elementy).

Krótko odpowiedz, co robi każda metoda poniżej.

```python
lst = ['a', 'b', 'c', 'b']

lst.append('d')                 # 1 --> dodanie elementu d do listy
lst.extend(['e', 'f'])          # 2 --> dodanie do listy elementow e oraz f
lst.pop()                       # 3 --> usuwa ostatni element listy i zwraca jego wartość
lst.remove('b')                 # 4 --> usuwa z listy element b
lst.insert(1, 'b')              # 5 --> dodaje element b w pozycji 1
lst.count('b')                  # 6 --> liczy elementy b
lst.index('b')                  # 7 --> podaje indeks pierwszego wystapienia elementu b
lst.index('z')                  # 8 (błąd) --> wyświetla komunikat: 'z' nie wystęuje w liście
lst.reverse()                   # 9 --> podaje elementy listy od końca
lst.sort()                      # 10 --> układa elementy listy w kolejności alfabetycznej
lst.sort(reverse=True)          # 11 --> układa elementy w kolejności alfabetycznej od końca
```

## Zad. 5
Przyporządkuj odpowiednie wyrażnie po prawej do odpowiedniej strzałki.
lst = [1, 3, 4, 5]
lst.pop
#3--> [1,3,4]
lst = lst + [5,3]
#5--> [1, 3, 4, 5, 3]
lst.reverse()
#1--> [3, 5, 4, 3, 1]
lst.remove(5)
#6--> [3, 4, 3, 1]
lst.sort()
#2--> [1, 3, 3, 4]
lst.append(4)
#4--> [1, 3, 3, 4, 4]



## Zad. 6
Czy poniższy kod zmodyfikuje listę `lst`?

```python
lst = [1, 2, 3]
for number in lst:
    number += 10
```
Powyższy kod nie zmodyfikuje listy.

## Zad. 7
Czy poniższy kod zmodyfikuje listę `lst`?

```python
lst = [1, 2, 3]
for i in range(len(lst)):
    lst[i] += 10
```
Tak, kod zmodyfikuje listę lst = [11, 12, 13]. Wartości listy zostaną zwiększone o 10

## Zad. 8
Podaj wynik poniższego kodu:

```python
lst1 = ['a', 'b', 'c']
lst2 = []
for letter in lst1:
    lst2.append(letter)
print(lst1) --> ['a', 'b', 'c']
print(lst2) --> ['a', 'b', 'c']
```

## Zad. 9
Napisz kod, który użyje pętli *for* i z listy `minutes = [2, 4, 1]` wygeneruje **nową** listę sekund `[120, 240, 60]` .

minutes = [2,4,1]
seconds = []
for mi in minutes:
    seconds.append(mi * 60)
print(minutes)
print(seconds)

## Zad. 10
Napisz kod, który użyje pętli *for* i przekształci **istniejącą** listę `minutes = [2, 4, 1]` w `[120, 240, 60]`.

minutes = [2,4,1]
for mi in range(len(minutes)):
    minutes[mi] *= 60

## Zad. 11
Rozszyfruj co robią poniższe funkcje `max`, `min` i `sum`:

```python
nums = [3, 7, 1, 5, 4]
print(max(nums)) --> zwraca wartość maksymalną listy
print(min(nums)) --> zwraca wartość minimalną
print(sum(nums)) --> zwraca sumę wartości
```

## Zad. 12
W jednej linii kodu (*one-liner*) oblicz średnią arytmetyczną z liczb w liście `nums` poprzedniego zadania.
print(sum(nums) /5)

## Zad. 13
Czy różni się funkcja `list()` od metody `split()`?

```python
word = 'Bioinformatics'
lst = list(word)
print(lst)
```

```python
word = 'B i o i n  f\t o r m\na t i c s'
lst = word.split()
print(lst)

word = 'Bio-informatics'
lst = word.split('-')
print(lst)
```
Fukcja list() tworzy listę, która powstaje z elementów zawartej w zmiennej np. "lst".
Metoda split() tworzy listę zawierającą elementy występujące w ciągu, domyślnie elementami listy zostają ciągi znaków oddzielone od siebie białymi znakami.
Natomiast jeśli zdefiniujemy parametr to jego wartość będzie stanowiła kryterium tworzenia elementów listy np. word.split('-') nowe elementy listy będą powstawać po wystąpieniu tego znaku.

## Zad. 14
Do czego służy metoda `join()`?

```python
lst = ['My', 'name', 'is', 'John']
string = '-'.join(lst)
print(string)

string = ' '.join(lst)
print(string)

string = ''.join(lst)
print(string)
```
Metoda join() łączy wszystkie elementy listy w ciąg znaków.


## Zad. 15
Napisz kod, który obliczy średnią długość wyrazu w poniższym zdaniu.

```python
text = "The Wellcome Trust Sanger Institute is a world leader in genome research."
```

Output:

```
Mean word size: 5.1
```
text = "The Wellcome Trust Sanger Institute is a world leader in genome research."
length_words = 0
total_words = 0
words = text.replace(".", '').split()

for word in words:
    length_words += len(word)
    total_words += 1

average = length_words / total_words

print(f'Mean word size: {average:.1f}')


## Zad. 16
Wyjaśnij, co robią poniższe dwie instrukcje.


```python
codons = [['TGA', 'TAA', 'TAG'], ['GAA', 'GAG'], ['TGG'], []]

# Instrukcja 1 (czytelna)
for lst in codons:
    for codon in lst:
        print(codon)

print()                            # Pusta linia dla rozdzielenia obu instrukcji

# Instrukcja 2 (mniej czytelna)
for i in range(len(codons)):
    lst = codons[i]
    for j in range(len(lst)):
        print(lst[j])
```
Instrukcje wypisują wartości zawarte w tablicy dwuwymiarowej.

# Krotki (*tuples*)

## Zad. 17
Krotka, działa dokładnie tak jak lista, jednak nie może być modyfikowana w miejscu (jest **niemutowalna**).

```python
tup = ()                        # Pusta krotka
tup = tuple()                   # Pusta krotka
tup = ('a', )                   # Krotka 1-elementowa
tup = ('a', 'b', 'c', 'd')      # Krotka 4-elementowa
```

Sprawdź, czy krotki obsługują indeksowanie, wycinki i funkcję `len`.
Krotki obsługują indeksowanie, wycinki oraz fukcję len.
print(tup[0])
print(tup[1:3])
print(len(tup))


# Słowniki (*dictionaries*)

## Zad. 18
Słowniki są *nieuporządkowanymi* kolekcjami obiektów. Słowniki wiążą zbiór wartości z kluczami,
tak by element słownika można było pobrać za pomocą klucza, pod którym jest on przechowywany.

```python
d = {}                                          # Pusty słownik
d = dict()                                      # Pusty słownik

en2pl = {'hi': 'cześć', 'bye': 'na razie'}      # Słownik 2-elementowy
```

Którą z wartości wygeneruje poniższy kod?

```python
print(en2pl['hi'])
```

1. `'hi'`
2. `'cześć'`
3. `True`
4. `0`

Kod wygeneruje wartość 2.

## Zad. 19
Którą z wartości wygeneruje poniższy kod?

```python
en2pl = {'hi': 'cześć', 'bye': 'na razie'}
print(en2pl['cześć'])
```

1. `'hi'`
2. `'cześć'`
3. `0`
4. `Błąd`

Kod wygeneruje wartość 4.

## Zad. 20
Którą z wartości wygeneruje poniższy kod?

```python
en2pl = {'hi': 'cześć', 'bye': 'na razie'}
print(en2pl.get('hi'))
print(en2pl.get('hello'))
print(en2pl.get('hello', 'no translation'))
```

1. `'hi' Error 'no translation'`
2. `'cześć' None 'no translation'`
3. `None None 'no translation'`
4. `None 'hello' None`

Kod wygeneruje wartość 2.

## Zad. 21
Którą z wartości wygeneruje poniższy kod?

```python
en2pl = {'hi': 'cześć', 'bye': 'na razie'}
en2pl['thanks'] = 'dzięki'
print(en2pl['thanks'])
```

1. `'thanks'`
2. `'dzięki'`
3. `None`
4. `Error`

Kod wygeneruje wartość 2.

## Zad. 22
Wyjaśnij, co robi poniższy kod:

```python
en2pl = {'hi': 'cześć', 'bye': 'na razie', 'thanks': 'dzięki'}

for key in en2pl:
    print(key, en2pl[key])
```
Pętla for iteruje po kluczach w słowniku i wypisuje na ekran klucz oraz jego wartość.

## Zad. 23
Co zwracają poniższe trzy metody działające na słowniku.

```python
en2pl = {'hi': 'cześć', 'bye': 'na razie', 'thanks': 'dzięki'}
print(en2pl.keys()) --> wypisuje klucze
print(en2pl.values()) --> zwraca wartośći poszczególnych kluczy
print(en2pl.items()) --> wypisuje wszystkie elementy słownika (klucze oraz ich wartości)
```


## Zad. 24
Wyjaśnij, co robi poniższy kod:

```python
en2pl = {'hi': 'cześć', 'bye': 'na razie', 'thanks': 'dzięki'}

for key, value in en2pl.items():
    print(key, value)
```
Kod wypisuje klucze oraz ich wartości.

## Zad. 25
Poniższy program zawiera **3 błędy**. Odszukaj je i popraw.

```python
d = {
    'alpha': [1, 2, 3],
    'beta': 'bioinfo'
    'gamma': 4,
    'delta': {'key': 'val'}
}

print(d['alpha'])

d['alpha'].append(4)

print(d['alpha'][4])

print(d['beta'][0])

print(d['delta']['val'])

```
d = {
    'alpha': [1, 2, 3],
    'beta': 'bioinfo',
    'gamma': 4,
    'delta': {'key': 'val'}
}

print(d['alpha'])

d['alpha'].append(4)

print(d['alpha'][0:4])

print(d['beta'][0])

print(d['delta']['key'])

## Zad. 26
Napisz program `molmass.py`, który w oparciu o poniższy słownik obliczy masę molową (kDa) sekwencji białkowej
wprowadzonej przez użytkownika.

Masa molowa sekwencji białkowej to suma mas wszystkich aminokwasów znajdujących się w sekwencji. Jeżeli
sekwencja użytkownika zawiera znak, którego nie ma w słowniku `protein_weights` to przyjmij,
że masa molowa tego znaku to `0`. Na przykład, masa molowa sekwencji
`MKSX` jest równa 149.2113 + 146.1876 + 105.0926 + 0 = 400.4915

```python
protein_weights = {
   'A': 89.0932,
   'C': 121.1582,
   'D': 133.1027,
   'E': 147.1293,
   'F': 165.1891,
   'G': 75.0666,
   'H': 155.1546,
   'I': 131.1729,
   'K': 146.1876,
   'L': 131.1729,
   'M': 149.2113,
   'N': 132.1179,
   'O': 255.3134,
   'P': 115.1305,
   'Q': 146.1445,
   'R': 174.201,
   'S': 105.0926,
   'T': 119.1192,
   'U': 168.0532,
   'V': 117.1463,
   'W': 204.2252,
   'Y': 181.1885
}
```
protein_weights = {
   'A': 89.0932,
   'C': 121.1582,
   'D': 133.1027,
   'E': 147.1293,
   'F': 165.1891,
   'G': 75.0666,
   'H': 155.1546,
   'I': 131.1729,
   'K': 146.1876,
   'L': 131.1729,
   'M': 149.2113,
   'N': 132.1179,
   'O': 255.3134,
   'P': 115.1305,
   'Q': 146.1445,
   'R': 174.201,
   'S': 105.0926,
   'T': 119.1192,
   'U': 168.0532,
   'V': 117.1463,
   'W': 204.2252,
   'Y': 181.1885
}
data = input("Pass your sequence: ").upper()
key_lst = list(data)
mass = 0

for key in key_lst:
    if key in protein_weights.keys():
        mass += protein_weights[key]
print(f'Mol mass = {mass:.4f}')


## Zad. 27
Utwórz program `translate.py`, który w oparciu o poniższy słownik kodonów dokona translacji sekwencji DNA na sekwencję białka.

```python
codons = {
    'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M', 'ACA': 'T',
    'ACC': 'T', 'ACG': 'T', 'ACT': 'T', 'AAC': 'N', 'AAT': 'N',
    'AAA': 'K', 'AAG': 'K', 'AGC': 'S', 'AGT': 'S', 'AGA': 'R',
    'AGG': 'R', 'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',
    'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P', 'CAC': 'H',
    'CAT': 'H', 'CAA': 'Q', 'CAG': 'Q', 'CGA': 'R', 'CGC': 'R',
    'CGG': 'R', 'CGT': 'R', 'GTA': 'V', 'GTC': 'V', 'GTG': 'V',
    'GTT': 'V', 'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
    'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E', 'GGA': 'G',
    'GGC': 'G', 'GGG': 'G', 'GGT': 'G', 'TCA': 'S', 'TCC': 'S',
    'TCG': 'S', 'TCT': 'S', 'TTC': 'F', 'TTT': 'F', 'TTA': 'L',
    'TTG': 'L', 'TAC': 'Y', 'TAT': 'Y', 'TAA': '*', 'TAG': '*',
    'TGC': 'C', 'TGT': 'C', 'TGA': '*', 'TGG': 'W'
}
```

```
Enter DNA sequence: ATGTACTCTCTAGCGTGA
```

Output:

```
MYSLA*
```
codons = {
    'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M', 'ACA': 'T',
    'ACC': 'T', 'ACG': 'T', 'ACT': 'T', 'AAC': 'N', 'AAT': 'N',
    'AAA': 'K', 'AAG': 'K', 'AGC': 'S', 'AGT': 'S', 'AGA': 'R',
    'AGG': 'R', 'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',
    'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P', 'CAC': 'H',
    'CAT': 'H', 'CAA': 'Q', 'CAG': 'Q', 'CGA': 'R', 'CGC': 'R',
    'CGG': 'R', 'CGT': 'R', 'GTA': 'V', 'GTC': 'V', 'GTG': 'V',
    'GTT': 'V', 'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
    'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E', 'GGA': 'G',
    'GGC': 'G', 'GGG': 'G', 'GGT': 'G', 'TCA': 'S', 'TCC': 'S',
    'TCG': 'S', 'TCT': 'S', 'TTC': 'F', 'TTT': 'F', 'TTA': 'L',
    'TTG': 'L', 'TAC': 'Y', 'TAT': 'Y', 'TAA': '*', 'TAG': '*',
    'TGC': 'C', 'TGT': 'C', 'TGA': '*', 'TGG': 'W'
}

seq = input('Pass sequence: ').upper()
protein = ''

if len(seq) % 3 == 0:
    for i in range(0, len(seq), 3):
        codon = seq[i : i + 3]
        protein += codons[codon]
    print(protein)

## Zad. 28
Krótko wyjaśnij, co robi poniższy kod?


```python
seq = 'MNNGGKAEKENTPSE'

d = {}
for char in seq:
    if char not in d:
        d[char] = 0
    d[char] += 1
print(d)
```
Tworzy słownik, w którym wartościami jest liczba wystąpień danej litery w ciągu znaków

## Zad. 29
Napisz kod, który wykorzysta słownik żeby wyświetlić liczbę wystąpień każdego wyrazu w poniższym tekście.


```python
text = 'The first rule of Fight Club is you do not talk about Fight Club'
```

Output:

```
1   The
1   first
1   rule
1   of
2   Fight
2   Club
1   is
1   you
1   do
1   not
1   talk
1   about
```
text = 'The first rule of Fight Club is you do not talk about Fight Club'
text = text.split()
count_words= []

for i in text:
    if i not in count_words:
        count_words.append(i)
for i in range(0, len(count_words)):
    print(f'{text.count(count_words[i])}  {count_words[i]}') 
    
# Zbiory (*sets*)

## Zad. 30
Zbiór to *nieuporządkowana* kolekcja unikalnych i niemutowalnych obiektów, obsługująca działania odpowiadające matematycznej teorii zbiorów.

```python
myset = set()                     # Pusty zbiór
myset = {'A', 'T', 'G', 'C'}      # Zbiór 4-elementowy
```

Sprawdź co zrobi każde wyrażenie ze zbiorem w środku (`s`).

![set1.png](../images/set.png)


## Zad. 31
Ile elementów będzie miał poniższy zbiór:

```python
nucl = {'A', 'A', 'T', 'T', 'G', 'G', 'C', 'C'}
print(nucl)
```

## Zad. 32
Które z poniższych sposobów tworzenia zbioru są prawidłowe?

1. `set()`
2. `set('AATTGGCC')`
3. `set(['A', 'T', 'G'])`
4. `{'A', 'T', 'G', 'C'}`


## Zad. 33
Które z poniższych wyrażeń są nieprawidłowe?

```python
s = {'A', 'T', 'G', 'C'}
```

1. `len(s)`
2. `s.add('G')`
3. `'G' in s`
4. `'G' not in s`
5. `s[0]`
6. `s['A']`
7. `s.remove('C')`


## Zad. 34
Co otrzymasz w wyniku poniższych działań matematycznych:

```python
dna = set('ATGC')
rna = set('AUGC')
```

1. `dna - rna` lub `dna.difference(rna)`
2. `dna | rna` lub `dna.union(rna)`
3. `dna & rna` lub `dna.intersection(rna)`
4. `dna ^ rna` lub `dna.symmetric_difference(rna)`


## Zad. 35
Jaką wartość boolean (`True`/`False`) otrzymasz w wyniku działania poniższych metod:

```python
nuc = set('ATGCU')
dna = set('ATGC')
```

1. `dna.issubset(nuc)` lub `dna <= nuc`
2. `nuc < dna`
3. `nuc <= nuc`
4. `nuc.issuperset(dna)` lub `nuc >= dna`
5. `nuc == dna`


## Zad. 36
Które z poniższych konwersji typów obiektów są prawidłowe?

1. `list({1, 2, 3})`
2. `set([1, 2, 3])`
3. `tuple([1, 2, 3])`
4. `list((1, 2, 3))`
5. `set((1, 2, 3))`


## Zad. 37
Utwórz *one-liner*, który zwróci listę wspólnych elementów dwóch list:

```python
lst1 = [1, 3, 6, 78, 35, 55]
lst2 = [12, 24, 35, 24, 88, 120, 155]
```


## Zad. 38
Która z poniższych instrukcji jest prawidłowa?

```python
dna_dic = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}        # Słownik
rna_set = {'A', 'U', 'G', 'C'}                        # Zbiór
```

1. `dna_dic.intersection(rna_set)`
2. `rna_set.intersection(dna_dic)`
3. `rna_set.union(dna_dic)`
4. `dna_dic.union(rna_set)`


## Zad. 39
Czy działania na zbiorach można wykonywać dla więcej niż dwóch zbiorów?

```python
s1 = {'Gene1', 'Gene2', 'Gene3'}
s2 = {'Gene2', 'Gene3', 'Gene4', 'Gene5'}
s3 = {'Gene6', 'Gene2', 'Gene7', 'Gene3'}
```

Np.:

```python
s1 & s2 & s3
s1.intersection(s2, s3)
```


## Zad. 40
Napisz program `common_aa.py`, który poprosi użytkownika o wpisanie dwóch sekwencji białkowych i wyświetli w porządku alfabetycznym wszystkie wspólne aminokwasy między sekwencjami.

```
Enter 1st protein sequence: MKSTGYWTRSFVCDH
Enter 2nd protein sequence: MGTYWSSQEG
```


Wynik:

```python
['G', 'M', 'S', 'T', 'W', 'Y']
```
