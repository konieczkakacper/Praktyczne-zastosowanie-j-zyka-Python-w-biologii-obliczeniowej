# Liczby

# Zad. 1
#Które wyrażenia dają w wyniku liczbę 8?

1. `0 + 8` --> 8
2. `2 * 4` --> 8
3. `8 / 1` -->
4. `65 / 8` --> 8.125
5. `65 // 8` --> 8
6. `17 % 9` --> 8
7. `2 ** 3` --> 8
8. `64 ** 0.5` --> 8

## Zad. 2
Wbudowana funkcja `type` zwraca typ dowolnego *literału* (to co programista wpisuje w kod z klawiatury, np.: liczba, tekst). Na przykład wyrażenie `type(3)` informuje, że literał `3` jest liczbą całkowitą.
Zapisz typy poniższych literałów:

1. `3` --> int
2. `3.14` --> float
3. `'3.14'` --> str
4. `"3.14"` --> str
5. `314E-2` --> int
6. `3E2` --> float
7. `True` --> bool
8. `"bioinfo"` --> str
9. `'3'` --> str
10. `None` --> NoneType

## Zad. 3
Jaki typ liczbowy (`int`/`float`) będą miały wyniki poniższych wyrażeń:

1. `1 + 2` --> int
2. `1.0 + 2` --> float
3. `1 + 2.0` --> float
4. `1.0 + 2.0` --> float

## Zad. 4
Podaj wartość uzyskaną w wyniku poniższych wyrażeń:

```python
# Kolejność obliczeń (ewaluacji wyrażeń) zależy od zasad pierwszeństwa operatorów:
# 1. Nawiasy okrągłe
# 2. Potęgowanie
# 3. Mnożenie i dzielenie (kolejność wykonywania: od lewej do prawej strony)
# 4. Dodawanie i odejmowane (kolejność wykonywania: od lewej do prawej strony)
```

1. `1 + 2 * 3` --> 17
2. `(1 + 2) * 3` --> 9
3. `3 * 1 ** 3` --> 3
4. `4 / 2 * 2` --> 4
5. `2 * 2 / 4` --> 1


## Zad. 5
Podaj wynik, który zwróci Python dla poniższego działania.

```python
print(0.1 + 0.2)  --> 0.30000000000000004
```

> Dlaczego `0.30000000000000004`? Liczby zmiennoprzecinkowe przechowywane są w formacie binarnym (o ograniczonej liczbie bitów), który uniemożliwia dokładną reprezentację takich liczb jak: `0.1`, `0.2`, `0.3` itd. Kiedy kod programu jest kompilowany lub interpretowany liczba `0.1` jest automatycznie zaokrąglana do liczby w formacie binarnym, co skutkuje drobnym błędem zaokrąglenia jeszcze przed wykonaniem samego obliczenia.

> Liczby całkowite w Pythonie mają nieograniczoną *precyzję* - tzn. mogą składać się z takiej liczby cyfr, na jaką pozwoli ilość miejsca w pamięci komputera.


# Zmienne

## Zad. 6
Tworzenie zmiennej w Pythonie jest bardzo naturalne. Zmienna tworzona jest, kiedy kod pierwszy raz przypisuje jej wartość. Oznacza to, że nigdy nie deklarujemy zmiennych wcześniej.

Na przykład:

```python
a = 3

# Python automatycznie wykona trzy osobne kroki:
# 1. Utworzenie obiektu reprezentującego wartość 3.
# 2. Utworzenie zmiennej `a`, o ile jeszcze nie istnieje.
# 3. Połączenie zmiennej `a` z nowym obiektem.
#
# Typ zmiennej ma typ obiektu, który ta zmienna przechowuje.
# Zmienna `a` staje się referencją do obiektu 3. Wewnętrznie,
# zmienna jest wskaźnikiem do miejsca w pamięci zajmowanego
# przez obiekt i utworzonego przez wykonanie wyrażenia literału 3.
```

Utwórz dwie zmienne:

```python
a = 1
b = 1 + 2         # Najpierw zostanie obliczona wartość wyrażenia
                  # znajdująca się po prawej stronie operatora `=`
                  # i ta wartość zostanie przypisana do zmiennej.
```

Używając funkcji `print` wyświetl wartość zmiennej `b`.
print(b) --> 3
Utwórz zmienną `c`, która będzie sumą kwadratów wartości zmiennych `a` i `b`.
c = a ** 2 + b ** 2
print(c) --> 10

## Zad. 7
Zmienne można swobodnie *nadpisywać obiektami dowolnego typu*. Jest to możliwe, ponieważ typy powiązane są z obiektami, a nie ze zmiennymi. Zmienna jest tylko referencją do danego obiektu (tj. do miejsca w pamięci komputera).

Wypróbuj poniższy kod:

```python
a = 1             # Zmienna `a` jest liczbą całkowitą.
a = 'one'         # Teraz zmienna `a` jest łańcuchem znaków
a = 3.14          # Teraz zmienna `a` jest liczbą zmiennoprzecinkową
                  # (string 'one' zostaje zwolniony z pamięci)
```

Jaki typ będzie miała zmienna `a` gdy przypiszemy do niej wartość `3 / 2`?
a = 3 / 2
type(a) --> float

## Zad. 8
Zmienne w Pythonie zawsze łączą się z obiektami i nigdy z innymi zmiennymi.

```python
a = 3             # Zmienna `a` jest przypisana do obiektu 3
b = a             # Zmienna `b` staje się referencją do tego samego obiektu

#  Zmienne      Referencje     Obiekt
#
#  -------
# |       |
# |   a   | --------
# |       |         |          -------
#  -------          |-------> |       |
#                             |   3   |
#  -------          |-------> |       |
# |       |         |          -------
# |   b   | --------
# |       |
#  -------

b = 5
```

Sprawdź, czy powyższe instrukcje zmienią wartość `a`?
powyższe instrukcje nie zmieni

Wartość nie została zmieniona, ponieważ
print(a) --> 3

## Zad. 9
Jakie wartości mają zmienne `a` i `b` po wykonaniu poniższego kodu?

Spróbuj odpowiedzieć na to pytanie zanim przetestujesz kod.

```python
a = 3
b = a
a = a + 2
```
print(a) --> 3
print(b) --> 5
## Zad. 10
Które z poniższych nazw zmiennych są prawidłowe? Spróbuj przypisać do nich jakieś wartości liczbowe.

```python
# Reguły nazewnictwa zmiennych:
# - Jedyne znaki dopuszczalne w nazwach zmiennych to litery, cyfry oraz _
# - Pierwszy znak nazwy zmiennej nie może być cyfrą.
# - Wielkie litery są odróżniane od małych liter.
# - Nazwy zmiennych nie mogą być słowami kluczowymi języka Python (np. if, for).

Gene --> poprawna
exon --> poprawna
5utr --> niepoprawna
utr5p --> niepoprawna
gene name --> niepoprawna
gene_name --> poprawna
gene.name --> niepoprawna
geneName --> poprawna
UTR --> poprawna
```

## Zad. 11
Ile wynosi `x` w każdym wyrażeniu:

```python
x = 1
x = x + 1   --> 2    # Do zmiennej x wynoszącej 1, dodaj jeszcze wartość 1
                # i zapisz całość do zmiennej `x`.
x = x * 2 --> 4
x = x / 2 --> 2.0
x = x - 1 --> 1.0
```

## Zad. 12
Ile wynosi `x` w każdym wyrażeniu:

```python
x = 1
x += 1 --> 2
x *= 2 --> 4
x /= 2 --> 2.0
x -= 1 --> 1.0
```

# Łańcuchy znaków (*strings*)

## Zad. 13
Jaką wartość będzie miała zmienna `full_name` w poniższym kodzie:

```python
first_name = 'James'                      # Nie ma różnicy, czy stringi definiujemy używając
last_name = "Watson"                      # pojedynczych czy podwójnych apostrofów (cudzysłowu).
full_name = first_name + ' ' + last_name
```
print(full_name) --> 'James Watson'

## Zad. 14
Funkcja `len` zwraca długość (liczbę znaków) danego łańcucha znaków.

Jaka jest długość tekstu znajdującego się pod zmienną `full_name`?

len(full_name) --> 12

## Zad. 15
Sprawdź, które z poniższych wyrażeń są prawidłowe?

```python
'2' + 3 --> nieprawidłowe           # 1
'2' + '3' --> prawidłowe            # 2
int('2') + 3  --> nieprawidłowe     # 3
'2' + str(3)  --> prawidłowe        # 4
float('2') + 3 --> prawidłowe       # 5
'2' * 3 --> prawidłowe              # 6
'2' * '3' --> nieprawidłowe         # 7
```

## Zad. 16
Jaką wartość będzie miała zmienna `seq` na koniec poniższego kodu?

```python
seq = ''
seq += 'A'
seq += 'TG'
seq += 'C' * 4
```
print(seq) --> 'ATGCCCC'

## Zad. 17
Co otrzymasz w wyniku poniższych operacji *indeksowania*?

```python
s = 'abcdefghij'
```

1. `s[0]` --> a
2. `s[1]` --> b
3. `s[9]` --> j
4. `s[10]` --> out of range
5. `s[-1]` --> j
6. `s[-2]` --> i


## Zad. 18
Co otrzymasz w wyniku poniższych operacji wycinania (*ekstrakcji podłańcucha*)?

1. `s[0:9]` --> 'abcdefghi'
2. `s[0:10]` --> 'abcdefghij'
3. `s[:len(s)]` --> 'abcdefghij'
4. `s[:]` --> 'abcdefghij'
5. `s[:11]` --> 'abcdefghij'
6. `s[-3:-1]` --> 'hi'
7. `s[-3:]` --> 'hij'
8. `s[1:10:2]` --> 'bdfhj'
9. `s[::2]` --> 'acegi'
10. `s[::-1]` --> 'jihgfedcba'


## Zad. 19
Utwórz poniższą zmienną, wyświetl jej wartość funkcją `print` i odpowiedz czym są znaki: `\n`, `\t`

```python
s = 'Hello\tHolla\nGuten tag! "Konnichi wa"!'
```
\n --> znak nowej linii
\t --> znak tabulacji

W jaki sposób umieścić znak lewego ukośnika `\` w łańcuchu znaków?
Należy zastosować zapis `\\`

## Zad. 20
Łańcuchy znaków w Pythonie są obiektami **niemutowalnymi**, co oznacza, że **nie można ich modyfikować** w miejscu. Dlatego jeżeli chcemy modyfikować łańcuch to musimy zawsze utworzyć nowy. Napraw poniższy kod.

```python
msg = 'Hello Vorld!'
msg[6] = 'W'
print(msg)
```
msg = 'Hello Vorld!'
print(msg.replace('V', 'W'))

## Zad. 21
Python udostępnia zbiór <a target="_blank" href="https://docs.python.org/3/library/stdtypes.html#string-methods">metod łańcuchów znaków</a>, które implementują często spotykane zadania związane z tym typem danych. Ponieważ łańuchy znaków są niemutowalne, metody te zawsze generują nowe łańuchy znaków.

```python
>>> s = 'Bioinformatics'
>>> s.upper()
'BIOINFORMATICS'
>>> print(s)
'Bioinformatics'
```

Jak zmodyfikować powyższy kod, aby zmienna `s` miała na końcu wartość `BIOINFORMATICS`?

s = 'Bioinformatics'
print(s.upper())

## Zad. 22
Rozszyfruj co robią poniższe wyrażenia:

```python
s = '  James Watson i Francis Crick odkryli strukturę DNA w 1953 roku.  '
```

1. `s.lstrip()` --> usuwa białe znaki z początku łańcucha znaków jeśli parametr nie został podany
2. `s.rstrip()` --> usuwa białe znaki z końca łańcucha znaków jeśli parametr nie został podany
3. `s.strip()` --> usuwa białe znaki z początku i końca łańcucha zanków
4. `s.strip().rstrip('.')` --> usuwa białe znaki z początku i końca oraz usuwa z końca '.'
5. `s.strip().rstrip(',')` --> usuwa białe znaki z początku i końca oraz ma usunać ',', który nie występuje w tym łańcuchu, więc .rstrip(',') sie nie wykona
6. `s.find('Watson) --> znajduje indeks w łancuchu znaków 'Watson' zwraca wartość 8
7. `s.find('Sherlock')` --> zwraca -1 jeśli 'Sherlock' , ponieważ nie został znaleziony
8. `s.lower()` --> zmienia wszystkie litery na małe
9. `s.count('Watson')` --> sprawdza ile razy występuje 'Watson' w ciągu znaków w tym przypadku występuje 1 raz, więc zwraca 1
10. `s.replace('o', '0')` -->  zamienia znaki 'o' na '0'
11. `s.strip().replace('roku.', 'roku!').upper()` --> usuwa białe znaki z początku i kopńca zamienia 'roku.' na 'roku!' oraz zmienia małe litery na duże
12. `s.strip().startswith('James')` --> usuwa białe znaki z początku, a następnie sprawdza czy ciąg znaków zaczyna się od 'James'
13. `s.endswith('roku.  ')` --> sprawdza czy ciąg znaków kończy się 'roku.  '


## Zad. 23
W jednej linii kodu (*one-liner*) sformatuj poniższą sekwencję aminokwasów poprzez jednoczesne:
- pozbycie się znaku `>`
- pozbycie się wszystkich spacji po prawej stronie sekwencji
- zamianę sekwencji na wielkie litery.


```python
sequence = ">MAnlFKLgaENIFLGrKW    "
```
sequence.lstrip('>').rstrip().upper()

## Zad. 24
Utwórz *one-liner*, który zwróci liczbę cytozyn w pierwszych 30 nukleotydach poniższej sekwencji DNA.

```python
sequence = "AGCCGAGCCCGGCGGCCACGGCTGGCGATGAGGAGCGGCGGGTTAGAGCGCGAGC"
```
sequence.count('C') --> 16

## Zad. 25
Python oferuje *trzy mechanizmy formatowania łańcuchów znaków*:
1. Wyrażenie formatujące (`%`) [bardzo stary mechanizm: niezalecany]
2. Metodę `format` [starzejący się mechanizm: spotykany, ale niezalecany]
3. *F-strings* [nowość od Python 3.6: preferowany mechanizm + najlepsza wydajność]

Przetestuj poniższe instrukcje dotyczące F-stringów:

```python
name = 'Human'
nucl = 3234830000      # Liczba nukleotydów całego ludzkiego DNA
metr = 1.94            # Długość DNA w komórce wyrażona w metrach

msg = f'{name} genome has {metr} meters and {nucl} bp'
print(msg)

msg = f'{name} genome has {metr:.1f} meters and {nucl:,} bp'
print(msg)

msg = f'{name.upper()} genome has {metr * 100} cm and {nucl} bp'
print(msg)
```

Z poniższych zmiennych utwórz F-string `GC content of the GW182 gene: 65.3%`.

```python
gene = 'gw182'
gc_content = 65.3424545
```
msg = f'GC content of the {gene.upper()} gene: {gc_content:.1f}%'
print(msg)

## Zad. 26
Zapoznaj się z poniższym kodem i odpowiedz, co umożliwia deklaracja formatowania `:20`?

```python
a = 'hi'
b = 'hello'
c = 'good morning'

print(f'{a} 1')
print(f'{b} 2')
print(f'{c} 3')

print()

print(f'{a:20} 1')
print(f'{b:20} 2')
print(f'{c:20} 3')
```
':20'  --> wypełnienie łańcucha znaków białymi znakami do długości 20 znków

## Zad. 27
Poniższy kod powinien przeliczyć temperaturę w skali Celsjusza na Fahrenheita. Program zawiera jednak **2 błędy**. Napraw kod, aby działał prawidłowo.

```python
#       9
# F =  --- * C + 32
#       5

c = input('Enter temperature in Celsius: ')
f = 9/5 * c + 32
print(f'{c:.1f}°C : {f:1f}°F')
```
c = float(input('Enter temperature in Celsius: '))
f = (9/5 * c) + 32
print(f'{c:.1f}°C : {f:1f}°F')

## Zad. 28
Wysoka zawartość nukleotydów `G` i `C` w sekwencji DNA wskazuje, że dany region DNA może być genem. Utwórz program `gc_content.py`, który przyjmie od użytkownika sekwencję DNA i obliczy w niej procentową zawartości sumy nukleotydów `G` i `C`.

```
$ python3 gc_content.py
DNA/RNA sequence: ATGCTGC
```

Output:

```
GC content: 57.1%
```
sequence = input("Sequence : ").upper()
c = sequence.count('G')
g = sequence.count('G')
total = len(sequence)
gc_content = ( g + c )/ total * 100

print(f'GC contetnt {gc_content:.1f} %')


## Zad. 29
Kartkę papieru można złożyć na pół maksymalnie 7 razy. Utwórz program `paper_fold.py`, który obliczy grubość kartki papieru gdyby można ją było złożyć na pół wiele razy. Standardowa kartka papieru ma grubość 0,05 mm. Po pierwszym złożeniu otrzymujemy kartkę o grubości 0,1 mm. Po drugim złożeniu kartka ma 0,2 mm grubości. Po trzecim złożeniu kartka ma grubość 0.4 mm. Przy siódmym złożeniu kartka ma 6,4 mm.

```
$ python3 paper_fold.py
Enter a number of paper folds: 7
```
fold = int(input('Enter a number of paper folds: '))
if 0 > fold:
    raise Exception("Podaj wartość złożeń od 1 do 7")
elif 7 < fold:
    raise Exception("Podaj wartość złożeń od 1 do 7")
thick = 0.05
result = 2 ** fold * thick
print(f'{result} mm')

Output:

```
Width: 6.4 mm
```

## Zad. 30
Utwórz program `mm2km.py`, który pobierze od użytkownika liczbę milimetrów i zamieni ją na liczbę kilometrów, metrów, centymetrów i pozostałych milimetrów.

```
$ python3 mm2km.py
Enter number of millimeters [mm]: 1530293
```
mili = int(input("Enter a number od milimeters [mm]: "))
# 1 km = 1 000 000 mm
# 1 m = 1000 mm
# 1 cm = 10 mm

km = int(mili / 1000000)
m = int(mili / 1000) - km * 1000
cm = int(mili / 10) - (km * 100000) - (m * 100)
mm = int(mili) - km * 1000000 - m * 1000 - cm * 10

print(f'{km} km {m} m {cm} cm {mm} mm')

Output:

```
1 km 530 m 29 cm 3 mm
```

Ile kilometrów ma grubość kartki złożonej na pół 45 razy?
1759219 km
