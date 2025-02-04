---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.16.3
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

# Übung

Der folgende Datensatz `automarkt_polen_DE.csv` (siehe campUAS) enthält die
Preise und Eigenschaften von Autos aus Polen. Das Jahr bezieht sich auf die
Erstzulassung der Autos. Stadt bzw. Region beziehen sich auf den Verkaufsort des
Autos. Die übrigen Eigenschaften sind selbsterklärend und ggf. mit ihren
Einheiten angegeben.

Bearbeiten Sie die folgenden Aufgaben. Vorab können Sie die folgenden Module
importieren. Schreiben Sie Ihre Antworten in eine Markdown-Zelle.

```{code-cell} ipython3
# import numpy as np
# import pandas as pd
# import plotly.express as px
# import plotly.graph_objects as go

# from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
# from sklearn.linear_model import LinearRegression, LogisticRegression, Perceptron
# from sklearn.model_selection import train_test_split, cross_validate, KFold, GridSearchCV
# from sklearn.neural_network import MLPClassifier, MLPRegressor
# from sklearn.preprocessing import PolynomialFeatures, MinMaxScaler, StandardScaler
# from sklearn.svm  import SVC, SVR
# from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor, plot_tree

# pd.DataFrame.iteritems = pd.DataFrame.items
```

```{admonition} Import und Bereinigung der Daten
:class: miniexercise
Importieren Sie die Daten 'automarkt_polen_DE.csv'. Verschaffen Sie sich einen
Überblick und beantworten Sie folgende Fragen:

* Wie viele Autos enthält die Datei?
* Wie viele Attribute/Eigenschaften/Features sind in den Daten enthalten?
* Sind alle Einträge gültig? Wenn nein: welche Eigenschaften sind unvollständig
  und wie viele Einträge dieser Eigenschaft sind nicht gültig?
* Welches sind die kategorialen/diskreten/qualitativen Eigenschaften und welches
  die numerischen/quantititaven Eigenschaften?
* Welchen Datentyp haben die einzelnen Attribute/Eigenschaften/Features?

Falls der Datensatz ungültige Werte aufweist oder Unstimmigkeiten enthält,
bereinigen Sie ihn.
```

````{admonition} Lösung
:class: minisolution, dropdown
```python
data = pd.read_csv('automarkt_polen_DE.csv', skiprows=3)
data.info()
```

```python
data.head()
```

Der Datensatz enthält 21420 Einträge mit Autos mit 11 Eigenschaften (Columns).

Die numerischen Eigenschaften sind:

* Kilometerstand [km], Jahr und Alter mit dem Datentyp Integer
* Preis [Zloty], Hubraum [cm3] mit dem Datentyp Float
  
Die kategorialen Eigenschaften sind:

* Marke, Modell, Preis [Zloty], Getriebe, Kraftstoff, Stadt, Region  mit
  dem Datentyp Objects (wahrscheinlich Strings)

Es gibt Eigenschaften, die unvollständig sind:

* Modell: 24
* Hubraum [cm3]: 96

```python
data.dropna(inplace=True)
data.info()
```
````

```{admonition} Statistische Kennzahlen (numerische Eigenschaften)
:class: miniexercise

* Ermitteln Sie von den numerischen Eigenschaften die statistischen Kennzahlen
  und visualisieren Sie sie. Verwenden Sie beim Plot eine aussagefähige
  Beschriftung.
* Interpretieren Sie jede Eigenschaft anhand der statistischen Kennzahlen und
  der Plots.
* Bereinigen Sie bei Ungereimtheiten den Datensatz weiter.
* Entfernen Sie Ausreißer.
* Beantworten Sie folgende Fragen:
  * In welchem Jahr wurden die meisten Autos zugelassen?
  * Wie viele Autos wurden in diesem Jahr mit den meisten Zulassungen zugelassen?
```

````{admonition} Lösung
:class: minisolution, dropdown
```python
data.describe()
```

```python
numerical_features = ['Preis [Zloty]', 'Kilometerstand [km]', 'Hubraum [cm3]', 'Jahr', 'Alter']
fig = px.box(data[numerical_features],
    labels={'variable': 'Merkmal', 'value':'Wert'},
    title='Statistische Eigenschaften der numerischen Merkmale')
fig.show()
```

Die Autopreise beginnen bei 1111 Zloty und geht bis 2,3 Mio. Zloty. Der
Mittelwert liegt deutlich höher als der Median, d.h. wenige Autos, die sehr
teuer sind, verzerren den Preis nach oben. Wir entfernen alle Ausreißer und
wählen als Grenze 189750 Zloty.

```python
rows = data[data['Preis [Zloty]'] > 189750].index
data = data.drop(rows)
data.info()
```

Auch der Kilometerstand hat einige Ausreißer mit Autos, die sehr viele Kilometer haben. Diese entfernen wir ebenfalls, wir wählen als Grenze 420000 km.

```python
rows = data[data['Kilometerstand [km]'] > 420000].index
data = data.drop(rows)
data.info()
```

```python
fig = px.box(data[numerical_features])
fig.show()
```

Der Hubraum fängt bei 0 cm^3 an und geht bis 8300 cm^3. Ein Auto kann keinen
Hubraum von 0 cm^3 haben, Das ist eine Ungereimtheit. Diese Daten werden daher
entfernt.

```python
rows = data[data['Hubraum [cm3]'] < 1].index
data = data.drop(rows)
data.info()
```

```python
fig = px.box(data[['Hubraum [cm3]','Jahr', 'Alter']])
fig.show()
```

Jahr und Alter sind direkt linear korreliert. Daher entfernen wir eine der
beiden Eigenschaften und nehmen das Alter.

```python
data.drop(columns='Alter', inplace=True)
data.info()
```

```python
data['Jahr'].value_counts()
```

Im Jahr 2017 wurden die meisten Autos zugelassen, die aktuell in Polen zum
Verkauf stehen. Es sind 1395 Autos.
````

```{admonition} Statistische Kennzahlen (kategoriale Eigenschaften)
:class: miniexercise
Beantworten Sie durch Datenanalyse die folgenden Fragen. Fassen Sie die
Ergebnisse bzw. die Interpretation davon jeweils kurz zusammen (als Kommentar in
der Code-Zelle oder in einer Markdown-Zelle).

* Welche Automarke wird momentan in Polen am häufigsten und welche Automarke am
  seltesten zum Verkauf angeboten? Geben Sie jeweils die Anzahl an.
* Visualisieren Sie die Anzahl der Autos pro Marke. Beschriften Sie das Diagramm
  mit einem aussagefähigen Titel.
* Analysieren Sie die Regionen. Gibt es Regionen, die Sie überraschen? Wenn ja,
  warum?
* Wie viel Prozent der Autos haben ein Automatik-Getriebe?
```

````{admonition} Lösung
:class: minisolution, dropdown
```python
marken = data['Marke'].value_counts()
print(marken)
```

Volkswagen wird mit 2473 Autos am häufigsten angeboten, Bentley mit 2 am
seltesten.

```python
fig = px.bar(marken,
    title='angebotene Autos in Polen',
    labels={'value':'Anzahl Autos'})
fig.show()
```

```python
regionen = data['Region'].unique()
print(regionen)
```

Etwas überraschend sind Regionen aus Deutschland dabei wie Berlin.

```python
data['Getriebe'].value_counts()
```

```python
7065 / (12465 + 7065) * 100
```

36 % der Autos haben ein Automatik-Getriebe.
````

```{admonition} Regression
:class: miniexercise
Ziel der Regressionsaufgabe ist es, den Preis der Autos zu prognostizieren.

* Wählen Sie zwei Regressionsmodelle aus. Begründen Sie Ihre Auswahl mit einer
  Scattermatrix.
* Adaptieren Sie die Daten jeweils passend zu den von Ihnen gewählten Modellen.
* Falls notwendig, skalieren Sie die Daten.
* Führen Sie einen Split der Daten in Trainings- und Testdaten durch.
* Trainieren Sie jedes ML-Modell.
* Validieren Sie jedes ML-Modell bzgl. der Trainingsdaten und der Testdaten.
* Bewerten Sie abschließend: welches der zwei Modelle würden Sie empfehlen?
  Begründen Sie Ihre Empfehlung.
```

````{admonition} Lösung
:class: minisolution, dropdown
```python
fig = px.scatter_matrix(data[['Preis [Zloty]', 'Kilometerstand [km]', 'Hubraum [cm3]', 'Jahr']])
fig.show()
```

Im Scatterplot Jahr -- Preis ist eine Tendenz erkennbar, je größer das Jahr
(also jünger das Auto), desto teurer ist das Auto. Aber ansonsten scheinen
lineare Modelle eher unpassend zu sein.

```python
X = data.loc[:, ['Kilometerstand [km]', 'Hubraum [cm3]', 'Jahr']]
y = data['Preis [Zloty]']

X_train, X_test, y_train, y_test = train_test_split(X,y)

scaler = MinMaxScaler()
scaler.fit(X_train)

X_trained_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)
```

```python
# Modell 1: SVM

model = SVR()

model.fit(X_train, y_train)
score_train = model.score(X_train, y_train)
score_test = model.score(X_test, y_test)
print(f'Score Trainingsdaten: {score_train:.2f}')
print(f'Score Testdaten: {score_test:.2f}')
```

```python
# Modell 2: neuronales Netz
model = MLPRegressor(solver='lbfgs', max_iter=300)

model.fit(X_train, y_train)
score_train = model.score(X_train, y_train)
score_test = model.score(X_test, y_test)
print(f'Score Trainingsdaten: {score_train:.2f}')
print(f'Score Testdaten: {score_test:.2f}')
```

```python
# Modell 3: DecisionTree
model = DecisionTreeRegressor()

model.fit(X_train, y_train)
score_train = model.score(X_train, y_train)
score_test = model.score(X_test, y_test)
print(f'Score Trainingsdaten: {score_train:.2f}')
print(f'Score Testdaten: {score_test:.2f}')
```

Das SVR-Modell scheidet aus, die Scores sind negativ. Das neuronale Netz ist
zwar positiv, aber nicht wirklich gut. Der Entscheidungsbaum ist sehr gut an die
Trainingsdaten angepasst, zeigt aber Overfitting. Daher würde ich keines der
Modelle produktiv einsetzen, sondern nach besseren Modellen suchen oder die
Hyperparameter tunen.
````

```{admonition} Klassifikation
:class: miniexercise
Ziel der Klassifikationsaufgabe ist es, die Preisklasse "billig" oder "teuer"
der Autos zu prognostizieren.

Achtung Vorbereitung:
Filtern Sie die Daten nach den Autos, deren Preis kleiner oder gleich dem
Median aller Preise ist. Diese Autos sollen als "billig" klassfiziert
werden. Autos, deren Preis größer als der Median aller Preise ist, sollen
als "teuer" klassifiziert werden.

* Wählen Sie die folgenden Eigenschaften aus: **Jahr** und **Kilometerstand
  [km]**.
* Adaptieren Sie die Daten passend.
* Falls notwendig, skalieren Sie die Daten.
* Trainieren Sie einen Entscheidungsbaum (Decision Tree). Begrenzen Sie dabei
  die maximale Tiefe des Baumes auf 2.
* Visualisieren Sie den Entscheidungsbaum (Decision Tree) inklusive Beschriftung
  der Labels.
* Bewerten Sie abschließend: Ist das Jahr oder der Kilometerstand wichtiger für
  die Einstufung als billiges oder teures Auto? Begründen Sie Ihre Entscheidung
  anhand des Entscheidungsbaumes (Decision Trees).
```

````{admonition} Lösung
:class: minisolution, dropdown
```python
# Vorbereitung

# Einteilung der Autos nach billig (=0) oder teuer (=1)
median = data['Preis [Zloty]'].median()
print(f'Median: {median:.2f}')

data.loc[ data['Preis [Zloty]'] <  median, 'Preisklasse'] = 0
data.loc[ data['Preis [Zloty]'] >= median, 'Preisklasse'] = 1
data['Preisklasse'].unique()
```

```python
X = data[['Jahr', 'Kilometerstand [km]']]
y = data['Preisklasse']

X_train, X_test, y_train, y_test = train_test_split(X,y)

model = DecisionTreeClassifier(max_depth=2)
model.fit(X_train, y_train)

plot_tree(model, feature_names=['Jahr', 'Kilometerstand [km]'], filled=True);
```

Das Jahr wird benutzt, scheint also wichtiger zu sein.
````
