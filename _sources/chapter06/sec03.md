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

# Polynomiale Regression


## Lernziele

```{admonition} Lernziele
:class: hint
* TODO
```

## Polynomiale Regression

Wenn wir uns das folgende Beispiel betrachten, werden wir feststellen, dass die
lineare Regression die Messdaten nicht besonders gut annähert. 

```{code-cell} ipython3
import numpy as np
from numpy.random import default_rng

def erzeuge_kuenstliche_messdaten(koeffizienten, anzahl_daten=50):
    zufallszahlen_generator = default_rng(seed=42)
    xmin = - 5.0
    xmax = + 5.0
    x = zufallszahlen_generator.uniform(xmin, xmax, anzahl_daten)

    error = 3.0 * zufallszahlen_generator.standard_normal(anzahl_daten)
    y = error
    
    for i in range(len(koeffizienten)):
        y += koeffizienten[i] * x**i
    return x.reshape(-1,1), y.reshape(-1,1)
```

```{code-cell} ipython3
# erzeuge künstliche Daten
X,y = erzeuge_kuenstliche_messdaten([-3, 7, 2, -2], 30)

# Split in Trainings- und Testdaten
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y)

# Auswahl des Modells 
from sklearn.linear_model import LinearRegression
model = LinearRegression()

# Training 
model.fit(X_train, y_train)
print('k0 = {}'.format(model.intercept_))
print('k1 = {}'.format(model.coef_))

# Validierung
from sklearn.metrics import r2_score
r2_train = r2_score(y_train, model.predict(X_train))
r2_test  = r2_score(y_test,  model.predict(X_test))
print('R2-Score der Trainingsdaten: {:.4}'.format(r2_train))
print('R2-Score der Testdaten: {:.4}'.format(r2_test))

# Visualisierung
X_vis = np.linspace(-5,5,100).reshape(-1,1)
y_vis = model.predict(X_vis)

import matplotlib.pylab as plt
fig, ax = plt.subplots(figsize=(12,9))
ax.scatter(X_train, y_train, label='train')
ax.scatter(X_test, y_test, label='test')
ax.plot(X_vis, y_vis, '--k')
ax.legend();
```

Der R2-Score ist sowohl bei den Trainingsdaten (0.7) als auch bei den Testdaten
(0.6) nicht gut. Ein Regressionspolynom 2. oder 3. Grades könnte vielleicht
besser passen. Wählen wir beispielsweise ein Polynom 3. Grades, so lautet das
polynomiale Regressionsproblem wie folgt: Bestimme die Polynomkoeffizienten
$k_0, k_1, k_2$ und $k_3$ so, dass $$y_i = k_0 + k_1\cdot x_i + k_2\cdot x_i^2 +
k_3 \cdot x_i^3 + \varepsilon_i.$$ Wenn Sie in der Dokumentation von
Scikit-Learn nun nach einer Funktion zur polynomialen Regression suchen, werden
Sie nicht fündig werden. Tatsächlich brauchen wir auch keine eigenständige
Funktion, sondern können uns mit einem Trick weiterhelfen. Wir erzeugen einfach
eine zweite Spalte mit $x_i^2$ und eine dritte Spalte mit $x_i^3$ in den $N$
Zeilen von $i=1, \ldots, N$. 

Dieser Trick wird auch bei anderen ML-Verfahren angewandt. Aus einem Input, aus
einer Eigenschaft werden jetzt drei neue Eigenschaften gemacht. Aus einem
eindimensionalen Input wird ein dreidimensionaler Input. Mathematisch gesehen
haben wir die Input-Daten in einen höherdimensionalen Bereich projiziert. Diese
Methode nennt man **Kernel-Trick**. Es ist auch möglich, andere Funktionen zu
benutzen, um die Daten in einen höherdimensionalen Raum zu projizieren, z.B.
radiale Gaußsche Basisfunktionen. Das nennt man dann **Kernel-Methoden**.  

In dieser Vorlesung bleiben wir aber bei den Polynomen als Basisfunktion.
Scikit-Learn stellt auch hier passende Methoden bereit.

```{code-cell} ipython3
from sklearn.preprocessing import PolynomialFeatures

# erzeuge eine Matrix mit den Zahlen 1 bis 10 in der 1. Spalte
X = np.arange(1,11).reshape(-1,1)
print('Original X:\n', X)

# lade die Polynom-Transformator 
polynom_transformator = PolynomialFeatures(degree = 3)

# transformiere X
X_transformiert =  polynom_transformator.fit_transform(X)
print('transformiertes X:\n', X_transformiert)
```

Damit können wir nun verschiedene Regressionspolynome ausprobieren:

```{code-cell} ipython3
# erzeuge künstliche Daten
X,y = erzeuge_kuenstliche_messdaten([-3, 7, 2, -2], 30)

# setze Polynomgrad
grad = 3
print('\nGrad: {}'.format(grad))

# Kernel-Trick, Split in Trainings- und Testdaten
polynom_transformator = PolynomialFeatures(degree = grad)
X = polynom_transformator.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X,y)

# Auswahl des Modells 
model = LinearRegression()

# Training 
model.fit(X_train, y_train)
#print('k0 = {}'.format(model.intercept_))
#print('k1 = {}'.format(model.coef_))

# Validierung
r2_train = r2_score(y_train, model.predict(X_train))
r2_test  = r2_score(y_test,  model.predict(X_test))
print('R2-Score der Trainingsdaten: {:.4}'.format(r2_train))
print('R2-Score der Testdaten: {:.4}'.format(r2_test))

# Visualisierung
X_vis = polynom_transformator.fit_transform( np.linspace(-5,5,100).reshape(-1,1) )
y_vis = model.predict(X_vis)

fig, ax = plt.subplots(figsize=(12,9))
ax.scatter(X_train[:,1], y_train, label='train')
ax.scatter(X_test[:,1],   y_test, label='test')
ax.plot(X_vis[:,1], y_vis, '--k')
ax.legend();
```

Das Transformieren der Daten in eine höhere Dimension machen den Code schwerer
lesbar. Deswegen definieren wir nun hiier eine Funktion, die erst transformiert
und dann das lineare Regressionsmodell anwendet. Der Grad des Polynoms wird
dabei als Argument übergeben. Damit diese Funktion Transformation und lineare
Regression hintereinander automatisch ausführen kann, benötigen wir von
Scikit-Learn die sogenannte Pipieline:

```{code-cell} ipython3
from sklearn.pipeline import make_pipeline
def PolynomialRegression(degree=2, **kwargs):
    return make_pipeline(PolynomialFeatures(degree), LinearRegression(**kwargs))
```

Damit kann der obige Code etwas kürzer geschrieben werden.

```{code-cell} ipython3
# erzeuge künstliche Daten
X,y = erzeuge_kuenstliche_messdaten([-3, 7, 2, -2], 30)

# setze Polynomgrad
grad = 3
print('\nGrad: {}'.format(grad))

# Split in Trainings- und Testdaten
X_train, X_test, y_train, y_test = train_test_split(X,y)

# Auswahl des Modells 
model = PolynomialRegression(degree = 3)

# Training 
model.fit(X_train, y_train)
#print('k0 = {}'.format(model.intercept_))
#print('k1 = {}'.format(model.coef_))

# Validierung
r2_train = r2_score(y_train, model.predict(X_train))
r2_test  = r2_score(y_test,  model.predict(X_test))
print('R2-Score der Trainingsdaten: {:.4}'.format(r2_train))
print('R2-Score der Testdaten: {:.4}'.format(r2_test))

# Visualisierung
X_vis = np.linspace(-5,5,100).reshape(-1,1) 
y_vis = model.predict(X_vis)

fig, ax = plt.subplots(figsize=(12,9))
ax.scatter(X_train, y_train, label='train')
ax.scatter(X_test, y_test, label='test')
ax.plot(X_vis, y_vis, '--k')
ax.legend();
```

Als nächstes beschäftigen wir uns erneut mit der Frage, welches Modell am besten
zu unseren Daten passt und ob Underfitting oder Overfitting vorliegt. Dazu
kopieren wir den Code aus der obigen Code-Zelle und oacken ihn in eine
for-Schleife:

```{code-cell} ipython3
# erzeuge künstliche Daten
X,y = erzeuge_kuenstliche_messdaten([-3, 7, 2, -2], 30)

# Split in Trainings- und Testdaten
X_train, X_test, y_train, y_test = train_test_split(X,y)

# FOR-Schleife
for grad in range(1,15):
    print('\nGrad: {}'.format(grad))


    # Auswahl des Modells 
    model = PolynomialRegression(degree = grad)

    # Training 
    model.fit(X_train, y_train)
    #print('k0 = {}'.format(model.intercept_))
    #print('k1 = {}'.format(model.coef_))

    # Validierung
    r2_train = r2_score(y_train, model.predict(X_train))
    r2_test  = r2_score(y_test,  model.predict(X_test))
    print('R2-Score der Trainingsdaten: {:.4}'.format(r2_train))
    print('R2-Score der Testdaten: {:.4}'.format(r2_test))

    # Visualisierung
    X_vis = np.linspace(-5,5,100).reshape(-1,1) 
    y_vis = model.predict(X_vis)

    fig, ax = plt.subplots(figsize=(12,9))
    ax.scatter(X_train, y_train, label='train')
    ax.scatter(X_test, y_test, label='test')
    ax.plot(X_vis, y_vis, '--k')
    ax.set_title('Grad: {}'.format(grad))
    ax.legend();
```

Am besten notieren wir die verschiedenen R2-Scores mit, um zu entscheiden, ob
Underfitting oder Overfitting vorliegt.

```{code-cell} ipython3
# erzeuge künstliche Daten
X,y = erzeuge_kuenstliche_messdaten([-3, 7, 2, -2], 30)

# Split in Trainings- und Testdaten
X_train, X_test, y_train, y_test = train_test_split(X,y)

r2_train_liste = []
r2_test_liste = []

# FOR-Schleife
for grad in range(1,15):
    # Auswahl des Modells 
    model = PolynomialRegression(degree = grad)

    # Training 
    model.fit(X_train, y_train)
   
    # Validierung
    r2_train = r2_score(y_train, model.predict(X_train))
    r2_test  = r2_score(y_test,  model.predict(X_test))
   
    r2_train_liste.append(r2_train)
    r2_test_liste.append(r2_test)

print(r2_train_liste)
print(r2_test_liste)
```

Ein Plot der R2-Scores hilft bei der Einschätzung Over-/Underfitting:

```{code-cell} ipython3
fig, ax = plt.subplots()
ax.plot(range(1,15), r2_train_liste, label='train')
ax.plot(range(1,15), r2_test_liste, label='test')
```

Offensichtlich sind wir nach Grad 12 so schlecht, dass wir besser uns nur den
Anfang angucken:

```{code-cell} ipython3
fig, ax = plt.subplots(figsize=(12,8))
ax.plot(range(1,12), r2_train_liste[0:11], label='train')
ax.plot(range(1,12), r2_test_liste[0:11], label='test')
ax.legend();
```

Zwischen Grad 3 und Grad 8 ist der R2-Score für die Trainingsdaten praktisch
gleich dem R2-Score der Testdaten. Diese Modelle können also gewählt werden. Für
Grad 1 und 2 ist der R2-Score sowohl für Trainings- als auch Testdaten schlecht,
es liegt Underfitting vor. Ab Grad 9 ist der R2-Score für die Trainingsdaten
super, aber er fällt für die Testdaten ab. Wir sind im Bereich des Overfittings.

Fazit: es kommen die polynomialen Regressionsmodelle für Grad 3 bis 8 infrage.
Wenn man die Wahl hat, wählt man das einfachste Modell, also hier das mit Grad
3.