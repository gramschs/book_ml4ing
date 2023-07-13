---
jupytext:
  formats: ipynb,md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.7
kernelspec:
  display_name: Python 3.9.12 ('python39')
  language: python
  name: python3
---

# Liste und Zählschleife

## Lernziele

```{admonition} Lernziele
:class: important
* Datentyp Liste
* Kontrollstrukturen: Schleifen mit "for"
```


## Datentyp Liste

Eine Liste ist eine Sequenz von Objekten, Dabei können die Objekte einen
beliebigen Datentyp aufweisen. Z.B. könnte eine Liste Integer enthalten:

```{code-cell} ipython3
a = [34, 12, 54]
print(a)
```

```{code-cell} ipython3
a = ['Alice', 'Bob', 'Charlie']
print(a)
```

Eine leere Liste wird durch `[]` definiert:

```{code-cell} ipython3
a = []
print(a)
```

Der Datentyp heißt formal `list`:

```{code-cell} ipython3
type(a)
```

Genau wie bei Strings gibt die Funktion `len()` die Anzahl der Elemente zurück:

```{code-cell} ipython3
a = ['Hund', 'Katze', 'Maus', 'Affe','Elefant']
len(a)
```

Es können verschiedene Datentypen in einer Liste gemischt werden:

```{code-cell} ipython3
a = [123, 'Ente', -42, 17.4, 0, 'Elefant']
print(a)
```

```{admonition} Mini-Übung
:class: miniexercise
Erzeugen Sie eine Einkaufsliste, um einen Obstsalat zuzubereiten und speichern
Sie diese Liste in der Variablen `einkaufsliste`. Lassen Sie dann den Computer
bzw. den Python-Interpreter zählen, wie viele Zutaten Ihre Liste enthält und
geben Sie dann die Anzahl aus.
```

```{code-cell} ipython3
# Hier Ihr Code:
```

````{admonition} Lösung
:class: minisolution, toggle
```python
einkaufsliste = ['Apfel', 'Banane', 'Trauben', 'Joghurt']
anzahl_zutaten = len(einkaufsliste)
print(anzahl_zutaten)
```
````

+++

Zwei Listen werden verkettet (“concatenate”) durch den `+` Operator:

```{code-cell} ipython3
a = [37, 3, 5] + [3, 35, 100]
print(a)
```

Um an das Ende der Liste ein neues Element einzufügen, verwendet man die Methode
`append()`. Eine **Methode** ist eine spezielle Funktion, die zu dem Datentyp
gehört und daher an die Variable angehängt wird, indem man einen Punkt schreibt
und dann den Methodennamen.

Was Methoden genau sind, werden wir noch lernen.

```{code-cell} ipython3
a = [34, 56, 23]
print(a)

a.append(42)
print(a)
```

Aus der Liste können Elemente durch die `remove()`-Methode gelöscht werden.
Dabei wird das Element, das gelöscht werden soll, der Methode als Argument
übergeben.

```{code-cell} ipython3
a = [34, 56, 23, 42]
print(a)

a.remove(56)
print(a)
```

```{admonition} Mini-Übung
:class: miniexercise
Nehmen Sie Ihre Einkaufsliste für den Obsalat von vorhin. Fügen Sie noch Zimt und Zucker hinzu. Leider passen in Ihren Einkaufswagen nur maximal 5 Sachen. Lassen Sie überprüfen, ob Ihre Einkaufsliste nun mehr als 5 Zutaten enthält. Falls ja, lassen Sie eine Warnung ausgeben.
```

```{code-cell} ipython3
# Hier Ihr Code:
```

````{admonition} Lösung
:class: minisolution, toggle
```python
einkaufsliste = ['Apfel', 'Banane', 'Trauben', 'Joghurt', 'Zimt', 'Zucker']
anzahl_zutaten = len(einkaufsliste)
if anzahl_zutaten > 5:
    print('Der Einkaufswagen ist zu voll!')
````
````

+++

<iframe width="560" height="315" src="https://www.youtube.com/embed/ihF8bZoauBs" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Listen sind (übrigens genau wie Strings) ein **sequentieller Container**.

Sequentielle Container sind Sammlungen von Datenobjekten. Manchmal werden sie
auch kurz als **Sequenzen** abgekürzt. Sequentielle Container sind mit ganzen
Zahlen, also Integern, durchnummeriert. Die Nummerierung beginnt bei 0. Die
Nummer eines Elementes aus der Sequenz nennt man Index. Umgangssprachlich könnte
man den Index auch als Hausnummer bezeichnen.

In einer Sequenz hat also das erste Element den Index 0. Das zweite Element hat
den Index 1 usw. Um ein einzelnes Element einer Sequenz herausgreifen zu können,
schreibt man `s[i]`. Dabei ist s der Name der Sequenz. Um einfach auf das letzte
Element einer Sequenz zugreifen zu können, hat Python den Index -1 eingeführt.

Probieren wir ein paar Beispiele aus:

```{code-cell} ipython3
a = [34, 56, 23, 42]
print('Das erste Element in der Liste ist: ')
erstes = a[0]
print(erstes)
```

Für sequentielle Container und damit auch insbesondere für Listen bietet Python
Standardfunktionen. Hier die wichtigsten:

* `liste[i]` gibt das i-te Element von `liste` zurück
* `liste[i:j]` gibt die Elemente i bis j-1 zurück
* `liste[start:ende:schrittweite]` gibt die Elemente von Index `start` bis
  `ende-1` mit einer Schrittweite aus 
* `len(liste)` gibt die Anzahl der Elemente von liste zurück
* `min(liste)` gibt das kleinste Element von `liste` zurück
* `max(liste)` gibt das größte Element von `liste` zurück
* `x in liste` gibt den Wahrheitswert `True` zurück, wenn `x` in der Sequenz
  `liste` enthalten ist
* `liste1 + liste2` verknüpft `liste1` und `liste2`
* `n * liste` generiert `n` Kopien der Sequenz `liste`


Probieren wir sie an Beispielen aus. Denken Sie sich eigene Beispiele aus, um
die Funktionen kennenzulernen:

```{code-cell} ipython3
liste = [1,2,'drei','VIER',5]
liste[3]
```

```{code-cell} ipython3
liste[2:4]
```

```{code-cell} ipython3
#max(liste)
```

```{code-cell} ipython3
liste = [1,2,3,4,5]
max(liste)
```

```{code-cell} ipython3
liste = ['a', 'b', 'c', 'd', 'e']
max(liste)
```

```{code-cell} ipython3
liste = ['a', 'b', 'c', 'd', 'e']
if 'a' in liste:
    print('Das a ist dabei!')
else:
    print('Das a ist leider nicht in der Liste.')
```

```{admonition} Mini-Übung
:class: miniexercise  
Bleiben wir beim Obsalat, bei Ihrem ursprünglichen Rezept. Erzeugen Sie zunächst
die Liste. Lassen Sie dann den Computer überprüfen, ob schon Zimt und Zucker auf
der Liste stehen. Wenn noch Platz im Einkaufswagen ist (maximal 5 Zutaten),
fügen Sie den Zimt dazu. Wenn dann noch Platz im Einkaufswagen ist, fügen Sie
auch noch den Zucker hinzu. Lassen Sie zuletzt das erste Element der Liste
ausgeben. 
```

```{code-cell} ipython3
# Hier Ihr Code:
```


````{admonition} Lösung
:class: minisolution, toggle
```python
einkaufsliste = ['Apfel', 'Banane', 'Trauben', 'Joghurt', 'Zimt']
if 'Zimt' not in einkaufsliste and len(einkaufsliste) < 5:
    einkaufsliste.append('Zimt')
if 'Zucker' not in einkaufsliste and len(einkaufsliste) < 5:
    einkaufsliste.append('Zucker')
print('Anfang der Einkaufsliste:')
print(einkaufsliste[0])
```
````

+++

<iframe width="560" height="315" src="https://www.youtube.com/embed/_XzWPXvya2w" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

+++

## Zählschleifen "for"

Bei einer While-Schleife wird ein Anweisungsblock solange wiederholt, bis die
dazugehörige Bedingung nicht mehr erfüllt ist. Manchmal möchte man jedoch die
Anweisungen auf alle Elemente einer Menge, d.h. einer Liste, anwenden. Dazu gibt
es die For-Schleife. Sie hat folgende Syntax:

```python
for element in liste:
    anweisungsblock
```

Dabei betrachten wir zwei Fälle:

1. Die Menge wird in Form einer Liste explizit aufgezählt, beispielsweise als
   `[4,5,7,11,21]`.
2. Die Menge wird als Zahlenbereich beschrieben, beispielsweise als
   `range(3,9)`. 

Schauen wir uns ein erstes Beispiel an. Jedes Element der Liste `[4,5,7,11,21]`
soll um 2 erhöht werden.

```python
for zahl in [4,5,7,11,21]:
    summe = zahl + 2
    print("Wenn ich zu", zahl, "zwei addiere, erhalte ich", summe)
print("Ich bin fertig!")
```

```{code-cell} ipython3
for zahl in [4,5,7,11,21]:
    summe = zahl + 2
    print("Wenn ich zu", zahl, "zwei addiere, erhalte ich", summe)
print("Ich bin fertig!")
```

```{admonition} Mini-Übung
:class: miniexercise  
Lassen Sie nacheinander die Zutaten Ihrer Einkaufsliste ausgeben. 
```

```{code-cell} ipython3
# Hier Ihr Code:
```

````{admonition} Lösung
:class: minisolution, toggle
```python
einkaufsliste = ['Apfel', 'Bananen', 'Trauben', 'Joghurt', 'Honig', 'Zimt']
for zutat in einkaufsliste:
    print(zutat)
```
````

+++

<iframe width="560" height="315" src="https://www.youtube.com/embed/ISo1uqLcVw8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Es kommt sehr häufig vor, dass über Listen mit Zahlen iteriert werden soll.
Dafür stellt Python 3 die Funktion `range()`zur Verfügung.

```{code-cell} ipython3
for zahl in range(17):
    print(zahl)
print('Fertig!')
```

Wird `range(endzahl)` mit nur einem Parameter aufgerufen, dann beginnt der
Python-Interpreter stets von `0` an zu zählen. Dabei ist die `endzahl` nicht
inkludiert, d.h. der Python-Interpreter stoppt bei `endzahl - 1`. Es ist auch
möglich, eine Startzahl vorzugeben, also:

```python
range(startzahl, endzahl)
```

```{code-cell} ipython3
for zahl in range(4,13):
    print(zahl)
print('Fertig!')
```

Zusätzlich kann der Zahlenbereich noch durch die Angabe einer Schrittweite
spezifiziert werden. Dadurch ist es beispielsweise möglich, nur ungerade Zahlen
zu generieren:

```{code-cell} ipython3
for zahl in range(3, 13, 2):
    print(zahl)
print('Fertig!')
```

```{admonition} Mini-Übung
:class: miniexercise 
Lassen Sie alle geraden Zahlen zwischen 100 und 120 ausgeben.
```

```{code-cell} ipython3
# Hier Ihr Code:
```

````{admonition} Lösung
:class: minisolution, toggle
```python
for zahl in range(100, 122, 2):
    print(zahl)
```
````

+++

Durch Angabe einer negativen Schrittweite kann auch rückwärts gezählt werden:

```{code-cell} ipython3
for zahl in range(13, 3, -2):
    print(zahl)
print('Fertig!')
```

For-Schleifen können auch ineinander verschachtelt werden. Das ist z.B.
hilfreich, wenn man alle Paare durch Kombination bilden will.

```{code-cell} ipython3
for i in ['rot', 'grün', 'blau']:
    for j in [1, 2, 5, 17]:
        print('Kombination Farbe mit Zahl: ', i, j)
```

Natürlich kann eine for- auch mit einer if-else-Konstruktion kombiniert werden.
Was vermuten Sie, macht folgender Code-Schnipsel?

```{code-cell} ipython3
for i in ['rot', 'grün', 'blau']:
    for j in [1,2,3]:
        if i == 'grün':
            print('Kombination der Farbe GRÜN mit Zahl: ', j)
        else:
            print('Kombination Farbe mit Zahl: ', i, j)
```

<iframe width="560" height="315" src="https://www.youtube.com/embed/pQh5Idw2sKM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
