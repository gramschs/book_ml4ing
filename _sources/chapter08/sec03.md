---
jupytext:
  formats: ipynb,md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.0
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

# Training eines Perzeptrons mit Scikit-Learn

Nachdem wir im letzten Abschnitt ein Perzeptron händisch für die Klassifikationsaufgabe des logischen Oders trainiert haben, lernen wir in diesem Abschnitt eine Bibliothek kennen, die das Training für uns übernimmt.

## Lernziele

```{admonition} Lernziele
:class: hint
* Sie kennen die Bibliothek Scikit-Learn.
* Sie können den grundlegenden Ablauf eines ML-Projektes mit Scikit-Learn beschreiben.
* Sie wissen, wie Sie die Trainingsdaten als Matrix bzw. Vektor mit dem Modul Numpy repräsentieren.
* Sie können das Perzeptron-Modell von Scikit-Learn laden und mit den gegebenen Trainingsdaten trainieren.
* Sie wissen, wie Sie auf die Gewichte des gelernten Modells zugreifen.
```

## Scikit-Learn

Gute Nachricht vorneweg: Sie müssen die ML-Algorithen nicht selbst
implementieren, das haben bereits Wissenschaftler:innen aus der Mathematik und
der Informatik erledigt. Eine der bekanntesten Bibliotheken bzw. eines der
bekanntesten Module ist Scikit-Learn

> https://scikit-learn.org/

das wir auch für diese Vorlesung verwenden werden. Bitte stellen Sie jetzt
sicher, dass Scikit-Learn bei Ihnen installiert ist. 

Das Modul Scikit-Learn wird mit ``sklearn`` abgekürzt, alle Funktionen werden
also z.B. mit

```{code-cell} ipython3
import sklearn
```

in den Namensraum importiert. Da das Modul aber so mächtig ist, werden wir immer
nur einzelne Funktionen aus Scikit-Learn importieren. 

## Grundlegender ML-Workflow mit Scikit-Learn 

Die ML-Algorithmen des Scikit-Learn-Moduls haben dabei immer die gleiche
Schnittstelle (API). Damit ist gemeint, dass die Methoden- und Funktionsnamen
für alle ML-Modelle gleich gewählt sind. Auch ist die Art und Weise, wie die
Trainingsdaten verarbeitet werden, stets gleich. Wir können den grundlegenden
Ablauf eines typischen ML-Projektes folgendermaßen zusammenfassen:

```{admonition} Wie funktioniert der grundlegende ML-Workflow mit Scikit-Learn?
:class: note

1. Zuerst packen wir die Inputdaten in eine Matrix X, bei der jede Spalte eine Eigenschaft repräsentiert. Die Zeilen stehen für die verschiedenen Datensätze.
2. Falls wir ein überwachtes Lernverfahren anwenden wollen, packen wir die Outputdaten in einen Vektor y.
3. Nun wählen wir ein Modell aus, das trainiert werden soll. 
4. Dazu spezifizieren wir die Hyperparameter des Modells. Hyperparameter sind Parameter des Modells, die wir vorab ohne die genaue Kenntnis der Daten festlegen.
5. Wir trainieren das ML-Modell, indem wir die fit()-Methode des Modells aufrufen.
6. Um das Modell zur Prognose neuer Daten zu verwenden, benutzten wir die predict()-Methode.
7. Zuletzt wird das Modell analysiert, validiert und produktiv eingesetzt.
```

## Das logische Oder Klassifikationsproblem - diesmal mit Scikit-Learn 

Im letzten Abschnitt {ref}`perzeptron_training_logisches_oder` haben wir
händisch ein Perzeptron trainiert. Zur Erinnerung, wenn wir die Bias-Einheit
weglassen, lautet das logische Oder in Tabellenform wie folgt:

x1 | x2 | y
---|----|---
 0 | 0  | 0
 0 | 1  | 1
 1 | 0  | 1
 1 | 1  | 1

Diese Daten formulieren wir nun als eine Inputmatrix $X$ mit den Spalten x1 und
x2. Für die Erzeugung und Weiterverarbeitung der Matrizen laden wir das Modul
Numpy.

```{code-cell} ipython3
import numpy as np

X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
    ])
```

Den Output formulieren wir als Vektor, ebenfalls mit Hilfe des Numpy-Moduls.

```{code-cell} ipython3
y = np.array([0, 1, 1, 1])
````

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
modell = Perceptron(eta0 = 1.0)
```

Nun können wir das Perzeptron-Modell mit den Input- und Outputdaten trainieren, indem wir die `.fit()`-Methode aufrufen.

```{code-cell} ipython3
modell.fit(X,y)
```

Nachdem wir den letzten Python-Befehl ausgeführt haben, passiert scheinbar
nichts. Nur der Klassenname `Perceptron()` des Objekts `modell` wird ausgegeben
(wenn Sie den Code interaktiv ausführen). Intern wurde jedoch das
Perzeptron-Modell trainiert, d.h. die Gewichte des Perzeptrons wurden iterativ
bestimmt. Die Gewichte sind nun in dem Objekt `modell` gespeichert. Davon können
wir uns überzeugen, indem wir auf die Attribute des Objekts zugreifen und diese
anzeigen lassen. Die Gewichte sind in dem Attribut `.coef_` gespeichert, während
das Gewicht der Bias-Einheit sich im Attribut `.intercept_` befindet.

```{code-cell} ipython3
print(modell.coef_)
print(modell.intercept_)
```

Zuletzt können wir das trainierte Perzeptron-Modell Prognosen treffen lassen.
Was prognostiziert das Modell beispielsweise für $x_1=0$ und $x_2=1$? Das
tatsächliche Ergebnis der logischen Oder-Verknüpfung ist $y=1$, was liefert das
Perzeptron?

```{code-cell} ipython3 
y_prognose = modell.predict(np.array([[0, 1]]))
print(y_prognose)
```

Wir können auch gleich für alle Datensätze eine Prognose erstellen.

```{code-cell} ipython3 
y_prognose = modell.predict(X)
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
genauigkeit = modell.score(X, y)
print(genauigkeit)
```

## Zusammenfassung und Ausblick

Mit Scikit-Learn steht schon eine Implementierung des Perzeptrons zur Verfügung,
die auch bei größeren Datenmengen eine binäre Klassifikation erlaubt. Welche
Daten dabei überhaupt binär klassifiziert können, klären wir in einem der
folgenden Abschnitte.
