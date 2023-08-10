---
jupytext:
  formats: ipynb,md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.7
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

# 3.3 Boxplots mit Plotly

Die wichtigsten statistischen Kennzahlen lassen sich mit einem Diagramm
visualisieren, das Boxplot genannt wird. Selten wird auch der deutsche Begriff
Kastendiagramm dafür gebraucht. In diesem Kapitel visualisieren wir nur einen
Datensatz. Die große Stärke der Boxplots ist normalerweise, die statistischen
Kennzahlen von verschiedenen Datensätzen nebeneinander zu visualisieren, um so
leicht einen Vergleich der Datensätze zu ermöglichen.


## Lernziele

```{admonition} Lernziele
:class: important
* Sie können **Plotly Express** mit der typischen Abkürzung **px** importieren.
* Sie können mit **px.box()** einen Boxplot eines Pandas-Series-Objektes
  visualisieren.
* Sie können die Beschriftung eines Boxplots verändern. Dazu gehört die die
  Beschriftung der Achsen und der Titel.
* Sie können die Datenpunkte neben einem Boxplot anzeigen lassen.
* Sie wissen, was ein **Ausreißer** ist und können Ausreißer im Boxplot anzeigen
  lassen.
```

## Plotly

Es gibt zahlreiche Python-Module, die zur Visualisierung von Daten geeignet
sind. In dieser Vorlesung verwenden wir **Plotly**. Plotly unterstützt sehr
viele verschiedene Diagrammtypen, wie auch das bekannteste Modul zur Erstellung
von Diagrammen, die sehr bekannte Python-Bibliothek **Matplotlib**. Im Gegensatz
zu Matplotlib ist Plotly jedoch interaktiv. Zusätzlich bietet Plotly das Module
**Plotly Express** an, das eine einfach zu bedienende Schnittstelle zur
Erstellung von Diagrammen zur Verfügung stellt.

Üblicherweise wird Plotly Express als `px` abgekürzt. Wir importieren das Modul
und schauen uns mit der `dir()`-Funktion an, welche Funktionalitäten Plotly
Express bietet. 

```{code-cell} ipython
import plotly.express as px

dir(px)
```

## Boxplots mit Plotly Express

Wir greifen erneut unser Autoscout24-Beispiel mit den 10 Autos auf.

```{code-cell} ipython
import pandas as pd

preisliste = [1999, 35990, 17850, 46830, 27443, 14240, 19950, 15950, 21990, 12450]
preise = pd.Series(preisliste, index = ['Audi Nr. 1', 'Audi Nr. 2', 'Audi Nr. 3', 'BMW Nr. 1', 'BMW Nr. 2', 
    'Citroen Nr. 1', 'Citroen Nr. 2', 'Citroen Nr. 3', 'Citroen Nr. 4', 'Citroen Nr. 5'])

print(preise)
```

Um einen Boxplot zu erstellen, nutzen wir die Funktion `box()` von Plotly
Express. Wir speichern das Diagramm, das durch diese Funktion erstellt wird, in
der Variablen `diagramm`. Um es dann auch nach seiner Erzeugung tatsächlich
anzeigen zu lassen, verwenden wir die Methode `.show()`. Zusammen sieht der
Python-Code zur Erzeugung eines Boxplots folgendermaßen aus:

```{code-cell} ipython
diagramm = px.box(preise)
diagramm.show()
```

Bewegen wir die Maus über dem Diagramm, so sehen wir die interaktiven
Möglichkeiten. Damit die Zahlen besser ablesbar sind, werden sie eingeblendet,
sobald wir mit dem Mauszeiger über der Box sind. Auch erscheinen rechts oben
weitere Einstellmöglichkeiten.

Die untere Antenne zeigt das Minimum an, die obere Antenne das Maximum der
Daten. Der Kasten, also die Box, wird durch das untere unteren Q1 und das obere
Quartil Q3 begrenzt. Oder anders formuliert liegen 50 % aller auftretenden
Elemente in der Box. Der Median wird durch die Linie in der Box dargestellt.

Das folgende Video erklärt, wie der Boxplot zu interpretieren ist.

```{dropdown} Video zu "Boxplot" von DATAtab
<iframe width="560" height="315" src="https://www.youtube.com/embed/1I_ma7nvKQw" 
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; 
clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen>
</iframe>
```

## Beschriftung des Boxplots verändern

Die Achsenbeschriftungen wurden automatisch gesetzt. Die x-Achse ist mit
'variable' und die y-Achse mit 'value' beschriftet. Darüber hinaus ist der Titel
der Box '0'. Das wird auch angezeigt, wenn die Maus sich über die Box bewegt.

Die 0 wird angezeigt, weil das Pandas-Series-Objekt 'preise' für den Boxplot als
Tabelle interpretiert wird und die erste Spalte den Index 0 hat. Wir können der
Spalte aber auch einen eigenen Namen geben. Am einfachsten klappt das direkt bei
der Erzeugung, indem der Parameter `name=` gesetzt wird.

```{code-cell} ipython
preisliste = [1999, 35990, 17850, 46830, 27443, 14240, 19950, 15950, 21990, 12450]
preise_mit_name = pd.Series(preisliste, index = ['Audi Nr. 1', 'Audi Nr. 2', 'Audi Nr. 3', 'BMW Nr. 1', 'BMW Nr. 2', 
    'Citroen Nr. 1', 'Citroen Nr. 2', 'Citroen Nr. 3', 'Citroen Nr. 4', 'Citroen Nr. 5'],
    name='XXS-Liste von Autoscout24')

print(preise_mit_name)
```

Der neue Name 'XXS-Liste von Autoscout24' wird zusätzlich zur Information 'dtype' angezeigt.
Damit sieht der Boxplot folgendermaßen aus:

```{code-cell} ipython
diagramm = px.box(preise_mit_name)
diagramm.show()
```

Sollen nun auch noch die Achsenbeschriftungen geändert werden, müssen wir die
automatisch gesetzten Beschriftungen durch neue Namen ersetzt werden.
Eingeleitet wird die Ersetzung durch das Schlüsselwort `labels=`. Danach steht
in geschweiften Klammern `{` und `}` der alten Name, dann folgt ein Doppelpunkt
und dann der neue Name.

```{code-cell} ipython
diagramm = px.box(preise_mit_name, labels={'variable': 'Name des Datensatzes'})
diagramm.show()
```

Sollen gleich mehrere Beschriftungen ersetzt werden, werden alle Paare mit einem
Komma getrennt aufgelistet.

```{code-cell} ipython
diagramm = px.box(preise_mit_name, labels={'variable': 'Name des Datensatzes', 'value': 'Verkaufspreis [EUR]'})
diagramm.show()
```

Fehlt noch eine Überschrift, ein Titel. Wie das englische Wort 'title' heißt
auch das entsprechende Schlüsselwort zum Erzeugen eines Titels, nämlich
`title=`.

```{code-cell} ipython
diagramm = px.box(preise_mit_name, 
              labels={'variable': 'Name des Datensatzes', 'value': 'Verkaufspreis [EUR]'},
              title='Statistische Kennzahlen als Boxplot')
diagramm.show()
```

## Datenpunkte im Boxplot anzeigen

Oft ist es wünschenswert die Rohdaten zusammen mit dem Boxplot zu visualisieren.
Das ist mit dem `points=`-Parameter recht einfach, jedoch haben wir zwei mögliche
Optionen. Wir können mit `'all'` alle Punkte anzeigen lassen oder nur die
Ausreißer (`'outliers'`).

Lassen wir zuerst alle Punkte anzeigen und setzen also `points='all'`.

```{code-cell} ipython
diagramm = px.box(preise_mit_name, 
              labels={'variable': 'Name des Datensatzes', 'value': 'Verkaufspreis [EUR]'},
              points='all')
diagramm.show()
```

Die Punkte werden links vom Boxplot platziert. Als nächstes lassen wir uns die
Ausreißer anzeigen.

```{code-cell} ipython
diagramm = px.box(preise_mit_name, 
              labels={'variable': 'Name des Datensatzes', 'value': 'Verkaufspreis [EUR]'},
              points='outliers')
diagramm.show()
```

Es sind keine Punkte zu sehen, was ist falsch? Nun, um das zu klären, müssen wir
erst einmal definieren, was ein Ausreißer ist.

## Ausreißer berechnen und visualisieren

Die Box im Boxplot enthält 50 % aller Datenpunkte, denn sie ist durch das untere
Quartil Q1 und das obere Quartil Q3 begrenzt. Die Differenz zwischen Q1 und Q3
wird **Interquartilsabstand** (manchmal auch kurz Quartilsabstand) genannt und
mit **IQR** (englisch für Interquartile Range) abgekürzt. In der Statistik
werden Punkte, die kleiner als Q1 - 1.5 IQR oder Punkte, die größer als Q3 + 1.5
IQR sind, als Ausreißer angesehen. Im Beispiel des XXS-Datensatzes der
Autopreise kommen keine Ausreißer vor, weil Minimum und Maximum noch innerhalb
dieses Bereichs liegen. Wir fügen daher noch ein neues, teureres Auto ein. Jetzt
sehen wir einen Ausreißer.

```{code-cell} ipython
preise_mit_name['BMW Nr. 3'] = 62999
diagramm = px.box(preise_mit_name, 
              labels={'variable': 'Name des Datensatzes', 'value': 'Verkaufspreis [EUR]'},
              points='outliers')
diagramm.show()
```


## Zusammenfassung und Ausblick

Der Boxplot ermöglicht eine einfache Visualisierung der wichtigsten
statistischen Kennzahlen eines Datensatzes. Seine Stärke spielt er aus, sobald
mehrere Datensätze miteinander verglichen werden sollen. Daher werden wir im
nächsten Kapitel uns mit Tabellen beschäftigen.