---
jupytext:
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

# Übung

```{admonition} Aufgabe 
:class: tip

Das Schiff Titanic galt bei seiner Fertigstellung als unsinkbar. 1912
kollidierte die Titanic mit einem Eisberg und sank. Bei dem Unglück kamen 1514
von 2220 Personen ums Leben, so dass der titanic-Untergan zu den größten
Unglücken der Schifffahrt zählt. Mehr Informationen zu der Titanic finden Sie
bei Wikipedia https://de.wikipedia.org/wiki/Titanic_(Schiff).

In der folgenden Übung werden Passagierlisten der Titanic benutzt, um die
Überlebenswahrscheinlichkeit zu prognostizieren (0 = gestorben, 1 = überlebt),
deren Quelle hier ist: https://www.kaggle.com/c/titanic

Laden sie den Datensatz 'titanic_train_DE.csv'. Führen Sie dann eine explorative
Datenanalyse (EDA) durch. Trainieren Sie zuletzt ein Perzeptron, ein
logistisches Regressionsmodell und ein SVM. Welches Modell kann am besten die
Überlebenswahrscheinlichkeit prognostizieren? Sie können Ihr Modell mit den
Testdaten validieren.
```

````{admonition} Lösung 
:class: tip, toggle

```python
import pandas as pd 

data = pd.read_csv('titanic_train_DE.csv', index_col=0)
```

```python
data.info()
```

```python
data.head()
```

Der Datensatz 'titanic_train_DE.csv' enthält 891 Einträge. Es gibt 11 Eigenschaften, wobei die Kategorie ueberlebt, die Klasse, die Anzahl_Geschwister_Partner und Anzahl_Eltern_Kinder durch Integers repräsentiert werden, das Alter und der Ticketpreis sind Floats und die Eigenschaften Name, Geschlecht, Ticket, Kabine und Einstiegshafen sind Objekte.

Die Eigenschaften Alter, Kabine und Einstiegshafen sind unvollständig.

```python
data.describe()
```

Die Eigenschaften ueberlebt und Klasse werden zwar durch Integers repräsentiert, aber ein Blick in die Daten zeigt, dass es sich um kategoriale Daten handelt.

```python
data['ueberlebt'].unique()
```

Es gibt nur zwei Kategorien für die Eigenschaft 'ueberlebt', nämlich 0 (gestorben) und 1 (überlebt).

```python
import plotly.express as px

fig = px.bar(data['ueberlebt'].value_counts(), title='Trainingsdaten Titanic',
             labels={'index': 'Überlebensvariable', 'value': 'Anzahl Personen'})
fig.show()
```

Bei dem Titanic-Unglück sind mehr Personen gestorben (549) als überlebt haben (342).

```python
data['Klasse'].unique()
```

Es gibt nur drei Kategorien bei der Eigenschaft Klasse, nämlich Klasse 1, 2 und 3.

```python
fig = px.bar(data['Klasse'].value_counts(),
             title='Trainingsdaten Titanic',
             labels={'index': 'Klasse', 'value': 'Anzahl Personen'})
fig.show()
```

In der 2. Klasse gab es am wenigsten Passagiere (184). 216 Personen fuhren in der 1. Klasse mit und am meisten (491) Personen reisten in der 3. Klasse. 

```python
fig = px.box(data['Alter'],
             title='Trainingsdaten Titanic',
             labels={'variable': '', 'value': 'Alter [Jahre]'})
fig.show()
```

Die Passagiere sind zwischen 0 und 80 Jahre alt. Die Hälfte aller Passigiere ist im Alter von 20 bis 38 bei einem Median von 28 Jahren. Der Median stimmt auch gut mit dem Mittelwert von 29.7 Jahren überein. Es gibt allerdings auch Ausreißer nach oben.

```python
fig = px.bar(data['Anzahl_Geschwister_Partner'].value_counts(),
             title='Trainingsdaten Titanic',
             labels={'index': 'Anzahl Geschwister/Partner', 'value': 'Anzahl Personen'})
fig.show()
```

Die meisten Passagiere (608) reisten ohne Geschwister oder Partner. 209 Passagiere gaben an, mit einem Geschwister oder Partner zu reisen. Die Anzahl von Passagieren, die mit zwei oder mehr Geschwistern/Partnern reisten, ist klein (zusammen 70 Personen).

```python
fig = px.bar(data['Anzahl_Eltern_Kinder'].value_counts(),
             title='Trainingsdaten Titanic',
             labels={'index': 'Anzahl der mitreisenden Eltern oder Kindern', 'value': 'Anzahl Personen'})
fig.show()
```

Auch sind die meisten Personen (687) ohne Eltern oder Kinder gereist. 

```python
fig = px.box(data['Ticketpreis'],
             title='Trainingsdaten Titanic',
             labels={'variable': '', 'value': 'Preis'})

fig.show()
```

Bei den Ticketpreisen gibt es einen sehr deutlichen Ausreißer nach oben (512) und andere Ausreißer (zwischen 65 und 263), aber es konnten auch einige Personen kostenlos mitreisen.


```python
data_by_class = data.groupby('Klasse')

fig = px.bar(data_by_class['ueberlebt'].mean(),
             title='Trainingsdaten Titanic',
             labels={'value': 'Überlwebenswahrscheinlichkeit'})
fig.show()
```

Die Passagiere der 1. Klasse hatten eine deutlich höhere Wahrscheinlichkeit (knapp 63 %), das Unglück zu überleben. Passagiere der 2. Klasse überlebten zu 47 %, wohingegen Passagiere der 3. Klasse nur zu 24 % überlebten.

```python
data_by_sex = data.groupby('Geschlecht')

fig = px.bar(data_by_sex['ueberlebt'].mean(),
             title='Trainingsdaten Titanic',
             labels={'value': 'Überlebenswahrscheinlichkeit'})
fig.show()
```

Frauen und Kinder zuerst gilt tatsächlich für das Titanic-Unglück. Zumindest überlebten 74 % der weiblichen Passagiere, aber nur knapp 19 % der Männer.

Vorbereitung der Daten

```python
data_cleaned = data.copy()
data_cleaned = data.drop(columns=['Name', 'Ticket', 'Kabine', 'Einstiegshafen'], axis=0)

data_cleaned['Geschlecht'] = data_cleaned['Geschlecht'].replace('maennlich', 0)
data_cleaned['Geschlecht'] = data_cleaned['Geschlecht'].replace('weiblich', 1)

data_cleaned = data_cleaned.dropna()
data_cleaned.info()
```

Training der ML-Modelle

```python
y_train = data_cleaned['ueberlebt']
X_train = data_cleaned.loc[:, 'Klasse' : 'Ticketpreis']
```

```python
from sklearn.linear_model import Perceptron 

model_perceptron = Perceptron()

model_perceptron.fit(X_train, y_train)
score_perceptron = model_perceptron.score(X_train, y_train)

print(f'Score Perzeptron Trainingsdaten: {score_perceptron :.2f}')
```

```python
from sklearn.linear_model import LogisticRegression

model_log_reg = LogisticRegression()

model_log_reg.fit(X_train, y_train)
score_log_reg = model_log_reg.score(X_train, y_train)

print(f'Score Logistische Regression Trainingsdaten: {score_log_reg :.2f}')
```

```python
from sklearn import svm

model_svm = svm.SVC(kernel='linear')

model_svm.fit(X_train, y_train)
score_svm = model_svm.score(X_train, y_train)

print(f'Score SVM Trainingsdaten: {score_svm :.2f}')
```

Am besten schneidet die logistische Regression ab, die eine Genauigkeit der Prognose auf den Trainingsdaten von 0.80 erreicht. Am zweitbesten funktioniert -- zumindest auf den Trainignsdaten -- das SVM-Modell mit einem Score von 0.78. Das Perzeptron ist mit einem Score von 0.68 am schlechtesten.
````

