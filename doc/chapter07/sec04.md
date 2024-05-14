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

# Übungen


```{admonition} Aufgabe 1
:class: tip
Laden Sie den Datensatz ``population_germany.csv``. Wie viele Menschen werden in
Deutschland im Jahr 2030 leben? Führen Sie eine vollständige Datenanalyse durch
(Erkundung der Daten, Ermittlung der statistischen Kennzahlen inklusive
Visualisierungen). Wählen Sie dann ein Modell aus, trainieren Sie es und
bewerten Sie die Qualität des trainierten Modells. Visualisieren Sie Ihre
Prognose.
```

````{admonition} Lösung
:class: tip, toggle

```python
import pandas as pd

# Datenimport und explorative Analyse
data = pd.read_csv('population_germany.csv')
data.info()
```

Es liegen 222 Einträge vor und 4 Spalten mit den Eigenschaften Region, Code,
Jahr, Population. Die ersten beiden Eigenschaften Region und Code sind Objekte.
Die Eigenschaften Jahr und Population sind Integers.

Als erstes untersuchen wir, welche Eigenschaften als Region und Code gespeichert
sind.

```python
data.head(10)
```

Bei den ersten 10 Einträgen findet sich bei Region nur 'Germany' und bei Code
nur 'DEU'. Mit .unique() überprüfen wir, wie viele verschiedene Einträge es
überhaupt gibt.

```python
data['Code'].unique()
```

```python
data['Region'].unique()
```

Beide Eigenschaften enthalten nur den Code 'DEU' und die Region 'Germany', so
dass wir die beiden Eigenschaften entfernen könnten. Wir belassen die beiden
Spalten vorerst im Datensatz, fokussieren aber auf Jahr und Population. Wir
wählen das Jahr als neuen Index und verschaffen uns einen Überblick über die
statistischen Kennzahlen:

```python
data.describe()
```

```python
import plotly.express as px

fig = px.box(data['Population'], 
             title='Bevölkerungsentwicklung in Deutschland seit 1800',
             labels={'value': 'Anzahl Personen', 'variable': 'Legende'})

fig.show()
```

Der Median ist mit 62 Mio. Personen höher als der Mittelwert mit 55 Mio. Personen und näher am Q3-Quartil. Es gibt keine Ausreißer.

Als nächstes betrachten wir den zeitlichen Verlauf der Bevölkerungsentwicklung.

```python
fig = px.bar(data, x = 'Jahr', y = 'Population',
             title='Bevölkerungsentwicklung in Deutschland seit 1800',
             labels={'value': 'Anzahl Personen', 'variable': 'Legende'})
fig.show()
```

Die Bevölkerung ist seit 1800 gewachsen. Zu Beginn betrug einen
Bevölkerungsrückgang bis 1919/1920, dann steigt die Bevölkerung wieder an. Auch
in den 1940er Jahren kam es zu einem Bevölkerungsrückgang. In beiden Fällen
können wir vermuten, dass diese mit den beiden Weltkriegen zu tun hat. Aber auch
in späteren Zeiten kam es trotz einer beständig wachsenden Bevölkerung immer
wieder zu einem kurzen Bevölkerungsrückgang, z.B. um 1984 oder 2010.

Wir wählen ein lineares Regressionsmodell.

```python
from sklearn.linear_model import LinearRegression

# Anpassung der Daten für das lineare Regressionsmodell
X = data[['Jahr']]
y = data['Population']

# Wahl des Modells
model = LinearRegression()

# Training 
model.fit(X, y)
   
# Validierung
r2 = model.score(X, y)
print(f'Der Score ist: {r2:.2f}')
```

Der Score ist mit 0.97 sehr gut. Wir visualisieren die Regressionsgerade
zusammen mit den Daten. Dazu erstellen wir zuerst eine Prognose der Population
für die Jahre 1800 bis 2030.

```python
import numpy as np

X_predict = pd.DataFrame(np.arange(1800, 2031), columns=['Jahr'])
y_predict = model.predict(X_predict)

prediction = X_predict.copy()
prediction['Population'] = y_predict

prediction.tail(10)
```

Im Jahr 2030 werden laut dem Modell 94.3 Mio. Menschen in Deutschland leben.
Zuletzt visualisieren wir noch die Prognose.

```python
import plotly.graph_objects as go

fig1 = px.line(prediction, x = 'Jahr', y = 'Population')
fig1.update_traces(line_color='#E60000')
fig2 = px.bar(data, x = 'Jahr', y = 'Population')

fig = go.Figure(fig1.data + fig2.data)
fig.update_layout(
  title='Bevölkerungsentwicklung in Deutschland seit 1800',
  xaxis_title = 'Jahr',
  yaxis_title = 'Anzahl Personen'
)
fig.show()
```
````

```{admonition} Aufgabe 2
:class: tip
Eine Firma erhebt statistische Daten zu ihren Verkaufszahlen (angegeben in
Tausend US-Dollar) abhängig von dem eingesetzten Marketing-Budget in den
jeweiligen Sozialen Medien (Quelle siehe
https://www.kaggle.com/datasets/fayejavad/marketing-linear-multiple-regression).

Importieren Sie die Daten aus der Datei 'marketing_data.csv'. Führen Sie eine
explorative Datenanalyse durch. Trainieren Sie dann für jeden Input ein lineares
Regressionsmodell und bewerten Sie es mit dem R2-Bestimmtheitsmaß. Trainieren
Sie dann anschließend ein multiples Regressionsmodell. Wenn Sie nur ein Medium
einsetzen dürften, welches Medium würden Sie wählen?
```

````{admonition} Lösung
:class: tip, toggle

```python
import pandas as pd

data = pd.read_csv('marketing_data.csv')
data.info()
```

Die Daten enthalten 171 Einträge, die von 0 bis 170 indiziert sind. Es gibt vier
Eigenschaften, die alle als Floats gespeichert sind. Alle Einträge sind gültig.
Aufgrund der Aufgabenstellung ist klar, dass die ersten drei Eigenschaften das
investierte Marketing-Budget in die sozialen Medien YouTube, Facebook und
Newspaper darstellen. Die Spalte 'sales' repräsentiert dahingehend die Wirkung
der Marketing-Budgets.

```python
data.head(10)
```

```python
data.describe()
```

Als nächstes visualisieren wir die statistischen Kennzahlen des
Marketing-Budgets.

```python
import plotly.express as px

X = data.loc[:, 'youtube' : 'newspaper']
fig = px.box(X,
             title='Marketing-Budget',
             labels={'variable': 'Kategorie', 'value': 'Tsd. US-Dollar'})

fig.show()
```

Mit großem Abstand wird am meisten in das Marketing bei YouTube investiert. Im
Mittel 178 Tsd. US-Dollar, wohingegen nur 27 Tsd. US-Dollar in Facebook und 35
Tsd. US-Dollar in Zeitungen (Newspaper) investiert werden. Bei allen drei
Kategorien ist der Median ungefähr mittig zwischen Q1 und Q3. Bei der Kategorie
Newspaper gibt es einen Ausreißer.

Zuletzt betrachten wir noch den Boxplot der Wirkung 'sales'.

```python
import plotly.express as px

y = data['sales']
fig = px.box(y,
             title='Verkäufe',
             labels={'variable': 'Kategorie', 'value': 'Tsd. US-Dollar'})

fig.show()
```

Auch bei den Verkäufen gibt es keine Ausreißer. Der Median liegt näher an Q1 als
an Q3 und unterhalb des Mittelwertes von 16 Tsd. US-Dollar.

Alle drei Ursachen YouTube, Facebook und Newspaper könnten eine Wirkung auf die
Verkaufszahlen haben. Am einfachsten ist zunächst die Visualisierung als
Scattermatrix.

```python
fig = px.scatter_matrix(data)
fig.show()
```

YouTube und Facebook scheinen eine stärke lineare Wirkung auf die Verkaufszahlen
zu haben als die Zeitungen. Wir trainieren zunächst drei einzelne lineare
Regressionsmodelle und bestimmen den jeweiligen R2-Score.

```python
# Import des linearen Regressionsmodells
from sklearn.linear_model import LinearRegression

# Adaption der Daten
X_youtube = data.loc[:,['youtube']]
X_facebook = data.loc[:,['facebook']]
X_newspaper = data.loc[:,['newspaper']]
y = data.loc[:,'sales']

# YouTube
model_youtube = LinearRegression()
model_youtube.fit(X_youtube, y)
r2_youtube = model_youtube.score(X_youtube, y)
print(f'R2-Score YouTube: {r2_youtube:.2f}')

# Facebook
model_facebook = LinearRegression()
model_facebook.fit(X_facebook, y)
r2_facebook = model_facebook.score(X_facebook, y)
print(f'R2-Score Facebook: {r2_facebook:.2f}')

# Newspaper
model_newspaper = LinearRegression()
model_newspaper.fit(X_newspaper, y)
r2_newspaper = model_newspaper.score(X_newspaper, y)
print(f'R2-Score Newspaper: {r2_newspaper:.2f}')
```

Wie erwartet sind die Verkaufszahlen bei YouTube linear abhängig, bei Facebook
nur schwach linear abhängig und bei den Zeitungen scheint es keine lineare
Abhängigkeit zu geben. Wenn wir nur ein Medium wählen dürfte, so wäre das 
sicherlich YouTube.

Zuletzt trainieren wir noch ein multiples Regressionsmodell mit dem
Marketing-Budget YouTube und Facebook.

```python
# multiples lineares Regressionsmodell für alle Inputs
X = data.loc[:, ['youtube', 'facebook']]
y = data.loc[:,'sales']

model = LinearRegression()
model.fit(X, y)
r2 = model.score(X,y)

print(f'R2-Score für lineares Regressionsmodell mit YouTube und Facebook: {r2:.2f}')
```

Zusammen kommen wir nun auf einen R2-Score von 0.9.
````
