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

# 2.2 Listen und for-Schleifen

Bisher haben wir drei verschiedene Datentypen kennengelernt:

* Integer (ganze Zahlen),
* Floats (Fließkommazahlen) und
* Strings (Zeichenketten).

Damit können wir einzelne Objekte der realen Welt ganz gut abbilden. Mit einem
String können wir den Namen einer Person erfassen, mit einem Integer das Alter
der Person und mit einem Float die Körpergröße der Person gemessen in Meter. Was
uns aber bisher fehlt ist eine Sammlung von Namen oder eine Sammlung von
Körpergrößen. Daher werden wir uns in diesem Kapitel mit dem Datentyp **Liste**
beschäftigen.

Oft kommt es vor, dass für jedes Element der Liste bestimmte Aktionen
durchgeführt werden sollen. Daher werden wir uns auch mit der Wiederholung von
Code-Abschnitten mittels der sogenannten **for-Schleife** beschäftigen.


## Lernziele

```{admonition} Lernziele
:class: goals
* Sie kennen den Datentyp **Liste**.
* Sie können Listen mit eckigen Klammern erzeugen. 
* Sie können Listen mit dem **Plus-Operator** verketten, Elemente mit
  **.append()** anhängen oder Werte mit **.remove()** aus der Liste löschen.
* Sie können über den **Index** auf einzelne Listenelementer zugreifen. 
* Sie können eine **for-Schleife mit Liste** programmieren.
* Sie wissen, wie die Fachbegriffe der einzelnen Bestandteil der Schleife
  lauten:
  * **Kopfzeile**, wird mit **Doppelpunkt :** abgeschlossen
  * Schlüsselwörter **for** und **in**
  * **Schleifenvariable**  
* Sie wissen, dass der Anweisungsblock des Schleifeninneren eingerückt werden
  muss. Die **Einrückung** muss immer mit der gleichen Anzahl von Zeichen
  (Leerzeichen oder Tab) erfolgen.
```


## Datentyp Liste

Eine Liste ist eine Sammlung von Objekten. Dabei können die Objekte einen
beliebigen Datentyp aufweisen. Eine Liste wird durch eckige Klammern erzeugt.

Beispielsweise könnte eine Liste drei Integer enthalten:

```{code-cell} ipython3
a = [34, 12, 54]
print(a)
```

Das folgende Beispiel zeigt eine Liste mit vier Namen, die durch Strings
repräsentiert werden:

```{code-cell} ipython3
a = ['Alice', 'Bob', 'Charlie', 'Dora']
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

Listen können gekürzt und erweitert werden. Eine sehr nützliche Funktion ist
daher die `len()`-Funktion. Das `len` steht dabei für `length`. Wird die
Funktion `len()` mit einer Liste (oder mit einem String) als Argument
aufgerufen, gibt sie die Anzahl der Listenelemente (oder Anzahl der Zeichen im
String) zurück.

```{code-cell} ipython3
a = ['Hund', 'Katze', 'Maus', 'Affe','Elefant']
len(a)
```

Listen müssen nicht nur Elemente eines Datentyps enthalten. In Python ist es
erlaubt, in eine Liste Objekte mit verschiedenen Datentypen zu sammeln. Das
folgende Beispiel zeigt eine Mischung aus Elementen der drei Datentypen Integer,
Float und String.

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

## Listen bearbeiten

Listen sind in Python veränderlich. Besonders häufig kommt es vor, dass zwei
Listen zu einer neuen Liste kombiniert werden sollen. Da diese Aktion so wichtig
ist, kann dies in Python direkt mit dem `+`-Operator erledigt werden. Der
Fachbegriff für das Aneinanderhängen von Listen ist **Verkettung** oder auf
Englisch **Concatenation**.

```{code-cell} ipython3
a = [37, 3, 5] + [3, 35, 100]
print(a)
```

Um an das Ende der Liste ein neues Element einzufügen, verwendet man die Methode
`append()`. Eine **Methode** ist eine spezielle Funktion, die zu dem Datentyp
gehört und daher an die Variable angehängt wird, indem man einen Punkt schreibt
und dann den Methodennamen.

```{code-cell} ipython3
a = [34, 56, 23]
print(a)

a.append(42)
print(a)
```

Aus der Liste können Elemente durch die `remove()`-Methode gelöscht werden.
Dabei wird das Element, das gelöscht werden soll, der Methode als Argument
übergeben. Es wird der erste auftretende Wert aus der Liste gelöscht.

```{code-cell} ipython3
a = [34, 56, 23, 42]
print(a)

a.remove(56)
print(a)
```

```{admonition} Mini-Übung
:class: miniexercise
Nehmen Sie Ihre Einkaufsliste für den Obsalat von vorhin. Fügen Sie noch Zimt und Zucker hinzu. Leider passen in Ihren Einkaufswagen nur maximal 5 Sachen. Lassen Sie daher die Anzahl der Elemente ausgeben.
```

```{code-cell} ipython3
# Hier Ihr Code:
```

````{admonition} Lösung
:class: minisolution, toggle
```python
einkaufsliste_alt = ['Apfel', 'Banane', 'Trauben', 'Joghurt']
einkaufsliste_neu = einkaufsliste_alt + ['Zimt', 'Zucker']
anzahl_zutaten = len(einkaufsliste_neu)
print(f'Anzahl der Zutaten: {anzahl_zutaten}')
```
````

```{dropdown} Video zu "Listen in Python - Einführung" von Programmieren lernen
<iframe width="560" height="315" src="https://www.youtube.com/embed/ihF8bZoauBs" 
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; 
clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen>
</iframe>
```

## Zugriff auf einzelne Listenelemente

Listen sind (übrigens genau wie Strings) ein sogenannter **sequentieller
Container**. Sequentielle Container sind Sammlungen von Datenobjekten. Was heißt
das? Eine Straße ist eine Sammlung von Häusern. Aber in einer Straße sind die
Häuser zusätzlich durchnummeriert. Eine Hausnummer ermöglicht es, die Position
eines Hauses innerhalb der Straße zu bestimmen. Sammlungen von Objekten mit
einer Positionsnummer werden sequentielle Container genannt. Sie sind mit ganzen
Zahlen, also Integern, durchnummeriert. In Python beginnt die Nummerierung bei
0. Die Nummer eines Elementes aus der Sequenz nennt man **Index**.
Umgangssprachlich könnte man den Index also auch als Hausnummer bezeichnen.

In einer Liste hat also das erste Element den Index 0. Das zweite Element hat
den Index 1 usw. Um ein einzelnes Element einer Liste herausgreifen zu können,
schreibt man `liste[i]`. Dabei ist `liste` der Name der Liste und `i` der Idnex.
Um einfach auf das letzte Element einer Liste zugreifen zu können, hat Python
den Index -1 eingeführt.

Probieren wir ein Beispiel aus:

```{code-cell} ipython3
a = [34, 56, 23, 42]
erstes = a[0]
print(f'Das erste Element in der Liste ist: {erstes}')
```

```{code-cell} ipython3
# Erzeugung Liste
meine_liste = ['rot', 'grün', 'blau', 'gelb', 'weiß', 'schwarz']

# das fünfte Elment weiß wird durch lila ersetzt
meine_liste[4] = 'lila'
print(meine_liste)
```

Das Bearbeiten von einzelnen Listenelementen wird auch **Zugriff** genannt. Das
folgende Video zeigt die Zugriffsmöglichkeiten von Listen.

```{dropdown} Video zu "Zugriff aus Listen" von Programmieren lernen
<iframe width="560" height="315" src="https://www.youtube.com/embed/_XzWPXvya2w" 
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; 
clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen>
</iframe>
```


## Code wiederholen mit der for-Schleife

Manchmal möchte man für jedes Element einer Liste eine oder mehrere Aktionen
durchführen. Dazu gibt es die **for-Schleife**. 

```{code-cell} ipython3
for i in [2, 4, 6, 8, 10]:
    print(i)
```

Eine Schleife beginnt mit dem Schlüsselwort **for**. Danach kommt der Name der
sogenannten **Schleifenvariable**, in diesem Fall also `i`. Als nächstes folgt
wieder ein Schlüsselwort, nämlich **in** und zuletzt Liste. Diese Zeile nennt
man **Kopfzeile**.

Python muss wissen, welche Kommandos für jeden Schleifendurchgang ausgeführt
werden sollen. Daher wird die Kopfzeile der Schleife mit einem Doppelpunkt `:`
beendet. Danach werden alle Kommandos aufgelistet, die ausgeführt werden sollen.
Damit Python weiß, wann es wieder mit dem normalen Programm weitergehen soll,
müssen wir dem Python-Interpreter das Ende der Schleife signalisieren. In vielen
Programmiersprachen wird das mit dem Schlüsselwort `end` gemacht oder es werden
Klammern gesetzt. In Python wird stattdessen mit **Einrückung** gearbeitet. Alle
Zeilen mit Anweisungen, die eingerückt sind, werden in der Schleife wiederholt.

Wie sieht das nun bei unserem Beispiel aus? Die Schleifenvariable heißt `i`. Sie
nimmt beim 1. Schleifendurchgang den Wert `2` an. Dann werden die Anweisungen im
Schleifeninneren ausgeführt, also die print()-Funktion für `i = 2` angewendet
und eine 2 ausgegeben. Dann wird die Schleife ein 2. Mal durchlaufen. Diesmal
nimmt die Schleifenvariable `i` den Wert `4` an und die print()-Funktion gibt 4
aus. Das geht so weiter bis zum 5. Schleifendurchgang, wo die Schleifenvariable
den Wert `i = 10` annimmt und eine 10 auf dem Bildschirm angezeigt wird. Da die
`10` das letzte Element der Liste war, macht der Python-Interpreter mit dem
normalen Programm weiter. Bei unserem kurzen Beispiel ist aber schon das Ende
des Programmes erreicht. Zusammengefasst, werden nacheinander die Elemente der
Liste `[2, 4, 6, 8, 10]` auf dem Bildschirm ausgegeben.

Schauen wir uns ein erstes Beispiel an. Jedes Element der Liste `[4,5,7,11,21]`
soll um 2 erhöht werden.

```{code-cell} ipython3
for zahl in [4,5,7,11,21]:
    summe = zahl + 2
    print(f'Wenn ich {zahl} + 2 rechne, erhalte ich {summe}.')
print('Ich bin fertig!')
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

```{dropdown} Video zu "Schleifen in Python: for-Schleife" von Programmieren lernen
<iframe width="560" height="315" src="https://www.youtube.com/embed/ISo1uqLcVw8" 
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; 
clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen>
</iframe>
```

Es kommt sehr häufig vor, dass über Listen mit Zahlen iteriert werden soll.
Dafür stellt Python3 die Funktion `range()`zur Verfügung.

```{code-cell} ipython3
for zahl in range(3):
    print(zahl)
print('Fertig!')
```

Wird `range(endzahl)` mit nur einem Parameter aufgerufen, dann beginnt der
Python-Interpreter stets von `0` an zu zählen. Dabei ist die `endzahl` nicht
inkludiert, d.h. der Python-Interpreter stoppt bei `endzahl - 1`. Es ist auch
möglich, eine Startzahl vorzugeben, also:

```{code-cell} ipython3
for zahl in range(1,4):
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

Durch Angabe einer negativen Schrittweite kann auch rückwärts gezählt werden:

```{code-cell} ipython3
for zahl in range(13, 3, -2):
    print(zahl)
print('Fertig!')
```

Zum Abschluss folgt hier noch ein weiteres Video zu for-Schleifen.

```{dropdown} Video zu "for-Schleife in Python: Zählerschleife"
<iframe width="560" height="315" src="https://www.youtube.com/embed/pQh5Idw2sKM" 
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; 
clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen>
</iframe>
```

## Zusammenfassung und Ausblick

In diesem Abschnitt haben wir uns mit dem Datentyp Liste befasst, der zur
Sammlung verschiedener Datenobjekte dient. Für die sequentielle Bearbeitung von
Listenelementen ist die for-Schleife besonders geeignet. Es existieren
zusätzliche Datentypen wie Dictionary, Tupel und Set, die sich ebenfalls zum
Speichern von Datenobjekten eignen. Neben der for-Schleife gibt es eine
alternative Schleifenstruktur, die while-Schleife, die Code wiederholt, solange
eine bestimmte Bedingung erfüllt ist. Anstatt uns weiterhin auf solche Aspekte
der Python-Programmierung zu konzentrieren, werden wir im nächsten Kapitel den
Fokus auf die Implementierung eigener Funktionen legen und einen kurzen Ausflug
in die objektorientierte Programmierung unternehmen.


