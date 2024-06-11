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

# 9.2 Random Forests

```{admonition} Warnung
:class: warning
Dieser Abschnitt wird gerade überarbeitet.
```

```{admonition} Lernziele
:class: goals
* Sie können das ML-Modell **Random Forest** in der Praxis anwenden.
```


## Random Forests mit Scikit-Learn

Entscheidungsbäume sind aufgrund ihrer Einfachheit und vor allem aufgrund ihrer
Interpretierbarkeit sehr beliebt. Allerdings ist ihre Tendenz zum Overfitting
problematisch. Die Idee des ML-Verfahrens Random Forests ist es, viele
Entscheidungsbäume zu erstellen und sie beispielsweise durch Mittelwertbildung
zusammenzufassen oder die Mehrheit entscheiden zu lassen. Wenn sich ein
einzelner Entscheidungsbaum zu sehr an die Trainingsdaten angepasst haben
sollte, wird das sozusagen durch die Mittelwertbildung oder Mehrheisbildung mit
einem anderen Entscheidungsbaum, der mit anderen Trainingsdaten trainiert wurde,
wieder ausgeglichen. Dabei wird werden die Trainigsdaten für jeden
Entscheidungsbaum zufällig ausgewählt.

Für die nachfolgenden Erläuterungen generieren wir uns wieder einmal künstliche
Messdaten. Diesmal verwenden wir die Funktion `make_moons` von Scikit-Learn.

```{code-cell} ipython3
import plotly.express as px
from sklearn.datasets import make_moons

# generate artificial data
X, y = make_moons(n_samples=120, random_state=0, noise=0.3)

# plot artificial data
fig = px.scatter(x = X[:,0], y = X[:, 1], color=y,
        title='Künstliche Daten',
        labels = {'x': 'Feature 1', 'y': 'Feature 2'})
fig.show()
```

```{code-cell} ipython3
from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier()
model.fit(X,y);


from sklearn.tree import plot_tree 
plot_tree(model, filled=True);
```

Das Ergebnis ist ein Entscheidungsbaum mit vielen Entscheidungen. Wir erzeugen jetzt ein Gitter

```{code-cell} ipython3
x0_min = X[:,0].min()
x0_max = X[:,0].max()
x1_min = X[:,1].min()
x1_max = X[:,1].max()

import numpy as np
gitter_x1, gitter_x2 = np.meshgrid(np.linspace(x0_min, x0_max), np.linspace(x1_min, x1_max))
gitter_y = model.predict(np.stack([gitter_x1.ravel(),gitter_x2.ravel()]).T)

import plotly.graph_objects as go

fig = go.Figure()
fig.add_trace(go.Scatter(x = gitter_x1.ravel(), y = gitter_x2.ravel(), 
                         marker_color=gitter_y.ravel(), mode='markers', opacity=0.1, name='Gitter'))
fig.add_trace(go.Scatter(x = X[:,0], y = X[:,1], mode='markers', marker_color=y, name='Daten'))
fig.update_layout(
  title='Künstliche Messdaten',
  xaxis_title = 'Feature 1',
  yaxis_title = 'Feature 2'
)
```

Jetzt lassen wir einen Random Forest erzeugen. Weitere Details finden Sie unter
[Scikit-Learn Dokumentation →
RandomForestClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html).
Zunächst erfolgt der übliche Import. Bei der Instanziierung müssen wir jedoch
diesmal angeben, aus wie vielen Entscheidungsbäumen der Random Forest bestehen
zoll. Dazu nutzen wir das Argument `n_estimators=`. 

Wir wählen 4 Entscheidungsbäume. Die Auswahl der Daten für jeden
Entscheidungsbaum erfolgt zufällig. Damit aus didaktischen Gründen die
Ergebnisse produzierbar sind, fixieren wir den Seed für den
Zufallszahlengenerator.

```{code-cell} ipython3
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(n_estimators=4, random_state=0)
model.fit(X,y)
```

Die vier erzeugten Entscheidungsbäume sind in der Variable `model` gespeichert.

```{code-cell} ipython3
for (nummer, baum) in zip(range(4), model.estimators_):
    gitter_y = baum.predict(np.stack([gitter_x1.ravel(),gitter_x2.ravel()]).T)

    fig = go.Figure()
    fig.add_trace(go.Scatter(x = gitter_x1.ravel(), y = gitter_x2.ravel(), 
                            marker_color=gitter_y.ravel(), mode='markers', opacity=0.1, name='Gitter'))
    fig.add_trace(go.Scatter(x = X[:,0], y = X[:,1], mode='markers', marker_color=y, name='Daten'))
    fig.update_layout(
      title=f'Entscheidungsbaum {nummer+1}',
      xaxis_title = 'Feature 1',
      yaxis_title = 'Feature 2'
    )
    fig.show()
```

Insgesamt erhalten wir:

```{code-cell} ipython3
gitter_y = model.predict(np.stack([gitter_x1.ravel(),gitter_x2.ravel()]).T)

fig = go.Figure()
fig.add_trace(go.Scatter(x = gitter_x1.ravel(), y = gitter_x2.ravel(), 
                        marker_color=gitter_y.ravel(), mode='markers', opacity=0.1, name='Gitter'))
fig.add_trace(go.Scatter(x = X[:,0], y = X[:,1], mode='markers', marker_color=y, name='Daten'))
fig.update_layout(
  title='Random Forest',
  xaxis_title = 'Feature 1',
  yaxis_title = 'Feature 2'
  )
fig.show()
```

## Zusammenfassung und Ausblick

Random Forests sind einfachen Entscheidungsbäumen vorzuziehen, da sie das
Overfitting reduzieren. Die Erzeugung der einzelnen Entscheidungsbäume kann
parallelisiert werden, so dass das Training eines Random Forests sehr schnell
durchgeführt werden kann. Auch für große Datenmengen mit sehr unterschiedlichen
Eigenschaften arbeitet der Random Forest sehr effizient. Er ermöglicht auch eine
Interpreation, welche Eigenschaften ggf. einen größeren Einfluss haben als
andere Eigenschaften.
