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

# DataFrames für Tabellen

## Lernziele

```{admonition} Lernziele
:class: hint
* TODO
```

## Zugriff auf Zellen mit loc

Im Folgenden betrachten wir verschiedene Möglichkeiten, um auf die Werte in
einer Zelle zuzugreifen. Wir werden uns vier Möglichkeiten ansehen:
* Zugriff auf eine einzelne Zeile, indem ein Index spezifiziert wird
* Zugriff auf mehrere Zeilen, indem eine Liste von Indizes übergeben wird
* Zugriff auf mehrere zusammenhängende Zeilen, indem ein Slice von Indizes
  übergeben wird
* Zugriff auf mehrere Zeilen, indem eine Liste mit True/False übergeben wird.

```{code-cell} ipython3
alter = pd.Series([25, 22, 43, 30], index=["Alice", "Bob", "Charlie", "Dora"])
alter
```

Zunächst greifen wir eine einzelne Zeile heraus. Dazu benutzen wir das Attribut
``.loc`` und spezifizieren mit eckigen Klammern den Index der Zeile, also
``.loc[index]``. Anders als bei den folgenden drei Zugriffsmöglichkeiten, wird
nur der Wert der Daten in der Zeile zurückgeliefert, nicht aber der dazugehörige
Index.

```{code-cell} ipython3
alter.loc['Alice']
```

```{code-cell} ipython3
alter.loc['Dora']
```

Nun erzeugen wir eine Liste von Indizes. Danach können wir aus dem
Pandas-Series-Objekt per ``.loc[liste]`` auf mehrere Zeilen zugreifen. 

```{code-cell} ipython3
frauen  = ['Alice', 'Dora']
alter.loc[frauen]
```

```{admonition} Mini-Übung
:class: miniexercise 
Erzeugen Sie analog zu dem obigen Beispiel eine Liste der Männer und geben Sie
das Alter der Männer aus.
```

```{code-cell} ipython3
# Hier Ihr Code

```

Als dritte Möglichkeit betrachten wir einen Slice, also das Herausschneiden
eines zusammenhängenden Stückes aus dem Pandas-Series-Objekt. Dazu spezifizieren
wir den Start- und den stoppindex mit einem Doppelpunkt dazwischen, also
``.loc[startindex : stoppindex]``. Das Herausschneiden von zusammenhängenden
Teilobjekten wird auch als **Slicing** bezeichnet.

```{code-cell} ipython3
alter.loc['Bob': 'Dora']
```

Als letzte Möglichkeit, um auf Zeilen in dem Pandas-Series-Objekt zuzugreifen,
betrachten wir die Übergabe eine Liste mit True/False-Werten.

```{code-cell} ipython3
filter = [True, False, False, True]
alter.loc[filter]
```

Letztere Möglichkeit wird vor allem dazu genutzt, Daten nach Eigenschaften zu
filtern. Ein simpler Vergleich des Pandas-Series-Objektes beispielsweie erzeugt
solche True/False-Objekte, die dann in einem zweiten Schritt genutzt werden
können, um das Pandas-Series-Objekt zu filtern. 

```{code-cell} ipython3
filter = alter < 28
alter.loc[filter]
```

Nachdem wir nun gelernt haben, wie auf einzelne Element des
Pandas-Series-Objektes zugegriffen wird, können wir Daten auch manipulieren.
Beispielsweise ist Charlie gar nicht 43 Jahre alt, sondern nur 42. Wir weisen
dem Objekt ``alter`` für den Index ``'Charlie'``einen neuen Wert zu:

```{code-cell} ipython3
alter.loc['Charlie'] = 42
alter
```

Oder wir wählen alle Frauen aus und machen sie drei Jahre jünger ;-)

```{code-cell} ipython3
print('Alter vor der Verjüngung: \n', alter)
alter.loc[ ['Alice', 'Dora']] = alter.loc[ ['Alice', 'Dora']] - 3
print('Alter danach: \n', alter)
```







## DataFrame erzeugen aus mehreren Series-Objekten

 Zunächst erzeugen wir zwei Series-Objekte. `alter` speichert das Alter der Personen, `wohnort` den aktuellen Wohnort.

```{code-cell} ipython3
import pandas as pd

alter = pd.Series([25, 22, 43, 30], index=["Alice", "Bob", "Charlie", "Dora"])
wohnort = pd.Series(['Frankfurt', 'Darmstadt', 'Mainz', 'Berlin'], index=["Alice", "Bob", "Charlie", "Dora"])
```

Danach führen wir die beiden Series-Objekte mit dem `concat`-Befehl zusammen zu
einem DataFrame. Dabei gibt es zwei verschiedene Möglichkeiten. Die beiden
Series-Objekte können vertikal or vhorizontal verkettet werden. Gesteuert wird
das mit der Option `axis=0` oder `axis=1`. In diesem Fall brauchen wir `axis=1`,
aber probieren Sie auch einmal die andere Option aus um zu sehen, was sie
bewirkt.

```{code-cell} ipython3
personen = pd.concat([alter, wohnort], axis=1)
print(personen)
```

Was jetzt noch fehlt ist eine Beschriftung der Spalten. Das geht am einfachsten,
wenn man den Series-Objekten Namen gibt, bevor der concatenate-Befehl ausgeführt
wird.

```{code-cell} ipython3
alter = pd.Series([25, 22, 43, 30, 6], index=["Alice", "Bob", "Charlie", "Dora", "Emil"], name='Alter')
wohnort = pd.Series(['Frankfurt', 'Darmstadt', 'Mainz', 'Berlin', 'Frankfurt'], index=["Alice", "Bob", "Charlie", "Dora", "Emil"], name='Wohnort')
personen = pd.concat([alter, wohnort], axis=1, keys=['Alter','Wohnort'])
print(personen)
```

## Zugriff auf Zellen

Wie bei den Pandas-Serien-Objekten können wir über das Attribut `.loc[]` auf
Zellen des Pandas-DataFrame-Objektes zugreifen.

```{code-cell} ipython3
print( personen.loc['Charlie', 'Alter'] )
```

Auch der schreibende Zugriff erfolgt analog zu den Zugriffsmöglichkeiten bei
Pandas-Series-Objekten.

```{code-cell} ipython3
personen.loc['Charlie', 'Alter'] = 44
print(personen)
```

Auf einen zusammenhängenden Bereich wird durch Slicing zugegriffen. Dabei kann
das Slicing für die Zeilen (index), die Spalten (columns) oder beides benutzt
werden.

```{code-cell} ipython3
tmp = personen.loc['Bob' : 'Dora', 'Alter']
print(tmp)
```

```{code-cell} ipython3
tmp = personen.loc['Bob', 'Alter':'Wohnort']
print(tmp)
```

Beim Slicing können wir den Startwert oder den Stoppwert oder beides weglassen.
Wenn wir den  Startwert weglassen, fängt der Slice von vorne an. Lassen wir den
Stoppert weg, geht der Slice bis zum Ende. Das nutzen wir, um auf eine ganze
Spalte zuzugreifen:

```{code-cell} ipython3
tmp = personen.loc[ 'Bob' , :]
print(tmp)
```

Sollen dahingegen mehrere Zellen gleichzeitig ausgewählt werden, die nicht
zusammenhängen, benutzt man Listen. Wiederum können die Listen für den index
oder die columns oder beides gemischt spezifiziert werden.

```{code-cell} ipython3
tmp = personen.loc[ ['Bob', 'Dora','Emil'] , 'Alter']
print(tmp)
```

Als nächstes fügen wir unserer Personen-Tabelle eine neue Spalte hinzu. In der
neuen Spalte soll die Note der letzten Klausur stehen. Dazu erzeugen wir
zunächst wieder einmal ein Pandas-Series-Objekt. Danach weisen wir das
Series-Objekt dem DataFrame-Objekt spalten weise zu, indem wir den neuen Namen
dem `.loc`-Attribut mitgeben.

```{code-cell} ipython3
note = pd.Series({'Alice': 1.3, 'Bob': 3.7, 'Charlie': 2.0, 'Dora': 1.7, 'Emil': 5.0})
note
```

```{code-cell} ipython3
personen.loc[:, 'Note'] = note
print(personen)
```
