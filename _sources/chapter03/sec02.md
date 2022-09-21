---
jupytext:
  formats: ipynb,md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.13.8
kernelspec:
  display_name: Python 3.9.13 ('python39')
  language: python
  name: python3
---

# Funktionen

## Lernziele

```{admonition} Lernziele
:class: hint
* Definition einer Funktion
* Funktionen mit Eingabeparametern
* Funktionen mit Eingabeparametern und einem Rückgabewert
* Funktionen mit Eingabeparametern und mehreren Rückgabewerten
* Funktionen: Vorsicht mit lokalen Variablen
```

## Funktionen

Eine Funktion ist eine Zusammenfassung von Code, der eine bestimmte Teilaufgabe
löst. Dabei arbeitet die Funktion nach dem EVA-Prinzip. Die Funktion übernimmt
Objekte als Eingabe, verarbeitet diese und liefert Objekte als Ergebnis zurück.
Wie die Funktion dabei im Inneren genau funktioniert (Verarbeitung), ist
unwichtig.

Beispielsweise gibt es im Modul `math` die Funktion `sqrt()`. Wir wissen, dass
wir der Funktion eine Zahl übergeben müssen (Eingabe), z.B. `sqrt(5)`. Die
Funktion liefert dann als Ergebnis $\sqrt{5}$ zurück. Welches Verfahren zur
Berechnung der Wurzel verwendet wurde, wissen wir nicht. 

Insbesondere muss die Teilaufgabe, die die Funktion löst, nichts mit Mathematik
zu tun haben. Eine Funktion in der Informatik hat nichts mit einer
mathematischen Funktion zu tun, auch wenn oft mathematische Funktionen als
Beispiel verwendet werden. Ein Beispiel für eine nicht-mathematische Funktion
haben Sie mit `print()` bereits kennengelernt.

### Die Benutzung von Funktionen (oder der Aufruf von Funktionen)

Der Aufruf einer Funktion hat folgende Syntax:

```code
funktion( argument1, argument2, ...)
```

Eine Funktion wird benutzt, indem man den Namen der Funktion hinschreibt und
dann in runden Klammern ihre Parameter, die sogenannten Argumente der Funktion.
Welche Argumente für eine Funktion verwendet werden dürfen, hängt von der
Implementierung der Funktion ab.

Beispielsweise kann als Argument für die `len()`-Funktion ein String übergeben
werden oder eine Liste. Stellen Sie eine Vermutung auf: was bewirkt die
`len()`-Funktion?

```{code-cell} ipython3
len('Hallo')
```

```{code-cell} ipython3
len([1,2,3,4,8,2])
```

In der Regel geben Funktionen wieder Ergebnisse zurück. Diese können einer
Variable zugewiesen werden, um mit dem Ergebnis weiter zu arbeiten.

```{code-cell} ipython3
laenge1 = len('Hallo')
laenge2 = len(['Apfel', 'Banane', 'Erdbeere'])

if laenge1 < laenge2:
    print('Das Wort Hallo enthält weniger Buchstaben als Früchte im Obstsalat.')
else:
    print('Das Wort Hallo enthält mehr Buchstaben als Einträge in der Liste.')
```

### Definition von einfachen Funktionen

Die allgemeine Syntax zur Definition einer eigenen Funktion sieht wie folgt aus:

```python
def meine_funktion():
    """Optionaler Docstring zur Erklärung."""

    # Implementierung der Funktion
    anweisung01
    anweisung02
     ...

```

Erstes Beispiel:

Die folgende Funktion hat keine Eingabewerte (Argumente, Input) und keine
Rückgabe (Ausgabe, Return-Value).


```{code-cell} ipython3
def gruesse_ausrichten():
    print('Ich grüße Sie!')
```

Nachdem die Funktion `gruesse_ausrichten()` so implementiert wurde, können wir
sie im Folgenden direkt verwenden.

```{code-cell} ipython3
gruesse_ausrichten()
```

Und natürlich kann man sie in Programmverzweigungen und Schleifen einbauen.

```{admonition} Mini-Übung
:class: miniexercise
Lassen Sie 10x Grüße ausrichten.
```

```{code-cell} ipython3
# Hier Ihr Code:
```

<iframe width="560" height="315" src="https://www.youtube.com/embed/LQCfN5HS9xI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Funktionen mit Parametern

Meistens haben Funktionen Argumente, um Eingaben/Input entgegennehmen und
verarbeiten zu können. Das Argument wird bei der Implementierung der Funktion
mit einem Platzhalter/Variable eingeführt. 

Die allgemeine Syntax zur Definition einer eigenen Funktion mit Parametern sieht
wie folgt aus:

```python
def meine_funktion(arg1, arg2, ..., argn):
    """Optionaler Docstring zur Erklärung."""

    # Implementierung der Funktion
    anweisung01
    anweisung02
     ...

```

```{code-cell} ipython3
def gruesse_ausrichten_mit_parameter(name):
    print('Ich grüße', name)
```

Der Aufruf einer Funktion ohne passende Argumente führt zu einer Fehlermeldung.
Entfernen Sie das Kommentarzeichen `#` und führen Sie die nachfolgende
Code-Zelle aus:

```{code-cell} ipython3
#gruesse_ausrichten_mit_parameter()
```

Daher müssen wir die modifizierte Funktion nun wie folgt aufrufen:

```{code-cell} ipython3
gruesse_ausrichten_mit_parameter('Bob')
```

Die Funktion `gruesse_ausrichten_mit_parameter()` hat aber keinen Rückgabewert.
Das können wir wie folgt testen:

```{code-cell} ipython3
x = gruesse_ausrichten_mit_parameter('Alice')
type(x)
```

`x` ist vom Typ `NoneType` oder anders ausgedrückt, es hat keinen Datentyp. 

Sind Funktionen ohne Rückgabewert sinnvoll?

Ja, denn so können Codeblöcke vereinfacht werden. Sollte in einem Programm Code
mehrmals ausgeführt werden, lohnt es sich, diesen in eine Funktion auszulagern,
um diese einfach aufrufen zu können.


````{admonition} Mini-Übung
:class: miniexercise
Schreiben Sie eine Funktion mit zwei Parametern, nämlich Vor- und Nachname. Wenn 
die Funktion z.B. mit `(Alice, Miller)` aufgerufen wird, soll sie Folgendes auf 
dem Bildschirm ausgeben:

```code
Vorname: Alice
Nachname: Miller
```
````

```{code-cell} ipython3
# Hier Ihr Code:
```

<iframe width="560" height="315" src="https://www.youtube.com/embed/af9ORp1Pty0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Funktionen mit Rückgabewert

In der Regel jedoch haben Funktionen einen Rückgabewert.

### Funktion mit einem Rückgabewert

Die allgemeine Syntax zur Definition einer eigenen Funktion mit Parametern und
Rückgabewert sieht wie folgt aus:

```python
def meine_funktion(arg1, arg2, ..., argn):
    """Optionaler Docstring zur Erklärung."""

    # Implementierung der Funktion
    anweisung01
    anweisung02
     ...

    return ergebnis  # optional, die Funktion kann auch keine Rückgabe haben
```

Schauen wir uns ein Beispiel an:

```{code-cell} ipython3
def berechne_quadrat(x):
    return x*x
```

```{code-cell} ipython3
berechne_quadrat(7)
```

```{code-cell} ipython3
for x in range(1,11):
    y = berechne_quadrat(x) 
    ausgabe = '{} * {} = {}'.format(x, x, y)
    print(ausgabe)
```

Hier ein Beispiel mit mehreren Argumenten.

```{code-cell} ipython3
def berechne_rechteck_flaeche(a,b):
    flaeche = a*b
    return flaeche

# main program

# Eingabe
a = 5
b = 3

# Verarbeitung
flaeche = berechne_rechteck_flaeche(a,b)

# Ausgabe
print('berechnete Fläche: ', flaeche)
```

### Funktionen mit mehreren Rückgabewerten

```python
def funktion(arg1, arg2, ...):
    # Verarbeitung
    anweisung01
    anweisung02
    ...
    
    return ergebnis1, ergebnis2
```

Es ist auch möglich, mehrere Ergebnisse gleichzeitig zurückzugeben. Diese werden
einfach nach dem Schlüsselwort `return` mit Kommas getrennt gelistet. 

```{code-cell} ipython3
def potenzen_bis_vier(x):
    x_hoch_2 = x**2
    x_hoch_3 = x**3
    x_hoch_4 = x**4
    return x_hoch_2, x_hoch_3, x_hoch_4
```

```{code-cell} ipython3
for x in range(1,11):
    print(potenzen_bis_vier(x))
```

```{code-cell} ipython3
for x in range(1,5):
    potenz2, potenz3, potenz4 = potenzen_bis_vier(x)
    print('Die 2. Potenz von {} ist {}, die dritte ist {} und die vierte ist {}.'.format(x, potenz2, potenz3, potenz4))
```

<iframe width="560" height="315" src="https://www.youtube.com/embed/ehSP-sYoKCY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Vorsicht bei der Ausführung von Funktionen: lokale und globale Variablen

Schauen Sie sich bitte folgende Funktionsimplementierung an. Was macht die
Funktion?

```{code-cell} ipython3
def erhoehe_um_eins(x):
    x = x + 1
```

```{code-cell} ipython3
x = 17
print(x)

# jetzt Funktion anwenden
print('jetzt Funktion auf x anwenden...')
erhoehe_um_eins(x)
print(x)
```

Wir schauen in die Funktion "hinein", um zu sehen, ob vielleicht gar nicht
erhöht wurde.

```{code-cell} ipython3
def erhoehe_um_eins(x):
    print('in der Funktion vor der Erhöhung:')
    print(x)
    
    # Erhöhung
    x = x + 1
    
    print('in der Funktion nach der Erhöhung:')
    print(x)    
```

```{code-cell} ipython3
x = 17
print(x)

# jetzt Funktion anwenden
print('jetzt Funktion auf x anwenden...')
erhoehe_um_eins(x)
print(x)
```

Was ist passiert? Die Variable `x` in der Funktion ist eine lokale Variable. Es
ist Zufall, das sie so heißt, wie die Variable außerhalb der Funktion. Ein
Programmierer einer Funktion kann nicht vorab wissen, wie alle anderen Variablen
genannt werden. Daher müssen alle Variablen in der Funktion lokal bleiben, um
nicht unabsichtlich Variablen, die dummerweise oder absichtlich den gleichen
Namen tragen, zu verändern.

Möchte man erreichen, dass eine Funktion den Wert einer Variable ändert, kann
man dies über die Rückgabe und explizite Zuweisung erreichen.

```{code-cell} ipython3
def erhoehe_um_eins(x):
    x = x + 1
    return x

x = 17
print('vorher', x)
 
x = erhoehe_um_eins(x)
print('nachher', x)
```

