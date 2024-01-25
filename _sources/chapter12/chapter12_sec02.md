---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.7
kernelspec:
  display_name: python39
  language: python
  name: python3
---

# 12.2 Neuronale Netze mit Scikit-Learn

```{admonition} Lernziele
:class: important
* Sie können mit Scikit-Learn ein neuronales Netz zur Klassifikation trainieren.
```

+++

## Neuronale Netze zur Klassifikation

Schauen wir uns an, wie das Training eines tiefen neuronalen Netzes in
Scikit-Learn funktioniert. Dazu benutzen wir aus dem Untermodul
``sklearn.neural_network`` den ``MLPClassifier``, also ein
Multi-Layer-Perzeptron für Klassifikationsaufgaben:

> https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html#sklearn.neural_network.MLPClassifier

Wir benutzen künstliche Daten, um die Anwendung des MLPClassifiers zu
demonstrieren.

```{code-cell} ipython3
import pandas as pd
import plotly.express as px
from sklearn.datasets import make_circles


# Generiere künstliche Daten
X, y = make_circles(noise=0.2, factor=0.5, random_state=1)

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

```{code-cell} ipython3
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split

# Auswahl des Models
# solver = 'lbfgs' für kleine Datenmengen, solver = 'adam' für große Datenmengen, eher ab 10000
# alpha = Lernrate
# hidden_layer: Anzahl der Neuronen pro verdeckte Schicht und Anzahl der verdeckten Schichten
model = MLPClassifier(solver='lbfgs', alpha=0.1, hidden_layer_sizes=[5, 5])

# Split Trainings- / Testdaten
X_train, X_test, y_train, y_test = train_test_split(X,y, random_state=0)

# Training
model.fit(X_train, y_train)

# Validierung 
score_train = model.score(X_train, y_train)
score_test = model.score(X_test, y_test)
print(f'Score für Trainingsdaten: {score_train:.2f}')
print(f'Score für Testdaten: {score_test:.2f}')
```

Funktioniert gar nicht mal schlecht :-) Um die Warnung kümmern wir uns später.
Wir zeichen die Entscheidungsgrenzen ein, um zu sehen, wo das neuronale Netz
die Trennlinien zieht.

```{code-cell} ipython3
import plotly.graph_objects as go
import numpy as np
import pandas as pd
from sklearn.datasets import make_circles

# Generate synthetic data
X, y = make_circles(noise=0.2, factor=0.5, random_state=1)

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

Im Folgenden wollen wir uns ansehen, welche Bedeutung die optionalen Parameter
haben. Dazu zunächst noch einmal der komplette Code, aber ohne einen Split in
Trainings- und Testdaten. Probieren Sie nun unterschiedliche Werte für die
Lernrate 'alpha' und die Architektur der verdeckten Schicht 'hidden_layer_sizes'
aus.


```{code-cell} ipython3
# setze verschiedene Werte für alpha und Architektur der verdeckten Schicht
my_alpha = 0.1
my_hidden_layers = [10,10]

# erzeuge künstliche Daten
X,y = make_circles(noise=0.2, factor=0.5, random_state=1)

# Auswahl des Model
model = MLPClassifier(solver='lbfgs', alpha=my_alpha, hidden_layer_sizes=my_hidden_layers)

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

Wie Sie sehen, ist es schwierig, ein gutes Verhältnis von Lernrate $\alpha$ und
der Architektur des neuronalen Netzes (= Anzahl der Neuronen pro verdeckter
Schicht und Anzahl verdeckter Schichten) zu finden. Auch fällt das Ergebnis
jedesmal ein wenig anders aus, weil stochastische Verfahren im Hintergrund für
das Trainieren der Gewichte benutzt werden. Aus diesem Grund sollten neuronale
Netze nur eingesetzt werden, wenn sehr große Datenmengen vorliegen und dann noch
ist das Finden der besten Architektur eine große Herausforderung.
