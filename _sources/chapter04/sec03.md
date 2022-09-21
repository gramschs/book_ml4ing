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


# Statistik mit Pandas


## Lernziele

```{admonition} Lernziele
:class: hint
* TODO
```

## Import von Tabellen

Um Tabellen im csv- einzulesen, bietet Pandas eine eigene Funktion namens
`read_csv` an (siehe
[Dokumentation/read_csv](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)).
Wird diese Funktion verwendet, um die Daten zu importieren, so wird automatisch
ein DataFrame-Objekt erzeugt. Beim Aufruf der Funktion wird der Dateiname
übergeben. 

Wir probieren es mit der Datei `bundesliga_top7_offensive.csv`, die von
[Kaggle](https://www.kaggle.com/rajatrc1705/bundesliga-top-7-teams-offensive-stats?select=bundesliga_top7_offensive.csv)
stammt. In dem Datensatz sind die Spielerdaten zu den Top7-Fußballvereinen der
Bundesligasaison 2020/21 enthalten. 

Laden Sie sich die csv-Datei
[hier](https://nextcloud.frankfurt-university.de/s/yJjkkMSkWqcSxGL) herunter und
speichern Sie sie in denselben Ordner, in dem auch dieses JupyterNotebook liegt.
Führen Sie dann anschlißend die folgende Code-Zelle aus.

```{code-cell} ipython
import pandas as pd
data = pd.read_csv('bundesliga_top7_offensive.csv')
```

Es erscheint keine Fehlermeldung, aber den Inhalt der geladenen Datei sehen wir
trotzdem nicht. Dazu verwenden wir die Methode `.head()`.

```{code-cell} ipython
data.head()
```

Die Methode `.head()` zeigt uns die ersten fünf Zeilen der Tabelle an. Wenn wir beispielsweise die ersten 10 Zeilen anzeigen lassen wollen, so verwenden wir die Methode `.head(10)`mit dem Argument 10.


```{code-cell} ipython
data.head(10)
```

## Übersicht verschaffen mit info und describe

Das obige Beispiel zeigt uns zwar nun die ersten 10 Zeilen des importierten
Datensatzes, aber wie viele Daten insgesamt enthalten sind, welche Vereine noch
kommen usw. können wir mit der `.head()`-Methode nicht erfassen. Dafür stellt
Pandas die beiden Methoden `.info()` und `.describe()`zur Verfügung. Probieren
wir es einfach aus.

```{code-cell} ipython
data.info()
```

Mit `.info()` erhalten wir eine Übersicht, wie viele Spalten es gibt und auch
die Spaltenüberschriften werden aufgelistet. Dabei sind Überschriften wie Name
selbsterklärend, aber was xG bedeutet, erchließt sich nicht von selbst. Dazu
brauchen wir mehr Informationen von den Autor:innen der Daten.

Weiterhin entnehmen wir der Ausgabe von `.info()`, dass in jeder Spalte 177
Einträge sind, die 'non-null' sind. Damit ist gemeint, dass diese Zellen beim
Import nicht leer waren. Zudem wird bei jeder Spalte noch der Datentyp
angegeben. Für die Namen, die als Strings gespeichert sind, wird der allgemeine
Datentyp 'object' angegeben. Beim Alter/Age wurden korrektweise Integer erkannt
und die mittlere erwartete Anzahl von Toren pro Spiel 'xG' (= expected number of
goals from the player in a match) wird als Float angegeben.


## noch mehr ...
Analog zu den statistischen Kennzahlen bei Series-Objekten gibt auch hier einige Methoden zur Beschreibung des Datensatzes. Wir beschäftigen uns im Folgenden mit

* ``.info()``
* ``.describe()``
* ``.sum()``
* ``.mean()``
* ``.std()``
* ``.min()``
* ``.max()``
* ``.plot(kind='line')``
* ``.plot(kind='bar)``

```{code-cell} ipython3
alter = pd.Series({"Alice" : 25, "Bob" : 22, "Charlie": 19, "Dora" : 30, "Emil": 43})
stadt = pd.Series({"Alice" : "Mannheim", "Bob" : "Frankfurt", "Charlie" : "Ludwigshafen", "Dora" : "Kaiserslautern", "Emil": "Darmstadt"})
note  = pd.Series({'Alice': 1.3, 'Bob': 3.7, 'Charlie': 2.0, 'Dora': 1.7, 'Emil': 5.0})

personen = pd.DataFrame({'Alter': alter, 'Wohnort': stadt, 'Note': note})
personen
```

```{code-cell} ipython3
personen.info()
```

```{code-cell} ipython3
personen.describe()
```

```{code-cell} ipython3
personen.sum()
```

```{code-cell} ipython3
personen.mean()
```

```{code-cell} ipython3
personen.std()
```

```{code-cell} ipython3
personen.min()
```

```{code-cell} ipython3
personen.max()
```

```{code-cell} ipython3
personen.plot(kind='bar')
```

```{code-cell} ipython3
personen.plot(kind='line')
```

**Mini-Übung:**   

Laden Sie - falls nicht schon geschehen - den Datensatz zu den Top7 der
Fußball-Bundesliga 2020/21. Beantworten Sie folgende Fragen:

* Welcher Spieler war in dieser Saison der jüngste und wie heißt er?
* Bei welchem Verein spielt der älteste Spieler?
* Filtern Sie den Datensatz nach einem der Vereine ('Bayern Munich', 'Borussia
  Dortmund', 'RB Leipzig', 'Wolfsburg', 'Eintracht Frankfurt', 'Bayer
  Leverkusen', 'Union Berlin').
* Lassen Sie sich die Infos dieses Vereines ausgeben. Wie viele Spieler spielten
  in diesem Verein?
* Wer hat die meisten Minuten gespielt? Sortieren Sie das DataFrame-Objekt nach
  der Anzahl der Minuten und visualisieren Sie die Minuten pro Spieler sortiert.
* Visualisieren Sie die Anzahl der Tore? Linienplot oder Barplot?
* Was ist das mittlere Alter der Spieler?

```{code-cell} ipython3
# Hier Ihr Code

```


**Mini-Übung**   

Der folgende Datensatz stammt von Kaggle, siehe
https://www.kaggle.com/rajatrc1705/bundesliga-top-7-teams-offensive-stats?select=bundesliga_top7_offensive.csv
. Er enthält die Spielerdaten zu den Top7-Fußballvereinen der Bundesligasaison
2020/21. Laden Sie ihn mit dem Befehl

> data = pd.read_csv('part06_data/bundesliga_top7_offensive.csv', index_col=0)



* Zeigen Sie zunächst den Inhalt der eingelesenen Daten an. Benutzten Sie dazu
  den Befehl
> data.head(10) um die ersten 10 Zeilen anzuzeigen.

* Anschließend zeigen Sie das Alter aller Eintracht Frankfurt Spieler an. Der
  Index beginnt bei Kevin Trapp und endet Ragnar Ache, die Spalte heißt 'Age'.

* Zuletzt zeigen Sie die roten und gelben Karten von Maximilian Arnold an.