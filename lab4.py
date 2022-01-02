# Funkcje

## Zad. 1
Na czym polega różnica między poniższymi dwoma funkcjami?

```python
def hello(name):
    print(f'Hello {name}!')

greeting = hello('John')
print(greeting)
```

```python
def hello(name):
    return f'Hello {name}!'

greeting = hello('John')
print(greeting)
```
W drugiej funkcji polecenie print zostało zastąpione poleceniem return,
które zwraca przypisaną wartość do fukncji, którą można przypisać do zmiennej.
Polecenie return także kończy wywoływanie funkcji i zwraca wynik.

## Zad. 2
Poniżej znajduje się kod, który oblicza skład nukleotydów `GC` w sekwencji DNA znajdującej się pod
zmienną `dna`. W oparciu o ten kod utwórz funkcję `gc_content`, która jako argument będzie
przyjmowała dowolny łańcuch znaków i zwracała liczbę zmiennoprzecinkową.

```python
dna = "ACTGACTCGATTACGTCCGATAGTA"

dna = dna.upper()
c_count = dna.count('C')
g_count = dna.count('G')
gc_content = (c_count + g_count) / len(dna)
```

Output:

```python
print(gc_content('ACGGTAGTCGATG'))      # 0.5384615384615384
print(gc_content('ATAT'))               # 0.0
print(gc_content(dna='ATGC'))           # 0.5
```
dna = "ACTGACTCGATTACGTCCGATAGTA"

def gc_content(dna):
    dna = dna.upper()
    c_count = dna.count('C')
    g_count = dna.count('G')
    gc_content = (c_count + g_count) / len(dna)
    return gc_content

print(gc_content('ACGGTAGTCGATG'))     # 0.5384615384615384
print(gc_content('ATAT'))              # 0.0
print(gc_content(dna='ATGC'))          # 0.5

## Zad. 3
Zapoznaj się z poniższym kodem dotyczącym funkcji `zip()`.

```python
>>> string1 = 'abc'
>>> string2 = '123'
>>> for char1, char2 in zip(string1, string2):
...     print(char1, char2)
...
a 1
b 2
c 3
```

Następnie utwórz funkcję `hamming_distance`, która przyjmuje jako argumenty dwie sekwencje równej długości i
obliczy między nimi [dystans Hamminga](https://pl.wikipedia.org/wiki/Odległość_Hamminga) - liczba miejsc (pozycji),
na których dwie sekwencje się różnią.


Input:

```python
seq1 = 'GAGCCTACTAACGGGAT'
seq2 = 'CATCGTAATGACGGCCT'
distance = hamming_distance(seq1, seq2)
print(distance)
```

Output:

```
7
```
seq1 = 'GAGCCTACTAACGGGAT'
seq2 = 'CATCGTAATGACGGCCT'

def hamming_distance(seq1, seq2):
    distance = 0
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            distance += 1
    return distance
print(hamming_distance(seq1, seq2))

## Zad. 4
Które zdanie jest nieprawdziwe?

```python
def multiply(a, b=2, c=3):
    return a * b * c
```

1. `multiply(1)` da `6` --> prawdziwe
2. `multiply(a=1)` da `6` --> prawdziwe
3. `multiply(1, 4)` da `12` --> prawdziwe
4. `multiply(1, 4, 5)` da `20` --> prawdziwe
5. `multiply(1, c=4)` da `8` --> prawdziwe
6. `multiply(1, c=4, b=2)` da `8` --> prawdziwe
7. `multiply(b=2, c=3)` da `6` --> nieprawdziwe


## Zad. 5
Python pozwala tworzyć funkcje, które przyjmują dowolną liczbę argumentów. Zapoznaj się z poniższym kodem.

```python
                              # Operator * zbiera wszystkie argumenty w krotkę.
def multiply(*args):          # *args oznacza, że funkcja oczekuje 0 lub więcej argumentów.
    print(args)               # Zmienna args jest krotką argumentów.

multiply(1)                   # (1,)
multiply(1, 2, 3)             # (1, 2, 3)
multiply()                    # ()
```

Następnie dopisz instrukcje wewnątrz funkcji `multiply()`, aby obliczała iloczyn liczb w krotce.

Output:

```python
print(multiply(2, 3, 4))      # 24
print(multiply(1))            # 1
print(multiply(1, 1, 1, 7))   # 7
```
def multiply(*args):
    i = 1
    for numbers in args : i *= numbers
    return i

print(multiply(2, 3, 4))      # 24
print(multiply(1))            # 1
print(multiply(1, 1, 1, 7))   # 7

## Zad. 6
Operator `**` jest podobny do `*`, jednak działa tylko dla argumentów funkcji ze słowami kluczowymi i zbiera je w
słownik.

```python
def profile(**kwargs):
    print(kwargs)

profile(name='John', age=26, job='programmer')
# {'name': 'John', 'age': 26, 'job': 'programmer'}
```

Dopisz instrukcje do funkcji `profile`, aby w pętli `for` wyświetliła poniższy wynik:

```
name  John
age   26
job   programmer
```
def profile(**kwargs):
    for kv in kwargs.items():
        print(kv[0], '\t', kv[1])
profile(name='John', age=26, job='programmer')

## Zad. 7
Operatory `*` i `**` można również użyć podczas **wywoływania** funkcji.
Zapoznaj się z poniższym kodem i krótko wyjaśnij, do czego służą te operatory w kontekście wywołania funkcji.

```python
def multiply(a, b, c):
    return a * b * c

numbers = [1, 2, 3]
print(multiply(*numbers))             # 6
```
Operator * zmienia argumenty funckji w krotkę, co wskazuje na to, że zmienna jest krotką argumentów.

```python
def multiply(a, b, c):
    return a * b * c

numbers = {'a': 1, 'b': 2, 'c': 3}
print(multiply(**numbers))            # 6
```
Operator ** zmienia argumenty funcji w słownik.

## Zad. 8
Poniższa funkcja powinna zliczać w sekwencji występowanie wszystkich podsekwencji danej długości.
Zwróc uwagę, że funkcja ma bardzo dobrą dokumentację (podobny styl stosuje firma *Google*).
Niestety funkcja zawiera **jeden błąd**, przez który nie są zliczane wszystkie podsekwencje.
Zlokalizuj błąd i napraw kod.

```python
def word_count(seq, word_size=2):
    """Count words of given size in DNA sequence

    Args:
        seq (str)       : DNA sequence
        word_size (int) : Word size (k-mer size)

    Returns:
        Dictionary with word/k-mer counts

    Example:
        >>> word_count('ATGCTCGTAGTAGATAG')
        {'AT': 2, 'TG': 1, 'GC': 1, 'CT': 1,
         'TC': 1, 'CG': 1, 'GT': 2, 'TA': 3,
         'AG': 3, 'GA': 1}
    """
    d = {}
    for i in range(len(seq) - word_size):
        word = seq[i:i+word_size]
        if word not in d:
            d[word] = 0
        d[word] += 1
    return d


print(word_count('ATGCT', 2))
```
  d = {}
    for i in range(len(seq) - word_size+1):
        word = seq[i:i+word_size]
        if word not in d:
            d[word] = 0
        d[word] += 1
    return d


print(word_count('ATGCT', 2))

## Zad. 9
Zapoznaj się z poniższym kodem i następnie utwórz funkcję `mutate()`,
która w sekwencji DNA wprowadzi jedną losową *substytucję* nukleotydu na losowej pozycji.


```python
import random

print(random.randint(1, 3))               # Zwraca liczbę całkowitą 1 lub 2 lub 3
print(random.choice(['Head', 'Tails']))   # Zwraca orła lub reszkę.
```

Output:

```python
mutate('ATGG')      # ACGG
mutate('ATG')       # TTG
mutate('AT')        # AA
mutate('ATGCGTGA')  # GTGCGTGA
mutate('ATG')       # ATG (nukleotyd może się nie zmienić)
```
import random
def mutate(dna):
    dna_list = list(dna)
    mutation = random.randint(0, len(dna_list) - 1)
    dna_list[mutation] = random.choice(list('ATGC'))
    return ''.join(dna_list)
print(mutate('ATGCGTGA'))

## Zad. 10
Utwórz funkcję `complement`, która przyjmuje sekwencję DNA i zamienia ją na sekwencję komplementarną.

Input:

```python
print(complement('ACTG'))
```

Output:

```
TGAC
```
seq = 'ACTG'
def complement(seq):
    complement = {'A' : 'T', 'T' : 'A', 'C' : 'G', 'G' : 'C'}
    return ''.join([complement[i] for i in seq])
print(complement(seq))

## Zad. 11
Utwórz funkcję `reverse_complement`, która przyjmuje sekwencję DNA i wywołuje funkcję `complement`, aby zwrócić sekwencję odwrotnie komplementarną.

Input:

```python
print(reverse_complement('ACTG'))
```

Output:

```
CAGT
```
seq = 'ACTG'
def complement(seq):
    complement = {'A' : 'T', 'T' : 'A', 'C' : 'G', 'G' : 'C'}
    return ''.join(reversed([complement[i] for i in seq]))
print(complement(seq))

## Zad. 12
Miejsce w kodzie, w którym przypisujemy zmienną ma znaczenie, w jakim zakresie ta zmienna jest widoczna.
Ile wynosi `x` w miejscu pierwszego i drugiego wyrażenia `print(x)`?

```python
x = 99             # Zmienna widoczna w całym pliku, również wewnątrz func().

def func():
    x = 88         # Zmienna widoczna jedynie wewnątrz funkcji func().
    print(x) # --> 88

func()
print(x) # --> 99
```

> W Pythonie jest tzw. reguła `LEGB`, która pozwala nam zrozumieć zasięgi zmiennych.
Reguła ta jest doskonale wytłumaczona na https://youtu.be/QVdf0LgmICw (20 min).


# Generatory

## Zad. 13
Jaka jest różnica w działaniu poniższych dwóch funkcji?

> Jeżeli potrzebujesz przypomnieć sobie generatory: https://youtu.be/bD05uGo_sVI (11 min).

```python
def sqrange1(n):
    lst = []
    for number in range(n):
        lst.append(number ** 2)
    return lst
```

```python
def sqrange2(n):
    for number in range(n):
        yield number ** 2
```
Obie fukncje zwracają taki sam wynik, ale funkcja 2, która jest generatorem wykona się szybciej oraz zajmie mniej pamięci.

## Zad. 14
Utwórz funkcję generatora `random_codon(n)`, która generuje *n* losowych kodonów.

Output:

```python
for codon in random_codon(5):
    print(codon)

# AGA
# TAT
# CAG
# ATG
# CCG
```
import random

letters = ['a' , 't', 'g', 'c']
def random_codon(n):
    ran = ''.join((random.choice(letters) for x in range(n)))
    res = list(ran)
    final = ''.join(res)
    return final
n = int(input('pass the length: '))
print(random_codon(n))

# Listy składane (*list comprehension*)

## Zad. 15
Poniżej znajduje się kod, który zamienia minuty na sekundy tworząc nową listę w tradycyjny sposób.

```python
minutes = [2, 3, 1, 5, 6]

seconds = []
for m in minutes:
    seconds.append(m * 60)
print(seconds)                # [120, 180, 60, 300, 360]
```

Ten sam wynik można uzyskać za pomocą alternatywnej składni tworzenia list, która nazywa się ***składaniem list*** (*list comprehensions*).

```python
minutes = [2, 3, 1, 5, 6]
seconds = [m * 60 for m in minutes]
```

Użyj listy składanej, aby do każdego genu na liście `genes` dodać przedrostek `Hs` (*Homo sapiens*).

```python
genes = ['foxp2', 'GW182', 'not1', 'disc1', 'BRCA1']
```

Output:

```python
['Hsfoxp2', 'HsGW182', 'Hsnot1', 'Hsdisc1', 'HsBRCA1']
```
genes = ['foxp2', 'GW182', 'not1', 'disc1', 'BRCA1']
hs = ['Hs' + m for m in genes]
print(hs)

## Zad. 16
> Listy składane działają przynajmniej **dwa razy szybciej** od ręcznie zapisanych instrukcji pętli `for`,
ponieważ ich iteracje wykonywane są wewnątrz interpretera Pythona z szybkością języka C, a nie z szybkością kodu Pythona.

Użyj listy składanej, aby utworzyć listę kwadratów pierwszych 10 liczb całkowitych.

Output:

```python
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```
numbers = [0, 1 , 2, 3, 4, 5, 6, 7, 8, 9]
power = [n ** 2 for n in numbers]
print(power)

## Zad. 17
> Z technicznego punktu widzenia listy składane są konskrukcją całkowicie opcjonalną, ponieważ zawsze możemy
zbudować listę wyników tradycyjnie. Listy składane mają jednak bardziej zwięzły zapis, a ponieważ
ten wzorzec kodu budowania list wyników jest w Pythonie tak często spotykany, w wielu kontekstach
okazują się bardzo przydatne.

Użyj listy składanej, aby zamienić poniższą listę stringów liczb na liczby całkowite.

```python
nums = ['1', '100', '2', '3']
```

Output:

```python
[1, 100, 2, 3]
```
nums = ['1', '100', '2', '3']
conv = [int(n) for n in nums]
print(conv)

## Zad. 18
W listach składanych można umieszczać klauzulę `if`, co pozwala na *odfiltrowanie* tych elementów wyników,
dla których warunek nie jest prawdziwy.

```python
# Odfiltrowanie liczb nieparzystych:
numbers = [2, 3, 1, 5, 6, 100, 3, 9]
numbers_even = [num for num in numbers if num % 2 == 0]    # [2, 6, 10]
```

Użyj listy składanej, aby z poniższej listy utworzyć listę liczb parzystych większych od 10.

```python
input_list = [4, 50, 51, 10, 21, 5, 11, 12, 16]
```

Output:

```python
[50, 12, 16]
```
numbers = [4, 50, 51, 10, 21, 5, 11, 12, 16]
numbers_even = [num for num in numbers if num % 2 == 0 and num > 10]
print(numbers_even)

## Zad. 19
Poniższa funkcja `complement` przyjmuje sekwencję DNA i zamienia ją na sekwencję komplementarną.
Zmodyfikuj tę funkcję stosując składnię listy składanej.


```python
def complement(dna):
    """Return a complementary DNA sequence"""
    d = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    cdna = []
    for nt in dna.upper():
        cdna.append(d.get(nt, 'N'))
    return "".join(cdna)
```
def complementary(dna):
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    return ''.join([complement[base] for base in dna])
print(complementary('ATGC'))

## Zad. 20
> Listy składane są przeznaczone do prostych instrukcji, nie należy ich nadużywać. Szybko mogą się one stać niezrozumiałe kiedy używamy wielu poziomów zagnieżdżeń.

Oprócz list składanych możemy również składać **słowniki** i **zbiory**. Nie możemy składać krotek (dowiesz się dlaczego w kolejnym zadaniu).

```python
# Składanie zbioru
gene_lst = ['foxp2', 'GW182', 'foxp2', 'disc1', 'gw182']
gene_set = {gene.upper() for gene in gene_lst}

print(gene_set)
# {'GW182', 'DISC1', 'FOXP2'}
```

```python
# Składanie słownika
gene_lst = ['foxp2', 'GW182', 'foxp2', 'disc1', 'gw182']
gene_dic = {gene.upper(): gene for gene in gene_lst}

print(gene_dic)
# {'FOXP2': 'foxp2', 'GW182': 'gw182', 'DISC1': 'disc1'}
```

Z poniższych dwóch list utwórz słownik, w którym nie będzie Batmana.

```python
names = ['Bruce', 'Clark', 'Peter']
heros = ['Batman', 'Superman', 'Spiderman']
```

Output:

```python
{'Clark': 'Superman', 'Peter': 'Spiderman'}
```
names = ['Bruce', 'Clark', 'Peter']
heros = ['Batman', 'Superman', 'Spiderman']
names.remove('Bruce')
heros.remove('Batman')
dictionary = {names[i] : heros[i] for i in range(len(names))}
print(dictionary)

## Zad. 21
Proste generatory można budować za pomocą **wyrażenia generatorów**, które składniono wygląda tak samo jak listy składane, z tym że zamiast nawiasów kwadratowych stosuje się nawiasy okrągłe.

```python
lst = [x ** 2 for x in range(10)]    # Lista składana: zwraca listę
gen = (x ** 2 for x in range(10))    # Wyrażenie generatora: zwraca obiekt iterowalny

print(lst)                           # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(gen)                           # <generator object <genexpr> at 0x102b8af90>
```

Jaką funkcję należy użyć na `gen` żeby dostać listę wszystkich wyników?
Należy użyć funkcji list()
gen_lst = list(gen), dzięki czemu otrzymamy całą listę wszystkich wyników.

## Zad. 22 (dla chętnych)
Bakterie wykorzystują enzymy restrykcyjne do walki z wirusami. Enzymy restrykcyjne rozpoznają w sekwencjach genomów wirusów palindromowe sekwencje DNA długości od 4 do 12
nukleotydów i w tych miejscach przeprowadzają rozcięcie cząsteczek wirusa.

Przykładową sekwencją palindromową jest `GATATC`, ponieważ jej sekwencja odwrotnie komplementarna to `GATATC`.

![palindrome](../images/palindrome.jpg)

Utwórz funkcję `restriction_sites`, która przyjmuje dwa argumenty - sekwencję DNA i długość palindromowej sekwencji, następnie w zadanej sekwencji zidentyfikuje pozycje początku i końca
wszystkich palindromowych sekwencji o podanej długości.

> Wskazówka: Niech funkcja `restriction_sites` skorzysta z już istniejącej funkcji `reverse_complement`.

Input:

```python
restriction_sites('TCAATGCATGCGGGTCTATATGCAT', size=4)
```

Output:

```python
[
  [5, 8, 'TGCA'],
  [7, 10, 'CATG'],
  [17, 20, 'TATA'],
  [18, 21, 'ATAT'],
  [21, 24, 'TGCA']
]
```

## Zad. 23 (dla chętnych)
<img align="right" src="../images/book-blindwatchmaker.jpg" alt="BlindWatchmaker" height="270px"> W książce "Ślepy zegarmistrz" Richard Dawkins zaprezentował symulację komputerową, która przedstawia działanie doboru naturalnego w zakresie tworzenia złożonych form biologicznych poprzez losowe mutacje. Symulacja zaczyna się od przypadkowej sekwencji liter i stopniowo przekształca się w sentencję z sztuki *Hamlet* **METHINKS IT IS LIKE A WEASEL** (*Zdaje mi się, że jest podobniejsza do łasicy*).

Napisz program `weasel.py`, który przeprowadzi procedurę Dawkinsa:

1. Wygeneruj losową sekwencję długości 28 znaków (alfabet: 26 liter i spacja).
2. Utwórz 100 kopii tej sekwencji (*reprodukcja*).
3. W każdej kopii sekwencji w jednym losowym miejscu zastąp znak innym przypadkowym znakiem z alfabetu (*mutacja*).
4. Określ, która z 100 kopii sekwencji jest najbardziej zbliżona do docelowej sekwencji METHINKS IT IS LIKE A WEASEL. W tym celu możesz obliczyć dystans Hamminga (liczbę pozycji w sekwencji niezgodnych z sekwencją docelową).
5. Zakończ program jeżeli któraś z 100 kopii sekwencji jest identyczna do hamletowskiej sentencji. W przeciwnym przypadku, wybierz jedną sekwencję, która wykazuje największe podobieństwo i przejdź do kroku 2.

Przykładowy output:

```
TATTIYAKXWTXTFTDXQHOFOYLPTLN  1
TATTIYAK WTXTFTDXQHOFOYLPTLN  2
TATTIYAK WTXTFTDXQHOF YLPTLN  3
TATTIYAK WTXTFTDXQEOF YLPTLN  4
TATTIYAK WTXTFTDXQE F YLPTLN  5
MATTIYAK WTXTFTDXQE F YLPTLN  6
...
METHINKS IT IS LIKE A WEASEL  N
```

Odpowiedz na pytania:

1. Ile pokoleń potrzebnych jest do wygenerowania docelowej sekwencji?
2. Czy symulacja Dawkinsa trafnie odwzorowuje działanie ewolucji? (dla chętnych)
