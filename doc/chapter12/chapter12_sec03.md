---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.7
kernelspec:
  display_name: python310
  language: python
  name: python3
---

# 12.3 Skalierung von Daten

```{admonition} Lernziele
:class: goals
* Sie wissen, dass Daten skaliert werden sollten. Ausnahme: Decision Tree oder Randon Forest.
* Sie können Daten **normieren**.
* Sie können Daten **standardisieren**.
```

# Beispiel: Weinqualität

Der folgende Datensatz stammt vom UCI Machine Learning Repository

https://archive.ics.uci.edu/dataset/186/wine+quality

und wurde ursprünglich in dieser Publikation betrachtet:
http://www3.dsi.uminho.pt/pcortez/wine5.pdf

Input sind physikalische und chemische Messungen, Output ist die Qualität des
Weines von 0 (sehr schlecht) bis 10 (exzellent). Wie üblich laden wir den
Datensatz:


```{code-cell} ipython3
import pandas as pd 

data = pd.read_csv('data/winequality_red_DE.csv', skiprows=2)
data.info()
```

Der Datensatz zur Weinqualität enthält 1599 Einträge mit 12 Eigenschaften. Die
ersten 11 Eigenschaften werden durch Floats repräsentiert, nur die letzte
Eigenschaft 'Qualität' wird durch Integers repräsentiert. Alle Einträge sind
gültig.

```{code-cell} ipython3
data.head()
```

Ein erster Blick auf die Daten zeigt bereits, dass die Eigenschaftswerte in
unterschiedlichen Bereichen liegen. Der feste Säuregehalt beispielsweise scheint
zwischen 7 und 11 zu liegen, wohingegen Cloride scheinbar eher im Bereich 0.076
bis 0.098 liegen. Das zeigt auch die Übersicht der statistischen Kennzahlen: 

```{code-cell} ipython3
data.describe()
```

Schwankt beispielsweise die Dichte zwischen 0.990070 und 1.003690, so liegen die
Gesamtschwefeldioxid-Werte zwischen 6 und 289 in einer völlig anderen
Größenordnung.

Damit ist auch der Boxplot nicht mehr lesbar:

```{code-cell} ipython3
import plotly.express as px 

fig = px.box(data,
             title='Eigenschaften Rotwein',
             labels={'variable': 'Eigenschaft', 'value': 'Werte'})
fig.show()
```

Das hat auch Auswirkungen auf das Training der ML-Modelle.

Zunächst interpretieren wir die Prognose der Weinqualität als
Klassifikationsproblem und setzen eine 1 für guten Wein (Qualität 6 und mehr)
und eine 0 für schlechten Wein (Qualität bis einschließlich 5). 

```{code-cell} ipython3
data_classification = data.copy()

data_classification.replace(3, 0, inplace=True) # schlechter Wein
data_classification.replace(4, 0, inplace=True) # schlechter Wein
data_classification.replace(5, 0, inplace=True) # schlechter Wein
data_classification.replace(6, 1, inplace=True) # guter Wein
data_classification.replace(7, 1, inplace=True) # guter Wein
data_classification.replace(8, 1, inplace=True) # guter Wein
```

Als nächstes trainieren wir ein neuronales Netz.

```{code-cell} ipython3
# Adaption der Daten
from sklearn.model_selection import train_test_split

X = data_classification.loc[:, 'fester Säuregehalt' : 'Alkohol']
y = data_classification['Qualität']

X_train, X_test, y_train, y_test = train_test_split(X,y, random_state=42)

# Training neuronales Netz
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split

# Auswahl des Models
# solver = 'lbfgs' für kleine Datenmengen, solver = 'adam' für große Datenmengen, eher ab 10000
# hidden_layer: Anzahl der Neuronen pro verdeckte Schicht und Anzahl der verdeckten Schichten
model = MLPClassifier(solver='lbfgs', hidden_layer_sizes=[5, 5], random_state=42)

# Training
model.fit(X_train, y_train)

# Validierung 
score_train = model.score(X_train, y_train)
score_test = model.score(X_test, y_test)
print(f'Score für Trainingsdaten: {score_train:.2f}')
print(f'Score für Testdaten: {score_test:.2f}')
```

Auf der einen Seite erhalten wir ein Resultat, aber auf der anderen Seite gibt
es auch eine Fehlmeldung. 

> lbfgs failed to converge (status=1): STOP: TOTAL NO. of ITERATIONS REACHED
> LIMIT.

Tatsächlich ist der Algorithmus nicht zu einem "richtigen" Ergebnis gekommen, er
ist nicht konvergiert. Scikit-Learn schlägt auch vor, wie wir den Algorithmus
unterstützen können. Wir könnten die Anzahl der Iterationen erhöhen in der
Hoffnung, dass dann der Algorithmus ein konvergentes Ergebnis erreicht, oder die
Daten skalieren. 

Wir betrachten daher beide Möglichkeiten. Zuerst setzen wir die Anzahl der
Iterationen hoch. Die [Dokumentation von
Scikit-Learn](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html#sklearn.neural_network.MLPClassifier)
gibt an, dass der Parameter 'max_iter' heißt und normalerweise auf 200 gesetzt
ist. Wir setzen ihn auf 10000:

```{code-cell} ipython3
model = MLPClassifier(solver='lbfgs', hidden_layer_sizes=[5, 5], max_iter=10000, random_state=42)

# Training
model.fit(X_train, y_train)

# Validierung 
score_train = model.score(X_train, y_train)
score_test = model.score(X_test, y_test)
print(f'Score für Trainingsdaten: {score_train:.2f}')
print(f'Score für Testdaten: {score_test:.2f}')
```

Hat funktioniert :-) Als nächstes betrachten wir noch das Skalieren der Daten.
Außer bei Decision Trees / Random Forests sollten Daten immer skaliert werden.

+++

## Skalieren von Daten

Sind die Bereich der Daten von ihren Zahlenwerten sehr verschieden, sollten alle numerischen Werte in dieselbe Größenordnung gebracht werden. Dieser Vorgang heißt **Skalieren** der Daten. Gebräulich sind dabei zwei verschiedene Methoden:

* **Normierung** und
* **Standardisierung**.

### Normierung

Bei der Normierung wird festgelegt, dass alle Zahlenwerte in einem festen
Intervall liegen. Besonders häufig wrid das Intervall $[0,1]$ genommen. Die
Dichte, die zwischen 0.990070 und 1.003690 liegt, würde so transformiert werden,
dass das Minimum 0.990070 der 0 entspricht und das Maximum 1.003690 der 1.
Genauso würde mit den anderen Eigenschaften verfahren werden. Wir nutzen zur
praktischen Umsetzung Scikit-Learn.


```{code-cell} ipython3
from sklearn.preprocessing import MinMaxScaler

# Auswahl Normierung 
normierung = MinMaxScaler()

# Analyse: jede Spalte wird auf ihr Minimum und ihre Maximum hin untersucht
# es werden immer die Trainingsdaten verwendet
normierung.fit(X_train)

# Transformation der Trainungs- und Testdaten
X_train_normiert = normierung.transform(X_train)
X_test_normiert = normierung.transform(X_test)
```

Wir schauen in 'X_train_normiert' hinein:

```{code-cell} ipython3
print(X_train_normiert)
```

Es werden zwar nicht alle Werte angezeigt, aber die Normierung der Daten scheint
funktioniert zu haben.

Jetzt trainieren wir das neuronale Netz erneut.

```{code-cell} ipython3
# Auswahl des Models
# solver = 'lbfgs' für kleine Datenmengen, solver = 'adam' für große Datenmengen, eher ab 10000
# hidden_layer: Anzahl der Neuronen pro verdeckte Schicht und Anzahl der verdeckten Schichten
model = MLPClassifier(solver='lbfgs', hidden_layer_sizes=[5, 5], max_iter=10000, random_state=42)

# Training
model.fit(X_train_normiert, y_train)

# Validierung 
score_train = model.score(X_train_normiert, y_train)
score_test = model.score(X_test_normiert, y_test)
print(f'Score für Trainingsdaten: {score_train:.2f}')
print(f'Score für Testdaten: {score_test:.2f}')
```

Der Score der Traingsdaten ist leicht besser geworden. 

### Standardisierung

Oft sind Daten normalverteilt. Die Standardisierung berücksichtigt das und
transformiert nicht auf ein festes  Intervall, sondern verschiebt den Mittelwert
auf 0 und die Varianz auf 1. Die normalverteilten Daten werden also
standardnormalverteilt. Auch das lassen wir Scikit-Learn erledigen:

```{code-cell} ipython3
from sklearn.preprocessing import StandardScaler

# Auswahl Normierung 
skalierung = StandardScaler()

# Analyse: jede Spalte wird auf ihr Minimum und ihre Maximum hin untersucht
# es werden immer die Trainingsdaten verwendet
skalierung.fit(X_train)

# Transformation der Trainungs- und Testdaten
X_train_skaliert = skalierung.transform(X_train)
X_test_skaliert = skalierung.transform(X_test)

print(X_train_skaliert)
```

```{code-cell} ipython3
# Auswahl des Models
# solver = 'lbfgs' für kleine Datenmengen, solver = 'adam' für große Datenmengen, eher ab 10000
# hidden_layer: Anzahl der Neuronen pro verdeckte Schicht und Anzahl der verdeckten Schichten
model = MLPClassifier(solver='lbfgs', hidden_layer_sizes=[5, 5], max_iter=10000, random_state=42)

# Training
model.fit(X_train_skaliert, y_train)

# Validierung 
score_train = model.score(X_train_skaliert, y_train)
score_test = model.score(X_test_skaliert, y_test)
print(f'Score für Trainingsdaten: {score_train:.2f}')
print(f'Score für Testdaten: {score_test:.2f}')
```

Der Score der Trainingsdaten hat sich leicht verbessert, der Score für die
Testdaten ist dafür leicht gesunken. Die Skalierung der Daten hat also einen
Einfluss auf die Performance der ML-Modelle.

## Zusammenfassung und Ausblick

Daten sollten immer skaliert werden, sofern nicht Decision Trees oder Random
Forests betrachtet werden. Es gibt zwei Möglichkeiten, Daten zu skalieren:
Normierung oder Standardisierung. Letzteres wird häufiger verwendet, hängt aber
natürlich von der Art der Daten ab.