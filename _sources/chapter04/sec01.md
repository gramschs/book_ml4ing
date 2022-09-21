---
jupytext:
  formats: ipynb,md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.13.8
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

# Series für eindimensionale Daten


## Lernziele

```{admonition} Lernziele
:class: hint
* TODO
```

## Import von pandas

Pandas ist eine Bibliothek zur Verarbeitung und Analyse von Daten in Form von
Tabellen und Zeitreihen. Die beiden grundlegenden Datenstrukturen sind
**Series** und **DataFrame**. Dabei wird Series für Datenreihen genommen, also
sozusagen die Verallgemeinerung von Vektoren bzw. eindimensionalen Arrays. Der
Datentyp DataFrame repräsentiert Tabllen, also sozusagen Matrizen bzw.
verallgemeinerte zweidimensionale Arrays. 

Um das Modul pandas benutzen zu können, müssen wir es zunächst importieren. Es
ist üblich, dabei dem Modul die Abkürzung **pd** zu geben, damit wir nicht immer
pandas schreiben müssen, wenn wir eine Funktion aus dem pandas-Modul benutzen.

```{code-cell} ipython
import pandas as pd # kürze das Modul pandas als pd ab, um Schreibarbeit zu sparen
```

## Series aus Liste erzeugen

Erzeugt werden kann ein Series-Objekt beispielsweise direkt aus einer Liste. Im
folgenden Beispiel haben wir Altersangaben in einer Liste, also `[25, 22, 43,
37]` und initialisieren über `Series` die Variable `alter`:

```{code-cell} ipython
alter = pd.Series([25, 22, 43, 37])
print(alter)
```

Was ist aber jetzt der Vorteil von Pandas? Warum nicht einfach bei der Liste
bleiben oder aber, wenn Performance wichtig sein sollte, ein eindimensionales
Numpy-Array nehmen? Der wichtigste Unterschied ist der **Index**.

Bei einer Liste oder einem Numpy-Array ist der Index implizit definiert. Damit
ist gemeint, dass bei der Initialisierung automatisch ein Index 0, 1, 2, 3, ...
angelegt wird. Wenn bei einer Liste `l = [25, 22, 43, 37]` auf das zweite
Element zugegriffen werden soll, dann verwenden wir den Index 1 (zur Erinnerung:
Python zählt ab 0) und schreiben

```{code-cell} ipython
l = [25, 22, 43, 37]
print("2. Element der Liste: ", l[1])
```

Das gleiche gilt für das Numpy-Array, das ebenfalls die Integer 0, 1, 2, 3
verwendet, um das folgende Array zu indizieren:

```{code-cell} ipython
import numpy as np
a = np.array([25, 22, 43, 37])
print("2. Element des Arrays: ", a[1])
```

Die Datenstruktur Series ermöglich es aber, einen expliziten Index zu setzen.
Über den optionalen Parameter `index=` speichern wir als Zusatzinformation noch
ab, von welcher Person das Alter abgefragt wurde. In dem Fall sind es die vier
Personen Alice, Bob, Charlie und Dora.

```{code-cell} ipython
alter = pd.Series([25, 22, 43, 30], index=["Alice", "Bob", "Charlie", "Dora"])
print(alter)
```





