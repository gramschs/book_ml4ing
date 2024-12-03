---
jupytext:
  formats: ipynb,md:myst
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

# Übung

## Aufgabe 6.1

Das Schiff Titanic galt bei seiner Fertigstellung als unsinkbar. 1912
kollidierte die Titanic mit einem Eisberg und sank. Bei dem Unglück kamen 1514
von 2220 Personen ums Leben, so dass der Titanic-Untergang zu den größten
Unglücken der Schifffahrt zählt. Mehr Informationen zu der Titanic finden Sie
bei Wikipedia
[https://de.wikipedia.org/wiki/Titanic_(Schiff)](https://de.wikipedia.org/wiki/Titanic_(Schiff)).

In der folgenden Übung werden Passagierlisten der Titanic benutzt, um die
Überlebenswahrscheinlichkeit zu prognostizieren (0 = gestorben, 1 = überlebt),
deren Quelle hier ist:
[https://www.kaggle.com/c/titanic](https://www.kaggle.com/c/titanic).

Laden sie den Datensatz 'titanic_DE_cleaned.csv'.

Führen Sie eine explorative Datenanalyse (EDA) durch. Führen Sie dazu
Python-Code in Code-Zellen aus und geben Sie in Markdown-Zellen Ihre Antworten
auf die folgenden Frage an.

1. Welche Daten enthält der Datensatz? Wie viele Personen sind in der Tabelle
   enthalten? Wie viele Merkmale werden dort beschrieben?

```{code-cell} ipython3
import pandas as pd 
daten = pd.read_csv('titanic_DE_cleaned.csv')

daten.info()
```

Der Datensatz enthält 183 Einträge, also 183 Personen. Es gibt 11 Merkmale.

+++

2. Sind die Daten vollständig?

+++

Die Daten sind vollständig. Für jedes Merkmal werden 183 non-null Einträge angezeigt.

+++

3. Welchen Datentyp haben die Merkmale? Welche Merkmale sind numerisch und
   welche sind kategorial?

+++

Die Merkmale ueberlebt, Klasse, Anzahl_Geschwister_Partner, Anzahl_Eltern_Kinder sind Integers. Die Merkmale Alter und Ticketpreis sind Floats. Die Merkmale Name, Geschlecht, Ticket, Kabine und Einstiegshafen sind Objekte. Mit `.head()`schauen wir uns die ersten fünf Zeilen an:

```{code-cell} ipython3
daten.head()
```

Name, Tickets und Kabine sind Strings. Geschlecht und Einstiegshafen sind zwar vom Datentyp her Strings, könnten aber hier auch für Klassen stehen.

+++

4. Erstellen Sie eine Übersicht der statistischen Merkmale für die numerischen
   Daten. Visualisieren Sie anschließend die statistischen Merkmale mit
   Boxplots. Interpretieren Sie die statistischen Merkmale. Gibt es Ausreißer?
   Sind die Werte plausibel?

```{code-cell} ipython3
daten.describe()
```

Die statistischen Daten zu `'ueberlebt'` sind unplausibel. Auch wenn hier Integer verwendet wurden, um überlebt/nicht überlebt zu klassifizieren, sind es eigentlich Klassen und sollten daher nicht statistisch ausgewertet werden.

Auf der Titanic gab es drei Preisklassen von 1 bis 3. Minimum und Maximum sind plausibel, aber dass 75 % der Passagiere in Klasse 1 (der teuersten Klasse) mitgereist sind, erscheint unwahrscheinlich.

Beim Alter fällt auf, dass das minimale Alter 0.92 ist. Da Jahre normalerweise als ganze Zahlen angegeben werden, ist das ungewöhnlich, aber nicht unplausibel. Die älteste Person war 80 Jahre alt. Der Durchschnitt lag bei 35.6 Jahren und der Median bei 36. 75 % der Passagiere waren jünger als 47.5 Jahre. Es erscheint plausibel, das vor allem jüngere Passagiere die Strapazen der Schifffahrt auf sich genommen haben.  

50 % der Passagiere reisten alleine, nur sehr wenige in Familien.

Offensichtlich wurden Passagiere auch kostenlos mitgenommen, denn der minimale Ticketpreis ist 0. Das Maximum verwundert, vielleicht eine Umrechnung der Währungen, denn normalerweise werden nur 2 Nachkommastellen angegeben.

```{code-cell} ipython3
import plotly.express as px 

kastendiagramm = px.box(daten[['Klasse', 'Alter', 'Anzahl_Geschwister_Partner', 'Anzahl_Eltern_Kinder', 'Ticketpreis']],
                       labels={'value': 'Wert', 'variable': 'Merkmal'},
                       title='Boxplot der numerischen Werte des Titanic-Datensatzes')
kastendiagramm.show()
```

Beim Ticketpreis gibt es deutiche Ausreißer, bei den anderen Merkmalen gibt es vereinzelte Ausreißer.

+++

5. Untersuchen Sie die kategorialen Daten. Sind es wirklich kategoriale Daten?
   Prüfen Sie für jedes kategoriale Merkmal die Einzigartigkeit der auftretenden
   Werte und erstellen Sie ein Balkendiagramm mit den Häufigkeiten.

```{code-cell} ipython3
merkmale = ['Name', 'Geschlecht', 'Ticket', 'Kabine', 'Einstiegshafen']
for m in merkmale:
    einzigartige_eintraege = daten[m].unique()
    anzahl = len(einzigartige_eintraege)
    print(f'Merkmal {m} hat {anzahl} einzigartige Einträge.')
```

Beim Merkmal Geschlcht gibt es nur zwei verschiedene Einträge, beim Einstiegshafen nur drei verschiedene Einstiegshäfen. Das sind (ungeordnete) kategoriale Daten. Die anderen Merkmale sind zu verschieden und sind damit nicht mehr als kategoriale Daten einzustufen. Es werden daher die Balkendiagramme mit den Häufigkeiten nur für die beiden Merkmale Geschlecht und Einstiegshafen erstellt.

```{code-cell} ipython3
geschlecht = daten['Geschlecht']

balkendiagramm_geschlecht = px.bar(geschlecht.value_counts(),
                                  labels={'value': 'Anzahl', 'variable': 'Geschlecht'},
                                  title='Häufigkeit Geschlecht')
balkendiagramm_geschlecht.show()
```

```{code-cell} ipython3
hafen = daten['Einstiegshafen']

balkendiagramm_hafen = px.bar(hafen.value_counts(),
                                  labels={'value': 'Anzahl', 'variable': 'Hafen'},
                                  title='Häufigkeit Einstiegshafen')
balkendiagramm_hafen.show()
```

6. Trainieren Sie mit den numerischen Merkmalen einen Entscheidungsbaum/Decision Tree.

```{code-cell} ipython3
X = daten[['Klasse', 'Alter', 'Anzahl_Geschwister_Partner',	'Anzahl_Eltern_Kinder',	'Ticketpreis']]
y = daten['ueberlebt']

from sklearn.tree import DecisionTreeClassifier

entscheidungsbaum =  DecisionTreeClassifier()
entscheidungsbaum.fit(X,y)
entscheidungsbaum.score(X,y)
```

7. Visualisieren Sie den Entscheidungsbaum

```{code-cell} ipython3
from sklearn.tree import plot_tree

plot_tree(entscheidungsbaum);
```

8. Spielen Sie mit den Hyperparametern des Entscheidungsbaumes/Decision Trees. Begrenzen Sie die Baumtiefe auf 2, 3 und 4. Was sind die wichtigsten Merkmale, die ein Überleben der Passagiere gesichert haben?

```{code-cell} ipython3
for baumtiefe in [2, 3, 4]:
    baum = DecisionTreeClassifier(max_depth=baumtiefe)
    baum.fit(X,y)
    score = baum.score(X,y)
    print(f'Score für eine Baumtiefe von {baumtiefe}: {score: .2f}')
```

Tatsächlich ist der Entscheidungsbaum/Decision Tree mit einer Baumtiefe von 3 und 4 kaum besser als der mit einer Baumtiefe von 2. Wir werten daher den Entscheidungsbaum mit einer Baumtiefe von 2 aus:

```{code-cell} ipython3
finales_modell = DecisionTreeClassifier(max_depth=2)
finales_modell.fit(X,y)

plot_tree(finales_modell,
    feature_names=['Klasse', 'Alter', 'Anzahl_Geschwister_Partner',	'Anzahl_Eltern_Kinder',	'Ticketpreis'],
    class_names=['nicht ueberlebt', 'ueberlebt']);
```

Zunächst einmal erscheint ein jüngeres Alter die Überlebenschance erhöht zu haben. Danach wirkt es so, also ob der Ticketpreis eine wichtige Rolle gepsielt haben könnte.

```{code-cell} ipython3

```

```{code-cell} ipython3

```

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
#
```

2. Sind die Daten vollständig?

```{code-cell} ipython3
#
```

3. Welchen Datentyp haben die Merkmale? Welche Merkmale sind numerisch und
   welche sind kategorial?

```{code-cell} ipython3
#
```

4. Erstellen Sie eine Übersicht der statistischen Merkmale für die numerischen
   Daten. Visualisieren Sie anschließend die statistischen Merkmale mit
   Boxplots. Interpretieren Sie die statistischen Merkmale. Gibt es Ausreißer?
   Sind die Werte plausibel?

```{code-cell} ipython3
#
```

5. Erstellen Sie eine Scatter-Matrix mit Insulin, BMI und Outcome. Welche der
  beiden Eigeschaften Insulin oder BMI könnte ehr geeignet sein, Diabetes
  ja/nein zu prognostizieren?

```{code-cell} ipython3
#
```

6. Visualisieren Sie Diabetes ja/nein in Abhängigkeit der gewählten Eigenschaft.
  Vermuten Sie einen Zusammenhang?

```{code-cell} ipython3
#
```

7. Trainieren Sie mit den numerischen Merkmalen einen Entscheidungsbaum/Decision Tree.

```{code-cell} ipython3
#
```

8. Visualisieren Sie den Entscheidungsbaum

```{code-cell} ipython3
#
```

9. Spielen Sie mit den Hyperparametern des Entscheidungsbaumes/Decision Trees. Begrenzen Sie die Baumtiefe auf 2, 3 und 4. Was sind die wichtigsten Merkmale, die ein Überleben der Passagiere gesichert haben?

```{code-cell} ipython3
#
```
