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

# Bool, Vergleiche und Programmverzweigung

## Lernziele

```{admonition} Lernziele
:class: hint
* Sie kennen den Datentyp **Bool**.
* Sie kennen die wichtigsten **Vergleichsoperatoren**.
* Sie können mit **if — elif — else** Programmverzeigungen programmieren.
```

## Datentyp Bool und Vergleiche

Später möchten wir Werte miteinander vergleichen. Ein simples Beispiel für einen
einfachen Vergleich ist beispielsweise das Alter einer Person mit der Zahl 18.
Dieser Vergleich ist entweder wahr (True) oder falsch (False). Oder anders
formuliert, diese Bedingung ist entweder erfüllt oder nicht erfüllt. 

Um den Wahrheitswert eines Vergleichs zu beschrieben, hat Python einen eigenen
Datentyp namens `bool`. Eine Variable des Datentyps `bool` kann dabei nur zwei
verschiedene Werte annehmen, nämlich

* `True`: Wahrheitswert ist wahr oder
* `False`: Wahrheitswert ist falsch.

Und auch für diesen Datentyp gibt es Operationen, wie man diese einsetzt ist
eine andere Frage.

```{code-cell} ipython3
True + True
```

```{code-cell} ipython3
False / True
```

Ein Vergleich ist ein Ausdruck mit zwei Operanden und einem Vergleichsoperator
in der Mitte. Die beiden Operanden können auch unterschiedliche Datentypen
haben, dann muss der Vergleichsoperator aber sinnvoll für diese Datentypen
definiert sein. Z.B. darf man einen Integer mit einem Float vergleichen `3 <
17.2`, aber `3 < 'vier'`ist nicht sinnvoll und undefiniert. Es gibt die
folgenden Vergleichsoperatoren in Python:

* `<` kleiner
* `<=` kleiner oder gleich
* `>` größer
* `>=` größer oder gleich
* `==`gleich
* `!=` ungleich
* `not` Umkehrung/Verneinung

Im interaktiven Modus können wir leicht den Wahrheitsgehalt von Vergleichen
überprüfen.

```{code-cell} ipython3
x = 30          
x > 15          
```

```{code-cell} ipython3
x > 42
```

```{code-cell} ipython3
x == 30    
```

```{code-cell} ipython3
x == 42
```

```{code-cell} ipython3
not x == 42 
```

```{code-cell} ipython3
x != 42
```

```{code-cell} ipython3
x > 30  
```

```{code-cell} ipython3
x >= 30
```

<iframe width="560" height="315" src="https://www.youtube.com/embed/ucsv_Nhhxmk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

+++

## Programmverzweigungen: if — elif — else 

Bei einer Programmverzweigung wird Code abhängig von einer Bedingung ausgeführt.
Dabei kann es sich um einfache Verzweigung wie die Frage: Gehe ich nach rechts
oder gehe ich nach links? Oder die Verzweigung kann komplizierter geschachtelt
sein.

### if-Anweisung
Im einfachsten Fall liegt ein `if`-Block vor. Die Syntax lautet wie folgt:

```python
if bedingung:
    anweisungsblock
```

Ist die Bedingung erfüllt, also `True`, so wird der eingerückte Anweisungsblock
ausgeführt, ansonsten übersprungen.

Wichtig ist, dass die Anweisung oder mehrere Anweisungen (d.h. der
Anweisungsblock) eingerückt ist. Hier kommt eine Python-spezifische Eigenschaft
zum Tragen. Der Block wird nicht durch Klammern oder ein begin/end
gekennzeichnet, sondern nur durch die Einrückung. Empfehlenswert sind hier vier
Leerzeichen. Was immer man wählt, in einer Python-Datei muss stets dieselbe
Einrückungstiefe verwendet werden. Daher ist es ungünstig, Tabulatore und
Leerzeichen zu mischen, weil man bei Weitergabe des Codes nicht weiß, wie auf
dem Zielsystem die Tabulatorbreite definiert ist.

Wir betrachten nun ein Beispiel:

```{code-cell} ipython3
alter = 19
if alter >= 18:
    print('Sie dürfen Alkohol kaufen.')
print('Bananen dürfen Sie immer kaufen, egal wie alt Sie sind ...')
```

<iframe width="560" height="315" src="https://www.youtube.com/embed/b6KzYbM-Hvg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

+++

### Mehrteilige Verzweigungen mit elif und else

Es gibt auch zweiteilige Programmverzweigungen. Die Syntax wird folgendermaßen
erweitert:

```python
if bedingung:
    anweisungsblock 1
else:
    anweisungsblock 2
```

Falls die Bedingung erfüllt ist, wird der 1. Anweisungsblock ausgeführt,
ansonsten der 2. Anweisungsblock. Danach führt der Python-Interpreter alles nach
dem `if-else`-Konstrukt aus. Wichtig ist, dass `if` und `else` die gleiche
Einrückungstiefe haben genau wie die beiden Anweisungsblöcke. Bei einer
Programmverzweigung wird Code abhängig von einer Bedingung ausgeführt.

```{code-cell} ipython3
alter = 21
if alter >= 18:
    print('Sie dürfen Alkohol kaufen.')
else:
    print('Sie sind noch nicht volljährig und dürfen daher keinen Alkohol kaufen.')
print('Jetzt haben wir aber genug über den Alkoholkauf geredet...')
```

Häufig müssen mehr als zwei Fälle unterschieden werden. Wenn man beispielsweise
unterscheiden will, ob eine Zahl negativ oder positiv oder Null ist, verwendet
man zusätzlich einen elif-Zweig.

Übersichtlicher wird die Programmverzweigung mit der `if-elif-else`-Syntax. `elif`ist die Abkürzung für `else if`. Allgemein sieht das Konstrukt so aus:

```python
if bedingung 1:
    anweisungsblock 1
elif bedingung 2:
    anweisungsblock 2
elif bedingung 3:
    anweisungsblock 3
    
    ...
    
else:
    anweisungsblock n
```

```{code-cell} ipython3
a = 17
if a == 0:
    print("a ist Null.")
elif a < 0:
    print("a ist negativ.")
else:
    print("a ist positiv.")
```

<iframe width="560" height="315" src="https://www.youtube.com/embed/f3YdEdYSNdk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
