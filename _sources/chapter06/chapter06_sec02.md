---
jupytext:
  cell_metadata_filter: -all
  formats: ipynb,md:myst
  main_language: python
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.5
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

# 6.2 Lineare Regression mit Scikit-Learn

Im vorherigen Kapitel haben wir die theoretischen Grundlagen des lineare
Regressionsmodells kennengelernt. Nun werden wir anhand eines praktischen
Datensatzes das lineare Regressionmodell mit dem Modul Scikit-Learn
ausprobieren.


## Lernziele

```{admonition} Lernziele
:class: important
* Sie können erste grundlegende Schritte der Datenvorverarbeitung anwenden:
    * Sie können unvollständige Daten mit **dropna** aus dem Datensatz
      entfernen. 
    * Sie können Ausreißer mit **drop** entfernen.
    * Sie können eine Eigenschaft als Input auswählen und mit **reshape** in
      Matrixform bringen.
* Sie können ein lineares Regressionsmodell aus Scikit-Learn laden und mit
  **fit** trainieren.
* Sie können mit dem trainierten Modell und **predict** eine Prognose abgeben.
```


## Deutscher Gebrauchtwagenmarkt (Autoscout24)

**Question**: Angenommen, Sie besitzen ein Auto, möchten es aber verkaufen. Für wieviel Euro
sollten Sie Ihr Auto zum Verkauf anbieten?

**Understanding the data**: Um diese Frage zu beantworten, sammeln wir zuerst
Daten von Auto-Verkaufspreisen und erkunden diese.

Dazu benutzen wir einen Datensatz über den deutschen Gebrauchtwagenmarkt von 2011
bis 2021 (Autoscout24). Der Datensatz stammt von
[Kaggle](https://www.kaggle.com/datasets/ander289386/cars-germany). Enthalten
sind Daten zu den Merkmalen

* mileage: kilometres traveled by the vehicle (= Kilometerstand)
* make: make of the car (= Marke)
* model: model of the car (= Modell)
* fuel: fuel type (= Treibstoffart)
* gear: manual or automatic (= Getriebe)
* offerType: type of offer (new, used, ...) (= Angebotsart)
* price: sale price of the vehicle (= Gebrauchtpreis)
* hp: horse power (= PS)
* year: the vehicle registration year (= Baujahr)

Wie immer laden wir die Daten und verschaffen uns zunächst einen Überblick.

```{code-cell} ipython3
import pandas as pd

data_raw = pd.read_csv('data/autoscout24-germany-dataset.csv')
data_raw.info()
```

Offensichtlich sind in den Spalten 'model', 'gear' und 'hp' einige Datensätze
nicht vollständig. Das erkennen wir daran, dass insgesmt 46.405 Einträge
vorliegen, aber in diesen drei Spalten weniger erfasst sind. 

Wir machen es uns jetzt einfach und entfernen die nicht vollständigen Daten aus
unserem Datensatz mit der Methode `.dropna()`, siehe [Pandas-Dokumentation →
dropna)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.dropna.html).
Bei einem echten Industrieprojekt müssten wir dem Problem nachgehen und die
fehlenden Daten beschaffen. Sollte das nicht gehen, so müssten wir als nächstes
analysieren, warum die Daten fehlen, ob beispielsweise eine Systematik
dahintersteckt, und uns dann einen geeigneten Plan machen, wie mit den fehlenden
Daten umzugehen ist. Das ist ein eigenständiges Thema innerhalb des ML, auf das
wir im späteren Verlauf der Vorlesung noch näher eingehen werden.

```{code-cell} ipython3
data = data_raw.dropna().copy()
data.info()
```

In dem Datensatz gibt es nur vier Eigenschaften, die numerisch sind, also
metrische oder quantitative Merkmale repräsentieren. Wir wählen die Eigenschaft
Preis als Zielgröße (=abhängige Variable oder Wirkung oder Output oder Target).

Als nächstes visualisieren wir den Preis abhängig von den Merkmalen

* Kilometerstand,
* Baujahr und
* PS.

Wir fangen mit dem Kilometerstand der Autos an.

```{code-cell} ipython3
import plotly.express as px

fig = px.scatter(data, x = 'mileage', y = 'price', title='Gebrauchtwagenmarkt 2011-2021 (Autoscout24)')
fig.update_layout(
    xaxis_title = 'Kilometerstand [km]',
    yaxis_title = 'Preis (Euro)'
)
fig.show()
```

Sieht nicht besonders linear aus, eher wie eine Hyperbel. Als nächstes
betrachten wir den Preis in Abhängigkeit des Baujahrs. 

```{code-cell} ipython3
fig = px.scatter(data, x = 'year', y = 'price', title='Gebrauchtwagenmarkt 2011-2021 (Autoscout24)')
fig.update_layout(
    xaxis_title = 'Baujahr',
    yaxis_title = 'Preis (Euro)'
)
fig.show()
```

Je jünger, desto teurer, könnte linear sein. Und zuletzt visualisieren wir den
Preis abhängig von der PS-Zahl.

```{code-cell} ipython3
fig = px.scatter(data, x = 'hp', y = 'price', title='Gebrauchtwagenmarkt 2011-2021 (Autoscout24)')
fig.update_layout(
    xaxis_title = 'Leistung (PS)',
    yaxis_title = 'Preis (Euro)'
)
fig.show()
```

Bei dem Input PS scheint es eine lineare Abhängigkeit zu geben. Je mehr PS desto
teurer. Wir wählen daher als Merkmal für unsere lineare Regression die PS-Zahl
aus.


## Training des linearen Regressionsmodell

So wie wir Pandas zur Verwaltung der Daten nutzen, so verwenden wir das Modul
**Scikit-Learn** für den ML-Part. Scikit-Learn ist eine der beliebtesten
Open-Source-Bibliotheken für maschinelles Lernen in Python. Ein großer Vorteil
von Scikit-Learn ist, dass die dort integrierten ML-Modelle stets dieselbe
Schnittstelle bieten. Die Dokumentation findet sich hier:

> https://scikit-learn.org/stable/index.html

Das Modul der Bibiolthek Scikit-Learn hat den Namen `sklearn`.  Lineare
ML-Modelle fasst Scikit-Learn in einem Untermodul namens `linear_model`
zusammen. Um also das lineare Regressionsmodell `LinearRegression` verwenden zu
können, müssen wir es folgendermaßen importieren und initialisieren:

```{code-cell} ipython3
from sklearn.linear_model import LinearRegression

# Algorithm selection
model = LinearRegression()
```

Mit der Methode `.fit()` werden die Parameter des Modells an die Daten
angepasst. Dazu müssen die Daten in einem bestimmten Format vorliegen. Bei den
Inputs wird davon ausgegangen, dass mehrere Eigenschaften in das Modell eingehen
sollen. Die Eigenschaften stehen normalerweise in den Spalten des Datensatzes.
Beim Output erwarten wir zunächst nur eine Eigenschaft, die durch das Modell
erklärt werden soll. Daher geht Scikit-Learn davon aus, dass der Input eine
Tabelle (Matrix) $X$ ist, die M Zeilen und N Spalten hat. M ist die Anzahl an
Datenpunkten, hier also die Anzahl der Autos, und N ist die Anzahl der Merkmale,
die betrachtet werden sollen. Da wir momentan nur die Abhängigkeit des Preises
von der PS-Zahl analysieren wollen, ist $N=1$. Beim Output geht Scikit-Learn
davon aus, dass eine Datenreihe (eindimensionaler Spaltenvektor) vorliegt, die
natürlich ebenfalls M Zeilen hat. Wir müssen daher unsere PS-Zahlen noch in das
Matrix-Format bringen. Dazu verwenden wir den Trick, dass mit `[ [list] ]` eine
Tabelle extrahiert wird. 

```{code-cell} ipython3
# Adaption of the data
X = data[['hp']]
y = data['price']

# Algorithm training
model.fit(X, y);
```

Es erfolgt keine Ausgabe, aber jetzt ist das lineare Regressionsmodell
trainiert. Die durch das Training bestimmten Parameter des Modells sind im
Modell selbst abgespeichert. Bei dem linearen Regressionsmodell sind das die
beiden Parameter $w_0$ und $w_1$, also Steigung `.coef_` und den
y-Achsenabschnitt `.intercept_`.

```{code-cell} ipython3
print(f'Steigung: {model.coef_}')
print(f'y-Achsenabschnitt: {model.intercept_}')
```

## Bewertung des Modell

Im vorherigen Kapitel haben wir das R<sup>2</sup>-Bestimmtheitsmaß
kennengelernt, das bewertet, wie gut das lineare Regressionsmodell
prognostiziert. In Scikit-Learn werden die Bewertungsmaße über die Methode
`.score()` ermittelt. 

```{code-cell} ipython3
# Validierung
r2 = model.score(X, y)
print('Der R2-Score ist: {:.2f}'.format(r2))
```

Ein R²-Score von 0.56 ist nicht besonders gut. Das lineare Regressionsmodell hat
keine Hyperparameter, die feinjustiert werden könnten. Zur Bewertung lassen wir
das Resultat visualisieren.

Damit brauchen wir eine Wertetabelle für PS-Zahlen von 0 bis 800 PS und die
Prognose des Modells für diese PS-Zahlen. Zunächst erzeugen 100 PS-Zahlen von 0
bis 800 PS. Dazu nutzen wir aus dem NumPy-Modul den Befehl `linspace(start,
stopp, anzahl_punkte)`.

```{code-cell} ipython3
import numpy as np

ps_zahlen = np.linspace(0, 800, 100)
print(ps_zahlen)
```

Das trainierte Modell erwartet Daten in demselben Format, mit dem es trainiert
wurde. Daher erstellen wir nun mit dem NumPy-Array einen Pandas-DataFrame und
lassen dann das trainierte Modell die Preise prognostizieren.

```{code-cell} ipython3
X_predict = pd.DataFrame(ps_zahlen, columns=['hp'])
y_predict = model.predict(X_predict)

import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Scatter(x = data['hp'], y = data['price'], mode='markers', name='Daten'))
fig.add_trace(go.Scatter(x = X_predict['hp'], y = y_predict, mode='lines', name='Prognose'))
fig.update_layout(
  title='Gebrauchtwagenmarkt 2011-2021 (Autoscout24)',
  xaxis_title = 'Leistung (PS)',
  yaxis_title = 'Preis (Euro)'
)
fig.show()
```

Damit könnten wir die Geradengleichung 

$$y = 191.76073729 \cdot x + 8939.6499591744$$

aufstellen und eine Funktion implementieren, um für eine PS-Zahl eine Prognose
abzugeben, welchen Verkauspreis das Auto erzielen könnte. Aber tatsächlich hat
das Scikit-Learn für uns schon erledigt. Die Methode `.predict()` berechnet mit
den intern gespeicherten Koeffizienten des linearen Regressionsmodells eine
Prognose. Für eine PS-Zahl von 80 PS wird ein Verkaufspreis von 

```{code-cell} ipython3
model.predict([[80]])
```

6.614 EUR erzielt. Denken Sie daran, dass eine Matrix als Input übergeben werden
muss, daher die doppelten eckigen Klammern.





+++

## Zusammenfassung

In diesem Abschnitt haben Sie gelernt, dass das Training eines linearen
Regressionsmodells darauf beruht, die Fehlerquadratsumme zu minimieren. Um
überhaupt beurteilen zu können, ob ein ML-Modell geeignet ist, brauchen wir
Qualitätskriterien. Für das lineare Regressionsmodell dient das Bestimmtheitsmaß
bzw. der R²-Score als Qualitätskriterium.
