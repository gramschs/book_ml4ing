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

# 9.1 Stacking, Bagging und Boosting

```{admonition} Warnung
:class: warning
Dieser Abschnitt wird gerade überarbeitet.
```

```{admonition} Lernziele
:class: goals
* Sie können in eigenen Worten erklären, was **Ensemble-Methoden** sind.
* Sie können die drei Ensemble-Methoden
  * **Stacking**,
  * **Bagging** und 
  * **Boosting**

  mit Hilfe einer Skizze erklären.
```

## Ensemble-Methoden

Der Begriff »Ensemble« wird im Allgemeinen eher mit Musik und Kunst in
Verbindung gebracht als mit Informatik. In der Musik bezeichnet ein Ensemble
eine kleine Gruppe von Musikern, die entweder das gleiche Instrument spielen
oder verschiedene Instrumente kombinieren. Im Theater bezeichnet man eine Gruppe
von Schauspielern ebenfalls als Ensemble, und in der Architektur beschreibt der
Begriff eine Gruppe von Gebäuden, die in einem besonderen Zusammenhang
zueinander stehen.   

Auch im Bereich des maschinellen Lernens hat sich der Begriff Ensemble
etabliert. Mit **Ensemble-Methoden** (Ensemble Learning) wird eine Gruppe von
maschinellen Modellen bezeichnet, die zusammen eine Prognose treffen sollen.
Ähnlich wie bei Musik-Ensembles können beim **Ensemble Learning** entweder
identische Modelle oder verschiedene Modelle kombiniert werden. Diese Modelle
können entweder gleichzeitig eine Prognose treffen, die dann kombiniert wird,
oder nacheinander verwendet werden, wobei ein Modell auf den Ergebnissen eines
anderen aufbaut. Je nach Vorgehensweise unterscheidet man im maschinellen Lernen
zwischen **Stacking**, **Bagging** und **Boosting**.

In dieser Vorlesung konzentrieren wir uns auf Bagging und Boosting mit ihren
bekanntesten Vertretern, den Random Forests und XGBoost. Das Konzept des
Stackings wird hier nur kurz ohne weitere Details vorgestellt. Eine allgemeine
Einführung in Ensemble-Methoden mit Scikit-Learn findet sich in der
[Dokumentation Scikit-Learn →
Ensemble](https://scikit-learn.org/stable/modules/ensemble.html).


## Stacking

```{figure} pics/concept_stacking.svg
---
width: 100%
---
Konzept Stacking: die Prognosen von mehreren *unterschiedlichen* ML-Modellen
werden zu einer finalen Prognose kombiniert. Die Kombination kann beispielsweise
durch Mehrheitsentscheidung (Voting) oder Mittelwertbildung erfolgen oder durch
ein weiteres ML-Modell.  
```

Stacking bedeutet auf Deutsch »Stapeln«, es werden sozusagen verschiedene
ML-Modelle gestapelt. In einem ersten Schritt werden mehrere ML-Modelle
unabhängig voneinander auf den Trainingsdaten trainiert. Jedes dieser Modelle
liefert eine Prognose, die dann auf verschiedene Arten miteinander kombiniert
werden können. Bei Klassifikationsaufgaben ist **Voting**, also die Wahl durch
**Mehrheitsentscheidung**, eine beliebte Methode, um die Prognosen zu
kombinieren. Wurden beispielsweie für das Stacking drei ML-Modellen gewählt, die
jeweils ja oder nein prognostizieren, dann wird für die finale Prognose das
Ergebnis genommen, das die Mehrheit der einzelnen Modelle vorausgesagt hat.
Scikit-Learn bietet dafür einen Voting Classifier an, siehe [Dokumentation
Scikit-Learn → Voting
Classifier](https://scikit-learn.org/stable/modules/ensemble.html#voting-classifier). 

Bei Regressionsaufgaben werden die einzelnen Prognosen häufig gemittelt.
Dabei kann entweder der übliche arithmetische Mittelwert verwendet werde oder ein
**gewichteter Mittelwert**, was als  **Weighted Averaging** bezeichnet
wird. Nichtsdestotrotz wird die Mittelwertbildung bei Regressionsaufgaben von
Scikit-Learn ebenfalls als Voting bezeichnet, siehe [Dokumentation Scikit-Learn
→ Voting
Regressor](https://scikit-learn.org/stable/modules/ensemble.html#voting-regressor). 

Eine alternative Kombinationsmethode ist die Verwendung eines weiteren
ML-Modells. In diesem Fall werden die Modelle, die die einzelnen Prognosen
liefern, als Basismodelle bezeichnet. In der ML-Community ist auch der
Fachbegriff **Weak Learner**, also schwache Lerner, für diese Basismodelle
gebräuchlich. Die Prognosen der Basismodelle dienen dann als Trainingsdaten für
ein weiteres ML-Modell, das als **Meta-Modell** bezeichnet wird.  Weitere
Informationen liefert die [Scikit-Learn Dokumentation → Stacked
Generalization](https://scikit-learn.org/stable/modules/ensemble.html#stacked-generalization).

Stacking bietet viele Vorteile. Der wichtigste Vorteil ist, dass die
Prognosefähigkeit des Gesamtmodells in der Regel deutlich besser ist als die der
einzelnen Basismodelle. Die Stärken der Basismodelle werden kombiniert und die
Schwächen ausgeglichen. Allerdings erfordert Stacking sehr viel Feinarbeit. Auch
steigt die Trainingszeit für das Gesamtmodell, selbst wenn die Basismodelle bei
genügend Rechenleistung parallel trainiert werden können. Aus diesem Grund
werden wir in dieser Vorlesung kein Stacking verwenden.


## Bagging

TODO

Es gibt verschiedene Methoden, mit denen die Trainingsdaten beim Training eines
Random Forests zufällig ausgewählt werden können:

1. **Bootstrapping**: Dies ist die gängigste Methode zur Auswahl der
Trainingsdaten für jeden Entscheidungsbaum in einem Random Forest. Dabei werden
einzelne Datenpunkte aus der Menge der Trainignsdaten zufällig ausgewählt,
jedoch sofort wieder zurückgelegt. Dadurch können Datenpunkte auch mehrfach
auftauchen, während andere Datenpunkte vielleicht gar nicht zum Training des
Entscheidungsbaumes genutzt werden.

2. **Stratifiziertes Sampling**: Bei dieser Methode werden die Trainingsdaten
anhand eines Kriteriums in verschiedene "Schichten" eingeteilt, aus denen dann
zufällig eine Teilmenge von Beispielen ausgewählt wird. Dies kann nützlich sein,
wenn die Trainingsdaten unausgewogen sind, d. h. es gibt deutlich mehr Beispiele
für eine Klasse als für die andere. Das Stratified Sampling kann dazu beitragen,
dass jeder Baum im Random Forest auf einer repräsentativen Stichprobe der Daten
trainiert wird.

3. **Cluster-Stichproben**: Bei dieser Methode werden die Trainingsdaten in
separate Cluster unterteilt und dann eine Teilmenge der Cluster zufällig
ausgewählt, die für das Training verwendet wird. Dies kann nützlich sein, wenn
die Trainingsdaten auf natürliche Weise in verschiedene Cluster unterteilt sind
und Sie sicherstellen möchten, dass jeder Baum im Random Forest auf einer
repräsentativen Stichprobe der Daten trainiert wird.

Es gibt auch andere Methoden, die zur zufälligen Auswahl der Trainingsdaten
verwendet werden können, wie z. B. das systematische Sampling, bei dem Beispiele
in regelmäßigen Abständen aus dem Trainingssatz ausgewählt werden, und das
einfache Zufallsstichprobenverfahren, bei dem Beispiele ohne Ersetzung zufällig
ausgewählt werden. Die Wahl der Methode hängt von den Besonderheiten der Daten
und den Zielen des Modells ab.


## Boosting

TODO


## Zusammenfassung und Ausblick

TODO