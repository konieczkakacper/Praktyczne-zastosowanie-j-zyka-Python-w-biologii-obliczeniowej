# Operatory logiczne

## Zad. 1
Liczby można porównywać za pomocą *operatorów porównania*. W wyniku otrzymujemy wartości logiczne (*boolean*): `True` lub `False`. 

Które z poniższych wyrażeń zwracają w wyniku `True`?

```python
print(3 == 2)   # 1 -->False
print(3 != 2)   # 2 --> True
print(3 > 2)    # 3 --> True
print(3 < 2)    # 4 --> False
print(3 >= 2)   # 5 --> True
print(3 <= 2)   # 6 --> False
```


## Zad. 2
Łańcuchy znaków również obsługują operatory porównania. Które z poniższych wyrażeń zwracają `True`?

```python
print('bio' == 'bio')              # 1 --> True
print('bio' != 'BIO')              # 2 --> True

# Operatory > i < dotyczą
# porządku alfabetycznego.
print('bio' > 'category')          # 3 --> False
print('bio' > 'Zebra')             # 4 --> True
                                   # Wszystkie duże litery mają pierwszeństwo
                                   # przed wszystkimi małymi literami.

# Stringi mają operator `in`
print('bio' in 'bioinformatics')   # 4 --> True
print('bio' not in 'Bioinfo')      # 5 --> True
```

## Zad. 3
Python ma trzy operatory logiczne: `and`, `or` i `not`.

> Na przykład, wyrażenie `x % 2 == 0 and x % 3 == 0` jest prawdziwe jeżeli liczba `x` jest podzielna przez `2` i `3`. 

Napisz wyrażenie, które jest prawdziwe jeżeli liczba `x` jest większa od `10` lub jednocześnie podzielna przez `2` i `3`.
x > 10 or x % 2 and x % 3

# Instrukcja if

## Zad. 4
Poniższy program jest poprawny pod względem składni języka Python, ale zawiera **błąd logiczny**. Napraw kod, aby działał prawidłowo.

```python
age = int(input('How old are you? '))

if age > 13:
    print("You can get ice cream")
elif age > 18:
    print("You are an adult")
elif age > 5:
    print("You can get candy")
else:
    print("You need a nap") 
```
age = int(input('How old are you? '))

if age >= 18:
    print("You are an adult")
elif age > 13:
    print("You can get ice cream")
elif age > 5:
    print("You can get candy")
else:
    print("You need a nap")
    
## Zad. 5
Utwórz program `bmi.py`, który prosi użytkownika o podanie wzrostu (cm) i wagi (kg), i obliczy wskaźnik masy ciała (BMI, *Body Mass Index*). Następnie w oparciu o obliczoną wartość BMI program wyświetli stosowny komunikat.

```python
'''
              waga (kg)
 BMI = -----------------------
       wzrost (m) * wzrost (m)
 
 Na przykład, BMI osoby ważącej 70 kg i mierzącej 175
 wynosi 70/(1.75 * 1.75) = 22.86

 BMI > 30           obesity
 25 <= BMI <= 30    overweight
 19 <= BMI <= 25    normal weight
 BMI < 19           underweight
'''
```
weight = float(input("Podaj swoją wagę [kg]:"))
height = float(input("Podaj swój wzrost [cm]:"))
BMI = weight / (height ** 2) * 10000
if BMI > 30:
    print(f'Twoje BMI wynosi {BMI:.2f}. Co wskazuje na otyłość.')
elif 25 <= BMI <= 30:
    print(f'Twoje BMI wynosi {BMI:.2f}. Co wskazuje na nadwagę.')
elif 19 <= BMI <= 25:
    print(f'Twoje BMI wynosi {BMI:.2f}. Co wskazuje na wagę prawidłową.')
else:
    print(f'Twoje BMI wynosi {BMI:.2f}. Co wskazuje na niedowagę.')



## Zad. 6
Mówi się, że każdy rok psa równy jest 7 latom człowieka. Na przykład, jak pies ma 10 lat to odpowiada on 70 letniemu człowiekowi. Jednak ponieważ pies zaczyna być dorosły w wieku 2 lat, sugeruje się, aby liczyć dwa pierwsze lata psa po 10,5 lat człowieka, a każdy kolejny rok psa liczyć jako 4 lata. Na przykład, jak pies ma 2 lata to odpowiada on 21-letniemu człowiekowi, jak pies ma 3 lata to odpowiada 25-letniemu człowiekowi. 

Napisz program `dog.py`, który przeliczy wiek psa na odpowiadający mu wiek człowieka.

```
How old is your dog? 4
```

Output:

```
That's 29.0 human years.
```
dog_age = float(input('How old is your dog: '))

if dog_age <= 2:
    human_age = dog_age * 10.5
else:
    human_age = (dog_age - 2) * 4 + 21

print(f'Dog is {human_age} yo in human years!')


## Zad. 7
Aby wiedzieć, które obiekty są prawdą, a które fałszem w Pythonie wystarczy zapamiętać poniższe dwie reguły:

1. Każda liczba jest prawdą jeśli nie jest zerem.
2. Pozostałe obiekty są prawdą jeśli nie są puste.

Które z poniższych instrukcji `if` zwrócą `True`? Spróbuj odpowiedzieć na to pytanie zanim przetestujesz kod.

```python
print(bool(1.2))       # 1 --> True
print(bool(-1))        # 2 --> True
print(bool(0))         # 3 --> False
print(bool(0.0))       # 4 --> False
print(bool('A'))       # 5 --> True
print(bool(''))        # 6 --> False
print(bool(len('')))   # 7 --> False
print(bool(None))      # 8 --> False
```

# Pętla while


## Zad. 8
Instrukcja `while` jest użyteczna jeżeli trzeba wykonać jakieś instrukcje wiele razy, ale nie jesteśmy w stanie z góry określić ile razy.

Jaki jest cel poniższego kodu?

```python
invalid_option = True

while invalid_option:
    option = input('Choose option a or b: ')
    if option == 'a' or option == 'b':
        invalid_option = False

print(f'Your option: {option}')
```
Program wykonuje się tak długo, aż nie wybierzemy opcji a lub b , wybierając dowolny znak z klawiatury program prosi 
nas o wybranie opcji a lub  b, ponieważ nie została wykonana instrukcja if. Jeśli wykona się instrukcja if pętla while 
zostaje przerwana i wyświetla się komunikat zależny od wyboru opcji a lub b. 

## Zad. 9
Czy poniższy kod ma ten sam cel co kod z poprzedniego zadania?
Tak ma taki cel. Rożni się tym, że w pętli while wartość True nie jest przypisana do zmiennej. Mimo to program działa tak samo.

```python
while True:
    option = input('Choose option a or b: ')
    if option == 'a' or option == 'b':
        break

print(f'Your option: {option}')
```

## Zad. 10
Funkcja `randint` wybiera losową liczbę całkowitą z przedziału od `1` do `10` (włącznie).

```python
import random
SECRET_NUMBER = random.randint(1, 10)
```

Dopisz kod, który będzie pytał użytkownika o podanie liczby dopóki użytkownik nie trafi liczby `SECRET_NUMBER`. Program powinien również poinformować użytkownika za którym razem odgadł liczbę `SECRET_NUMBER`.

```
Enter a number: 7 
Enter a number: 1
Enter a number: 2
Enter a number: 3
Enter a number: 4
You guessed the secret number after 5 trials.
```
import random
SECRET_NUMBER = random.randint(1, 10)
chances = 0
while True:
    option = int(input('Enter a number: '))
    if option == SECRET_NUMBER:
        print(f"You guessed the secret number after {chances + 1}trial{'s' if chances > 1 else ''}!")
        break
    chances += 1



# Pętla for


## Zad. 11
Zmodyfikuj poniższy kod, aby w wyniku otrzymać `PP yy tt hh oo nn`:

```python
for letter in 'Python':
    print(letter, end=' ')
print()
```
for letter in 'Python':
    print(letter * 2, end=' ')
print()

## Zad. 12
Uruchom poniższy kod i odpowiedz na pytanie, czym różni się instrukcja `break` od instrukcji `continue`.

```python
# break
for letter in 'Python':
    if letter == 'h':
        break
    print(letter)
```

```python
# continue
for letter in 'Python':
    if letter == 'h':
        continue
    print(letter)
```
Instrukcja break kończy działanie pętli, następuje przejście do dalszej częśći programu.

Instrukcja continue kończy iterację bieżącej pętli i wraca na początek, aby określić czy pętla 
wykona się ponownie lub czy zakończyć i przejść dalej.

## Zad. 13
Unikatową cechą pętli `for` i `while` w Pythonie jest opcjonalny blok `else`. Uruchom poniższy kod dla różnch wartości zmiennych `name` i rozszyfruj kiedy blok `else` jest wykonywany.

```python
name = 'Python'
for letter in name:
    if letter == 'h':
        break
    print(letter)
else:
    print('I iterated over all letters')
```
Blok else jest wykonywany gdy w zmiennej name nie występuje litera 'h' przez co nie wykonuje się if zawarty w pętli for, który kończy działanie programu, gdy
zmienna letter przyjemuje wartość 'h'.

## Zad. 14
Funkcja `range` zwraca serię kolejnych liczb całkowitych.

```python
# Funkcja range z jednym argumentem
for i in range(10):
    print(i, end=' ') 
```

```python
# Funkcja range z dwoma argumentami
for i in range(1, 10):
    print(i, end=' ') 
```

```python
# Funkcja range z trzema argumentami
for i in range(1, 10, 2):
    print(i, end=' ') 
```

Utwórz *pętle for*, która wygeneruje taki wynik:

```
1 4 9 16 25 36 49
```
for i in range(1, 8):
    print(i ** 2, end=' ')

## Zad. 15
Utwórz *pętle for*, która wygeneruje taki wynik:

```
5 4 3 2 1 0 -1 -2 -3 -4 -5
```
for i in range(5, -6, -1):
    print(i, end=' ')

## Zad. 16
Na czym polega różnica między poniższymi dwoma instrukcjami?

```python
total = 0
for i in range(10):
    total += i
print(total)
```

oraz

```python
total = 0
for i in range(10):
    total += i
    print(total)
```
Między powyższymi instrukcjami różnica polega na umieszczeniu za pętlą print, który wypisze wynik ostatniej iteracji, natomiast jeśli print zostanie
umieszczony w pętli for tak jak w przykladzie grugim po każdej iteracji zostanie wypisany wynik.

## Zad. 17
Użyj pętli for, aby obliczyć silnię z liczby 20. Następnie sprawdź, czy otrzymałe/aś prawidłowy wynik używając modułu `math`.

num = 20
fac = 1

for i in range(1, num + 1):
    fac = fac * i
print(fac) --> 2432902008176640000

```python
import math

print(math.factorial(20)) --> 2432902008176640000
```
Używając modyłu math otrzymałem prawidłowy wynik.

## Zad. 18
Poniższy kod wyświetla na ekran wszystkie pozycje adeniny (A) w sekwencji DNA. Niestety kod zawiera **cztery błędy**. Napraw kod, aby działał prawidłowo.

```python
seq = 'ATGCTGACT"
position = 1

for char in seq
    if char = "A":
        print(position)
position = position + 1
```
seq = 'ATGCTGACT'
position = 1

for char in seq:
    if char == 'A':
        print(position)
    position = position + 1
    
## Zad. 19
Napisz kod, który dla stopni Celcjusza od 0 do 100 wyświetli odpowiedające stopnie Fahrenheita (F = 32 + 9/5 * C).

Output:

```
0°C   32.0°F
1°C   33.8°F
2°C   35.6°F
3°C   37.4°F
4°C   39.2°F
5°C   41.0°F
...
```
for celc in range(0, 101):
    fahr = float(9/5 * celc + 32)
    print(f'{celc}°C  {fahr:.1f}°F')


## Zad. 20
Użyj pętli `for` i funkcji `range`, aby obliczyć *dystans Hamminga* między poniższymi dwiema sekwencjami. Dystans Hamminga to liczba miejsc (pozycji), na których dwie sekwencje się różnią.

```python
seq1 = 'GAGCCTACTAACGGGAT'
seq2 = 'CATCGTAATGACGGCCT'

ham_dis = 0
for pos in range(len(seq1)):
    if seq1[pos] != seq2[pos]:
        ham_dis += 1
print(f'Hamming distance: {ham_dis}') # --> Hamming distance: 7
```
Output: Hamming distance: 7
```

## Zad. 21
Użytkownik znowu będzie zgadywał liczbę, którą wylosował komputer z przedziału [1, 10]. Tym razem, użytkownik ma tylko trzy próby żeby odgadnąć liczbę.

Użytkownik wygrywa:

```
Enter a number: 7
Enter a number: 1
You won! The number was 1.
```

Użytkownik przegrywa:

```
Enter a number: 7
Enter a number: 1
Enter a number: 5
Sorry, you failed! The number was 3.
```

## Zad. 22
Rozwiązując poprzednie zadanie być może wprowadziłe/aś zmienną, która przyjmowała `True` lub `False`, aby wyświetlić komunikat o przegranej użytkownika. Jeżeli tak, to zamiast tego spróbuj użyć klauzuli `else` pętli `for`.


## Zad. 23
Dokończ poniższą pętle `for`, aby wypisać wszystkie dwunukleotydowe wyrazy znajdujące się w poniższej sekwencji.

```python
dna = 'ATGCTGATGATGAT'
for i in range():
```

Output:

```
AT
TG
GC
CT
TG
GA
AT
TG
GA
AT
TG
GA
AT
```
dna = 'ATGCTGATGATGAT'
for i in range(len(dna) - 1 ):
    if i % 2 == 0:
        print(dna[i], dna[i + 1])
        continue
    else:
        print(dna[i], dna[i + 1])

## Zad. 24
Napisz kod, który w oparciu o dwie pętle `for` wyświetli na ekranie tabliczkę mnożenia.

```python
1   2   3   4   5   6   7   8   9   10  
2   4   6   8   10  12  14  16  18  20  
3   6   9   12  15  18  21  24  27  30  
4   8   12  16  20  24  28  32  36  40  
5   10  15  20  25  30  35  40  45  50  
6   12  18  24  30  36  42  48  54  60  
7   14  21  28  35  42  49  56  63  70  
8   16  24  32  40  48  56  64  72  80  
9   18  27  36  45  54  63  72  81  90  
10  20  30  40  50  60  70  80  90  100
```

## Zad. 25 (dla chętnych)
Zapis dot-bracket używany jest do tekstowego przedstawienia struktury drugorzędowej cząsteczek RNA.

Przykładowy zapis dot-bracket:

```
.((..(((...)))..((..)))).
```

Utwórz program `dotbracket.py` sprawdzający, czy zapis dot-bracket jest prawidłowy, tj:

- składa się jedynie z nawiasów i kropek,
- liczba nawiasów otwierających i zamykających musi być identyczna,
- każdy nawias otwierający musi mieć swój nawias zamykający.


Przykłady prawidłowego zapisu:

```
.((.))..()
.(((...).(...)))
()
.(.).
```

Przykłady nieprawidłowego zapisu:

```
.(..)..(.
.(..)..a()..
..()..)(..
(.)))(((.)
```

## Zad 26 (dla chętnych)

Utwórz kod, który poprosi użytkownika o podanie liczby całkowitej i sprawdzi, czy podana liczba jest liczbą pierwszą.

```
Enter an integer number: 4
```

Output:

```
The number 4 is not prime.
```