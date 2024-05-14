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

# 7.1 Theorie der linearen Regression 

Die lineare Regression gehört zu den überwachten maschinellen Lernverfahren
(Supervised Learning). Meist ist sie das erste ML-Modell, das eingesetzt wird,
um Regressionsprobleme zu lösen. In diesem Kapitel stellen wir die theoretischen
Grundlagen der linearen Regression vor.

## Lernziele

```{admonition} Lernziele
:class: goals
* Sie kennen das **lineare Regressionsmodell**.
* Sie können erklären, was die **Fehlerquadratsumme** ist.
* Sie wissen, dass das Training des lineare Regressionsmodells durch die
  **Minimierung** der Fehlerquadratsumme (Kleinste-Quadrate-Schätzer) erfolgt.
* Sie können mit dem **Bestimmtheitsmaß** bzw. **R²-Score** beurteilen, ob das
  lineare Regressionsmodell geeignet zur Erklärung der Daten ist.
```


## Regression kommt aus der Statistik

In der Statistik beschäftigen sich Mathematikerinnen und Mathematiker bereits
seit Jahrhunderten damit, Analyseverfahren zu entwickeln, mit denen
experimentelle Daten gut erklärt werden können. Falls wir eine “erklärende”
Variable haben und wir versuchen, die Abhängigkeit einer Messgröße von der
erklärenden Variable zu beschreiben, nennen wir das Regressionsanalyse oder kurz
**Regression**. Bei vielen Problemen suchen wir nach einem linearen Zusammenhang
und sprechen daher von **linearer Regression**. Mehr Details finden Sie auch bei
[Wikipedia → Regressionsanalyse](https://de.wikipedia.org/wiki/Regressionsanalyse).

Etwas präziser formuliert ist lineare Regression ein Verfahren, bei dem es eine
Einflussgröße $x$ und eine Zielgröße $y$ gibt. In der ML-Sprechweise wird die
Einflussgröße $x$ typischerweise als Merkmal (oder englisch Feature) bezeichnet.
Die Zielgröße (manchmal auch Output oder Target genannt), soll stetig sein
(manchmal auch kontinuierlich, metrisch oder quantitativ genannt). Zu dem
Merkmal oder den Merkmalen liegen $M$ Datenpunkte mit den dazugehörigen Werte
der Zielgröße vor. Diese werden üblicherweise als Paare (wenn nur ein Merkmal
vorliegt) zusammengefasst:

$$(x^{(1)},y^{(1)}), \, (x^{(2)},y^{(2)}), \, \ldots, \, (x^{(M)},y^{(M)}).$$ 

Ziel der linearen Regression ist es, zwei Parameter $w_0$ und $w_1$ so zu
bestimmen, dass möglichst für alle Datenpunkte $(x^{(i)}, y^{(i)})$ die lineare
Gleichung 

$$y^{(i)} \approx w_0 + w_1 x^{(i)}$$

gilt. Geometrisch ausgedrückt: durch die Daten soll eine Gerade gelegt werden,
wie die folgende Abbildung zeigt. Die Datenpunkte sind blau, die
Regressionsgerade ist in rot visualisiert.

```{figure} pics/Linear_regression.svg
---
name: fig_linear_regression
---
Lineare Regression: die erklärende Variable (= Input oder unabhängige Variable oder Ursache) ist auf der x-Achse, die
abhängige Variable (= Output oder Wirkung) ist auf der y-Achse aufgetragen, Paare von Messungen sind in blau
gekennzeichnet, das Modell in rot. 
([Quelle:](https://en.wikipedia.org/wiki/Linear_regression#/media/File:Linear_regression.svg) "Example of simple linear regression, which has one independent variable" von Sewaqu. Lizenz: Public domain))
```

In der Praxis werden die Daten nicht perfekt auf der Geraden liegen. Die Fehler
zwischen dem echten $y^{(i)}$ und dem Funktionswert der Gerade $f(x^{(i)}) = w_0 +
w_1 x^{(i)}$ werden unterschiedlich groß sein, je nachdem, welche Parameter
$w_0$ und $w_1$ gewählt werden. Wie finden wir jetzt die beste Kombination $w_0$
und $w_1$, so dass diese Fehler möglichst klein sind?


## Wie groß ist der Fehler?

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
Residuen. Dann wird diese **Fehlerquadratsumme** minimiert, um die Koeffizienten
des Regressionsmodells zu berechnen.


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

<iframe width="560" height="315" src="https://lti.mint-web.de/examples/index.php?id=01010320"  allowfullscreen>
</iframe>


## Zusammenfassung und Ausblick

In diesem Abschnitt haben Sie das theoretische Modell der linearen Regression
kennengelernt. Im nächsten Kapitel trainieren wir ein lineares Regressionsmodell
mit Scikit-Learn.
