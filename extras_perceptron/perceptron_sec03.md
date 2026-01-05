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

# Training eines Perzeptrons mit Scikit-Learn

Nachdem wir im letzten Abschnitt ein Perzeptron händisch für die
Klassifikationsaufgabe des logischen Oders trainiert haben, benutzen wir nun
Scikit-Learn.

## Lernziele

```{admonition} Lernziele
:class: attention
* Sie können das Perzeptron-Modell von Scikit-Learn laden und mit den gegebenen
  Trainingsdaten trainieren.
* Sie wissen, wie Sie auf die Gewichte des gelernten Modells zugreifen.
```

## Das logische Oder Klassifikationsproblem - diesmal mit Scikit-Learn

Im letzten Abschnitt haben wir händisch ein Perzeptron trainiert. Zur
Erinnerung, wenn wir die Bias-Einheit weglassen, lautet das logische Oder in
Tabellenform wie folgt:

x1 | x2 | y
---|----|---
 0 | 0  | 0
 0 | 1  | 1
 1 | 0  | 1
 1 | 1  | 1

Diese Daten packen wir in ein DataFrame.

```{code-cell} ipython3
import pandas as pd

data =  pd.DataFrame({'x1' : [0, 0, 1, 1], 'x2'  : [0, 1, 0, 1], 'y' : [0, 1, 1, 1]})
data.head()
```

Nun wählen wir das Perzeptron als das zu trainierende ML-Modell aus. Direkt beim
Laden des Modells legen wir die Hyperparameter des Modells fest. Welche
Hyperparameter ein Modell hat, steht in der
[Perzeptron-Dokumentation](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Perceptron.html?highlight=perceptron#sklearn.linear_model.Perceptron).
In diesem Fall wäre beispielsweise die Lernrate ein Hyperparameter. Laut
Dokumentation wird die Lernrate beim Scikit-Learn-Perzeptron mit `eta0`
bezeichnet. Der Python-Code, um das Perzeptron-Modell mit einer Lernrate von 1
zu laden, lautet also wie folgt:

```{code-cell} ipython3
from sklearn.linear_model import Perceptron 
model = Perceptron(eta0 = 1.0)
```

Nun können wir das Perzeptron-Modell mit den Input- und Outputdaten trainieren,
indem wir die `.fit()`-Methode aufrufen. Zuvor bereiten wir die Daten noch
passend für das Perzeptron auf.

```{code-cell} ipython3
X = data[['x1', 'x2']]
y = data['y']

model.fit(X,y)
```

Nachdem wir den letzten Python-Befehl ausgeführt haben, passiert scheinbar
nichts. Nur der Klassenname `Perceptron()` des Objekts `model` wird ausgegeben
(wenn Sie den Code interaktiv ausführen). Intern wurde jedoch das
Perzeptron-Modell trainiert, d.h. die Gewichte des Perzeptrons wurden iterativ
bestimmt. Die Gewichte sind nun in dem Objekt `model` gespeichert. Davon können
wir uns überzeugen, indem wir auf die Attribute des Objekts zugreifen und diese
anzeigen lassen. Die Gewichte sind in dem Attribut `.coef_` gespeichert, während
das Gewicht der Bias-Einheit sich im Attribut `.intercept_` befindet.

```{code-cell} ipython3
print(model.coef_)
print(model.intercept_)
```

Zuletzt können wir das trainierte Perzeptron-Modell Prognosen treffen lassen.
Was prognostiziert das Modell beispielsweise für $x_1=0$ und $x_2=1$? Das
tatsächliche Ergebnis der logischen Oder-Verknüpfung ist $y=1$, was liefert das
Perzeptron?

```{code-cell} ipython3
y_prognose = model.predict([[0, 1]])
print(y_prognose)
```

Wir können auch gleich für alle Datensätze eine Prognose erstellen.

```{code-cell} ipython3
y_prognose = model.predict(X)
print(y_prognose)
```

Tatsächlich funktioniert unser trainiertes Perzeptron zu 100 % korrekt und ist
damit validiert. Bei nur vier Datensätzen lässt sich relativ leicht überblicken,
dass alle vier Prognosen korrekt sind. Sobald die Datenanzahl zunimmt, wird es
schwieriger, den Überblick zu behalten. Daher stellt Scikit-Learn die Methode
`.score()` zur Verfügung, die bei Klassifikatoren die Anzahl der korrekt
prognostizierten Outputs im Verhältnis zur Gesamtanzahl berechnet. Das Ergbnis
ist also eine Bewertung zwischen 0 (keine einzige korrekte Prognose) und 1
(perfekt Prognose).

```{code-cell} ipython3
genauigkeit = model.score(X, y)
print(genauigkeit)
```

## Erkennung von Brustkrebs

Als nächstes betrachten wir einen sehr bekannten ML-Datensatz, nämlich Daten zur
Erkennung von Brustkrebs, siehe
<https://scikit-learn.org/stable/datasets/toy_dataset.html#breast-cancer-dataset>.

```{code-cell} ipython3
# Importieren des Breast Cancer Datensatzes aus Scikit-Learn
import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer

cancer = load_breast_cancer()
data = pd.DataFrame(np.c_[cancer['data'], cancer['target']],
                  columns= np.append(cancer['feature_names'], ['target']))
data.info()
```

Wie immer berschaffen wir uns einen Überblick über die statistischen Kennzahlen.

```{code-cell} ipython3
data.describe()
```

Für das Training des Perzeptrons teilen wir die Daten in Trainings- und Testdaten auf.

```{code-cell} ipython3
from sklearn.model_selection import train_test_split 
data_train, data_test = train_test_split(data, test_size=0.2, random_state=42)

X_train = data_train.loc[:, 'mean radius' : 'worst fractal dimension']
X_test  = data_test.loc[:, 'mean radius' : 'worst fractal dimension']

y_train = data_train['target']
y_test = data_test['target']
```

Nun laden wir das Perzeptron-Modell und trainieren es mit den Trainingsdaten.

```{code-cell} ipython3
# Create a Perceptron model 
model = Perceptron(eta0=0.1)

# Train the model 
model.fit(X_train, y_train)
```

Wie üblich können wir es nun zu Prognosen nutzen.

```{code-cell} ipython3
# Make predictions 
y_test_prognose = model.predict(X_test) 
print(y_test_prognose)
```

Vor allem aber die systematische Bestimmung der Scores für Trainingsdaten und
Testdaten ist interessant:

```{code-cell} ipython3
score_train = model.score(X_train, y_train)
score_test = model.score(X_test, y_test)

print(f'Score Trainingsdaten: {score_train}')
print(f'Score Testdaten: {score_test}')
```

Wir könnten vermuten, dass wir bereits im Bereich des Overfittings sind.
Allerdings ist auch die Initialisierung der Zufallszahlen fixiert. Ohne
`random_state=42` kommen andere Scores für Trainings- und Testdaten heraus, so
dass wir das Perzeptron-Modell zunächst für eine erste Schätzung nehmen dürfen.

## Zusammenfassung und Ausblick

Mit Scikit-Learn steht schon eine Implementierung des Perzeptrons zur Verfügung,
die auch bei größeren Datenmengen eine binäre Klassifikation erlaubt. Welche
Daten dabei überhaupt binär klassifiziert können, klären wir in einem der
folgenden Abschnitte.
