# Pliki

> Obejrzyj wprowadzenie do wczytywania i zapisywania plików: https://youtu.be/Uh2ebFW8OYM [24 min].


## Zad. 1
Utwórz plik tekstowy `human.txt` zawierający poniższe dane (*lokalizacje pierwszych 20 genów człowieka na chrom. 1*):

```
#name start end strand
OR4F5 65419 71585 +
OR4F29 450703 451697 -
OR4F16 685679 686673 -
SAMD11 923928 944581 +
NOC2L 944204 959309 -
KLHL17 960587 965715 +
PLEKHN1 966497 975865 +
PERM1 975204 982093 -
HES4 998962 1000172 -
ISG15 1001138 1014540 +
AGRN 1020123 1056118 +
RNF223 1070966 1074307 -
C1orf159 1081818 1116361 -
TTLL10 1173884 1197935 +
TNFRSF18 1203508 1206691 -
TNFRSF4 1211326 1214138 -
SDF4 1216908 1232031 -
B3GALT6 1232226 1235041 +
C1QTNF12 1242446 1246722 -
UBE2J2 1253909 1273885 -
```

W tym samym katalogu, w którym znajduje się powyższy plik tekstowy utwórz skrypt `human.py` i umieść w nim poniższy kod. W brakujące miejsca wstaw: `close`, `line`, `'human.txt'`, `print`, aby skrypt działał prawidłowo.

```python
fh = open(___)
for ____ in fh:
    ____(line)           # Zmienna `line` jest typu string.
fh.____()
```
fh = open("human.txt")
for line in fh:
    print(line)           # Zmienna `line` jest typu string.
fh.close()

## Zad. 2
Zmodyfikuj skrypt z poprzedniego zadania, aby w pętli *for* obliczał i wyświetlał długość sekwencji każdego z 20 genów.


```python
fh = open('human.txt')
fh.readline()            # Wczytanie pierwszego wiersza i natychmiastowe uwolnienie go z pamięci.
for line in fh:          # Iteracja zaczyna się od drugiego wiersza.
    print(line)
fh.close()
```

Output:

```
OR4F5   6167
OR4F29  995
OR4F16  995
SAMD11  20654
NOC2L   15106
...
```
fh = open('human.txt', 'r')
fh.readline()

for line in fh:
    length = line.split(' ')
    print('{0:8} {1}'.format(length[0], int(length[2]) - int(length[1]) + 1))

fh.close()

## Zad. 3
Zmodyfikuj skrypt `human.py`, aby długości genów zapisane zostały do pliku wynikowego `human.txt.out`.

fh = open('human.txt', 'r')
fhOutput = open('human.txt.out', 'w')

fh.readline()

for line in fh:
    length = line.split(' ')
    fhOutput.write('{0:8} {1}\n'.format(length[0], int(length[2]) - int(length[1]) + 1))

fhOutput.close()
fh.close()

## Zad. 4
Zmodyfikuj skrypt `human.py`, aby wyświetlił na ekranie średnią długość genu w pliku.


Output:

```
Mean gene length: 11302.2
```
fh = open('human.txt', 'r')

fh.readline()
lengths = []

for line in fh:
    length = line.split(' ')
    lengths.append((int(length[2]) - int(length[1]) + 1))

fh.close()

print(f'Mean gene length: {float(sum(lengths) / len(lengths))}')


## Zad. 5
<img align="right" src="../images/Gadsby-book_cover.jpg" alt="Gadsby book cover" height="270px">

Powieść *"Gadsby"* autorstwa Ernesta Vincenta Wrighta to książka w której nie występuje litera *e*. W pliku [gadsby.txt](../data/gadsby.txt) znajduje się ta powieść.
Napisz program `gadsby.py`, który sprawdzi, czy w książce rzeczywiście nie występuje litera *e*.

Output:

```
Letter e occurrences: X
```
fh = open('gadsby.txt', 'r')

letter = fh.read()
print('Letter e occurrences:', letter.count('e'))

fh.close()

## Zad. 6
Rozszerz kod programu `gadsby.py`, aby policzyć liczbę wszystkich słów znajdujących się w powieści *Gadsby*.

Wczytaj zawartość całej książki jako łańcuch znaków, usuń wszystkie wystąpienia znaków `. , ? ! ; : " ' - _ () * `. Następnie rozdziel łańcuch znaków na listę słów.

Output:

```
Letter e occurrences : X
Words in total       : X
```
fh = open('gadsby.txt', 'r')

strPrev = fh.read()

charRemove = ['.', ',', '?', '!', ';', ':', '"', '-', '_', '(', ')', '*', "'"]
strAfr = strPrev.lower()

for character in charRemove:
    strAfr = strAfr.replace(character, '')

print('Letter e occurrences:', strPrev.count('e'))
print('Words in total:', len(strPrev.split()))

fh.close()

## Zad. 7
Rozszerz kod programu `gadsby.py`, aby policzyć liczbę różnych słów zawartych w *Gadsby*.

Output:

```
Letter e occurrences : X
Words in total       : X
Uniq words           : X
```
fh = open('gadsby.txt', 'r')

strPrev = fh.read()

charRemove = ['.', ',', '?', '!', ';', ':', '"', '-', '_', '(', ')', '*', "'"]
strAfr = strPrev.lower()

for character in charRemove:
    strAfr = strAfr.replace(character, '')

unique = set()

for word in strPrev.split():
    unique.add(word)

print('Letter e occurrences:', strPrev.count('e'))
print('Words in total:', len(strPrev.split()))
print('Uniq words: ', len(unique))

fh.close()

## Zad. 8
Rozszerz kod programu `gadsby.py`, aby obliczyć liczbę wystąpień każdego słowa i zapisać wyniki do pliku `gadsby_words.txt`. Słowa powinny być uszeregowane alfabetycznie.

Zawartość pliku `gadsby_words.txt`

```
count    word
X        a
X        abiding
X        abigail
X        ability
X        abnormality
X        abnormally
X        aboard
...
```
fh = open('gadsby.txt', 'r')
fhOut =open('gadsby_words.txt', 'w')

strPrev = fh.read()

charRemove = ['.', ',', '?', '!', ';', ':', '"', '-', '_', '(', ')', '*', "'"]
strAfr = strPrev.lower()

for character in charRemove:
    strAfr = strAfr.replace(character, '')

unique = set()

for word in strPrev.split():
    if word in strPrev.lower():
        unique.add(word)

unique = sorted(unique)

for word in unique:
    fhOut.write('{} {}\n'.format(strPrev.lower().count(word), word))

fhOut.close()
fh.close()

## Zad. 9

W trzech plikach [cancer1.txt](../data/cancer1.txt), [cancer2.txt](../data/cancer2.txt) i [control.txt](../data/control.txt)
znajdują się nazwy genów, które wykazują podwyższony poziom ekspresji, odpowiednio, dla pacjentów z nowotworem skóry, białaczki i ludzi zdrowych.

Utwórz program `common_genes.py`, który wyszuka geny charakterystyczne jedynie dla pacjentów chorych na oba typy raka (i których nie ma w control) i zapisze je do pliku tekstowego `cancer_common.txt`

Input:

```
cancer1.txt     cancer2.txt       control.txt
-----             -----             -----
gene1             gene3             gene1
gene2             gene4             gene3
gene3             gene2             gene5
```

Output:

```
cancer_common.txt
-----
gene2
```
fhC1 = open('cancer1.txt', 'r')
fhC2 = open('cancer2.txt', 'r')
fhC = open('control.txt', 'r')

c1= set(fhC1)
c2 = set(fhC2)
cont = set(fhC)

commonFile = open('cancer_common.txt', 'w')
genes = c1 & c2 - cont
for gene in genes:
    commonFile.write(gene)

fhC1.close()
fhC2.close()
fhC.close()
commonFile.close()

## Zad. 10
W pliku [lotto_history.txt](../data/lotto_history.txt) znajdują się wszystkie historyczne wyniki losowania Dużego Lotka od 27.01.1957 do 30.12.2021. Napisz program `lotto_history.py`,
który przedstawi procentowy udział każdej z 49 liczb w odbytych losowaniach.

Wynik:

```
1   X%
2   X%
3   X%
...
47  X%
48  X%
49  X%
```

fh = open('lotto_history.txt', 'r')

lottoHistory = fh.read().split('\n')
results = []
for draw in lottoHistory:
    d = draw.find(',')
    results.append(list(map(int, draw[d - 2:].strip(' ').split(','))))
freq = dict()

for draw in lottoHistory:
    for ticket in lottoHistory:
        if ticket in freq:
            freq[ticket] += 1
        else:
            freq[ticket] = 1

drawsInHistory = sum(value for value in freq.values())

for key in sorted(freq.keys()):
    print(f'{key}  {freq[key] / drawsInHistory * 100 :.2f}%')

fh.close()

## Zad. 11
W katalogu [data/](../data/) znajduje się 10 plików, z których każdy zawiera jeden rekord sekwencji w formacie GenBank. Pobierz sekwencje na dysk. Napisz kod,
który w pętli *for* otworzy te 10 plików i odczyta identyfikator każdej sekwencji.

Output:

```
XM_003063680
NM_001031912
NM_001047041
NM_001013207
NM_171360
XM_013499304
XM_012793813
XM_011130266
XM_638989
XM_626579
```
for i in range(1, 11):
        file = open('data/seqNumber.genbank.txt'.replace('Number', str(i)), 'r')
        print(file.readline().split()[1])
        file.close()

## Zad. 12
Poniżej znajdują się dwa pliki wejściowe dotyczące sekwencji DNA bakterii *Mycoplasma hominis*:

1. [Mycoplasma_hominis.fasta](../data/Mycoplasma_hominis.fasta) zawiera 15 sekwencji genomowych tej bakterii.
```
>contig011
ACAGCCAGCGTTCATCCTGAGCCAGGATCAAACTCTTATAAAAAAATTTGAATTGGTTGA
TTATAAATAAAAAAATAAATTGACGTTAATGGTATTCGTATCCAGTTTTCAAAGAACTAT
CTCGTTGTTTCAAAACAACCTTTAAATATTATATACACTTTTTTTTATTTTTTCAAAAAA
...
>contig008
CAAGAAGTCAAATTGAAGCATTCATTAATGCAAATAAAACTAATCAAAATTATGCAGATT
TGATTGCAAAATTAACTAATGCTAAAAAAGCAAAGGAATCAGTTTCTGAATCTTCAAATA
AATCAGACATTATTGCAGCAAATCAAGCCTTACAACAAGCATTAAATACTGCGAAGGCTA
...
```
2. [Mycoplasma_hominis.csv](../data/Mycoplasma_hominis.csv) zawiera w osobnych wierszach lokalizację wszystkich znanych fragmentów genomowych tej bakterii (np.: genów, transkryptów itd.) w
odniesieniu do sekwencji genomowej powyżej.
```
#contig,feature,start,end,strand,gene_id,biotype
contig011,gene,1,105,-,JX73_01575,rRNA
contig011,transcript,1,105,-,JX73_01575,rRNA
contig011,exon,1,105,-,JX73_01575,rRNA
contig011,gene,5831,5905,+,JX73_01605,tRNA
contig011,transcript,5831,5905,+,JX73_01605,tRNA
contig011,exon,5831,5905,+,JX73_01605,tRNA
...
```

Na przykład gen `JX73_01575` znajduje się w sekwencji `contig011` na nici `-` w lokalizacji `1` - `105` i koduje `rRNA`.
Z kolei gen `JX73_01605` znajdujący się w sekwencji `contig011` umiejscowiony jest na nici `+` w pozycji `5831` - `5905`.


Zaprojektuj i utwórz program `mycoplasma.py`, który na podstawie informacji zawartych w pliku *csv* wydobędzie sekwencje **genów** i zapisze je do pliku `genes.fasta` w poniższym formacie:

Output:

```
>contig011|gene|JX73_01575|1:105|-
ACAGCCAGCGTTCATCCTGAGCCAGGATCAAACTCTTATAAAAAAATTTGAATTGGTTGATTATAAATAAAAAAATAAATTGACGTTAATGGTATTCGTATCCAG
>contig011|gene|JX73_01605|5831:5905|+
GGTCGCATAGCTCAGTGGAAGAGCACGAGCCTCCTAAGCCCGGGGTCGCAGGTTCAACTCCTGTTGCGATCGCCA
>...
```
ffasta = open('Mycoplasma_hominis.fasta', 'r')
fcsv = open('Mycoplasma_hominis.csv', 'r')
output = open('genes.fasta', 'w')

fcsv.readline()
fasta = []
fa = ffasta.read().split('>')
for x in fa:
    fasta.append(x.replace('\n', ''))
fasta = [x for x in fasta if x != '']

cs = fcsv.read().split('\n')
csv = []

for x in cs:
    csv.append(x.split(','))

for x in csv:

    output.write(f'>{x[0]}|{x[1]}|{x[5]}|{x[2]}:{x[3]}| {x[4]}\n')

    for seq in fasta:
        if seq[0:9] == x[0]:

            rseq = seq[9:]
            output.write(rseq[int(x[2]) - 1:int(x[3])] + '\n')

fasta.close()
fcsv.close()
output.close()

## Zad. 13
Zmodyfikuj program, aby sekwencje genów nici `-` zostały zapisane do pliku w kierunku 5'-3' (tj. odwrotnie komplementarnym).

> Wskazówka: Wykorzystaj funckję `reverse_complement` z poprzednich zajęć.

Output:

```
>contig011|gene|JX73_01575|1:105|-
CTGGATACGAATACCATTAACGTCAATTTATTTTTTTATTTATAATCAACCAATTCAAATTTTTTTATAAGAGTTTGATCCTGGCTCAGGATGAACGCTGGCTGT
>contig011|gene|JX73_01605|5831:5905|+
GGTCGCATAGCTCAGTGGAAGAGCACGAGCCTCCTAAGCCCGGGGTCGCAGGTTCAACTCCTGTTGCGATCGCCA
>...
```
ffasta = open('Mycoplasma_hominis.fasta', 'r')
fcsv = open('Mycoplasma_hominis.csv', 'r')
output = open('genes.fasta', 'w')

def revCompl(seq):
    d = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    return ''.join(d[nucleotide] for nucleotide in reversed(seq))

fcsv.readline()
fasta = []
fa = ffasta.read().split('>')
for x in fa:
    fasta.append(x.replace('\n', ''))
fasta = [x for x in fasta if x != '']

cs = fcsv.read().split('\n')
csv = []

for x in cs:
    csv.append(x.split(','))

for x in csv:

    output.write(f'>{x[0]}|{x[1]}|{x[5]}|{x[2]}:{x[3]}| {x[4]}\n')

    for seq in fasta:
        if seq[0:9] == x[0]:

            rseq = seq[9:]
            if x[4] == '-':
                output.write(revCompl(rseq[int(x[2]) - 1:int(x[3])]) + '\n')
            else:
                output.write(rseq[int(x[2]) - 1:int(x[3])] + '\n')
def revCompl(seq):
    d = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    return ''.join(d[nucleotide] for nucleotide in reversed(seq))

fasta.close()
fcsv.close()
output.close()
