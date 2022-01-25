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
if __name__ == '__main__':
    seq_elem1 = ''
    seq_elem2 = ''
    min_dist = len(SEQUENCES['seq1'])

    for seq in itertools.combinations(SEQUENCES,2): #obliczanie dystansu hamminga dla wszystkich kombinacji
        dist = hamming_distance(SEQUENCES[seq[0]], SEQUENCES[seq[1]])
        print(f'{seq[0]} i {seq[1]} dystans hamminga = {hamming_distance(SEQUENCES[seq[0]], SEQUENCES[seq[1]])}')

        if dist < min_dist: #wyszukiwanie najmniejszego dystansu
            min_dist = dist
            seq_elem1 = seq[0]
            seq_elem2 = seq[1]
    print(f'Najmnieszy dystans wystepuje dla {seq_elem1} oraz {seq_elem2} = {min_dist} ')

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
import itertools

table = ['Anna', 'Andrzej', 'Igor', 'Antoni', 'Łucja', 'Kajetan', 'Agata', 'Dominika', 'Stanisław', 'Mikołaj']
counter = 0
for person in itertools.permutations(table):
    counter += 1
    #print(person)
print(counter)

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
import itertools

lst1 = [1, 2, 3]
lst2 = ['a', 'b', 'c']
lst3 = ['A', 'B', 'C']
for elem in itertools.product(lst1, lst2, lst3):
    print(f'{elem[0]}, {elem[1]}, {elem[2]}')

# Moduł [random](https://docs.python.org/3/library/random.html)

> Generowanie pseudolosowych liczb i wartości z podanej sekwencji (np. listy, krotki).


## Zad. 6
Przyporządkuj wywołanie funkcji do odpowiedniej definicji.

Funkcje:

```python
import random

# a --> 4
print(random.random())

# b --> 5
print(random.uniform(1, 3))

# c --> 6
print(random.randint(1, 3))

# d --> 2
print(random.choice(['Head', 'Tails']))

# e --> 1
print(random.sample(['a', 'b', 'c'], 2))

# f --> 3
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
import random

def nucl_generator(length):
    seq=''
    for nucl in range(length):
        nucl = random.choice(['A', 'T', 'G', 'C'])
        seq += nucl
    return seq
print(nucl_generator(length = int(input('Enter a DNA length:'))))

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

import sys
import random

def nucl_generator(length):
    seq=''
    for nucl in range(length):
        nucl = random.choice(['A', 'T', 'G', 'C'])
        seq += nucl
    return seq

if __name__=='__main__':
    print(nucl_generator(int(sys.argv[1])))

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
import os
for i in range(1000):
    os.system('python3 random_dna2.py 20')

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
Kod tworzy katalog o nazwie data jeśli taki nie istnieje i tworzy w nim 10 plików .txt, których zawartość to nazwa pliku.

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
Odnajduje katalog data i po nim iteruje zwracając ścieżkę do pliku każdego z plików, nazwę pliku, nazwę bez rozszerzenia oraz typ rozszerzenia.

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
Kod tworzy podkatalog w katalogu data jesśli taki nie istnieje iteruje po zawartości tego podkatalogu sparawdzjąc rodzaje elementów (plik lub katalog) oraz wypisując jego ścieżkę.

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
Sprawdza czy istnieje katalog data oraz czy w katalogu data występuje plik file11.txt
## Zad. 14
W skompresowanym pliku [human_proteins.zip](../data/human_proteins.zip) znajduje się katalog zawierający 250 sekwencji białkowych człowieka (każda sekwencja w osobnym pliku). Użyj modułu `pathlib`, aby otworzyć każdy z 250 plików i obliczyć średnią długość wszystkich sekwencji.

```python
import pathlib

# Your code goes here.

directory = pathlib.Path('human_proteins')
length=[]
for path in directory.iterdir():
    with open(path, 'r') as fh:
        fh.readline()
        proteins = fh.read().strip()
        length.append(len(proteins))
print(f'Mean sequence length:{(sum(elem for elem in length)) / len(length)}')
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
Pobiera dane z podanego linku odczytuje je, zapisuje a następnie je wypisuje na ekran

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
Pobiera dane z podanego linku, zapisuje je, a następnie linia po linii zamienia
dane na string. Gdy linia nie zaczyna się na > to zostaje wypisana.

## Zad. 17
Utwórz skrypt `uniprot1.py`, który pobierze z bazy UniProt sekwencje białkowe (w formacie FASTA) dla podanych poniżej identyfikatorów i zapisze pobrane sekwencje do pliku `uniprot.txt`.

```python
import urllib.request

uniprot_ids = ['P68431', 'Q6ZQ08', 'O94687']

# Your code goes here.

with open('uniprot.txt', 'w') as fh:
    for id in uniprot_ids:
        fh.write(urllib.request.urlopen(f'http://www.uniprot.org/uniprot/{id}.fasta').read().decode('utf-8'))
```

## Zad. 18
Funkcja `sleep` modułu `time` powoduje, że program nic nie będzie robił przez podaną liczbę sekund.

```python
import time

for i in range(10):
    print(i)
    time.sleep(0.3)
```
import urllib.request
import time

uniprot_ids = ['P68431', 'Q6ZQ08', 'O94687']

# Your code goes here.
with open('uniprot.txt', 'w') as fh:
    for id in uniprot_ids:
        fh.write(urllib.request.urlopen(f'http://www.uniprot.org/uniprot/{id}.fasta').read().decode('utf-8'))
        time.sleep(1)

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
Argparse odpowiada za obsługę argumentów linii komend. Dzięki niemu możemy przekazywać
wartości z zewnątrz np. podczas uruchamiania konsoli.

## Zad. 20
Do skryptu `uniprot2.py` dodaj kod, który pobierze rekordy sekwencji
z bazy UniProt i zapisze je do odpowiedniego pliku tekstowego.

import argparse
import urllib.request

parser = argparse.ArgumentParser(description='Retrieve proteins from UniProt database')
parser.add_argument('-i', '--id', dest='uniprot', required=True, nargs='+', help='Uniprot ID (e.g. P68431)')
parser.add_argument('-o', '--o', '--out', dest='output', default='uniprot.txt', help='Output filename (default: %(default)s)')

args = parser.parse_args()

with open(args.output,'w') as f:
        for arg in args.uniprot:
            f.write(urllib.request.urlopen(f'http://www.uniprot.org/uniprot/{arg}.fasta').read().decode('utf-8'))


## Zad. 21
UniProt pozwala wyświetlać rekord białkowy *w dwóch formatach*:

1. *fasta*: <a href="http://www.uniprot.org/uniprot/Q93062.fasta">http://www.uniprot.org/uniprot/Q93062.fasta</a>
2. *txt*:   <a href="http://www.uniprot.org/uniprot/Q93062.txt">http://www.uniprot.org/uniprot/Q93062.txt</a>

Dodaj do skryptu argument `--format`, który będzie umożliwiał użytkownikowi wybranie jednego z dwóch formatów (domyślnie `fasta`).

import argparse
import urllib.request

parser = argparse.ArgumentParser(description='Retrieve proteins from UniProt database')
parser.add_argument('-f', '--f', '--format', dest='format', default='fasta', help='Input file format')
parser.add_argument('-i', '--id', dest='uniprot', required=True, nargs='+', help='Uniprot ID (e.g. P68431)')
parser.add_argument('-o', '--o', '--out', dest='output', default='uniprot.txt', help='Output filename (default: %(default)s)')

args = parser.parse_args()

with open(args.output,'w') as f:
        for arg in args.uniprot:
            f.write(urllib.request.urlopen(f'http://www.uniprot.org/uniprot/{arg}.{args.format}').read().decode('utf-8'))


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
import argparse

__version__ = 3.0

import random

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

probs = [args.adenine, args.cytosine, args.guanine, args.thymine]
nucl = ['A', 'T', 'G', 'C']

if sum(prob for prob in probs) != 1:
    print(f'Probability of nucleotides is wrong')
    exit()
d = {}
for nucleotide, prob in zip(nucl, probs):
    d[nucleotide] = prob

seq = []
for keys, values in d.items():
    print(values * args.dna_length)
    for i in range(round(values * args.dna_length)):
        seq.append(keys)
random.shuffle(seq)
print(''.join(seq))
