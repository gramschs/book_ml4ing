---
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# 12.3 Neuronale Netze mit Scikit-Learn

```{admonition} Lernziele
:class: attention
* Sie können mit Scikit-Learn ein neuronales Netz zur Klassifikation trainieren.
```

+++

## Neuronale Netze zur Klassifikation

Schauen wir uns an, wie das Training eines neuronalen Netzes in Scikit-Learn
funktioniert. Dazu erzeugen wir zunächst künstliche Daten für eine binäre
Klassifikationsaufgabe, splitten sie in Trainings- und Testdaten und lassen sie
visualisieren.

```{code-cell} ipython3
import pandas as pd
import plotly.express as px
from sklearn.datasets import make_circles
from sklearn.model_selection import train_test_split

# Generiere künstliche Daten
X, y = make_circles(noise=0.2, factor=0.5, random_state=1)

# Split Trainings- / Testdaten
X_train, X_test, y_train, y_test = train_test_split(X,y, random_state=0)

# Konvertierung in ein DataFrame-Objekt für Plotly Express
df = pd.DataFrame({
    'Feature 1': X[:, 0],
    'Feature 2': X[:, 1],
    'Category': pd.Series(y, dtype='category')
})

# Visualisierung
fig = px.scatter(df, x='Feature 1', y='Feature 2', color='Category',
                 title='Künstliche Daten')
fig.show()
```

Die neuronalen Netze sind in dem Untermodul `sklearn.neural_network`. Da es sich
um eine Klassifikationsaufgabe handelt, laden wir das Multilayer-Perzeptron mit
`MLPClassifier`. Wir lassen das neuronale Netz mit `.fit()` trainieren und geben
die Scores für die Trainings- und Testdaten mit `.score()` aus.

```{code-cell} ipython3
from sklearn.neural_network import MLPClassifier

# Auswahl des Modells
neuronales_netz = MLPClassifier()

# Training
neuronales_netz .fit(X_train, y_train)

# Validierung 
score_train = neuronales_netz.score(X_train, y_train)
score_test = neuronales_netz.score(X_test, y_test)
print(f'Score für Trainingsdaten: {score_train:.2f}')
print(f'Score für Testdaten: {score_test:.2f}')
```

Beim Training des neuronalen Netzes erscheint die Warnung: `Stochastic
Optimizer: Maximum iterations (200) reached and the optimization hasn't
converged yet.`. Zum Bestimmen der Gewichte des neuronalen Netzes wird ein
iteratives Verfahren verwendet, das Schritt für Schritt die optimalen Gewichte
berechnet. Iterative Verfahren können in eine Endlichschleife geraten. Um das zu
verhindern, wird in der Regel die Anzahl der Schritte (Iterationen) begrenzt.
Die Warnung besagt, dass in unserem Beispiel die Suche nach den optimalen
Gewichten des neuronalen Netzes nach der fest eingestellten Anzahl von 200
Schritten eingestellt wurde. Wir erhöhen diese Zahl auf 2000 mit dem optionalen
Argument `max_iter=2000` und wiederholen das Training.

```{code-cell} ipython3
# Auswahl des Modells mit maximal 2000 Iterationen
neuronales_netz = MLPClassifier(max_iter=2000)

# Training
neuronales_netz .fit(X_train, y_train)

# Validierung 
score_train = neuronales_netz.score(X_train, y_train)
score_test = neuronales_netz.score(X_test, y_test)
print(f'Score für Trainingsdaten: {score_train:.2f}')
print(f'Score für Testdaten: {score_test:.2f}')
```

Hinweis: Oft ist das Skalieren der Daten besser als das Erhöhen der maximalen
Anzahl an Iterationen. Im Maschinenbau messen wir oft Größen mit sehr
unterschiedlichen Einheiten: Temperaturen (20-100°C), Drücke (1-200 bar) oder
Drehzahlen (0-3000 rpm). Liegen Werte in recht unterschiedlichen Größenordnungen
vor, so erschwert das das Training. Daher ist es sinnvoll, die Daten auf
ähnliche Bereich zu skalieren.

```{code-cell} ipython3
from sklearn.preprocessing import StandardScaler

# Daten skalieren
scaler = StandardScaler()
X_scaled_train = scaler.fit_transform(X_train)

# Training
neuronales_netz.fit(X_scaled_train, y_train)

# Validierung 
score_train = neuronales_netz.score(X_train, y_train)
score_test = neuronales_netz.score(X_test, y_test)
print(f'Score für Trainingsdaten: {score_train:.2f}')
print(f'Score für Testdaten: {score_test:.2f}')
```

Die Scores für die Trainings- und Testdaten sind zwar sehr gut, aber wir
erhalten auch eine Warnung . Neuronale Netze können zwar
komplexe Strukturen in den Daten sehr gut abbilden, brauchen aber auch viele
Datenpunkte, damit beim Training kein Overfitting auftritt. Diese Warnung ist
ein Zeichen dafür, dass etwas nicht stimmt. Mit wie vielen Neuronen (und damit
Gewichten) arbeitet das aktuelle neuronale Netz eigentlich?

Wir konsultieren die Dokumentation

> [https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html#sklearn.neural_network.MLPClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html#sklearn.neural_network.MLPClassifier)

Die Voreinstellung für die Anzahl der versteckten Schichten ist
`hidden_layer_sizes=(100,)`. Dem optionalen Argument `hidden_layer_sizes` wird
ein Tupel mit ganzen Zahlen übergeben, wobei hier das Tupel nur eine Zahl
enthält, nämlich 100. Das bedeutet, dass das neuronale Netz eine versteckte
Schicht hat und diese aus 100 Neuronen besteht. Besteht das Tupel aus mehreren
Zahlen, z.B. `(50, 20, 40)`, dann gibt die die erste Zahl in dem Tupel die
Anzahl der Neuronen in der ersten versteckten Schicht an (also 50), die zweite
Zahl die Anzahl der Neuronen in der zweiten Schicht (also 20) und immer so
weiter.

Jetzt wo wir wissen, dass das neuronale Netz eine versteckte Schicht mit 100
Neuronen hat, können wir uns überlegen, wie viele Gewichte gebraucht werden. Bei
zwei Merkmalen, einer versteckten Schicht mit 100 Neuronen und einer Ausgabe
brauchen wir 2 x 100 + 1 + 1 = 202 Gewichte. Gleichzeitig haben wir nur 100
Datenpunkte, also nur halb so viele Informationen wie Gewichte. Das reicht
nicht, um Overfitting zu vermeiden, daher die Konvergenzwarnung. Wir reduzieren
nun die Anzahl der Neuronen in der versteckten Zwischenschicht auf 10.

```{code-cell} ipython3
# Auswahl des Modells
neuronales_netz = MLPClassifier(hidden_layer_sizes=(5,5))

# Training
neuronales_netz .fit(X_train, y_train)

# Validierung 
score_train = neuronales_netz .score(X_train, y_train)
score_test = neuronales_netz .score(X_test, y_test)
print(f'Score für Trainingsdaten: {score_train:.2f}')
print(f'Score für Testdaten: {score_test:.2f}')
```

Funktioniert gar nicht mal schlecht :-) Wir zeichnen die Entscheidungsgrenzen
ein, um zu sehen, wo das neuronale Netz die Trennlinien zieht.

```{code-cell} ipython3
:tags: ["hide-input"]
import plotly.graph_objects as go
import numpy as np
import pandas as pd
from sklearn.datasets import make_circles

# Generate synthetic data
X, y = make_circles(noise=0.2, factor=0.5, random_state=1)

# Create grid for contour plot
gridX, gridY = np.meshgrid(np.linspace(-1.5, 1.5, 50), np.linspace(-1.5, 1.5, 50))
gridZ = neuronales_netz .predict_proba(np.column_stack([gridX.ravel(), gridY.ravel()]))[:, 1]
Z = gridZ.reshape(gridX.shape)

# Create scatter plot
scatter = go.Scatter(x=df['Feature 1'], y=df['Feature 2'], mode='markers',
                     marker=dict(color=df['Category'], colorscale='BlueRed_r'))

# Create contour plot
contour = go.Contour(x=np.linspace(-1.5, 1.5, 50), y=np.linspace(-1.5, 1.5, 50), z=Z, 
                     opacity=0.2, colorscale='BlueRed_r')

# Create figure and add plots
fig = go.Figure()
fig.add_trace(contour)
fig.add_trace(scatter)
fig.update_layout(title='Künstliche Messdaten und Konturen des Modells',
                  xaxis_title='Feature 1',
                  yaxis_title='Feature 2')
fig.show()
```

Im Folgenden wollen wir uns ansehen, welche Bedeutung die optionalen Parameter
haben. Dazu zunächst noch einmal der komplette Code, aber ohne einen Split in
Trainings- und Testdaten. Probieren Sie nun unterschiedliche Werte für die
Architektur der versteckten Schicht 'hidden_layer_sizes' aus.

```{code-cell} ipython3
# setze verschiedene Werte für die Architektur der versteckten Schicht
my_hidden_layers = [10,10]

# erzeuge künstliche Daten
X,y = make_circles(noise=0.2, factor=0.5, random_state=1)

# Auswahl des Model
model = MLPClassifier(solver='lbfgs', hidden_layer_sizes=my_hidden_layers)

# Training und Validierung
model.fit(X, y)
print('Score: {:.2f}'.format(model.score(X, y)))

# Visualisierung
# Create grid for contour plot
gridX, gridY = np.meshgrid(np.linspace(-1.5, 1.5, 50), np.linspace(-1.5, 1.5, 50))
gridZ = model.predict_proba(np.column_stack([gridX.ravel(), gridY.ravel()]))[:, 1]
Z = gridZ.reshape(gridX.shape)

# Create scatter plot
scatter = go.Scatter(x=df['Feature 1'], y=df['Feature 2'], mode='markers',
                     marker=dict(color=df['Category'], colorscale='BlueRed_r'))

# Create contour plot
contour = go.Contour(x=np.linspace(-1.5, 1.5, 50), y=np.linspace(-1.5, 1.5, 50), z=Z, 
                     opacity=0.2, colorscale='BlueRed_r')

# Create figure and add plots
fig = go.Figure()
fig.add_trace(contour)
fig.add_trace(scatter)
fig.update_layout(title='Künstliche Messdaten und Konturen des Modells',
                  xaxis_title='Feature 1',
                  yaxis_title='Feature 2')
fig.show()
```

Wie Sie sehen, ist es schwierig, eine gute Architektur des neuronalen Netzes (=
Anzahl der Neuronen pro versteckter Schicht und Anzahl versteckter Schichten) zu
finden. Auch fällt das Ergebnis jedesmal ein wenig anders aus, weil
stochastische Verfahren im Hintergrund für das Trainieren der Gewichte benutzt
werden. Aus diesem Grund sollten neuronale Netze nur eingesetzt werden, wenn
sehr große Datenmengen vorliegen und dann noch ist das Finden der besten
Architektur eine große Herausforderung.

Bemerkung:

* solver = 'lbfgs' für kleine Datenmengen, solver = 'adam' für große Datenmengen, eher ab 10000
* hidden_layer: Anzahl der Neuronen pro versteckte Schicht und Anzahl der versteckten Schichten