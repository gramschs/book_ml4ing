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

# Übung

```{admonition} Aufgabe 
:class: tip

Auf der Internetseite
https://archive.ics.uci.edu/dataset/151/connectionist+bench+sonar+mines+vs+rocks
finden Sie einen Datensatz mit Sonarsignalen. Die Muster der Signals sind durch
60 Zahlenwerte codiert (es handelt sich um die Energie zu bestimmten
Frequenzen). Darüber hinaus wird angegeben, ob das Sonarsignal Gestein (= Stein)
oder Metall detektiert hat.

Laden Sie nun die Datei 'metall_oder_stein.csv'. Führen Sie eine explorative
Datenanalyse durch. Lassen Sie dann alle Ihnen bekannten Klassifikations-Modelle
trainieren und validieren, um die Materialeigenschaft Stein/Metall auf Basis der
numerischen Werte zu prognostizieren.
```

````{admonition} Lösung 
:class: tip, toggle

Import der Daten (es gibt keine Spaltenüberschriften, daher wird das optionale Argument 'header=None' gesetzt):

```python
import pandas as pd

data = pd.read_csv('metall_oder_stein.csv', header=None, skiprows=2)
data.info()
```

Blick in die Daten:

```python
data.head()
```

Der Datensatz enthält 208 Einträge und 61 Eigenschaften. Die ersten 60
Eigenschaften werden durch Floats repräsentiert, die Eigenschaft '60' wird durch
Objekte repräsentiert. 

Allerdings ist die Ausgabe beschränkt, so dass wir nicht mehr ablesen können, ob
alle Einträge gefüllt sind. Wir nutzen daher die Methode '.isnull()', um
NA-Werte aufzuspüren. Die Methode liefert Booleans zurück. Wir summieren über
das Ergebnis spaltenweise (False = 0, True = 1).

```python
anzahl_ungueltige_eintraege = data.isnull().sum()
anzahl_ungueltige_eintraege.describe()
```

Offensichtlich sind alle Spalten in der Summe 0, bestehen also nur aus False.
Daher sind alle Einträge gültig.

Als nächstes untersuchen wir, welche Einträge in der 61. Spalte, also
Eigenschaft 60 enthalten sind.

```python
data[60].unique()
```

Die letzte Spalte enthält nur zwei verschiedene String-Werte: Stein oder Metall.

```python
data.describe()
```

Die statistischen Kennzahlen lassen sich so kaum interpretieren. Daher hilft hier ein Boxplot.

```python
import plotly.express as px

fig = px.box(data.loc[:, 0:59], 
             title='Stein oder Metall',
             labels={'variable': 'Eigenschaft', 'value':'Wert'})
fig.show()
```

Die Median-Werte scheinen einem Muster zu folgen. Beginnend bei Eigenschaft 0 steigen sie bis zu Eigenschaft 25, wo der Median den Wert 0.7545 erreicht, um dann wieder abzufallen. Ab Eigenschaft 49 liegt der Median unter 0.0179. Bei Eigenschaften mit einem größeren Median ist auch der Interquartilsabstand größer, dafür gibt es keine Ausreißer. Das Maximum scheint bei 1 zu liegen, wobei man das noch genauer untersuchen müsste. 

Als nächstes schauen wir uns, wie die Zielgröße verteilt ist.

```python
fig = px.bar(data[60].value_counts(),
             title='Stein oder Metall',
             labels={'index': 'Material', 'value': 'Anzahl', 'variable': 'Eigenschaft'})

fig.show()
```

Die beiden Materialen sind ungefähr gleich verteilt, 53 % der untersuchten
Proben sind Metall, 47 % sind Stein.

```python
from sklearn.model_selection import train_test_split

X = data.loc[:,0 : 59]
y = data.loc[:, 60]
y.replace('Stein', 0, inplace=True)
y.replace('Metall', 1, inplace=True)

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
```

```python
from sklearn.linear_model import Perceptron, LogisticRegression

model_perceptron = Perceptron()
model_perceptron.fit(X_train, y_train)
score_perceptron_train = model_perceptron.score(X_train, y_train)
score_perceptron_test = model_perceptron.score(X_test, y_test)

print(f'Score Trainingsdaten Perzeptron: {score_perceptron_train :.2f}')
print(f'Score Testdaten Perzeptron: {score_perceptron_test :.2f}')

model_log_reg = LogisticRegression()
model_log_reg.fit(X_train, y_train)
score_log_reg_train = model_log_reg.score(X_train, y_train)
score_log_reg_test = model_log_reg.score(X_test, y_test)

print(f'Score Trainingsdaten logistische Regression: {score_log_reg_train :.2f}')
print(f'Score Testdaten logistische Regression: {score_log_reg_test :.2f}')
```

```python
from sklearn.svm  import SVC

model_svm_linear = SVC(kernel='linear')
model_svm_linear.fit(X_train, y_train)
score_svm_linear_train = model_svm_linear.score(X_train, y_train)
score_svm_linear_test = model_svm_linear.score(X_test, y_test)

print(f'Score Trainingsdaten lineare SVM: {score_svm_linear_train :.2f}')
print(f'Score Testdaten lineare SVM: {score_svm_linear_test :.2f}')

model_svm_rbf = SVC(kernel='rbf')
model_svm_rbf.fit(X_train, y_train)
score_svm_rbf_train = model_svm_rbf.score(X_train, y_train)
score_svm_rbf_test = model_svm_rbf.score(X_test, y_test)

print(f'Score Trainingsdaten RBF SVM: {score_svm_rbf_train :.2f}')
print(f'Score Testdaten RBF SVM: {score_svm_rbf_test :.2f}')
```

```python
from sklearn.tree import DecisionTreeClassifier

model_decision_tree = DecisionTreeClassifier()
model_decision_tree.fit(X_train,y_train)

score_decision_tree_train = model_decision_tree.score(X_train, y_train)
score_decision_tree_test = model_decision_tree.score(X_test, y_test)

print(f'Score Trainingsdaten Entscheidungsbaum: {score_decision_tree_train :.2f}')
print(f'Score Testdaten Entscheidungsbaum: {score_decision_tree_test :.2f}')
```

```python
from sklearn.ensemble import RandomForestClassifier

list_score_train = []
list_score_test = []
for n in range(1,101):
    model_random_forest = RandomForestClassifier(n_estimators=n, random_state=0)
    model_random_forest.fit(X_train, y_train)

    score_random_forest_train = model_random_forest.score(X_train, y_train)
    score_random_forest_test = model_random_forest.score(X_test, y_test)

    print(f'Anzahl Entscheidungsbäume: {n} \t Score Training: {score_random_forest_train :.2f} | Score Test: {score_random_forest_test :.2f}')

    list_score_train.append(score_random_forest_train)
    list_score_test.append(score_random_forest_test)

score_random_forest = pd.DataFrame({'Trainingsscore': list_score_train, 'Testscore': list_score_test})
fig = px.scatter(score_random_forest)
fig.show()
```

Ab Index 51 scheint sich Trainingsscore und Testscore zu stabilisieren, wir
wählen daher 'n_estimators' = 51. Damit hat der Random Forest den höchsten 
Trainings- und Testscore.
````