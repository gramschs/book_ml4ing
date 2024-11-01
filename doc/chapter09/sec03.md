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

# 9.3 XGBoost

In der bisherigen Vorlesung haben wir vor allem Pandas und Scikit-Learn benutzt.
Zwar bietet Scikit-Learn Boosting-Verfahren an, in vielen Wettbewerben hat sich
jedoch eine andere Bibliothek durchgesetzt, die eine optimierte Variante des
Stochastic Gradient Boosting anbietet: **XGBoost**.

```{admonition} Warnung
:class: warning
Falls bei Ihnen XGBoost nicht installiert sein sollte, folgen Sie bitte den Anweisungen auf der Internesetseite [https://xgboost.readthedocs.io](https://xgboost.readthedocs.io/en/stable/install.html) und installieren Sie XGBoost jetzt nach.
```

## Lernziele

```{admonition} Lernziele
:class: goals
* Sie können XGBoost für Regressions- und Klassifikationsaufgaben einsetzen.
* Sie wissen, wie Sie mit Analysen der Maßzahlen Fehler und Logloss für
  Trainings- und Testdaten beurteilen können, ob Überanpassung (Overfitting)
  vorliegt.
* Sie kennen die Methode **Frühes Stoppen** zur Reduzierung der Überanpassung
  (Overfitting).
* Sie wissen, dass XGBoost nicht manuell feinjustiert werden sollte, sondern mit
  Gittersuche oder weiteren Bibliotheken (z.B. Optuna).
```

## XGBoost benutzt Scikit-Learn API

XGBoost steht für e**X**treme **G**radient **Boost**ing und ist aus
Performancegründen in der Programmiersprache C++ implementiert. Für
Python-Programmier wurde ein Python-Modul mit dem Ziel geschaffen, die gleichen
Schnittstellen wie Scikit-Learn anzubieten, so dass kaum Einarbeitungszeit in
eine neue Bibliothek erforderlich ist. Vor allem benötigen Data Scientists auch
keine C++\-Programmierkenntnisse, sondern können weiterhin mit Python arbeiten.

Wir bleiben bei unserem Beispiel mit der Verkaufsaktion im Autohaus aus dem
vorherigen Kapitel.

```{code-cell}
import pandas as pd 
from sklearn.datasets import make_moons

# Erzeugung künstlicher Daten
X_array, y_array = make_moons(n_samples=120, random_state=0, noise=0.3)

daten = pd.DataFrame({
    'Kilometerstand [km]': 10000 * (X_array[:,0] + 2),
    'Preis [EUR]': 5000 * (X_array[:,1] + 2),
    'verkauft': y_array,
    })
```

XGBoost kann Pandas DataFrames nicht verarbeiten, sondern benötigt die reinen
Zahlenwerte in Form von Matrizen. Das ist in der Tat kein Problem, denn die
Datenstruktur DataFrame stellt die reinen Matrizen über die Methode `.values`
direkt zur Verfügung.

```{code-cell}
# Adaption der Daten
X = daten[['Kilometerstand [km]', 'Preis [EUR]']].values
y = daten['verkauft'].values
```

Als nächstes importieren wir XGBoost. Es ist üblich, das ganze Modul zu
importieren und mit `xgb` abzukürzen. Danach initialisieren wir das
Klassifikationsmodell `XGBClassifier` und trainieren es auf den Daten.

```{code-cell}
import xgboost as xgb 

modell = xgb.XGBClassifier()
modell.fit(X,y)
```

Als nächstes visualisieren wir die Prognose des trainierten
XGBoost-Klassifikators.

```{code-cell}
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.colors import ListedColormap
from sklearn.inspection import DecisionBoundaryDisplay

my_colormap = ListedColormap(['#EF553B33', '#636EFA33'])
fig = DecisionBoundaryDisplay.from_estimator(modell, X,  cmap=my_colormap)
fig.ax_.scatter(X[:,0], X[:,1], c=y, cmap=my_colormap)
fig.ax_.set_xlabel('Kilometerstand [km]');
fig.ax_.set_ylabel('Preis [EUR]');
fig.ax_.set_title('XGBoost: Entscheidungsgrenzen');
```

Die Entscheidungsgrenzen sehr plausibel aus.

## XGBoost neigt stark zur Überanpassung (Overfitting)

XGBoost ist bekannt für Überanpassung (Overfitting) an die Trainingsdaten. Um
das an unserem Beispiel mit der Verkaufsaktion im Autohaus zu zeigen, fügen wir
noch neue, unbekannte Testdaten hinzu. Dazu verdoppeln wir die Anzahl der Autos
(`n_samples=2000`).

```{code-cell}
# Erzeugung künstlicher Daten
X_array, y_array = make_moons(n_samples=2000, random_state=0, noise=0.3)

daten = pd.DataFrame({
    'Kilometerstand [km]': 10000 * (X_array[:,0] + 2),
    'Preis [EUR]': 5000 * (X_array[:,1] + 2),
    'verkauft': y_array,
    })

X = daten[['Kilometerstand [km]', 'Preis [EUR]']].values
y = daten['verkauft'].values
```

Anschließend teilen wir die 2000 Autos in zwei Gruppen: Trainings- und
Testdaten.

```{code-cell}
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X,y, train_size=0.5, random_state=0)
```

Diesmal legen wir explizit fest, aus wievielen Modellen das Boosting-Verfahren
bestehen soll. Dazu setzen wir `n_estimators=200`. Oft wird auch von der Anzahl
der »Boosting-Runden« gesprochen. Das Training auf den Trainingsdaten liefert
sehr gute Ergebnisse:

```{code-cell}
import xgboost as xgb

modell = xgb.XGBClassifier(n_estimators=200)

modell.fit(X_train, y_train)

score_train = modell.score(X_train, y_train)
print(f'Score bezogen auf Trainingsdaten: {score_train:.2f}')
score_test = modell.score(X_test, y_test)
print(f'Score bezogen auf Testdaten: {score_test:.2f}')
```

Die Trainingsdaten werden perfekt prognostiziert. Auch bei den Testdaten
erhalten wir ein gutes Ergebnis, das aber im Vergleich zu dem sehr guten Score
bei den Trainingsdaten abfällt. Es fällt schwer, zu entscheiden, ob eine
Überanpassung (Overfitting) vorliegt. XGBoost ist ein iteratives Verfahren.
Zunächst wird Modell Nr. 1 trainiert, darauf aufbauend Modell Nr. 2 usw. Wir
wiederholen jetzt das Training des XGBoost-Klassifikators, aber lassen durch ein
weiteres Argument mitprotokollieren, was in den einzelnen Iterationen passiert.

Zuerst legen wir fest, welche internen Bewertungskennzahlen (= Metrik, Maßzahl)
mitprotokolliert werden sollen. Wir wählen als erste Maßzahl den Fehler, also
die relative Anzahl der falsch klassifizierten Autos. Die zweite Maßzahl
berechnet, wie weit die Wahrscheinlichkeit für »verkauft« oder »nicht verkauft«
vom tatsächlichen Ergebnis weg ist. Mathmatisch etwas präziser betrachten wir
die [Kreuzentropie](https://de.wikipedia.org/wiki/Kreuzentropie), bekannt als
»Losslog«.

Technisch setzen wir dies um, indem wir bei der Initialisierung des
XGBoost-Modells das optionale Argument `eval_metric=['error', 'logloss']`
setzen.

```{code-cell}
modell = xgb.XGBClassifier(n_estimators=200, eval_metric=['error', 'logloss'])
```

Allerdings ist damit noch nicht festgelegt, auf welchen Daten die Fehler-Maßzahl
und die Logloss-Maßzahl berechnet werden. Zunächst sollen beide Maßzahlen für
die Trainingsdaten berechnet werden, dann für die Testdaten. Das erreichen wir
mit dem optionalen Argument `eval_set=`, dem wir folgendermaßen die Trainings-
und Testdaten mitgeben.

```{code-cell}
modell.fit(X_train, y_train, eval_set=[(X_train, y_train), (X_test, y_test)], verbose=False)
```

Wir setzen noch `verbose=False`, damit nicht für jedes Modell bzw. jede
Iteration die vier Maßzahlen auf dem Bildschirm ausgegeben werden. Nach dem
Training können wir die vier Maßzahlen mit der Methode `.evals_result()` aus dem
trainierten Modell extrahieren. Um die Maßzahlen zu visualisieren, packen wir
sie in einen Pandas-DataFrame.

```{code-cell} ipython3
masszahlen = modell.evals_result()
fehler = pd.DataFrame({
    'Fehler Trainingsdaten': masszahlen['validation_0']['error'],
    'Fehler Testdaten': masszahlen['validation_1']['error']
    })
losslog = pd.DataFrame({
    'Losslog Trainingsdaten': masszahlen['validation_0']['logloss'],
    'Losslog Testdaten': masszahlen['validation_1']['logloss']
    })
```

Wir visualisieren Fehler und Losslog getrennt voneinander.

```{code-cell}
import plotly.express as px 

fig = px.scatter(fehler,
    title='Fehler in jeder Iteration (Boosting-Runde)',
    labels={'value': 'Fehler', 'index': 'Iteration', 'variable': 'Legende'})
fig.show()
```

Der Fehler bei den Trainingsdaten wird von Boosting-Runde zu Boosting-Runde
kleiner, aber der Fehler der Testdaten wächst. Zunächst wird der Fehler der
Testdaten kleiner, erreicht in Minimum in der 6. Iteration, um dann wieder zu
steigen. Dieses Verhalten ist typisch für Überanpassung (Overfitting). Etwas
deutlicher wird dieses Phänomen, wenn wir uns die (transoformierte) Differenz
der Wahrscheinlichkeiten ansehen, die Losslog-Maßzahl.

```{code-cell}
import plotly.express as px 

fig = px.scatter(losslog,
    title='Losslog in jeder Iteration (Boosting-Runde)',
    labels={'value': 'Losslog', 'index': 'Iteration', 'variable': 'Legende'})
fig.show()
```

Am kleinsten ist die Losslog-Maßzahl für die Iteration 9, danach steigt die
Losslog-Maßzahl wieder an. Am besten wäre es nach dieser Analyse gewesen, nach
der 6. oder 9. Iteration aufzuhören, da dann die Überanpassung (Overfitting) an
die Trainingsdaten einsetzt.

## Bekämpfen von Überanpassung (Overfitting)

Es gibt einige Hyperparamter von XGBoost, die helfen, Überanpassung
(Overfitting) zu reduzieren. Eine Möglichkeit ist es, früher zu stoppen und
nicht die voreingestellte Anzahl an Modellen bzw. Iterationen / Boosting-Runden
zu durchlaufen. Das wird durch das optionale Argument `early_stopping_rounds=`
im Konstruktor ermöglicht. Die Zahl, die diesem Parameter übergeben wird, gibt
die Anzahl der Boosting-Runden vor, nach denen gestoppt wird, falls sich kaum
etwas an der Maßzahl geändert hat.

```{code-cell}
modell = xgb.XGBClassifier(n_estimators=200, early_stopping_rounds=10, eval_metric=['error', 'logloss'])
modell.fit(X_train, y_train, eval_set=[(X_train, y_train), (X_test, y_test)], verbose=False)
```

Visualisiert sieht die Losslog-Statistik für das obige Beispiel so aus:

```{code-cell}
masszahlen = modell.evals_result()
fehler = pd.DataFrame({
    'Fehler Trainingsdaten': masszahlen['validation_0']['error'],
    'Fehler Testdaten': masszahlen['validation_1']['error']
    })
losslog = pd.DataFrame({
    'Losslog Trainingsdaten': masszahlen['validation_0']['logloss'],
    'Losslog Testdaten': masszahlen['validation_1']['logloss']
    })

fig = px.scatter(fehler,
    title='Frühes Stoppen: Fehler',
    labels={'value': 'Fehler', 'index': 'Iteration', 'variable': 'Legende'})
fig.show()

fig = px.scatter(losslog,
    title='Frühes Stoppen: Losslog',
    labels={'value': 'Losslog', 'index': 'Iteration', 'variable': 'Legende'})
fig.show()
```

Eine weitere Möglichkeit, Überanpassung (Overfitting) zu reduzieren, besteht
darin, die Tiefe der Entscheidungsbäume zu begrenzen. Wir benutzen
Entscheidungsbaum-Stümpfe, die eine Tiefe von Eins haben. Das erreichen wir mit
dem optionalen Argument `max_depth=1`.

```{code-cell}
modell = xgb.XGBClassifier(max_depth=1, n_estimators=200, eval_metric=['error', 'logloss'])
modell.fit(X_train, y_train, eval_set=[(X_train, y_train), (X_test, y_test)], verbose=False)

masszahlen = modell.evals_result()
fehler = pd.DataFrame({
    'Fehler Trainingsdaten': masszahlen['validation_0']['error'],
    'Fehler Testdaten': masszahlen['validation_1']['error']
    })
losslog = pd.DataFrame({
    'Losslog Trainingsdaten': masszahlen['validation_0']['logloss'],
    'Losslog Testdaten': masszahlen['validation_1']['logloss']
    })

fig = px.scatter(fehler,
    title='Begrenzte Entscheidungsbäume: Fehler',
    labels={'value': 'Fehler', 'index': 'Iteration', 'variable': 'Legende'})
fig.show()

fig = px.scatter(losslog,
    title='Begrenzte Entscheidungsbäume: Losslog',
    labels={'value': 'Losslog', 'index': 'Iteration', 'variable': 'Legende'})
fig.show()
```

Es gibt noch einige weitere Hyperparameter, die für "das" beste Modell
feinjustiert werden können. Händisch gelingt es kaum, alle Hyperparameter
optimal einzustellen, so dass hier eine Gittersuche oder gar eine Bibliothek wie
[Optuna](https://github.com/optuna/optuna) eingesetzt werden sollte.

## Zusammenfassung und Ausblick

Mit XGBoost haben Sie ein ML-Modell für das überwachte Lernen kennengelernt, das
in den vergangen Jahren sehr viele Wettbewerbe gewonnen hat. Die Mächtigkeit der
Algorithmen führt aber häufig zur Überanpassung (Overfitting), so dass die
sorgsame Feinjustierung der Hyperparameter besonders wichtig ist.
