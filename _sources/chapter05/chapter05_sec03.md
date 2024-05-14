---
jupytext:
  formats: ipynb,md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.7
kernelspec:
  display_name: Python 3.9.13 ('python39')
  language: python
  name: python3
---

# 5.3 Daten filtern und gruppieren

Im vorherigen Kapitel haben wir Autos basierend auf ihrem Kilometerstand
gruppiert und visualisiert. Während diese Gruppierung automatisch im Hintergrund
stattfand, werden wir in diesem Kapitel lernen, wie wir direkt auf die
gruppierten Daten zugreifen und zusätzliche Analysen durchführen können.


## Lernziele

```{admonition} Lernziele
:class: goals
* Sie wissen, dass die Wahrheitswerte `True` (wahr)  oder `False` (falsch) in
  dem Datentyp **bool** gespeichert werden.
* Sie kennen die wichtigstens Vergleichsoperatoren (`<`, `<=`, `>`, `>=`, `==`,
  `!=`, `in`, `not in`) in Python.
* Sie können ein Pandas-DataFrame-Objekt nach einem Wert filtern.
* Sie können ein Pandas-DataFrame-Objekt mit den Methoden `groupby()` und
  `get_group()` gruppieren.
```


## Daten filtern

Im vorherigen Kapitel haben wir die Kilometerstände von Autos untersucht, die im
Jahr 2020 zugelassen und Mitte 2023 auf Autoscout24.de angeboten wurden. Bei der
Kategorisierung der Kilometerstände fiel auf, dass Fahrzeuge mit einer
Laufleistung von über 200000 km selten sind. Trotzdem beeinflusste dies die
Aufteilung in zehn gleichmäßige Gruppen, die von 0 km bis 435909 km reichten,
erheblich. Um eine genauere Analyse zu ermöglichen, wäre es sinnvoll, Fahrzeuge
mit einer Laufleistung von bis zu 200.000 km in den Fokus zu nehmen und die
Ausreißer auszuschließen. Daher widmen wir uns in diesem Kapitel der Filterung
von tabellarischen Datensätzen mithilfe von Pandas.

Zuerst laden wir den Datensatz und überprüfen den Inhalt.

```{code-cell} ipython3
import pandas as pd

data = pd.read_csv('autoscout24_DE_2020.csv')
data.info()
```

Um die Autos mit einem Kilometerstand von bis zu 200000 km zu filtern,
vergleichen wir die entsprechende Spalte mit dem Wert 200000, indem wir den aus
der Mathematik bekannten Kleiner-gleich-Operators `<=` benutzen. Das Ergebnis
dieses Vergleichs speichern wir in der Variable `bedingung`.

```{code-cell} ipython3
bedingung = data['Kilometerstand (km)'] <= 200000
```

Aber was genau ist in der Variable `bedingung` enthalten? Schauen wir uns den
Datentyp an:

```{code-cell} ipython3
type(bedingung)
```

Offensichtlich handelt es sich um ein Pandas-Series-Objekt. Für weitere
Informationen können wir die `.info()`-Methode aufrufen:

```{code-cell} ipython3
bedingung.info()
```

In dem Series-Objekt sind 18566 Einträge vom Datentyp `bool` gespeichert. Diesen
Datentyp haben wir bisher nicht kennengelernt. Wir lassen die ersten fünf
Einträge ausgeben:

```{code-cell} ipython3
bedingung.head()
```

Sind alle Einträge mit dem Wert `True` gefüllt? Wie viele und vor allem welche
einzigartige Einträge gibt es in diesem Series-Objekt?

```{code-cell} ipython3
bedingung.unique()
```

Das Series-Objekt enthält nur `True` und `False`, was den Datentyp `bool`
charakterisiert. In diesem Datentyp können nur zwei verschiedene Werte
gespeichert werden, nämlich wahr (True) und falsch (False). Oft sind
Wahrheitswerte das Ergebnis eines Vergleichs, wie das folgende Code-Beispiel
zeigt:

```{code-cell} ipython3
x = 19
print(x  < 100)
```

In der Python-Programmierung wird der Datentyp bool oft verwendet, um
Programmcode zu verzweigen. Damit ist gemeint, dass Teile des Programms nur
durchlaufen und ausgeführt werden, wenn eine bestimmte Bedingung wahr (True)
ist. In dieser Vorlesung benutzen wir bool-Werte hauptsächlich zum Filtern von
Daten.

```{admonition} Welche Vergleichsoperatoren kennt Python
In Python können die mathematischen Vergleichsoperatoren in ihrer gewohnten
Schreibweise verwendet werden:
* `<` kleiner als
* `<=` kleiner als oder gleich 
* `>` größer
* `>=` größer als oder gleich
* `==` gleich (`=` ist der Zuweisungsoperator, nicht mit Gleichheit
  verwechseln!)
* `!=` ungleich 

Darüber hinaus kann mit `in` oder `not in` getestet werden, ob
ein Element in einer Liste ist oder eben nicht.
```

Aber was machen wir jetzt mit diesem Series-Objekt? Wir können es als Index
benutzen für den ursprünglichen Datensatz benutzen. Die Zeilen, in denen `True`
sthet, werden übernommen, die anderen verworfen.

```{code-cell} ipython3
autos_bis_200000km = data[bedingung]
autos_bis_200000km.info()
```

Von den 18566 Autos wurden 18525 Autos übernommen. Ist denn die Filterung
geglückt? Wir verschaffen uns mit der `.describe()`-Methode einen schnellen
Überblick.

```{code-cell} ipython3
autos_bis_200000km.describe()
```

Der maximale Eintrag für die Spalte `Kilometerstand (km)` ist 199000 km. Mit dem
Tilde-Operaot `~` können wir das Pandas-Series-Objekt `bedingung` in das
Gegenteil umwandeln. Damit können wir also die Autos, bei denen der Vergleich
`<= 200000` zu `False` ausgewertet wurde, herausfiltern.

```{code-cell} ipython3
autos_ab_200000km = data[~bedingung]
autos_ab_200000km.info()
```

41 Autos, die 2020 zugelassen wurden, sollten Mitte 2023 mit einem
Kilometerstand von mehr als 200000 km verkauft werden. Schauen wir uns die
Statistik an.

```{code-cell} ipython3
autos_ab_200000km.describe()
```

Und was sind das für Autos?

```{code-cell} ipython3
autos_ab_200000km.head(10)
```


## Gruppieren

Eine Filterung nach Kilometerstand ermöglicht es uns, die Autos in zwei
Datensätze zu teilen: Autos mit bis zu 200000 km Laufleistung und jene mit mehr
als 200000 km (hierzu kann der Tilde-Operator (~) verwendet werden).

Wenden wir nun diese Technik an, um die Fahrzeuge basierend auf ihrer Marke zu
trennen. Ein Beispiel: Um alle "Audi"-Fahrzeuge zu extrahieren, verwenden wir
den folgenden Code:

```{code-cell} ipython3
bedingung_audi = data['Marke'] == 'audi'
audis = data[bedingung_audi]
audis.info()
```

Diese Bedingung erfüllen 1.190 Autos. Der Gesamtdatensatz enthält jedoch 41
unterschiedliche Automarken. Es wäre ineffizient, für jede Marke eine separate
Filterung durchzuführen. Deshalb bietet Pandas die `.groupby()`-Methode, die es
erlaubt, die Daten automatisch nach den einzigartigen Einträgen einer Spalte zu
gruppieren:

```{code-cell} ipython3
autos_nach_marke = data.groupby('Marke')
type(autos_nach_marke)
```

Das Resultat ist eine spezielle Pandas-Datenstruktur namens `DataFrameGroupBy`.
Es sind nicht alle bisher bekannte Methoden auf dieses Objekt anwendbar, aber
beispielsweise die `.describe()`-Methode darf verwendet werden:

```{code-cell} ipython3
autos_nach_marke.describe()
```

Für jede Automarke werden nun für jede Spalte mit metrischen (quantitativen)
Informationen die statistischen Kennzahlen ermittelt. Die entstehende Tabelle
ist etwas unübersichtlich. Besser ist daher, sich die statistischen Kennzahlen
einzeln ausgeben zu lassen. Im folgenden ermitteln wir die Mittelwerte der
metrischen Informationen nach Automarke. Damit tatsächlich auch nur die
metrischen Daten gemittelt werden, müssen wir als Argument noch zusätzlich
`numeric_only=True` setzen.

```{code-cell} ipython3
autos_nach_marke.mean(numeric_only=True)
```

Eine sehr wichtige Methode der GroupBy-Datenstruktur ist die
`get_group()`-Methode. Damit können wir ein bestimmtes DataFrame-Objekt aus dem
GroupBy-Objekt extrahieren:

```{code-cell} ipython3
audis_alternativ = autos_nach_marke.get_group('audi')
audis_alternativ.info()
```

In der Variablen `audis_alternativ` steckt nun der gleiche Datensatz wie in der
Variablen `audis`, den wir bereits durch das Filtern des ursprünglichen
Datensatzes extrahiert haben. 


## Zusammenfassung und Ausblick

Dieses Kapitel hat uns in die Technik des Datenfilterns eingeführt. Um
spezifische Einträge aus einem Datensatz basierend auf einem bestimmten Wert zu
extrahieren, nutzen wir Vergleichsoperationen und verwenden das resultierende
Series-Objekt als Index. Wenn das Ziel darin besteht, Daten anhand der
einzigartigen Werte einer Spalte zu gruppieren, dann ist die Kombination von
`.groupby()` und `.get_group()` oft der effizienteste Weg. Damit haben wir
unsere Einführung in die Datenexploration abgeschlossen, obwohl es noch viele
weitere Möglichkeiten gibt, die Daten zu erkunden. Im nächsten Kapitel starten
wir mit den Grundlagen des maschinellen Lernens und befassen uns mit der
linearen Regression.
