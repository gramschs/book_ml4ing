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

# 7.2 Multiple lineare Regression

Bisher haben wir nur ein einzelnes Merkmal aus den gesammelten Daten
herausgegriffen und untersucht, ob es zwischen diesem Merkmal und der Zielgröße
einen linearen Zusammenhang gibt. So simpel ist die Welt normalerweise nicht,
oft wirken mehrere Einflussfaktoren gleichzeitig. Daher steht die **multiple
lineare Regression** in diesem Kapitel im Fokus.


## Lernziele

```{admonition} Lernziele
:class: goals
* Sie wissen, was eine **multiple lineare Regression** ist und können sie mit
  Scikit-Learn durchführen.
* Sie wissen, was **positive lineare Korrelation** und **negative lineare
  Korrelation** bedeuten.
* Sie können die lineare Korrelation der Merkmale miteinander mit Hilfe der
  **Korrelationsmatrix** beurteilen.
* Sie können die Korrelationsmatrix als **Heatmap** visualisieren.
```


## Zwei Merkmale: PS und Alter beinflussen Preis

Im vorherigen Kapitel haben wir den Einfluss des Merkmals `Leistung [PS]` auf
die Zielgröße `Preis [EUR]` betrachtet. Nun wollen wir noch das Merkmal `Alter`
gemessen in Jahren hinzunehmen. 0 Jahre meint dabei einen Neuwagen. Aus
didaktischen Gründen werden wir auch hier künstlich erzeugte Daten nutzen, um
die multiple lineare Regression zu erklären. Als erstes erzeugen wir die Daten,
diesmal direkt mit Hilfsmitteln des Moduls NumPy.

```{code-cell} ipython3
import numpy as np 
import pandas as pd 

np.random.seed(0)
anzahl_autos = 100

x = np.floor( np.random.uniform(0, 11, anzahl_autos) )
y = np.floor( np.random.uniform(50, 301, anzahl_autos) )
z = np.floor( -2000 * x + 200 * y + 500 * np.random.normal(0, 1, anzahl_autos) + 10000 )

daten = pd.DataFrame({
    'Alter': x,
    'Leistung [PS]': y,
    'Preis [EUR]': z
    })
```

Dann visualisieren wir die Daten.

```{code-cell} ipython3
import plotly.express as px

fig = px.scatter_3d(daten, x = 'Alter', y = 'Leistung [PS]', z = 'Preis [EUR]',
  title='Künstliche Verkaufspreise für Autos')
fig.show()
```

Mehr als zwei Merkmale und eine Zielgröße können wir nicht sinnvoll
visualisieren. Um insbesondere zu visualisieren, wie die Zielgröße von jedem
einzelnen Merkmal abhängt, verwenden wir die Scattermatrix. Das hilft uns auch
zu erkennen, ob vielleicht ein Merkmal von einem anderen Merkmal abhängt.

```{code-cell} ipython3
fig = px.scatter_matrix(daten,
    title='Künstliche Daten: Verkaufspreise Autos')
fig.show()
```

Wir betrachten die letzte Zeile, in der die Zielgröße auf der y-Achse
aufgetragen ist. In der ersten Spalte wird der Preis abhängig vom Alter
dargestellt. Je älter das Auto, desto geringer der Preis. In der zweiten Spalte
wird der Preis abhängig von der Leistung gezeigt. Je leistungsstärker ein Auto,
desto höher der Preis. Insbesondere vermittelt das Diagramm den Eindruck, dass
durch die Punktewolke sehr gut eine Regressionsgerade gelegt werden könnte, was
bei der Abhängigkeit Alter -- Preis eher fraglich ist.

Wir trainieren jetzt ein lineares Regressionsmodell

$$y = w_0 + w_1 \cdot x_1 + w_2 \cdot x_2.$$

Damit ist gemeint, dass wir die Gewichte $w_0, w_1$ und $w_2$ des Modells so
bestimmen wollen, dass der Preis $y$ möglichst gut durch die beiden Merkmale
Alter $x_1$ und Leistung $x_2$ prognostiziert wird.

In einem ersten Schritt laden wir das lineare Regressionsmodul.

```{code-cell} ipython3
from sklearn.linear_model import LinearRegression

modell = LinearRegression()
```

Dann adaptieren wir die Daten. 

```{code-cell} ipython3
# Adaption der Daten
X = daten[['Alter', 'Leistung [PS]']]
y = daten['Preis [EUR]']
```

Jetzt können wir das lineare Regressionsmodell von Scikit-Learn mit der
`.fit()`-Methode trainieren. Wir lassen auch gleich den R²-Score mit ausgeben.

```{code-cell} ipython3
# Training
modell.fit(X, y)

# Validierung
r2_score = modell.score(X, y)
print(f'Der R2-Score ist: {r2_score:.4f}')
```

Schauen wir uns doch einmal an, welche Koeffizienten von Scikit-Learn für unsere
mehrdimensionale lineare Modellfunktion gefunden wurden.

```{code-cell} ipython3
print(f'Achsenabschnitt w0: {modell.intercept_:.2f}')
print(f'Koeffizienten (Steigungen): {modell.coef_}')
```

Damit lautet unsere Modellfunktion abhängig von Alter und Leistung also

$$y = f(x_1, x_2) = 10168 -2025\cdot x_1 + 199\cdot x_2.$$


## Korrelationsmatrix

Das Prognoseergebnis des multiplen linearen Regressionsmodell ist für die
Trainingsdaten sehr gut. Beim Betrachten der Scattermatrix wirkt das Merkmal
Leistung mehr einen linearen Einfluss zu haben als das Alter. Als nächstes
wollen wir bewerten, wie viel mehr der lineare Einfluss jedes einzelnen Merkmals
auf die Zielgröße ist. Dazu betrachten wir die sogenannte
**Korrelationsmatrix**. Mit der Methode `corr()` können wir sie einfach
berechnen lassen:

```{code-cell} ipython3
daten.corr()
```

In der ersten Zeile 'Alter' wird die Stärke der Korrelation von der Ursache
Alter auf die Zielgrößen Alter, Leistung und Preis bewertet. Wenn eine Erhöhung
der Ursache zu einer Erhöhung der Wirkung führt, nennt man das **positiv
korreliert**. Der umgekehrte Fall ist, wenn eine Verminderung der Ursache zu
einer Erhöhung der Wirkung führt. Dann spricht man von **negativ korreliert**.
Die Zahl 1 drückt dabei aus, dass die beiden Merkmale perfekt linear positiv
korreliert sind. In der ersten Zeile und der ersten Zeile wird der Einfluss des
Alters auf die Zielgröße Alter bewertet. Dort muss eine 1 stehen, denn hier sind
ja Ursache und Wirkung identisch. In der ersten Zeile und der zweiten Spalte
wird die lineare Korrelation zwischen Alter und Leistung bewertet. Die Zahl
-0.074244 ist nahe bei 0 und bedeutet daher, dass es nur einen sehr, sehr
schwachen Zusammenhang zwischen Alter und Leistung gibt, wenn überhaupt. Unser
technisches Verständnis eines Autos bestätigt, dass Alter und PS nicht
zusammenhängen (zumidnest, wenn man die Leistung des Autos nimmt, wie sie im
Fahrzeugschien eingetragen ist). Dahingegen scheint es eine schwache negative
Korrelation zwischen Alter und Preis zu geben. Je älter ein Auto ist, desto
geringer ist sein Preis. -1 würde bedeuten, dass die negative Korrelation
perfekt ist.

Am stärksten linear scheint sich die Leistung auf den Preis auszuwirken. In der
zweiten Zeile und der dritten Spalte findet sich der Eintrag 0.914003. Je größer
die Leistung des Autos, desto höher sein Preis.


## Heatmaps

Es ist üblich, die Korrelationsmatrix als sogenanntes Heatmap-Diagramm zu
visualisieren. Bei einer Heatmap wird die Zahlenwerte der Matrix durch Farben
visualisiert. Ploty Express bietet dazu die Funktion `imshow()` an.

```{code-cell} ipython3
korrelationsmatrix = daten.corr()

fig = px.imshow(korrelationsmatrix)
fig.show()
```

Es ist hilfreich, die Werte der Korrelationsmatrix direkt in der Heatmap
anzeigen zu lassen. Daher verwenden wir die zusätzliche Option `text_auto=True`.

```{code-cell} ipython3
fig = px.imshow(korrelationsmatrix, text_auto=True)
fig.show()
```

Weitere Optionen zum Stylen der Heatmaps finden Sie in der [Plotly Dokumentation
→ Heatmaps in Plotly](https://plotly.com/python/heatmaps/).


## Zusammenfassung

In diesem Kapitel haben wir uns mit der linearen multiplen Regression
beschäftigt. Es wird eine lineare Modellfunktion für einen oder mehrere
Einflussfaktoren gesucht. Die Parameter der Modellfunktion, also die
Koeffizienten der mehrdimensionalen linearen Funktion werden so an die Daten
angepasst, dass die Fehlerquadratsumme möglichst klein wird. Um beurteilen zu
können, ob die beste gefundene Modellfunktion eine gute Prognose liefert, werten
wir den R²-Score aus.

Um zu analysieren, ob einzelne Merkmale miteinander linear korreliert sind,
werden die Korrelationsmatrix und die Heatmap eingesetzt.
