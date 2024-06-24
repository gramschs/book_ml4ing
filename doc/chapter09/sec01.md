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
Die Prognosen von mehreren *unterschiedlichen* ML-Modellen werden zu einer
finalen Prognose kombiniert. Die Kombination kann beispielsweise durch
Mehrheitsentscheidung (Voting) oder Mittelwertbildung (Averaging) erfolgen.
Werden die Einzelprognosen durch ein weiteres ML-Modell zu einer finalen
Prognose kombiniert, nennt man das *Stacking*.
```

Stacking bedeutet auf Deutsch »Stapeln«, es werden sozusagen verschiedene
ML-Modelle gestapelt. In einem ersten Schritt werden mehrere ML-Modelle
unabhängig voneinander auf den Trainingsdaten trainiert. Jedes dieser Modelle
liefert eine Prognose, die dann auf verschiedene Arten miteinander kombiniert
werden können. Bei Klassifikationsaufgaben ist **Voting**, also die Wahl durch
**Mehrheitsentscheidung**, eine beliebte Methode, um die Einzelprognosen zu
kombinieren. Wurden beispielsweie für das Stacking drei ML-Modellen gewählt, die
jeweils ja oder nein prognostizieren, dann wird für die finale Prognose das
Ergebnis genommen, das die Mehrheit der einzelnen Modelle vorausgesagt hat.
Scikit-Learn bietet dafür einen Voting Classifier an, siehe [Dokumentation
Scikit-Learn → Voting
Classifier](https://scikit-learn.org/stable/modules/ensemble.html#voting-classifier). 

Bei Regressionsaufgaben werden die einzelnen Prognosen häufig gemittelt. Dabei
kann entweder der übliche arithmetische Mittelwert verwendet werden oder ein
**gewichteter Mittelwert**, was als  **Weighted Averaging** bezeichnet wird.
Nichtsdestotrotz wird die Mittelwertbildung bei Regressionsaufgaben von
Scikit-Learn ebenfalls als Voting bezeichnet, siehe [Dokumentation Scikit-Learn
→ Voting
Regressor](https://scikit-learn.org/stable/modules/ensemble.html#voting-regressor). 

Eine alternative Kombinationsmethode ist die Verwendung eines weiteren
ML-Modells. In diesem Fall werden die Modelle, die die einzelnen Prognosen
liefern, als Basismodelle bezeichnet. In der ML-Community ist auch der
Fachbegriff **Weak Learner**, also schwache Lerner, für diese Basismodelle
gebräuchlich. Die Prognosen der Basismodelle dienen dann als Trainingsdaten für
ein weiteres ML-Modell, das als **Meta-Modell** bezeichnet wird. Diese
Ensemble-Methode wird **Stacking** genannt. Weitere Informationen liefert die
[Scikit-Learn Dokumentation → Stacked
Generalization](https://scikit-learn.org/stable/modules/ensemble.html#stacked-generalization).

Stacking bietet viele Vorteile. Der wichtigste Vorteil ist, dass die
Prognosefähigkeit des Gesamtmodells in der Regel deutlich besser ist als die der
einzelnen Basismodelle. Die Stärken der Basismodelle werden kombiniert und die
Schwächen ausgeglichen. Allerdings erfordert Stacking sehr viel Feinarbeit. Auch
steigt die Trainingszeit für das Gesamtmodell, selbst wenn die Basismodelle bei
genügend Rechenleistung parallel trainiert werden können. Aus diesem Grund
werden wir in dieser Vorlesung kein Stacking verwenden.


## Bagging 

```{figure} pics/concept_bagging.svg
---
width: 100%
---
Beim Bagging wird das gleiche ML-Modell auf *unterschiedlichen* Stichproben der
Trainingsdaten trainiert (Bootstrapping). Die Einzelprognosen der Modelle werden
dann zu einer finalen Prognose kombiniert (Aggregating).
```

Bagging ist eine Ensemble-Methode, ähnlich wie Stacking. Im Gegensatz zum
Stacking wird beim Bagging jedoch dasselbe Modell für die Einzelprognosen
verwendet. Die Unterschiede in den Einzelprognosen entstehen dadurch, dass für
das Training der einzelnen Modelle unterschiedliche Daten verwendet werden.

Im ersten Schritt werden zufällige Datenpunkte aus den Trainingsdaten ausgewählt
und in einen neuen Datensatz, „Stichprobe 1“, aufgenommen. Nachdem ein
Datenpunkt ausgewählt wurde, kehrt er in die ursprüngliche Menge der
Trainingsdaten zurück und kann erneut ausgewählt werden. Dieser Prozess wird in
der Mathematik als **Ziehen mit Zurücklegen** bezeichnet, auf Englisch
**Bootstrapping**. Durch Bootstrapping werden dann noch weitere Stichproben
gebildet.

Im zweiten Schritt wird ein ML-Modell gewählt und für jede Bootstrap-Stichprobe
trainiert. Da die Stichproben unterschiedliche Trainingsdaten enthalten,
entstehen unterschiedlich trainierte Modelle, die für neue Daten verschiedene
Einzelprognosen liefern. Diese Einzelprognosen werden kombiniert bzw. nach
festgelegten Regeln zu einer finalen Prognose zusammengefasst. In der Statistik
wird die Zusammenfassung von Daten als Aggregation bezeichnet. Auf Englisch
heißt der Vorgang des Zusammenfassens **Aggregating**.

Die beiden wesentlichen Schritte der Bagging-Methode sind also **B**ootstrapping
und **Agg**regat**ing**, was zu der Abkürzung Bagging geführt hat. Scikit-Learn
bietet sowohl für Klassifikations- als auch für Regressionsaufgaben eine
allgemeine Implementierung der Bagging-Methode an (siehe [Dokumentation
Scikit-Learn →
Bagging](https://scikit-learn.org/stable/modules/ensemble.html#bagging-meta-estimator)).
Die bekannteste Bagging-Methode ist das Verfahren **Random Forests**, bei dem
Entscheidungsbäume (Decision Trees) auf unterschiedlichen Stichproben trainiert
und aggregiert werden. Random Forests werden wir im nächsten Kapitel
detaillierter betrachten. Vorab beschäftigen wir uns noch mit dem Konzept der
Boosting-Methoden.


## Boosting

TODO


## Zusammenfassung und Ausblick

TODO