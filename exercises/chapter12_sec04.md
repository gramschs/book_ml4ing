---
jupytext:
  formats: ipynb,md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.15.2
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Übungen logistische Regression

```{admonition} Aufgabe 1
:class: tip

Ein sehr berühmter Datensatz für maschinelles Lernen ist die Irisblütensammlung,
siehe auch https://de.wikipedia.org/wiki/Portal:Statistik/Datens%C3%A4tze#Iris .
In dem Datensatz sind Beispiele für die drei Irisarten

* Iris Setosa,
* Iris Virginica und 
* Iris Versicolor.

1. Laden Sie den Datensatz ('iris.csv') und verschaffen Sie sich einen
   Überblick.
    * Durch welche Eigenschaften/Attribute werden die Iris-Blumen beschrieben?
      Lesen Sie dazu auch die oben angegebene Wikipedia-Seite.
    * Welche Spalte enthält die Bezeichnung der Irisart?
    * Wie viele Blumen sind pro Irisart in dem Datensatz enthalten?
2. Bestimmen Sie die statistischen Kennzahlen der Eigenschaften getrennt nach
   Irisart und visualisieren Sie die Eigenschaften jeweils als Boxplots.
   Interpretieren Sie die Ergebnisse.
3. Geben Sie eine Einschätzung basierend auf den statistischen Analysen aus
   Punkt 2 ab und einer Scattermatrix (color = 'species'). Lassen sich die drei
   Irisarten durch ein Perzeptron klassifizieren?
4. Vergleichen Sie ein trainiertes Perzeptron mit einem trainierten logistischen Regressionsmodell.
```

````{admonition} Lösung
:class: tip, toggle

```python
import pandas as pd

# Datenimport 
data = pd.read_csv('iris.csv')
data.info()
```

Es gibt vier Spalten mit den Eigenschaften:

* sepal_length: Länge Sepalum (= Kelchblatt)
* sepal_width: Breite Sepalum
* petal_length: Länge Petalum (= Kronblatt)
* petal_width: Breite Petalum

Alle vier Größenangaben werden durch Floats repräsentiert. Die Spalten sind
vollständig. Die Spalte species gibt die Irisart an.
  

```python
data.head()
```

```python
data['species'].value_counts()
```

Es gibt drei verschiedene Irisarten, jede kommt 50 x vor.

Statistische Kennzahlen:

```python
data_by_species = data.groupby('species')

print('Iris setosa: ')
data_by_species.get_group('Iris-setosa').describe()
```

```python
print('Iris versicolor: ')
data_by_species.get_group('Iris-versicolor').describe()
```

```python
print('Iris virginica: ')
data_by_species.get_group('Iris-virginica').describe()
```

```python
import plotly.express as px

fig = px.box(data, x = 'species', y = 'sepal_length',
             title='Länge Sepalum (Kelchblatt)',
             labels={'species': 'Irisart', 'sepal_length': 'Länge in cm'})
fig.show()
```

Die drei Irisarten unterscheiden sich bzgl. der Länge des Sepalums: Iris Setosa
hat einen Median von 5 cm, Iris Versicolor einen Median von 5,9 cm und Iris
Virginica einen Median von 6,5 cm. Es gibt nur einen Ausreißer bei der Irisart
Iris Virginica.

```python
fig = px.box(data, x = 'species', y = 'sepal_width',
             title='Breite Sepalum (Kelchblatt)',
             labels={'sepal_width': 'Breite in cm', 'species': 'Irisart'})
fig.show()
```

Dafür hat Iris Setosa breitere Kelchblätter (Median 3.4 cm) im Vergleich zu Iris
Versicolor (Median 2.8 cm) und Iris Virginica (Median 3 cm). Es gibt keine
Ausreißer.

```python
fig = px.box(data, x = 'species', y = 'petal_length',
            title='Länge Petalum (Kronblatt)',
            labels={'petal_length': 'Länge in cm', 'species': 'Irisart'})
fig.show()
```

Bei der Länge der Kronblätter gibt es einen deutlichen Unterschied zwischen Iris
Setosa (Median 1.5 cm) und den beiden anderen Irisarten: Iris Versicolor (Median
4.35 cm) und Iris Virginica (Median 5.55 cm).

```python
fig = px.box(data, x = 'species', y = 'petal_width',
            title='Breite Petalum (Kronblatt)',
            labels={'petal_width': 'Breite in cm', 'species': 'Irisart'})
fig.show()
```

Der Unterschied bei der Länge der Kronblätter ist auch bei der Breite
wiederzufinden. Iris Setosa hat im Median 0.2 cm deutlich dünnere Kronblätter
als Iris Versicolor (Median 1.3 cm) und Iris Virginica (2 cm).

```python
fig = px.scatter_matrix(data, color='species')
fig.show()
```

Die Irisart Iris Setosa lässt sich von den anderen beiden Arten trennen. Dazu
können wir entweder die Länge oder die Breite der Kronblätter nehmen. Ist ein
Kronblatt kürzer als beispielsweise 2.5 cm, so wird es eine Iris Setosa sein.
Das gleiche gilt, wenn ein Kronblatt dünner als 0.8 cm ist.

Wir trainieren ein Perzeptron für die Trennung in Iris Setosa und keine Iris
Setosa.

```python
# Encoding 
data_classification_setosa = data.copy()
data_classification_setosa.replace('Iris-setosa', 1, inplace=True)
data_classification_setosa.replace('Iris-versicolor', 0, inplace=True)
data_classification_setosa.replace('Iris-virginica', 0, inplace=True)

# Model selection
from sklearn.linear_model import Perceptron
model = Perceptron()

# Adaption of data
X = data_classification_setosa.loc[:, 'sepal_width':'petal_length']
y = data_classification_setosa['species']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

# Training
model.fit(X_train, y_train)

# Validation
score_train = model.score(X_train, y_train)
score_test = model.score(X_test, y_test)

print(f'Score Trainingsdaten: {score_train}')
print(f'Score Testdaten: {score_test}')
```

Zuletzt trainieren wir ein Perzeptron und ein logistisches Regressionsmodell für
die Irisart Iris Virginica und vergleiche beide miteinander.

```python
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Perceptron
from sklearn.linear_model import LogisticRegression

# Encoding
classification_virginica = data.copy()

classification_virginica.replace('Iris-virginica', 1, inplace=True)
classification_virginica.replace('Iris-setosa', 0, inplace=True)
classification_virginica.replace('Iris-versicolor', 0, inplace=True)

# Adaption of data
X = classification_virginica.loc[:, 'sepal_length' : 'petal_width']
y = classification_virginica['species']


X_train, X_test, y_train, y_test = train_test_split(X,y, random_state=42)

# Model selection
model_perceptron = Perceptron()
model_logistic_regression = LogisticRegression()

# Training
model_perceptron.fit(X_train, y_train)
model_logistic_regression.fit(X_train, y_train)

# Validation
score_perceptron_train = model_perceptron.score(X_train, y_train)
score_perceptron_test = model_perceptron.score(X_test, y_test)
score_logistic_regression_train = model_logistic_regression.score(X_train, y_train)
score_logistic_regression_test = model_logistic_regression.score(X_test, y_test)

print(f'Score Trainingsdaten Perzeptron: {score_perceptron_train:.2f}')
print(f'Score Testdaten Perzeptron: {score_perceptron_test:.2f}')
print(f'Score Trainingsdaten logistische Regression: {score_logistic_regression_train:.2f}')
print(f'Score Testdaten logistische Regression: {score_logistic_regression_test:.2f}')
```
````

```{admonition} Aufgabe 2
:class: tip

Der Datensatz 'diabetes.csv' ist eine Sammlung von medizinischen Daten, die vom
National Institute of Diabetes and Digestive and Kidney Diseases, erhoben
wurden, siehe
https://www.kaggle.com/datasets/whenamancodes/predict-diabities?resource=download
. Bei Frauen des Pima-Stammes wurden folgende medizinische Daten erhoben:

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

Im letzten Kapitel haben wir bereits ein Perzeptron zur Prognose Diabetes
ja/nein trainiert. Vergleichen Sie nun das Perzeptron mit der logistischen
Regression. 
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
anderen Eigenschaften werden durch Integer repräsentiert. 

Als nächstes ermitteln wir die statistischen Kennzahlen.

```python
data.describe()
```

Einige Eigenschaften haben 0 als Minimum. Wie in Aufgabe 8.1 analysiert, wurde
die 0 wahrscheinlich als NaN missbraucht. Wir korrigieren daher den Datensatz.

```python
eigenschaften_mit_na = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']

for eigenschaft in eigenschaften_mit_na: 
    zeilen_zum_loeschen = data[ data[eigenschaft] == 0.0 ].index
    data = data.drop(zeilen_zum_loeschen)
data.info()
```

Als nächstes trainieren wir das Perzeptron.

```python
# Auswahl des ML-Modells
from sklearn.linear_model import Perceptron
model_perceptron = Perceptron()

# Adaption der Daten
from sklearn.model_selection import train_test_split 
data_train, data_test = train_test_split(data)

X_train = data_train.loc[:, 'Pregnancies' : 'Age']
X_test = data_test.loc[:, 'Pregnancies' : 'Age']
y_train = data_train['Outcome']
y_test = data_test['Outcome']

# Training
model_perceptron.fit(X_train, y_train)

# Validierung
score_train = model_perceptron.score(X_train, y_train)
print(f'Score für Trainingsdaten: {score_train:.2f}')
score_test = model_perceptron.score(X_test, y_test)
print(f'Score für Testdaten: {score_test:.2f}')
```

Nun trainieren wir das logistische Regressionsmodell.

```python
# Auswahl des ML-Modells
from sklearn.linear_model import LogisticRegression
model_log_regression = LogisticRegression() 

# Training
model_log_regression.fit(X_train, y_train)

# Validierung
score_train = model_log_regression.score(X_train, y_train)
print(f'Score für Trainingsdaten: {score_train:.2f}')
score_test = model_log_regression.score(X_test, y_test)
print(f'Score für Testdaten: {score_test:.2f}')
```

Das logistische Regressionsmodell hat einen besseren Score. Für die
Trainingsdaten verbessert sich der Score (für diesen Split der Trainings- und
Testdaten) von 0.58 auf 0.75. Für die Testdaten steigt der Score von 0.62 auf
0.77.

Bemerkung: Es erscheint eine Warnung und die Empfehlung, entweder die Anzahl der
Iterationen zu erhöhen oder die Daten zu skalieren. Falls man der Empfehlung
folgen wollte, könnte man folgendermaßen die Daten skalieren:

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

y = data['Outcome']
X = data.drop('Outcome', axis=1)


X = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X, y)


# Training
model_log_regression.fit(X_train, y_train)

# Validierung
score_train = model_log_regression.score(X_train, y_train)
print(f'Score für Trainingsdaten: {score_train:.2f}')
score_test = model_log_regression.score(X_test, y_test)
print(f'Score für Testdaten: {score_test:.2f}')
```
````
