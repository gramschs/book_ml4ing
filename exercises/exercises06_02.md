---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.16.3
kernelspec:
  display_name: python312
  language: python
  name: python3
---

## Aufgabe 6.2

Der Datensatz 'diabetes.csv' ist eine Sammlung von medizinischen Daten, die vom
National Institute of Diabetes and Digestive and Kidney Diseases, erhoben
wurden, siehe
[https://www.kaggle.com/datasets/whenamancodes/predict-diabities?resource=download](https://www.kaggle.com/datasets/whenamancodes/predict-diabities?resource=download).
Bei Frauen des Pima-Stammes wurden folgende medizinische Daten erhoben:

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

Führen Sie eine explorative Datenanalyse (EDA) durch. Führen Sie dazu
Python-Code in Code-Zellen aus und geben Sie in Markdown-Zellen Ihre Antworten
auf die folgenden Frage an.

1. Welche Daten enthält der Datensatz? Wie viele Personen sind in der Tabelle
   enthalten? Wie viele Merkmale werden dort beschrieben?

```{code-cell} ipython3
import pandas as pd 

daten = pd.read_csv('diabetes.csv')
daten.info()
```

Der Datensatz enthält 768 Personen mit insgesamt 9 Merkmalen. Aufgelistet sind die Merkmale Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age und Outcome.

+++

2. Sind die Daten vollständig?

Die Daten sind für jedes Merkmal vollständig. In jeder Spalte gibt es 768 non-null Einträge.

3. Welchen Datentyp haben die Merkmale? Welche Merkmale sind numerisch und
   welche sind kategorial?

Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, Age und Outcome sind Integers. BMI und DiabetesPedigreeFunction sind Floats. Kein Merkmal wird als object eingestuft.

4. Erstellen Sie eine Übersicht der statistischen Merkmale für die numerischen
   Daten. Visualisieren Sie anschließend die statistischen Merkmale mit
   Boxplots. Interpretieren Sie die statistischen Merkmale. Gibt es Ausreißer?
   Sind die Werte plausibel?

```{code-cell} ipython3
daten.describe()
```

Die Pregnancies reichen von 0 Schwangerschaften bis hin zu 17 Schwangerschaften, was ungewöhnlich hoch ist. Der Mittelwert von 3.85 Schwangerschaften erscheint plausibel, 50 % der Frauen waren maximal dreimal schwanger.

Der Glucose-Wert reicht von 0 bis 199. An der Stelle müsste mit einem Mediziner Rücksprache gehalten werden, ob ein Glucose-Wert von 0 plausibel ist. 

Beim BloodPressure, also den Blutdruck, ist der minimale Wert von 0 jedoch unplausibel. Eine PErson mit einem Blutdruck von 0 ist tot. 

SkinThickness kann erneut nur von Medizinern korrekt eingeordnet werden. Ob eine minimale SkinThickness von 0 und eine maximale SkinThickness von 99 sinnvolle Werte darstellen, können Nichtmediziner nicht sinnvoll beurteilen.

Auch der minimale Insulin-Wert von 0 wirkt seltsam sowie der Body-Maß-Index BMI. Ein BMI von 0 kann nicht sein, denn beim BMI wird das Gewicht einer Person durch die quadrierte Körpergröße geteilt. Ein BMI von 0 bedeutet ein Gewicht von 0, was nicht sein kann.

Die DiabetesPedigree-Funktion können wir ohne medizinisches Fachwissen nicht bewerten.

Beim Alter fällt auf, dass keine Kinder dabei waren. Die jüngste Person ist 21, das mittlere Alter liegt bei 33 Jahren und 75 % aller Personen sind jünger als 41. 

Das Outcome darf nicht einfach statistisch interpretiert werden. Das Outcome gibt an, ob eine Person Diabetes hat (1) oder nicht (0). Auch wenn hier Zahlen verwendet wurden, ist das Outcome eigentlich ein kategoriales Merkmal. Es ist sogar die kategoriale Zielgröße unserer Problemstellung.

5. Erstellen Sie eine Scatter-Matrix mit Insulin, BMI und Outcome. Welche der
  beiden Eigeschaften Insulin oder BMI könnte ehr geeignet sein, Diabetes
  ja/nein zu prognostizieren?

```{code-cell} ipython3
import plotly.express as px 

auswahl = ['Insulin', 'BMI', 'Outcome']
fig = px.scatter_matrix(daten[auswahl],
    title='Wirkung Insulin und BMI auf Diabetes')
fig.show()
```

Beim Insulin kann man kaum eine Wirkung des Insulins auf den Diabeteszustand erkennen. Beim BMI kann man erkennen, dass ein höherer BMI scheinbar mehr zu Diabetes führt als ein niedriger BMI.

```{code-cell} ipython3
fig = px.scatter(daten, x = 'BMI', y = 'Outcome',
    title='Wirkung BMI auf Diabetes')
fig.show()
```

Es ist kaum ein Zusammenhang erkennbar außer der Feststellung, dass höherer BMI anscheinend häufiger mit Diabetes korreliert ist als niedriger BMI.

7. Trainieren Sie mit den numerischen Merkmalen einen Entscheidungsbaum/Decision Tree.

```{code-cell} ipython3
X = daten.loc[:, 'Pregnancies' : 'Age']
y = daten['Outcome']
```

```{code-cell} ipython3
from sklearn.tree import DecisionTreeClassifier

modell = DecisionTreeClassifier()
modell.fit(X,y)

score = modell.score(X,y)
print(f'Score: {score:.2f}')
```

8. Visualisieren Sie den Entscheidungsbaum

```{code-cell} ipython3
from sklearn.tree import plot_tree

plot_tree(modell);
```

9. Spielen Sie mit den Hyperparametern des Entscheidungsbaumes/Decision Trees. Begrenzen Sie die Baumtiefe auf 2, 3 und 4. Was sind die wichtigsten Merkmale, die Diabetes auslösen können?

```{code-cell} ipython3
for baumtiefe in [2, 3, 4]:
    baum = DecisionTreeClassifier(max_depth=baumtiefe)
    baum.fit(X,y)
    score = baum.score(X,y)
    print(f'Score für eine Baumtiefe von {baumtiefe}: {score: .2f}')
```

Wieder gibt es kaum Unetrschiede im Score für die verschiedenen Baumtiefen. Wir betrachten nun ein Modell das Baumtiefe 2.

```{code-cell} ipython3
finales_modell = DecisionTreeClassifier(max_depth=2)
finales_modell.fit(X,y)

plot_tree(finales_modell,
    feature_names=['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin',
       'BMI', 'DiabetesPedigreeFunction', 'Age'],
    class_names=['kein Diabetes', 'Diabetes']);
```

Als erstes Entscheidungskriteriujm wird der Glucose-Wert benutzt. Je nachdem, ob der Glucose-Wert kleiner 127.5 ist oder nicht, wird danach das Alter (jünger als 28.5 bedeutet dann kein Diabetes) oder der BMI (kleiner als 29.95 kein Diabetes) als Entscheidungsmerkmal verwendet.
