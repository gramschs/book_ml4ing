---
jupytext:
  formats: ipynb,md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.15.2
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Übungen

```{admonition} Übung 2.1
:class: miniexercise 
Welcher Datentyp liegt vor? Kopieren Sie diesen Text in eine Markdown-Zelle und
schreiben Sie Ihre Antwort hinter den Pfeil.

* 3 -->
* -3 -->
* 'drei'-->
* 3.3 -->
* 3,3 -->
* 3**3 -->
* 3**(1/3) -->
```

```{admonition} Lösung
:class: minisolution, dropdown
* 3 –> int, also Integer
* -3 –> int, also Integer
* ‘drei’–> str, also String
* 3.3 –> float, also Float
* 3,3 –> Fehlermeldung, das Dezimaltrennzeichen ist der Punkt, nicht das Komma
* 3**3 –> int, also Integer
* 3**(1/3) –> float, also Float
```

```{admonition} Übung 2.2
:class: miniexercise 
Schreiben Sie ein Programm, das die Zahlen von 5 bis 15 mit ihrem Quadrat
ausgibt, also "Das Quadrat von 5 ist 25." usw.
```

````{admonition} Lösung
:class: minisolution, dropdown
```{code}
for zahl in range(5, 16):
    print(f'Das Quadrat von {zahl} ist {zahl**2}.')
```
````

````{admonition} Übung 2.3
:class: miniexercise 
Schreiben Sie eine For-Schleife, die die Brüche 1/7, 2/7, 3/7, bis 7/7 als
Fließkommazahl gerundet auf 2 Nachkommastellen ausgibt. Beispielausgabe:
```{code}
1/7 = 0.14.
2/7 = 0.29.
3/7 = 0.43.
4/7 = 0.57.
5/7 = 0.71.
6/7 = 0.86.
7/7 = 1.00.
```
````

````{admonition} Lösung
:class: minisolution, dropdown
```{code}
for zahl in range(1, 8):
    print(f'{zahl}/7 = {zahl/7:.2f}.')
```
````

````{admonition} Übung 2.4
:class: miniexercise 
Schreiben Sie ein Programm, das eine Liste von Namen durchgeht und jede Person
begrüßt. Wenn beispielsweise die Namen Alice, Bob und Charlie in der Liste
stehen, lauten die Begrüßungen:

```{code}
Hallo, Alice!
Hallo, Bob!
Hallo, Charlie!
```
````

````{admonition} Lösung
:class: minisolution, dropdown
```{code}
namensliste = ['Alice', 'Bob', 'Charlie']
for name in namensliste:
    print(f'Hallo, {name}!')
```
````

````{admonition} Übung 2.5
:class: miniexercise 
Schreiben Sie ein Programm, das das kleine 1x1 in schöner Tabellenform ausgibt,
also

```{code}
1 x 1 = 1
1 x 2 = 2
```
usw.
````

````{admonition} Lösung
:class: minisolution, dropdown
```{code}
for i in range(1,11):
    for j in range(1,11):
        print(f'{i} x {j} = {i*j}')
```
````
