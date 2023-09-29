---
jupytext:
  formats: ipynb,md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.7
kernelspec:
  display_name: Python 3.9.13 ('python39')
  language: python
  name: python3
---

# Training eines linearen Regressionsmodells

## Lernziele

```{admonition} Lernziele
:class: important
* Sie können erklären, was die **Fehlerquadratsumme** ist.
* Sie wissen, dass das Training des lineare Regressionsmodells durch die
  **Minimierung** der Fehlerquadratsumme (Kleinste-Quadrate-Schätzer) erfolgt.
* Sie können mit dem **Bestimmtheitsmaß** bzw. **R²-Score** beurteilen, ob das
  lineare Regressionsmodell geeignet zur Erklärung der Daten ist.
```

+++

## Was ist die "beste" Regressionsgerade?

Im letzten Abschnitt hat Scikit-Learn als Steigung 186.8 und für den
y-Achsenabschnitt -8330 geschätzt. Ist das tatsächlich das beste lineare
Regressionsmodell für die vorgegebenen Daten? Wie werden Regressionsmodelle
miteinander vergleichen?

Das Prinzip für das lineare Regressionsmodell und auch die folgenden ML-Modelle
ist jedesmal gleich. Das Modell ist eine mathematische Funktion, die aber noch
Parameter (hier beispielsweise die Koeffizienten der Gerade) enthält. Dann wird
festgelegt, was eine gute Prognose ist, also wie Fehler berechnet und beurteilt
werden sollen. Das hängt jeweils von dem bettrachteten Problem ab. Sobald das
sogenannte Fehlermaß feststeht, werden die Parameter der Modellfunktion so
berechnet, dass das Fehlermaß (z.B. Summe der Fehler oder Mittelwert der Fehler)
möglichst klein wird. In der Mathematik sagt man dazu **Minimierungsproblem**. 

Für die lineare Regression wird als Fehlermaß die Kleinste-Quadrate-Schätzung
verwendet (siehe [Wikipedia  → Methode der kleinsten
Quadrate](https://de.wikipedia.org/wiki/Methode_der_kleinsten_Quadrate)). Dazu
berechnen wir, wie weit weg die Gerade von den Messpunkten ist. Wie das geht,
veranschaulichen wir uns mit der folgenden Grafik.

```{figure} pics/kq_regression.png
---
width: 600px
name: kq_regression
---
Messpunkte (blau) und der Abstand (grün) zu einer Modellfunktion (rot)

([Quelle:](https://de.wikipedia.org/wiki/Methode_der_kleinsten_Quadrate#/media/Datei:MDKQ1.svg) Autor: Christian Schirm, Lizenz: CC0) 
```

Unsere rote Modellfunktion trifft die Messpunkte mal mehr und mal weniger gut.
Wir können jetzt für jeden Messpunkt berechnen, wie weit die rote Kurve von ihm
weg ist (= grüne Strecke), indem wir die Differenz der y-Koordinaten errechnen:
$r = y_{\text{blau}}-y_{\text{rot}}$. Diese Differenz nennt man **Residuum**.
Danach summieren wir die Fehler (also die Residuen) auf und erhalten den
Gesamtfehler. Leider kann es dabei passieren, dass am Ende als Gesamtfehler 0
herauskommt, weil beispielsweise für den 1. Messpunkt die blaue y-Koordinate
unter der roten y-Koordinate liegt und damit ein negatives Residuum herauskommt,
aber für den 5. Messpunkt ein positives Residuum. Daher quadrieren wir die
Residuen. Scikit-Learn minimiert diese **Fehlerquadratsumme**, um die
Koeffizienten des Regressionsmodells zu berechnen.

+++

## Ist das beste Modell gut genug?

Auch wenn wir mit der Minimierung der Fehlerquadratsumme bzw. der
Kleinsten-Quadrate-Methode die besten Parameter für unsere Modellfunktion
gefunden haben, heißt das noch lange nicht, dass unser Modell gut ist. Bereits
die Modellfunktion kann ja völlig falsch gewählt sein. Beispielsweise könnten
wir Messungen rund um eine sinus-förmige Wechselspannung vornehmen und dann wäre
ein lineares Regressionsmodell völlig ungeeignet, auch wenn die
Fehlerquadratsumme minimal wäre.

Wir brauchen daher noch ein Kriterium dafür, ob das trainierte Modell auch
valide ist. Über die Validierung eines ML-Modells werden wir auch in den
nächsten Vorlesungen noch intensiv sprechen. Für die lineare Regression
betrachten wir erstmal das **Bestimmtheitsmaß**, das in der ML-Community auch
**R²-Score** genannt wird.

Beim R²-Score wird zunächst der Mittelwert der Fehlerquadratsumme mit der
Modellfunktion $f$ gebildet:

$$\frac{1}{M}\sum_{i=1}^M (y^{(i)} - f(x^{(i)})^2. $$

Danach wird der Mittelwert der Output-Daten gebildet, nämlich

$$\bar{y} = \frac{1}{M} \sum_{i=1}^{M} y^{(i)}.$$

Nun wird dieser Mittelwert in die Fehlerquadratsumme eingesetzt, als ob die
Modellfunktion die konstante Funktion $f(x)=\bar{y}$ wäre.

$$\frac{1}{M}\sum_{i=1}^M (y^{(i)} - \bar{y})^2.$$

Diese beiden Fehlerquadratsummen werden nun miteinander ins Verhältnis gesetzt.
Wir vergleichen sozusgen den mittleren Fehler bei Wahl der Modellfunktion mit
dem mittleren Fehler, wenn wir machen würden, wenn wir einfach nur den
Mittelwert als Schätzer für unser Modell nehmen würden. 

In der Statistik wurde dieses Verhältnis (Gesamtfehler geteilt durch
Gesamtfehler Mittelwert) als Qualitätkriterium für ein lineares
Regressionsproblem festgelegt. Genaugenommen, rechnet man 1 - Gesamtfehler /
(Gesamtfehler Mittelwert) und nennt diese Zahl Bestimmtheitsmaß oder R²-Score.
Die Formel zur Berechnung des R²-Scores lautet:

$$R^2 = 1 - \frac{\sum_{i=1}^M (y^{(i)} - f(x^{(i)}))^2}{\sum_{i=1}^M(y^{(i)}-\bar{y})}. $$

Dabei kürzt sich das $\frac{1}{M}$ im Zähler und Nenner weg. Nachdem der
R²-Score ausgerechnet wurde, können wir nun die Qualität der Anpassung
beurteilen:

* Wenn $R^2 = 1$  ist, dann gibt es den perfekten linearen Zusammenhang und die
  Modellfunktion ist eine sehr gute Anpassung an die Messdaten.
* Wenn $R^2 = 0$ oder gar negativ ist, dann funktioniert die lineare
  Modellfunktion überhaupt nicht.

+++

## Interaktive Visualisierung R²-Score

Auf der Seite [https://mathweb.de](https://mathweb.de) finden Sie eine Reihe von
Aufgaben und interaktiven Demonstrationen rund um die Mathematik. Insbesondere
gibt es dort auch eine interaktive Demonstration des R²-Scores.

Drücken Sie auf den zwei kreisförmigen Pfeile rechts oben. Dadurch wird ein
neuer Datensatz erzeugt. Die Messdaten sind durch grüne Punkte dargestellt, das
lineare Regressionsmodell durch eine blaue Gerade. Im Titel wird der aktuelle
und der optimale R²-Wert angezeigt. Ziehen Sie an den weißen Punkten, um die
Gerade zu verändern. Schaffen Sie es, den optimalen R²-Score zu treffen?
Beobachten Sie dabei, wie die Fehler (rot) kleiner werden.

<iframe width="560" height="315" src="https://lti.mint-web.de/examples/index.php?id=01010320"  allowfullscreen></iframe>

+++

## R²-Score mit Scikit-Learn

Müssen Sie die Formel für das Bestimmtheitsmaßes jetzt auswendig lernen? Nein,
dafür ist Scikit-Learn da. Verwenden Sie einfach die Methode `.score()`, um sich
das Bestimmtheitsmaß ausgeben zu lassen.

Damit lautet das vollständige Training des linearen Regressionsmodells:

```{code-cell} ipython3
import pandas as pd
from sklearn.linear_model import LinearRegression

# Vorbereitung der DAten
data_raw = pd.read_csv('data/autoscout24-germany-dataset.csv')
data = data_raw.dropna().copy()
data = data.drop([11753, 11754, 21675])

# Extraktion der Input- und Output-Daten als NumPy-Arrays
X = data.loc[:, 'hp'].values.reshape(-1,1)
y = data.loc[:, 'price'].values

# Modellwahl
model = LinearRegression()

# Training
model.fit(X, y)

# Prognose
y_predict = model.predict(X)

# Validierung
r2 = model.score(X, y)
print('Der R2-Score ist: {:.2f}'.format(r2))
```

Ein R²-Score von 0.61 ist zur Not brauchbar, aber eigentlich würden wir jetzt
nach einem besseren Modell suchen.

+++

## Zusammenfassung

In diesem Abschnitt haben Sie gelernt, dass das Training eines linearen
Regressionsmodells darauf beruht, die Fehlerquadratsumme zu minimieren. Um
überhaupt beurteilen zu können, ob ein ML-Modell geeignet ist, brauchen wir
Qualitätskriterien. Für das lineare Regressionsmodell dient das Bestimmtheitsmaß
bzw. der R²-Score als Qualitätskriterium.
