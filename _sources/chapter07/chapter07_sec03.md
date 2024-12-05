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

# 7.3 Polynomiale Regression

In den letzten beiden Kapiteln haben wir uns mit der linearen Regression
befasst. Dabei haben wir die einfache lineare Regression betrachtet, bei der die
Zielgröße von einem einzelnen Merkmal abhängt, sowie die multiple lineare
Regression, bei der die Zielgröße von mehreren Merkmalen beeinflusst wird. In
diesem Kapitel werden wir uns damit beschäftigen, wie eine Regression für
quadratische, kubische oder allgemein für polynomiale Modelle durchgeführt wird.

## Lernziele

```{admonition} Lernziele
:class: goals
* Sie können eine **polynomiale Regression** durchführen.
* Sie wissen, dass die Wahl des Polynomgrades entscheidend dafür ist, ob
  **Underfitting (Unteranpassung)**, **Overfitting (Überanpassung)** oder ein
  geeignetes Modell vorliegt.
* Sie wissen, dass der Polynomgrad ein **Hyperparameter** ist.
```

## Künstliches Experiment zu Bremswegen eines Autos

Ausnahmsweise werden wir uns in diesem Kapitel nicht mit dem Verkauf von Autos
beschäftigen, sondern mit dem Bremsweg von Autos. Die Faustformel zur Berechnung
des Bremsweges $s$ in Metern lautet

$$s = \frac{1}{100} \cdot v^2,$$

wobei die Geschwindigkeit $v$ des Autos in km/h angegeben wird. Natürlich
variiert der tatsächliche Bremsweg abhängig von der Straßenoberfläche (trocken /
nass / vereist) oder dem Fahrzeugtyp (inbesondere Leistung der Bremse). Wird die
Bremsung aufgrund eines plötzlich auftauchenden Hindernisses eingeleitet, kommt
zum Bremwsweg noch der Reaktionsweg hinzu. Mehr Details finden Sie auf den
Internetseiten des ADAC unter [Bremsweg berechnen: Mit dieser Formel
geht's](https://www.adac.de/verkehr/rund-um-den-fuehrerschein/erwerb/bremsweg-berechnen/).

Wir simulieren nun ein Experiment, bei dem der Bremsweg von Autos abhängig von
der Geschwindigkeit gemessen wird. In einem ersten schritt erzeugen wir zufällig
50 Geschwindigkeiten zwischen 30 km/h und 150 km/h. Gemäß der obigen Faustformel
lassen wir zunächst die dazugehörigen Bremswege berechnen, addieren dann aber
noch zufällige Schwankungen.

```{code-cell}
import numpy as np 
import pandas as pd 

np.random.seed(0)
anzahl_experimente = 50
v_min = 30
v_max = 151

v = np.floor( np.random.uniform(v_min, v_max, anzahl_experimente) )
zufaellige_schwankungen = 3 * np.random.normal(0, 1, anzahl_experimente)
bremsweg = 1/100 * v**2 

daten = pd.DataFrame({
    'Geschwindigkeit [km/h]': v,
    'Bremsweg [m]': bremsweg + zufaellige_schwankungen,
    })
```

Als nächstes lassen wir die künstlich erzeugten Bremsweg-Experimente visualisieren.

```{code-cell}
import plotly.express as px 

fig = px.scatter(daten, x = 'Geschwindigkeit [km/h]', y = 'Bremsweg [m]',
    title='Künstliche Daten: Bremsweg eines Autos')
fig.show()
```

## Erster Versuch: lineare Regression

Als erstes verwenden wir die lineare Regression, um ein Modell für die Messdaten
zu finden. Wenn wir die Geschwindigkeit mit $x$ bezeichnen und den Bremsweg mit
$y$, dann lautet das lineare Regressionsmodell

$$y = \omega_0 + \omega_1 \cdot x.$$

```{code-cell}
from sklearn.linear_model import LinearRegression

# Adaption der Daten
X = daten[['Geschwindigkeit [km/h]']]
y = daten['Bremsweg [m]']

# Training des Modells
model = LinearRegression()
model.fit(X, y)

# Bewertung
r2_score = model.score(X, y)
print(f'R2-score Trainingsdaten: {r2_score}')
```

Der R2-Score sieht sehr gut aus. Um uns einen Eindruck zu verschaffen, wie gut
das lineare Modell tatsächlich ist (wir wissen ja, dass es eigentlich
quadratisch ist!), erzeugen wir nun systematisch Geschwindigkeiten in dem
Bereich von 30 km/h und 150 km/h und verwenden die Faustformel für die
Berechnung der Bremswege.

```{code-cell}
v_test = np.linspace(v_min, v_max, 200)
s_test = 1/100 * v_test**2
testdaten = pd.DataFrame({
    'Geschwindigkeit [km/h]': v_test,
    'Bremsweg [m]': s_test
    })
```

Mit Hilfe des linearen Regressionsmodells prognostizieren wir die Bremswege für
diese Geschwindigkeiten und lassen den R2-Score berechnen.

```{code-cell}
# Prognose 
X_test = testdaten[['Geschwindigkeit [km/h]']]
y_test = testdaten['Bremsweg [m]']
y_prognose = model.predict(X_test)

# Bewertung
r2_score = model.score(X_test, y_test)
print(f'R2-score Testdaten: {r2_score}')
```

Zuletzt visualisieren wir die Prognose.

```{code-cell}
fig = px.scatter(daten, x = 'Geschwindigkeit [km/h]', y = 'Bremsweg [m]',
    title='Bremsweg eines Autos: lineares Modell')
fig.add_scatter(x = testdaten['Geschwindigkeit [km/h]'], y = y_prognose, mode='lines', name='Prognose')
fig.add_scatter(x = testdaten['Geschwindigkeit [km/h]'], y = y_test, mode='lines', name='Faustformel')
fig.show()
```

Vor allem die Visualisierung zeigt die Schwächen des linearen Modells. Bei
niedrigen Geschwindigkeiten wie in der Stadt unterschätzt das lineare Modell den
Bremsweg. Unterhalb von 40 km/h prognostiziert das Modell sogar einen negativen
Bremsweg. Zwischen 60 km/h und 120 km/h überschätzt das Modell den Bremsweg und
oberhalb von 120 km/h unterschätzt es den Bremsweg wieder. Das Modell ist zu
einfach für die Prognose, es liegt **Underfitting** vor. Daher probieren wir
als nächstes ein quadratisches Regressionsmodell aus.

## Quadratische Regression

Wenn Sie in der Dokumentation von Scikit-Learn nun nach einer Funktion zur
quadratischen Regression suchen, werden Sie nicht fündig werden. Tatsächlich
brauchen wir auch keine eigenständige Funktion, sondern können uns mit einem
Trick weiterhelfen.

Das lineare Regressionsmodell, das wir eben ausprobiert haben, lautet
mathematisch formuliert folgendermaßen:

$$y = \omega_0 + \omega_1 \cdot x$$

mit nur einem Merkmal $x$, nämlich der Geschwindigkeit.

Wenn wir eine quadratische Funktion als Modellfunktion wählen möchten, erzeugen
wir einfach ein zweites Merkmal. Wir nennen die bisherigen x-Werte $x$
jetzt $x_1$ und fügen als zweites Merkmal die neue Eigenschaft

$$x_2 = \left( x_1 \right)^2$$

hinzu. Damit wird aus dem quadratischen Regressionsmodell

$$y = w_0 + w_1 \cdot x + w_2 \cdot x^2$$

das *multiple* lineare Regressionsmodell

$$y = w_0 + w_1 \cdot x_1 + w_2 \cdot x_2.$$

Scikit-Learn stellt auch hier passende Methoden bereit. Aus dem
Vorbereitungsmodul `sklearn.preprocessing` importieren wir `PolynomialFeatures`.
Mehr Details dazu finden Sie in der [Dokumentation Scikit-Learn →
PolynomialFeature](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PolynomialFeatures.html).
Wir erzeugen das PolynomialFeature-Objekt mit der Option `degree=2`, um die
Quadrate hinzuzufügen. Dann transformieren wir die Input-Daten, indem wir die
`fit_transform()`-Methode auf den Input anwenden.

```{code-cell}
from sklearn.preprocessing import PolynomialFeatures

# Adaption der Daten
polynom_transformator = PolynomialFeatures(degree = 2)
X = polynom_transformator.fit_transform(daten[['Geschwindigkeit [km/h]']])
y = daten['Bremsweg [m]']
```

Danach können wir das multiple lineare Regressionsmodell trainieren und bewerten
lassen.

```{code-cell}
# Training des Modells
model = LinearRegression()
model.fit(X, y)

# Bewertung
r2_score = model.score(X, y)
print(f'R2-score Trainingsdaten: {r2_score}')
```

Zuletzt lassen wir das quadratische Regressionsmodell noch visualiseren. Wichtig
ist, dass nun auch die Testdaten quadriert werden müssen, da das ML-Modell für
Prognosen voraussetzt, dass die Daten in der gleichen Art und Weise vorliegen
wie die Trainingsdaten. Wir müssen denselben  Transformator nehmen wie zum
Training der Daten und neutzen daher nur die `transform()`-Methode.

```{code-cell}
# Prognose 
X_test = polynom_transformator.transform(testdaten[['Geschwindigkeit [km/h]']])
y_prognose = model.predict(X_test)
   
fig = px.scatter(daten, x = 'Geschwindigkeit [km/h]', y = 'Bremsweg [m]',
    title='Bremsweg eines Autos: quadratisches Modell')
fig.add_scatter(x = testdaten['Geschwindigkeit [km/h]'], y = y_prognose, mode='lines', name='Prognose')
fig.add_scatter(x = testdaten['Geschwindigkeit [km/h]'], y = y_test, mode='lines', name='Faustformel')
fig.show()
```

Die Prognose ist so gut, dass wir die Prognose (rot) und die Faustformel (grün)
kaum unterscheiden können. Kleinere Abweichungen gibt es bei den Bremswegen für
Geschwindigkeiten oberhalb von 130 km/h. Zoomen Sie in den Plot hinein, um sich
die Unterschiede anzusehen.

**Bemerkung:** Dieser Trick wird auch bei anderen ML-Verfahren angewandt. Aus
einem Merkmal, aus einer Eigenschaft werden jetzt eine neue Eigenschaften
erzeugt. Aus einem eindimensionalen Input wird ein zweidimensionaler Input.
Mathematisch gesehen haben wir die Input-Daten in einen höherdimensionalen
Bereich projiziert. Diese Methode nennt man **Kernel-Trick**. Es ist auch
möglich, andere Funktionen zu benutzen, um die Daten in einen höherdimensionalen
Raum zu projizieren, z.B. radiale Gaußsche Basisfunktionen. Das nennt man dann
**Kernel-Methoden**. In dieser Vorlesung bleiben wir aber bei den Polynomen als
Basisfunktion.

## Polynomiale Regression

Mit diesem Trick, die Merkmale zu quadrieren, können wir weitermachen, z.B. die
Merkmale mit 3 potenzieren. Letztendlich können wir so jedes gewünschte Polynom
als Regressionspolynom trainieren lassen. Das ein höheres Polynom nicht
unbedingt besser sein muss, zeigt das folgende Beispiel. Wir wählen als
Polynomgrad 14.

```{code-cell}
# Adaption der Daten
polynom_transformator = PolynomialFeatures(degree = 14)
X = polynom_transformator.fit_transform(daten[['Geschwindigkeit [km/h]']])
y = daten['Bremsweg [m]']

# Training des Modells
model = LinearRegression()
model.fit(X, y)

# Bewertung
r2_score = model.score(X, y)
print(f'R2-score Trainingsdaten: {r2_score}')

# Prognose
X_test = polynom_transformator.transform(testdaten[['Geschwindigkeit [km/h]']])
y_prognose = model.predict(X_test)

fig = px.scatter(daten, x = 'Geschwindigkeit [km/h]', y = 'Bremsweg [m]',
    title='Bremsweg eines Autos: Polynom 14. Grades')
fig.add_scatter(x = testdaten['Geschwindigkeit [km/h]'], y = y_prognose, mode='lines', name='Prognose')
fig.add_scatter(x = testdaten['Geschwindigkeit [km/h]'], y = y_test, mode='lines', name='Faustformel')
fig.show()
```

Nach 150 km/h wird der Brewmsweg wieder weniger, was natürlich nicht mit der
Praxis übereinstimmt. Die Visualisierung der Prognose zeigt, dass das ein
polynomiales Regressionsmodell mit Grad 14 zu sehr an die Trainingsdaten
angepasst ist und für neue Daten (siehe Geschwindigkeiten größer 150 km/h) nicht
gut geeignet ist. Es liegt **Overfitting** vor.

Bei der polynomialen Regression wird der Polynomgrad zu einem
**Hyperparameter**. Hyperparameter haben wir auch schon bei den
Entscheidungsbäumen (Decision Trees) kennengelernt. Zur Wiederholung geben wir
hier erneut die Definition an.

```{admonition} Was ist ... ein Hyperparameter?
:class: note
Ein Hyperparameter ist ein Parameter, der vor dem Training eines Modells
festgelegt wird und nicht aus den Daten während des Trainings gelernt wird. Die
Hyperparameter steuern den gesamten Lernprozess und haben einen wesentlichen
Einfluss auf die Leistung des Modells.
```

## Zusammenfassung und Ausblick

In diesem Kapitel haben wir die polynomiale Regression mit Scikit-Learn
kennengelernt. Auch bei der polynomialen Regression ist die Wahl des
Hyperparameters Polynomgrad wichtig. Im nächsten Kapitel werden wir uns ansehen.
wie Hyperparameter getunt werden können.
