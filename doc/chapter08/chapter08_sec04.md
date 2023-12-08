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

# Übungen

```{admonition} Aufgabe 8.1
:class: tip
Der Datensatz 'diabetes.csv' ist eine Sammlung von medizinischen Daten, die vom National Institute of Diabetes and Digestive and Kidney Diseases, erhoben wurden, siehe https://www.kaggle.com/datasets/whenamancodes/predict-diabities?resource=download . Bei Frauen des Pima-Stammes wurden folgende medizinische Daten erhoben:

* Pregnancies: Anzahl der Schwangerschaften	
* Glucose: Glukose-Level im Blut
* BloodPressure: Messung des Blutdrucks	
* SkinThickness: Dicke der Haut	
* Insulin: Messung des Insulinspiegels im Blut
* BMI: Body-Maß-Index (Gewicht geteilt durch Körpergröße ins Quadrat)	
* DiabetesPedigreeFunction: Wahrscheinlichkeit von Diabetes aufgrund der Familienhistorie	
* Age: Alter	

Enthalten ist auch, ob bei der Person Diabetes festgestellt wurde oder nicht.
* Outcome: Diabetes = 1, kein Diabetes = 0	

Fragen:
* Laden Sie den Datensatz und überprüfen Sie die Daten auf Vollständigkeit. Sind
  die angegeben Werte plausibel? Bereinigen Sie den Datensatz.
* Führen Sie eine explorative Datenanalyse durch. 
* Erstellen Sie eine Scatter-Matrix mit Insulin, BMI und Outcome. Welche der
  beiden Eigeschaften Insulin oder BMI könnte ehr geeignet sein, Diabetes
  ja/nein zu prognostizieren? 
* Visualisieren Sie Diabetes ja/nein in Abhängigkeit der gewählten Eigenschaft.
  Vermuten Sie einen Zusammenhang? 
* Trainieren Sie ein Perzeptron mit der gewählten Eigenschaft.
* Trainieren Sie ein Perzeptron, um zu prognostizieren, ob eine Person bei den
  gegebenen medizinischen Kennzahlen Diabetes haben könnte oder nicht.
* Vergleichen Sie beide Modelle.
```

````{admonition} Lösung
:class: tip, toggle
```python
import pandas as pd

data = pd.read_csv('diabetes.csv')
data.info()
```

Der Datensatz enthält 768 Einträge. Alle Einträge sind vorhanden und numerisch.
Die beiden Eigenschaften BMI und DiabetesPedigreeFunction enthalten Floats, die
anderen Eigenschaften werden durch Integers repräsentiert. 

Als nächstes ermitteln wir die statistischen Kennzahlen.

```python
data.describe()
```

Die Mittelwerte wirken plausibel. Im Schnitt hatten die PIMA-Frauen 3,8
Schwangerschaften, einen Glukose-Wert von 120, einen sehr niedrigen Blutdruck
von 69, eine Hautdicke von 21, eien Insulin-Wert von 80, einen BMI von 32, einen
Diabetes-Pedigree-Wert von 0.5 und ein mittleres Alter von 33.

Verwunderlich sind jedoch die Minima, bei denen einige Eigenschaften einen
minimalen Wert von 0 aufweisen. 0 Schwangerschaften sind plausibel. Aber wenn
der Glukose-Wert oder der Blutdruck oder die Haut-Dicke oder der BMI 0 sind, ist
das nicht möglich. Es ist daher anzunehmen, dass die Einträge 0 tatsächlich für
NA stehen.

Um das zu überprüfen, visualisieren wir die Anzahl der auftretenden Werte.

```python
import plotly.express as px

fig = px.bar(data['Glucose'].value_counts(),
             title='Glucose',
             labels={'value' : 'Anzahl', 'index' : '', 'variable': 'Legende'})
fig.show()
```

```python
fig = px.bar(data['BloodPressure'].value_counts(),
             title='BloodPressure',
             labels={'value' : 'Anzahl', 'index' : '', 'variable': 'Legende'})
fig.show()
```

```python
fig = px.bar(data['SkinThickness'].value_counts(),
             title='SkinThickness',
             labels={'value' : 'Anzahl', 'index' : '', 'variable': 'Legende'})
fig.show()
```

```python
fig = px.bar(data['Insulin'].value_counts(),
             title='Insulin',
             labels={'value' : 'Anzahl', 'index' : '', 'variable': 'Legende'})
fig.show()
```

```python
fig = px.bar(data['BMI'].value_counts(),
             title='BMI',
             labels={'value' : 'Anzahl', 'index' : '', 'variable': 'Legende'})
fig.show()
```

Die Nullen scheinen tatsächlich als NA-Ersatz missbraucht worden zu sein. Wir
löaschen nacheinander diese Datensätze.

```python
eigenschaften_mit_na = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']

for eigenschaft in eigenschaften_mit_na: 
    zeilen_zum_loeschen = data[ data[eigenschaft] == 0.0 ].index
    data = data.drop(zeilen_zum_loeschen)
data.info()
```

```python
data.describe()
```

Der deutlich kleinere Datensatz mit nur noch 392 enthält nun (hoffentlich)
gültige Messungen. Wir visualisieren die statistischen Kennzahlen.

```python
fig = px.box(data,
             title='Statistische Kennzahlen der PIMA-Frauen',
             labels={'value': 'Wert', 'variable': 'Eigenschaft'})
fig.show()
```

Bei den Schwangerschaften gibt es Ausreißer nach oben (bis zu 17
Schwangerschaften), beim Blutdruck wenige Ausreißer nach oben und unten, der
einzelne Ausreißer bei der Haut-Dicke ist vernachlässigbar, aber bei den
Insulin-Werten gibt es sehr viele Ausreißer, die deutlich vom Mittelwert
entfernt sind. Beim BMI gibt es wiederum nur wenige Ausreißer nach oben, genau
wie beim Alter.

```python
fig = px.scatter_matrix(data[['Insulin', 'BMI', 'Outcome']])
fig.show()
```

Die Eigenschaft BMI ist (bei der Wahl des Perzeptrons als ML-Modell) besser
geeignet als Erklärung für Diabetes, da eine Grenze bei ca. 22.9 gezogen werden
kann, unterhalb derer Diabetes nicht vorkommt.

```python
fig = px.scatter(data, x='BMI', y ='Outcome',
                 title='Abhängigkeit Diabetes von BMI bei den Pima-Frauen')
fig.show()
```

Ein BMI, der kleiner als ungefähr 22 ist, scheint vor Diabetes zu schützen.

```python
# Auswahl des ML-Modells
from sklearn.linear_model import Perceptron
model = Perceptron()

# Adaption der Daten
from sklearn.model_selection import train_test_split 
data_train, data_test = train_test_split(data)
X_train = data_train[['BMI']]
X_test = data_test[['BMI']]
y_train = data_train['Outcome']
y_test = data_test['Outcome']

# Training
model.fit(X_train, y_train)

# Validierung
score_train = model.score(X_train, y_train)
print(f'Score für Trainingsdaten: {score_train:.2f}')
score_test = model.score(X_test, y_test)
print(f'Score für Testdaten: {score_test:.2f}')
```

Kein besonders gutes Modell.

Nun nehmen wir alle verfügbaren Daten.

```python
X_train = data_train.loc[:, 'Pregnancies' : 'Age']
X_test = data_test.loc[:, 'Pregnancies' : 'Age']
y_train = data_train['Outcome']
y_test = data_test['Outcome']

# Training
model.fit(X_train, y_train)

# Validierung
score_train = model.score(X_train, y_train)
print(f'Score für Trainingsdaten: {score_train:.2f}')
score_test = model.score(X_test, y_test)
print(f'Score für Testdaten: {score_test:.2f}')
```

Die Hinzunahme der weiteren Eigenschaften verbessert die Prognosequalität, aber
wirklich gut ist das ML-Modell nicht. Im nächsten Kapitel werden wir uns ein
besseres Modell zur Klassifikation ansehen.
````