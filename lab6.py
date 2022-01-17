# Moduł [itertools](https://docs.python.org/3/library/itertools.html)

> Zestaw szybkich i wydajnych w pamięci generatorów związanych z iteracjami (np. permutacje, kombinacje).

## Zad. 1
Wyjaśnij, co robią poniższe dwie pętle `for`:

```python
import itertools

for pair in itertools.combinations(['A', 'B', 'C', 'D'], 2):
    g1 = pair[0]
    g2 = pair[1]
    print(g1, g2)
```
Wypisanie dwuliterowych kombinacji bez powtórzeń.

```python
for g1, g2, g3 in itertools.combinations('ABCD', 3):
    print(g1, g2, g3)
```
Wypisanie trzyliterowych kombinacji bez powtórzeń.

## Zad. 2
Na przyjęcie urodzinowe przyszło 10 osób i wszyscy zaczynają się witać między sobą. Użyj funkcji `combinations`
żeby odpowiedzieć na pytanie, ile będzie wszystkich przywitań (podań ręki)?

import itertools

hand = 0
for g1 in itertools.combinations('0123456789', 2):
    hand += 1
print('Ilość powitań: ',hand)


## Zad. 3
Użyj funkcji `combinations` aby obliczyć dystans Hamminga pomiędzy każdą parą sekwencji w słowniku `SEQUENCES`.
Dodaj również kod, który wskażę parę sekwencji o najmniejszym dystansie.

```python
import itertools

def hamming_distance(seq1, seq2):
    return sum([1 for n1, n2 in zip(seq1, seq2) if n1 != n2])

SEQUENCES = {
    'seq1': 'ATCGTCGTAGAT',
    'seq2': 'GCTGCTGATAGT',
    'seq3': 'TATGATGAGTAG',
    'seq4': 'ATGATGATTTGG',
    'seq5': 'CCTGCTAATAGA',
    'seq6': 'TTAGATGATGCT',
    'seq7': 'AGCTGATGCGTG'
}

# Your code goes here.
```


## Zad. 4
Funkcja `permutations` zwraca permutacje przekazanej sekwencji. Na ile różnych sposób można usadzić 10 osób przy stole?

```python
import itertools

nucleotides = ['A', 'T', 'G']

for tup in itertools.permutations(nucleotides):
    print(tup)

# ('A', 'T', 'G')
# ('A', 'G', 'T')
# ('T', 'A', 'G')
# ('T', 'G', 'A')
# ('G', 'A', 'T')
# ('G', 'T', 'A')
```


## Zad. 5
Z [dokumentacji modułu itertools](https://docs.python.org/3/library/itertools.html) wybierz odpowiednią *funkcję kombinatoryczną*, która uprości poniższe trzy zagnieżdżone pętle `for` do jednej pętli.

```python
lst1 = [1, 2, 3]
lst2 = ['a', 'b', 'c']
lst3 = ['A', 'B', 'C']

for v1 in lst1:
    for v2 in lst2:
        for v3 in lst3:
            print(v1, v2, v3)
```


# Moduł [random](https://docs.python.org/3/library/random.html)

> Generowanie pseudolosowych liczb i wartości z podanej sekwencji (np. listy, krotki).


## Zad. 6
Przyporządkuj wywołanie funkcji do odpowiedniej definicji.

Funkcje:

```python
import random

# a
print(random.random())

# b
print(random.uniform(1, 3))

# c
print(random.randint(1, 3))

# d
print(random.choice(['Head', 'Tails']))

# e
print(random.sample(['a', 'b', 'c'], 2))

# f
lst = ['a', 'b', 'c', 'd']
random.shuffle(lst)
print(lst)
```

Definicje:

1. Zwraca *k* losowych elementów z zadanej sekwencji.
2. Zwraca losowo wybrany element z zadanej sekwencji (np. listy czy łańcucha znaków).
3. Zmienia listę w miejscu poprzez losowe ułożenie jej elementów.
4. Zwraca losową liczbę zmiennoprzecinkową znajdującą się w przedziale [0, 1).
5. Zwracana losową liczbę zmiennoprzecinkową z zadnaego przez użytkownika przedziału [a, b].
6. Zwraca losową liczbę całkowitą z zadanego przez użytkownika przedziału [a, b].


## Zad. 7
Utwórz program `random_dna1.py`, który będzie generował losową sekwencję DNA o podanej przez użytkownika długości.

```python
length = int(input('Enter a DNA length: '))
```

Input:

```bash
python random_dna1.py
Enter a DNA length: 50
```

Output:

```
ATTGCTGATGATGAGTAGATCGTATAGGATTAGTAGAGATATGATAGAGC
```


# Moduł [sys](https://docs.python.org/3/library/sys.html)

> Polecenia związane z Pythonem i jego środowiskiem.

## Zad. 8
Moduł `sys` umożliwia m.in. przekazywanie argumentów podczas wywoływania programu.


```python
import sys

print(sys.argv)       # Lista argumentów
print(sys.argv[0])    # Nazwa wykonywanego programu
```

Utwórz program `random_dna2.py`, który będzie przyjmował od użytkownika długość sekwencji DNA jako argument (a nie za pomocą funkcji `input`).

Input:

```bash
python random_dna2.py 50
```

Output:

```
TCGTCGCTAGTAGCTGATGATCGATGCGCTGATCGCTGATGATCGTAGCG
```



# Moduł [os](https://docs.python.org/3/library/os.html)

> Pozwala uruchamiać z poziomu Pythona zewnętrzne programy (np. polecenia powłoki, programy napisane w C++, itd.).


## Zad. 9
Utwórz program `simulation.py`, który 1000 razy wykona program `random_dna2.py` dla sekwencji długości 20 nukleotydów.

```python
import os
os.system('python random_dna2.py 20')
```

Alternatywą dla modułu `os` jest moduł subprocess.

```python
# Moduł subprocess, podobnie jak os, umożliwia wykonywanie zewnętrznych
# programów z poziomu Pythona. Zaleta modułu subprocess to możliwość
# bezpośredniego wczytania outputu wykonywanego programu jako string.

import subprocess
process = subprocess.run(
    ['python', 'random_dna2.py', '20'],
    text=True, capture_output=True
)
print(process.stdout)
#print(process.stderr)
```

# Moduł [pathlib](https://docs.python.org/3/library/pathlib.html)

> Praca z plikami i katalogami oraz poruszanie się po drzewie katalogów i plików.


## Zad. 10
Sprawdź i wyjaśnij, co robi poniższy kod.

```python
import pathlib

directory = pathlib.Path('data')
directory.mkdir(exist_ok=True)

for i in range(10):
    file = directory.joinpath(f'file{i}.txt')
    oh = open(file, 'w')
    oh.write(file.name)
    oh.close()
```

## Zad. 11
Sprawdź i wyjaśnij, co robi poniższy kod.

```python
import pathlib

directory = pathlib.Path('data')

for file in directory.iterdir():
    print(file)
    print(file.name)
    print(file.stem)
    print(file.suffix)
    print()
```

## Zad. 12
Sprawdź i wyjaśnij, co robi poniższy kod.

```python
import pathlib

directory = pathlib.Path('data')
sub_directory = directory.joinpath('subdir')
sub_directory.mkdir(exist_ok=True)

for path in directory.iterdir():
    if path.is_file():
        print(f'Path is a file: {path}')
    if path.is_dir():
        print(f'Path is a directory: {path}')
```


## Zad. 13
Sprawdź i wyjaśnij, co robi poniższy kod.

```python
import pathlib

directory = pathlib.Path('data')
file = directory.joinpath('file11.txt')

if directory.exists():
    print('Directory exists.')
if file.exists():
    print('File exists.')
```

## Zad. 14
W skompresowanym pliku [human_proteins.zip](../data/human_proteins.zip) znajduje się katalog zawierający 250 sekwencji białkowych człowieka (każda sekwencja w osobnym pliku). Użyj modułu `pathlib`, aby otworzyć każdy z 250 plików i obliczyć średnią długość wszystkich sekwencji.

```python
import pathlib

# Your code goes here.
```

Output:

```
Mean sequence length: 628.1
```


# Moduł [urllib](https://docs.python.org/3/library/urllib.request.html#module-urllib.request)

> Służy do pobierania zasobów z internetu/sieci za pośrednictwem adresów URL.

## Zad. 15
Sprawdź i wyjaśnij, co robi poniższy kod.

```python
import urllib.request

f = urllib.request.urlopen('http://www.uniprot.org/uniprot/Q93062.fasta')
respond = f.read()
f.close()

print(respond)                    # Obiekt bajtowy
print(respond.decode('utf-8'))    # Łańcuch znaków (string)
```


## Zad. 16
Sprawdź i wyjaśnij, co robi poniższy kod.

```python
import urllib.request

f = urllib.request.urlopen('http://www.uniprot.org/uniprot/Q93062.fasta')
for line in f:
    line = line.decode('utf-8')
    if not line.startswith('>'):
        print(line)
f.close()
```

## Zad. 17
Utwórz skrypt `uniprot1.py`, który pobierze z bazy UniProt sekwencje białkowe (w formacie FASTA) dla podanych poniżej identyfikatorów i zapisze pobrane sekwencje do pliku `uniprot.txt`.

```python
import urllib.request

uniprot_ids = ['P68431', 'Q6ZQ08', 'O94687']

# Your code goes here.
```

## Zad. 18
Funkcja `sleep` modułu `time` powoduje, że program nic nie będzie robił przez podaną liczbę sekund.

```python
import time

for i in range(10):
    print(i)
    time.sleep(0.3)
```

W skrypcie `uniprot1.py` zadbaj o to, aby czas pomiędzy wykonywaniem instrukcji `urllib.request.urlopen` wynosił przynajmniej 1 sekundę.


# Moduł [argparse](https://docs.python.org/3/library/argparse.html)

> Służy do przekazywanie argumentów z wiersza poleceń.


## Zad. 19
Zapisz poniższy kod do pliku `uniprot2.py`.

```python
import argparse

parser = argparse.ArgumentParser(description='Retrieve proteins from UniProt database')
parser.add_argument('-i', '--id', dest='uniprot', required=True,
                    nargs='+', help='Uniprot ID (e.g. P68431)')
parser.add_argument('-o', '--o', '--out', dest='output', default='uniprot.txt',
                    help='Output filename (default: %(default)s)')
args = parser.parse_args()


print(args.uniprot)
print(args.output)
```

Następnie uruchom skrypt poniższymi poleceniami i na podstawie ich wyników wyjaśnij, do czego służy moduł `argparse`.

```bash
python3 uniprot2.py
python3 uniprot2.py -h
python3 uniprot2.py --help
python3 uniprot2.py --id P68431
python3 uniprot2.py -i P68431 Q6ZQ08
python3 uniprot2.py --id P68431 Q6ZQ08 -o output.fasta
```


## Zad. 20
Do skryptu `uniprot2.py` dodaj kod, który pobierze rekordy sekwencji z bazy UniProt i zapisze je do odpowiedniego pliku tekstowego.


## Zad. 21
UniProt pozwala wyświetlać rekord białkowy *w dwóch formatach*:

1. *fasta*: <a href="http://www.uniprot.org/uniprot/Q93062.fasta">http://www.uniprot.org/uniprot/Q93062.fasta</a>
2. *txt*:   <a href="http://www.uniprot.org/uniprot/Q93062.txt">http://www.uniprot.org/uniprot/Q93062.txt</a>

Dodaj do skryptu argument `--format`, który będzie umożliwiał użytkownikowi wybranie jednego z dwóch formatów (domyślnie `fasta`).


## Zad. 22
Zapisz poniższy kod do pliku `random_dna3.py`.

```python
import argparse

__version__ = 3.0

p = argparse.ArgumentParser(description='Generate a random DNA sequence')
p.add_argument('dna_length', type=int, help='Length of random DNA sequence')
p.add_argument('-a', '--a', dest='adenine', type=float,
               default=0.25, help='Adenine probability [default =  %(default)s]')
p.add_argument('-c', '--c', dest='cytosine', type=float,
               default=0.25, help='Cytosine probability [default =  %(default)s]')
p.add_argument('-g', '--g', dest='guanine', type=float,
               default=0.25, help='Guanine probability [default =  %(default)s]')
p.add_argument('-t', '--t', dest='thymine', type=float,
               default=0.25, help='Thymine probability [default =  %(default)s]')
p.add_argument('-v', '--v', '--version', action='version',
               version=f'v.{__version__}',
               help="Show tool's version number and exit")
args = p.parse_args()


print(args.dna_length)
print(args.adenine)
print(args.cytosine)
print(args.guanine)
print(args.thymine)
```

Uruchom program `random_dna3.py` poniższymi poleceniami. Następnie dokończ program, aby generował losową sekwencję DNA o podanej przez użytkownika długości. Program powinien mieć możliwość podania prawdopodobieństwa wystąpienia każdego z nukleotdów (domyślnie nukleotdy występują z jednakowym prawdopodobieństwem, czyli suma ich prawdopodobieństw musi być równa 1).

```bash
python random_dna3.py
python random_dna3.py -h
python random_dna3.py --help
python random_dna3.py 100
python random_dna3.py 100 -a 0.2 -c 0.3
python random_dna3.py 100 -v
```
