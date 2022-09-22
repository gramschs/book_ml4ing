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