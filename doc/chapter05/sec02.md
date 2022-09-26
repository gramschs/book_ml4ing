---
jupytext:
  formats: ipynb,md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.0
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

# Visualisierung von DataFrames

## Lernziele

```{admonition} Lernziele
:class: hint
* TODO
```

Aber wie kombinieren wir jetzt die Funktionalitäten des Pandas-Moduls mit denen
des Matplotlib-Moduls? Der grundlegende Datentyp für Matplotlib ist das
NumPy-Array und auch in den Pandas-Datenobjekten stecken im Kern NumPy-Arrays.
Wenn wir also Pandas-Objekte visualisieren wollen, extrahieren wir die Daten als
NumPy-Arrays und plotten dann diese mit Matploblib.

Wir benutzen die folgenden Methoden: 

* ``.index`` liefert den Zeilenindex
* ``.columns`` liefert die Spaltennamen 
* ``.values`` liefert die Werten in der Tabelle als NumPy-Array

Hier ein Beispiel:

```{code-cell}
import pandas as pd

alter = pd.Series({"Alice" : 25, "Bob" : 22, "Charlie" : 30, "Dora": 43})
stadt = pd.Series({"Alice" : "Mannheim", "Bob" : "Frankfurt", "Charlie" : "Ludwigshafen", "Dora" : "Kaiserslautern"})
personen = pd.DataFrame({'Alter': alter, 'Wohnort': stadt})

print('Datentyp personen: ', type(personen) )
print('Inhalt personen: ', personen)
print('\n')

print('Datentyp personen.index: ', type(personen.index))
print('Inhalt personen.index', personen.index)
print('\n')

print('Datentyp personen.columns: ', type(personen.columns))
print('Inhalt personen.columns', personen.columns)
print('\n')

print('Datentyp personen.values: ', type(personen.values))
print('Inhalt personen.values', personen.values)
print('\n')
```

So kann man direkt die Daten aus einem Pandas-Dataframe extrahieren und visualisieren.

```{code-cell}
x = personen.index
y = personen.loc[:, 'Alter'].values

fig, ax = plt.subplots()
ax.bar(x,y)
ax.set_ylabel('Alter')
ax.set_title('Personen aus meinem Adressbuch');
```

## Plot von Mittelwert und Standardabweichung
