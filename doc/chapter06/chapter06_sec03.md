---
jupytext:
  cell_metadata_filter: -all
  formats: ipynb,md:myst
  main_language: python
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.5
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

# 6.3 Multiple lineare Regression

Bisher haben wir nur eine einzelne Eigenschaft aus den gesammelten Daten
herausgegriffen und untersucht, ob es zwischen dieser Eigenschaft und der
Zielgröße einen linearen Zusammenhang gibt. So simpel ist die Welt normalerweise
nicht, oft wirken mehrere Einflussfaktoren gleichzeitig. Daher steht die
**multiple lineare Regression** in diesem Abschnitt im Fokus.

## Lernziele

```{admonition} Lernziele
:class: important
* Sie wissen, was eine **multiple lineare Regression** ist und können sie mit Scikit-Learn durchführen.
```

+++

## Zwei Einflussfaktoren: PS und Baujahr beinflussen Preis

Bei unserem Beispiel-Datensatz von Autoscout24 mit den
Gebrauchtwagenpreis-Listen der Jahre 2011 bis 2021 gab es drei Spalten mit
numerischen Werten, die den Preis bestimmen könnten: Kilometerstand, Baujahr und
PS. Wir hatten zunächst die Analyse des linearen Zusammenhangs zwischen der
PS-Zahl und dem Preis durchgeführt. Das Ergebnis war eine Regressionsgerade

$$f(x_{\text{PS}}) = 186.8 -8330 \cdot x_{\text{PS}}.$$

Als R²-Score haben wir für diese Modellfunktion einen Wert von 0.61 ermittelt.

Nun möchten wir untersuchen, was passiert, wenn wir zusätzlich noch das Baujahr
$x_{\text{BJ}}$ hinzunehmen. Wir suchen jetzt also eine lineare Modellfunktion

$$f(x_{\text{PS}}, x_{\text{BJ}}) = \omega_0 + \omega_1\cdot x_{\text{PS}} +
\omega_2\cdot x_{\text{BJ}}.$$

Natürlich kann auch diese Modellfunktion nicht alle Datenpunkte
$(x_{\text{PS}}^{(i)}, x_{\text{BJ}}^{(i)}, y^{(i)})$ perfekt treffen. Wir
wünschen uns also, dass der Fehler zwischen den prognostizierten Werten und den
echten Werten möglichst klein ist. Als Fehlermaß benutzen wir wiederum die
Fehlerquadratsumme.

Wir importieren zuerst die benötigten Module und Funktionen und laden dann die
Daten.

```{code-cell} ipython3
import pandas as pd
from sklearn.linear_model import LinearRegression

# Vorbereitung der Daten
data_raw = pd.read_csv('data/autoscout24-germany-dataset.csv')
data = data_raw.dropna().copy()
data = data.drop([11753, 11754, 21675])
```

Diesmal wollen wir zwei Spalten mit Inputs aus dem DataFrame-Objekt extrahieren,
nämlich PS-Zahl ('hp') und Baujahr ('year'). Dazu benutzen wir eine Selektion
der Spalten über eine Liste.

```{code-cell} ipython3
# Extraktion der Input- und Output-Daten
X = data.loc[:, ['hp', 'year']].values
y = data.loc[:, 'price'].values
```

Jetzt können wir das lineare Regressionsmodell von Scikit-Learn mit der
`.fit()`-Methode trainieren. Da Scikit-Learn zwingend eine  Matrix als Input
erfordert, mussten wir beim letzten Mal, als wir nur mit der PS-Zahl trainiert
haben, aus dem Vektor mit der PS-Zahl eine Matrix mit einer Spalte machen. Das
entfällt hier, da wir nun eine Matrix mit zwei Spalten haben.

Wir lassen auch gleich den R²-Score mit ausgeben.

```{code-cell} ipython3
# Wahl des Modells
model = LinearRegression()

# Training
model.fit(X, y)

# Validierung
r2 = model.score(X, y)
print('Der R2-Score ist: {:.2f}'.format(r2))
```

Wir haben unsere Prognosequalität von 0.61 auf 0.71 gesteigert.

Aber vielleicht war die PS-Zahl ein schlechtes Kriterium und das Baujahr ist die
einzig wahre Ursache für den Preis im Gebrauchtwagenmarkt? Sicherheitshalber
trainieren wir ein lineares Regressionsmodell nur für das Baujahr und schauen
uns den R²-Score an.

```{code-cell} ipython3
# extraxt input and output data
X = data.loc[:,  'year'].values.reshape(-1,1)
y = data.loc[:, 'price'].values

# choose model
model = LinearRegression()

# train linear regression model
model.fit(X, y)

# check quality
r2 = model.score(X, y)
print('Der R2-Score ist: {:.2f}'.format(r2))
```

Das Baujahr alleine ist sicher nicht geeignet, um die Autopreise zu erklären.
Wenn wir uns nur für eine Eigenschaft entscheiden müssten, dann würden wir
besser die PS-Zahl nehmen. 

+++

## Erklären PS, Baujahr und Kilometerstand am besten den Preis?

Probieren wir es doch einfach aus, ob die Kombination aller drei Einflussgrößen
nochmal eine Verbesserung bringt.

```{code-cell} ipython3
# extraxt input and output data
X = data.loc[:, ['hp', 'year', 'mileage']].values
y = data.loc[:, 'price'].values

# choose model
model = LinearRegression()

# train linear regression model
model.fit(X, y)

# check quality
r2 = model.score(X,y)
print('Der R2-Score ist: {:.2f}'.format(r2))
```

Tatsächlich, damit schaffen wir erneut eine leichte Verbesserung, jetzt haben
wir einen R²-Score von 0.73.

Schauen wir uns doch einmal an, welche Koeffizienten von Scikit-Learn für unsere
mehrdimensionale lineare Modellfunktion gefunden wurden.

```{code-cell} ipython3
print('Achsenabschnitt w0:')
print(model.intercept_)
print('Koeffizienten (Steigungen):')
print(model.coef_)
```

Damit lautet unsere Modellfunktion abhängig von PS-Zahl (PS), Baujahr (BJ) und
Kilometerstand (KM) also

$$f(x_{\text{PS}}, x_{\text{BJ}}, x_{\text{KM}}) = 16507.02 + 13409.75\cdot
x_{\text{PS}} + 3245.26 \cdot x_{\text{BJ}} - 3395.56 \cdot x_{\text{KM}}.$$

PS-Zahl und Baujahr wirken positiv, also je mehr PS und je höher das Baujahr (=
jünger), desto höher der Preis. Der Kilometerstand wirkt umgekehrt. Je kleiner
der Kilomterstand, desto höher der Preis.

+++

## Zusammenfassung

In diesem Kapitel haben wir uns mit der linearen (multiplen Regression)
beschäftigt. Es wird eine lineare Modellfunktion für einen oder mehrere
Einflussfaktoren gesucht. Die Parameter der Modellfunktion, also die
Koeffizienten der mehrdimensionalen linearen Funktion werden so an die Daten
angepasst, dass die Fehlerquadratsumme möglichst klein wird. Um beurteilen zu
können, ob die beste gefundene Modellfunktion eine gute Prognose liefert, werten
wir den R²-Score aus.
