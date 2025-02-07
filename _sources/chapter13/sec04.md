---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.16.3
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

# Übung

Der folgende Datensatz enthält die Preise und Eigenschaften von Diamanten. Die
Eigenschaften sind:

* Karat (Gewicht des Diamanten)
* Schliff (Qualität: befriedigend, gut, sehr gut, erstklassig, ideal)
* Farbe des Diamanten (von J (schlechteste) bis D (beste))
* Reinheit - ein Maß für die Klarheit des Diamanten (I1 (schlechteste), SI2,
  SI1, VS2, VS1, VVS2, VVS1, IF (beste))
* Tiefe (Gesamttiefe in Prozent = z / Mittelwert (x, y) = 2 * z / (x + y))
* Tafel (Breite der Oberseite des Diamanten im Verhältnis zur breitesten Stelle)
* Preis (in US-Dollar)
* x - Länge in mm
* y - Breite in mm
* z - Tiefe in mm

Bearbeiten Sie die folgenden Aufgaben. Vorab können Sie die folgenden Module
importieren. Schreiben Sie Ihre Antworten als Kommentar oder in eine
Markdown-Zelle. Lassen Sie das Jupyter Notebook am Ende noch einmal komplett
ausführen, bevor Sie es abgeben.

```{code-cell}
# import numpy as np
# import pandas as pd
# import plotly.express as px
# import plotly.graph_objects as go

# from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
# from sklearn.linear_model import LinearRegression, LogisticRegression, Perceptron
# from sklearn.model_selection import train_test_split, cross_validate, KFold, GridSearchCV
# from sklearn.neural_network import MLPClassifier, MLPRegressor
# from sklearn.preprocessing import PolynomialFeatures, MinMaxScaler, StandardScaler
# from sklearn.svm  import SVC, SVR
# from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor, plot_tree

# pd.DataFrame.iteritems = pd.DataFrame.items
```

## Explorative Datenanalyse

```{admonition} Import und Bereinigung der Daten
:class: miniexercise
Importieren Sie die Daten 'diamonds_DE.csv'. Verschaffen Sie sich einen
Überblick und beantworten Sie folgende Fragen in einer Markdown-Zelle:

* Wie viele Diamanten enthält die Datei?
* Wie viele Merkmale/Attribute/Eigenschaften/Features sind in den Daten enthalten?
* Sind alle Einträge gültig? Wenn nein, wie viele Einträge sind nicht gültig?
* Welchen Datentyp haben die einzelnen Attribute/Eigenschaften/Features?

Falls der Datensatz ungültige Werte aufweist oder Unstimmigkeiten enthält,
bereinigen Sie ihn.
```

````{admonition} Lösung
:class: minisolution, dropdown
```python
daten = pd.read_csv('diamonds_DE.csv', skiprows=3)
daten.info()
```

```python
daten.head()
```

Der Datensatz enthält 53940 Diamanten mit 11 Attributen/Eigenschaften. Alle
Einträge sind gültige Einträge. Die Eigenschaften 'Unnamed: 0' und 'Preis' sind
Integers. Die Eigenschaften 'Karat', 'Tiefe', 'Tafel', 'x', 'y' und 'z' sind
Floats. Die Eigenschaften 'Schliff', 'Farbe' und 'Reinheit' sind Objekte.

Der Datensatz enthält nur gültige Werte, aber sollte dennoch bereinigt werden,
da die ersten fünf Zeilen des Datensatzes nahelegen, dass die Eigenschaft
'Unnamed: 0' ein Index ist. Wir visualisieren diese Eigeschaft, um die Hypothese
zu überprüfen.

```python
fig = px.scatter(daten, y = 'Unnamed: 0',
                 title='Diamanten')
fig.show()
```

Tatsächlich stimmen (zumindest visuell) der automatisch erzeugte Index des
DataFrame-Objektes und die Werte von 'Unnamed: 0' überein. Die überflüssige
Spalte wird gelöscht.

```python
daten = daten.drop(columns='Unnamed: 0')
daten.info()
```
````

```{admonition} Statistische Kennzahlen der numerischen Eigenschaften
:class: miniexercise
* Ermitteln Sie von den numerischen Eigenschaften die statistischen Kennzahlen
  und visualisieren Sie sie. Verwenden Sie beim Plot eine aussagefähige
  Beschriftung.
* Interpretieren Sie jede Eigenschaft anhand der statistischen Kennzahlen und
  der Plots.
* Bereinigen Sie bei Ungereimtheiten den Datensatz weiter.
* Entfernen Sie Ausreißer.
```

````{admonition} Lösung
:class: minisolution, dropdown
```python
numerische_merkmale = ['Karat', 'Tiefe', 'Tafel', 'Preis', 'x', 'y', 'z']
daten.describe()
```

```python
fig = px.box(daten, y = numerische_merkmale,
             title='Diamanten: numerische Eigenschaften',
             labels={'variable': 'Eigenschaft', 'value': 'Wert'})
fig.show()
```

Die Skalen der einzelnen Eigenschaften sind stark verschieden, so dass ein
gemeinsamer Boxplot nicht möglich ist. Daher werden die Eigenschaften einzeln
oder in vergleichbaren Gruppen sortiert.

```python
fig = px.box(daten, y = 'Karat',
             title='Diamanten')
fig.show()
```

75 % der Diamanten haben ein Karat und weniger, wobei der Median bei 0.7 Karat
liegt. Das ist etwas niedriger als der Mittelwert von 0.8 Karat. Der höhere
Mittelwert wird sicherlich bedingt durch die vielen Ausreißer nach oben ab 2 bis
ca. 5 Karat.

Als nächstes werden Tiefe und Tafel untersucht.

```python
fig = px.box(daten, y = ['Tiefe', 'Tafel'],
             title='Diamanten: numerische Eigenschaften',
             labels={'variable': 'Eigenschaft', 'value': 'Größe'})
fig.show()
```

50 % aller Diamanten haben eine Tiefe zwischen 61 % und 62 %. Der Median ist mit
61.8 % mittig zwischen Q1 und Q3 und stimmt mit dem Mittelwert 61.7 % überein.
Es gibt Ausreißer nach oben und unten.

Bei der Breite ist der Median 57 näher am Q1-Wert 56 und und liegt auch etwas
unterhalb des Mittelwertes von 57.4.

```python
fig = px.box(daten, y = ['x', 'y', 'z'],
             title='Diamanten: numerische Eigeschaften',
             labels={'variable': 'Eigenschaft', 'value': 'Wert'})
fig.show()
```

Der Boxplot sowie die statistischen Kennzahlen der Eigenschaften x, y und z
zeigen Ungereimtheiten. Bei allen drei Eigenschaften wird auch der Wert Null
angenommen. Das ist unmöglich, daher müssen diese Diamanten aus dem Datensatz
entfernt werden.

```python
daten[ daten['x'] == 0 ] 
```

```python
daten[ daten['y'] == 0 ]
```

```python
daten[ daten['z'] == 0 ]
```

Es ist mühsam, die Indizes (Zeilennummern) abzuschreiben. Daher benutzen wir das
Attribut `.index`, um die Indizes direkt der drop()-Methode als Argument zu
übergeben.

```python
zeilen = daten[ daten['x'] == 0 ].index
daten = daten.drop(zeilen)

zeilen = daten[ daten['y'] == 0 ].index
daten = daten.drop(zeilen)

zeilen = daten[ daten['z'] == 0 ].index
daten = daten.drop(zeilen)

daten.info()
```

Darüber hinaus gibt es bei der Größe in y-Richtung zwei deutliche Ausreißer mit
31.8 mm und 58.9 mm. Auch bei der Größe in z-Richtung gibt es einen deutlichen
Ausreißer nach oben mit z = 31.8 mm. Diese Diamanten werden ebenfalls entfernt.

```python
zeilen = daten[ daten['y'] > 31.0 ].index
daten = daten.drop(zeilen)

zeilen = daten[ daten['z'] > 31.0 ].index
daten = daten.drop(zeilen)

daten.info()
```

Somit sind es nur 53917 Einträge von ehemals 53940 Einträgen. Es wurden 23
Diamanten entfernt.

Zuletzt betrachten wir noch den Preis.

```python
fig = px.box(daten, y = 'Preis',
             title='Diamanten: numerische Eigenschaften')
fig.show()
```

Der Median von 2401 US-Dollar liegt nicht mittig zwischen Q1 und Q3 und ist deutlich niedriger als der Mittelwert von 3932 US-Dollar. Die Preise müssen sehr asymmetrisch verteilt sein.

```python
fig = px.histogram(daten['Preis'],
                   title='Histogramm des Diamantenpreises',
                   labels={'value':'Preis in US-Dollar', 'count': 'Anzahl'})
fig.show()
```

Die Verteilung der Preise ist rechtsschief (linkssteil).
````

```{admonition} Statistische Kennzahlen (kategoriale Eigenschaften)
:class: miniexercise
* Ermitteln Sie, wie häufig jeder Wert einer Kategorie in der jeweiligen Spalte
  vorkommt.
* Lassen Sie die Anzahl der Werte auch visualisieren. Beschriften Sie die
  Diagramme mit einem aussagefähigen Titel.
* Fassen Sie die Ergebnisse bzw. die Interpretation davon jeweils kurz zusammen
  (in einer Markdown-Zelle).
```

````{admonition} Lösung
:class: minisolution, dropdown
```python
for kategorie in ['Schliff', 'Farbe', 'Reinheit']:
    print(f'Eigenschaft {kategorie}: {daten[kategorie].unique()}')

```

```python
daten['Schliff'].unique()
daten['Schliff'].value_counts()
```

```python
fig = px.bar(daten['Schliff'].value_counts(),
             title='Schliff der Diamanten',
             labels={'value': 'Anzahl', 'index': 'Qualität', 'variable':'Legende'})
fig.show()
```

In dem Datensatz kommen überraschend viele Diamanten der Qualität ideal vor. Die
Anzahl der Diamanten in den einzelnen Qualitätsstufen nimmt immer weiter ab.

```python
fig = px.bar(daten['Farbe'].value_counts(),
             title='Farbe der Diamanten',
             labels={'value': 'Anzahl', 'index': 'Farbname', 'variable':'Legende'})
fig.show()
```

Am häufigsten kommt die Farbe G vor, am seltesten ist Farbe J.

```python
fig = px.bar(daten['Reinheit'].value_counts(),
             title='Reinheit der Diamanten',
             labels={'value': 'Anzahl', 'index': 'Reinheitskategorie', 'variable':'Legende'})
fig.show()
```

I1 ist die schlechteste Reinheit und kommt auch am seltesten vor. IF ist die
beste Reinheitskategorie und kommt am zweitseltesten vor. Die meisten Diamanten
im Datensatz haben eine mittlere Reinheitsstufe SI1.
````

## ML-Modelle

```{admonition} Regression
:class: miniexercise
Ziel der Regressionsaufgabe ist es, den Preis der Diamanten zu prognostizieren.

* Wählen Sie zwei Regressionsmodelle aus.
* Wählen Sie für jedes der zwei Modelle eine oder mehrere Eigenschaften aus, die
  Einfluss auf den Preis haben könnten. Begründen Sie Ihre Auswahl.
* Adaptieren Sie die Daten jeweils passend zu den von Ihnen gewählten Modellen.
* Falls notwendig, skalieren Sie die Daten.
* Führen Sie einen Split der Daten in Trainings- und Testdaten durch.
* Trainieren Sie jedes ML-Modell.
* Validieren Sie jedes ML-Modell bzgl. der Trainingsdaten und der Testdaten.
* Bewerten Sie abschließend: welches der zwei Modelle würden Sie empfehlen?
  Begründen Sie Ihre Empfehlung.
```

````{admonition} Lösung
:class: minisolution, dropdown
Wahl der Regressionsmodelle: lineare Regression und SVM.

```python
fig = px.scatter_matrix(daten.loc[:, ['Karat', 'Tiefe', 'Tafel', 'x', 'y', 'z', 'Preis']])
fig.show()
```

Karat (Gewicht des Diamanten) scheint von der Größe (x, y und z) abzuhängen. Es
ist zunächst kein linearer Zusammenhang zwischen Tiefe/Tafel und dem Preis
erkennbar. Im Folgenden wird daher für die lineare Regression nur Karat als
Input gewählt.

```python
selected_data = daten.loc[:, ['Karat']]

scaler = StandardScaler()
scaler.fit(selected_data)
input_numerical = scaler.transform(selected_data)

X_train, X_test, y_train, y_test = train_test_split(input_numerical, daten['Preis'])
```

```python
model_linear_regression = LinearRegression()
model_linear_regression.fit(X_train, y_train)

score_train = model_linear_regression.score(X_train, y_train)
score_test = model_linear_regression.score(X_test, y_test)

print(f'Score Trainingsdaten: {score_train:.2f}')
print(f'Score Testdaten: {score_test:.2f}')
```

Support Vector Machines beherrschen auch nichtlineare Zusammenhänge. Es werden
daher alle Features verwendet.

```python
selected_data = daten.loc[:, ['Karat', 'Tiefe', 'Tafel', 'x', 'y', 'z']]

scaler = StandardScaler()
scaler.fit(selected_data)
input_numerical = scaler.transform(selected_data)

X_train, X_test, y_train, y_test = train_test_split(input_numerical, daten['Preis'])
```

```python
model_svr = SVR()
model_svr.fit(X_train, y_train)

score_train = model_svr.score(X_train, y_train)
score_test = model_svr.score(X_test, y_test)

print(f'Score Trainingsdaten: {score_train:.2f}')
print(f'Score Testdaten: {score_test:.2f}')
```

Zusammenfassung der Scores für die Testdaten:

lineare Regression: 0.85
Support Vector Machines: 0.55

Die lineare Regression erreicht bessere Testscores als die SVM, daher ist dieses
Modell zu bevorzugen.
````

```{admonition} Klassifikation
:class: miniexercise
Ziel der Klassifikationsaufgabe ist es, die Preisklasse "billig" oder "teuer"
der Diamanten zu prognostizieren.

* Vorbereitung: Filtern Sie die Daten nach den Diamanten, deren Preis kleiner
oder gleich dem Median aller Preise ist. Diese Diamanten sollen als "billig"
klassfiziert werden. Diamanten, deren Preis größer als der Median aller Preise
ist, sollen als "teuer" klassifiziert werden. Speichern Sie dieses neue Merkmal
in einer neuen Spalte "Preisklasse".
* Trainieren Sie einen Entscheidungsbaum (Decision Tree) mit den Merkmalen
  "Karat" und "Schliff".
* Adaptieren Sie die Daten.
* Falls notwendig, skalieren Sie die Daten.
* Führen Sie einen Split der Daten in Trainings- und Testdaten durch.
* Führen Sie eine Gittersuche für
  * die Baumtiefe (2, 3) und
  * die minimale Anzahl an Samples pro Blatt (1, 2, 5) durch.
* Lassen Sie das beste Modell als Baum visualisieren.
* Bewerten Sie abschließend: ist das Modell für den Produktiveinsatz geeignet?
  Begründen Sie Ihre Bewertung.
```

````{admonition} Lösung
:class: minisolution, dropdown

Vorbereitung: Filterung der Daten bezogen auf den Median des Preises

```python
median_preis = daten['Preis'].median()
print(f'Median Preis: {median_preis} US-Dollar')

daten.loc[daten['Preis'] <= median_preis].index
```

```python
daten.loc[ daten['Preis'] <= median_preis, 'Preisklasse'] = "billig"
daten.loc[ daten['Preis'] >  median_preis, 'Preisklasse'] = "teuer"

daten['Preisklasse'].unique()
daten.head()
```

Die kategorialen Werte müssen durch Zahlen ersetzt werden. Wir wählen 0 für den
schlechtesten Schliff (fair) und 4 für den besten Schliff (ideal).

```python
schliff_kodierung = {
  'fair': 0,
  'gut': 1,
  'sehr gut': 2,
  'erstklassig': 3,
  'ideal': 4 
}

daten['Schliff'] = daten['Schliff'].replace(schliff_kodierung).astype('int')
daten['Schliff'].unique()

preisklasse_kodierung = {
    'billig': 0,
    'teuer': 1
}
daten['Preisklasse'] = daten['Preisklasse'].replace(preisklasse_kodierung).astype('int')
daten['Preisklasse'].unique()
```

Die Werte für Karat liegen zwischen 0.2 und 5 und sind daher vergleichbar den
Werten für die Schliffqualität von 0 bis 4. Letztere dürfen nicht skaliert
werden und bei der Eigenschaft Karat ist es nicht notwendig. Daher erfolgt keine
Skalierung der Daten.

```python
input_categorical = daten[['Karat', 'Schliff']]

X_train, X_test, y_train, y_test = train_test_split(input_categorical, daten['Preisklasse'])
```

Training Entscheidungsbaum mit Gittersuche

```python
gitter = {
    'max_depth': [2, 3],
    'min_samples_leaf': [1, 2, 5]
}
kfold = KFold()

suche_modell = GridSearchCV(DecisionTreeClassifier(), param_grid=gitter, cv=kfold)

suche_modell.fit(X_train, y_train)
score_train = suche_modell.score(X_train, y_train)
score_test = suche_modell.score(X_test, y_test)

print(f'Score Trainingsdaten: {score_train:.2f}')
print(f'Score Testdaten: {score_test:.2f}')

```

```python
suche_modell.best_params_
```

```python
bestes_modell = DecisionTreeClassifier(max_depth = 3, min_samples_leaf = 1)

bestes_modell.fit(X_train, y_train)
score_train = bestes_modell.score(X_train, y_train)
score_test = bestes_modell.score(X_test, y_test)

plot_tree(bestes_modell);
```

Dieses Modell ist nicht für den Produktiveinsatz geeignet, da Trainings- und
Testscore bei 0.1 liegen.
````
