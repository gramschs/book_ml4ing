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


# Series für Datenreihen

## Lernziele

```{admonition} Lernziele
:class: hint
* Sie können **Pandas** mit der üblichen Abkürzung pd importieren.
* Sie können aus einer Liste das Datenobjekt **Series** erzeugen.
* Sie können auf Elemente eines Series-Objektes lesend und schreibend zugreifen:
  * Zugriff auf eine einzelne Zeile, indem ein Index spezifiziert wird
  * Zugriff auf mehrere Zeilen, indem eine Liste von Indizes übergeben wird
  * Zugriff auf mehrere zusammenhängende Zeilen, indem ein Slice von Indizes
    übergeben wird
* Sie können ein Series-Objekt nach einer Eigenschaft filtern.
```

## Import von pandas

Pandas ist eine Bibliothek zur Verarbeitung und Analyse von Daten in Form von
Datenreihen und Tabellen. Die beiden grundlegenden Datenstrukturen sind
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
Die Datenstruktur Series ermöglich es aber, einen *expliziten Index* zu setzen.
Über den optionalen Parameter `index=` speichern wir als Zusatzinformation noch
ab, von welcher Person das Alter abgefragt wurde. In dem Fall sind es die vier
Personen Alice, Bob, Charlie und Dora.

```{code-cell} ipython
alter = pd.Series([25, 22, 43, 30], index=["Alice", "Bob", "Charlie", "Dora"])
print(alter)
```

Jetzt ist auch klar, warum beim ersten Mal, als wir `print(alter)` ausgeführt
haben, die Zahlen 0, 1, 2, 3 ausgegeben wurden. Zu dem Zeitpunkt hatte das
Series-Objekt noch einen impliziten Index wie eine Liste. Was noch an
Informationen ausgegeben wird, ist das Attribut `dtype`. Darin gespeichert ist
der Datentyp der gespeicherten Werte. Auf dieses Attribut kann auch direkt mit
dem Punktoperator zugegegriffen werden.

```{code-cell} ipython3
print(alter.dtype)
```

Offensichtlich sind die gespeicherten Werte Integer.

```{admonition} Mini-Übung
:class: miniexercise 
Erzeugen Sie ein Series-Objekt mit den Wochentagen als Index und der Anzahl der
Vorlesungs/Übungs-Stunden an diesem Wochentag.
```

```{code-cell} ipython3
# Hier Ihr Code:

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






