---
jupytext:
  formats: ipynb,md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.13.8
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

# Was ist maschinelles Lernen?

## Lernziele

```{admonition} Lernziele
:class: important
* Sie wissen, wie langes es das Forschungsgebiet **maschinelles Lernen** gibt und warum es sich in den letzten beiden Jahrzehnten so stark entwickelt hat.
* Sie kennen Basis-Fachbegriffe des maschinellen Lernens wie **Feature**, **Target** und **Label**.
* Sie können anhand eines Beispiels erklären, was die Fachbegriffe
  * **überwachtes Lernen**,
  * **unüberwachtes Lernen** und
  * **verstärkendes Lernen**
  bedeuten.
* Sie können beim überwachten Lernen zwischen **Regression** und **Klassifikation** unterscheiden.
```

## Ein wenig Geschichte

Es ist ein weit verbreiteter Irrtum, dass die Forschungsgebiete "Künstliche
Intelligenz" oder "maschinelles Lernen" neu sind und dem 21. Jahrhundert
zuzuordnen sind. Tatsächlich hat bereits Arthur L. Samuel maschinelles Lernen
beschreiben als

> »... ein Forschungsgebiet, das Computer in die Lage versetzen soll, zu lernen,
ohne explizit darauf programmiert zu sein.« (Arthur L. Samuel, 1959)

Dennoch ist richtig, dass beides sich vor allem in den letzten zwei Jahrzehnten
revolutionär entwickelt hat. Dafür gibt es drei Gründe, wie im folgenden Video
erklärt wird:

<iframe width="560" height="315" src="https://www.youtube.com/embed/l_HSWmxMRlU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Wir kürzen in dieser Vorlesung maschineller Lernen mit ML ab.

## Maschinelles Lernen = Algorithmen + Daten

Ein notwendiger Baustein des maschinellen Lernens sind Daten, am besten ganz,
ganz viele! Aber selbst ein riesiger Haufen an Daten ist alleine wertlos. Erst
durch Algorithmen, die in diesen Daten Muster finden, gewinnen wir neues Wissen,
können Prozesse analysieren und Entscheidungen treffen. 

Was ist ein Algorithmus? In dem folgenden Video wird zuerst erklärt, was ein
Algorithmus ist. Dann wird aufgezeigt, was so schwierig daran ist, einen
Algorithmus zu entwickeln, der Katzenbilder von Hundebildern unterscheidet.
Schauen Sie sich das Video an und beantowrten Sie folgende Fragen:

* Geben Sie drei Beispiele für Algorithmen.
* In dem Video wird der Fachbegriff "Feature" eingeführt. Was bedeutet der Begriff?
* Wie lautet der ML-Fachbegriff für Zielgröße?
* Erklären Sie in eigenen Worten, was der Fachbegriff "Labelling" bedeutet.

<iframe width="560" height="315" src="https://www.youtube.com/embed/HmUzceKCI9I" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Maschinelles Lernen wird in drei Kategorien eingeteilt: 
* Überwachtes Lernen (Supervised Learning),
* Unüberwachtes Lernen (Unsupervised Learning) und
* Verstärkendes Lernen (Reinforcement Learning).

Im Folgenden betrachten wir für jede der drei Kategorien typische Beispiele.

## Überwachtes Lernen (Supervised Learning)

Das überwachte Lernen wiederum wird in zwei Arten unterteilt:
* Regression und
* Klassifikation.

Im letzten Video ist ein Klassifikationsproblem vorgestellt worden. Ein
ML-Algorithmus sollte erkennen, ob das Bild einen Hund oder eine Katze zeigt.
Sicherlich sind Ihnen aber auch schon Regressionsprobleme begegnet, bei denen
numerische Werte prognostiziert werden sollen. Auf beide Problemarten gehen
die beiden nächsten Videos ein:

### Regression 

Im folgenden Video wird erklärt, was der Fachbegriff **Regression** bedeutet.
Welches Beispiel aus Ihrem Alltag oder Studium fällt Ihnen ein, das ebenfalls
ein Regressionsproblem ist?

<iframe width="560" height="315" src="https://www.youtube.com/embed/NCCctUdfA3E" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Klassifikation

Zurück zu den Hunden und Katzen. Ist die Zielgröße nicht ein kontinuierlicher
Wert, der durch Zahlen beschrieben werden kann, sondern versuchen wir, Klassen
zu bilden, so handelt es sich um **Klassifikation**. Da wir zu den Eingangsdaten
die Klassenbezeichnungen vorgeben, gehören Klassifikationsprobleme ebenso wie
Regressionsprobleme zu den überwachten ML-Lernverfahren.

Schauen Sie sich das nächste Video an.
* Welche Klassen werden genannt?
* Was sind die Features?

<iframe width="560" height="315" src="https://www.youtube.com/embed/g6zuVEDlAzo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Springen Sie am Ende noch einmal zum Zeitindex 2:45 min und betrachten Sie sich
die gelabelten Datenpunkte. Welches Mischungsverhältnis und welche
Ofentemperatur würden Sie wählen, um ein gutes Produkt herzustellen?

## Unüberwachtes Lernen (Unsupervised Learning)

Unüberwachtes Lernen kommt in der Praxis seltener vor. Eine sehr populäre
Methode des unüberwachten Lernens ist das **Clustering**. Welches Beispiel wird
im folgenden Video für Clusterin vorgestellt?

<iframe width="560" height="315" src="https://www.youtube.com/embed/P2Qwc63iCVQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Verstärkendes Lernen (Reinforcement Learning)

Wir schließen unsere Übersicht der maschinellen Lernverfahren mit dem
verstärkendem Lernen ab. Auch wenn es das Lernverfahren ist, mit dem wir
Menschen lernen, werden wir in dieser Vorlesung nicht weiter darauf eingehen.

<iframe width="560" height="315" src="https://www.youtube.com/embed/5HhQgFCQGIY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Zusammenfassung

In diesem Abschnitt haben Sie die drei wichtigsten Kategorien des maschinellen
Lernens kennengelernt: überwachtes Lernen, unüberwachtes Lernen und
verstärkendes Lernen. Für die Ingenieurwissenschaften ist vor allem das
überwachte Lernen von Bedeutung. Dabei unterscheiden wir zwischen überwachtem
Lernen für diskrete Zielgrößen (= Klassen, Kategorien), das wir Klassifikation
nennen, und überwachtem Lernen für kontinuierliche Zielgrößen, das wir
Regression nennen.
