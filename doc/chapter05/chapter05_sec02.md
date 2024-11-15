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

# 5.2 Barplots und Histogramme

Barplots (Balken- oder Säulendiagramme) sind die am häufigsten verwendeten
Visualisierungen für kategoriale Daten. In diesem Kapitel lernen wir, wie mit
Plotly ein Barplot erstellt und von einem Histogramm unterschieden wird.

## Lernziele

```{admonition} Lernziele
:class: goals
* Sie wissen, was ein **Barplot** ist.
* Sie können ein **Säulendiagramm** von einem **Balkendiagramm** unterscheiden.
* Sie können mit der Funktion **bar()** des Plotly-Express-Moduls einen Barplot
  generieren lassen.
* Sie wissen, wie aus numerischen Daten ein **Histogramm** erzeugt wird.
* Sie können mit der Funktion **histogram()** des Plotly-Express-Moduls ein
  Histogramm erzeugen lassen.
```

## Barplots

Im letzten Kapitel haben wir uns mit kategorialen (qualitativen) Daten
auseinandergesetzt. Um solche Daten zu visualisieren und zu vergleichen,
benötigen wir geeignete Diagramme. Ein Boxplot ist hierfür nicht geeignet, da
man mit kategorialen Daten keine Rechenoperationen wie Mittelwertbildung oder
die Berechnung von Streuungsmaßen durchführen kann. Eine Methode, die wir
bereits kennengelernt haben, ist `.value_counts()`. Sie zählt, wie oft jeder
einzigartige Wert in einer Datenreihe vorkommt. Die Anzahl der Werte pro
Kategorie wird mit dem sogenannten **Barplot** visualisiert.

Ein Barplot muss nicht nur die Anzahl der Werte pro Kategorie zeigen. Er kann
jede numerische Information darstellen, die einer Kategorie zugeordnet ist.
Dabei werden prinzipiell zwei Varianten unterschieden. Zum einen können die
Kategorien entlang der x-Achse aneinandergereiht werden. Die Höhe der Rechtecke
repräsentiert dann den Zahlenwert dieser Kategorie. Da die Rechtecke an Säulen
erinnern, wird diese Variante **Säulendiagramm** genannt. Die andere Möglichkeit
ist, die Kategorien untereinander entlang der y-Achse aufzuführen. Dann ist die
Länge der Rechtecke repräsentativ für den Zahlenwert dieser Kategorie. Diese
Variante wird **Balkendiagramm** genannt.

```{admonition} Was ist ... ein Barplot?
Ein Barplot ist ein Diagramm, das kategoriale Daten visualisiert. Jede Kategorie
wird durch die Höhe oder Länge eines Rechtecks repräsentiert, das den
zugehörigen Wert darstellt.
```

Probieren wir Barplots am Beispiel der Autoscout24-Verkaufspreise für Autos aus,
die 2020 zugelassen wurden. Zuerst laden wir die Daten und verschaffen uns einen
Überblick.

```{code-cell}
import pandas as pd

data = pd.read_csv('autoscout24_DE_2020.csv')
data.info()
```

Mit der Methode `.value_counts()` lassen wir Python die Anzahl der Autos pro
Marke bestimmen.

```{code-cell}
anzahl_pro_marke = data['Marke'].value_counts()
anzahl_pro_marke.info()
```

Schauen wir uns die ersten zehn Einträge an:

```{code-cell}
anzahl_pro_marke.head(10)
```

Die Methode `.value_counts()` sortiert die Einträge standardmäßig von der
höchsten zur niedrigsten Anzahl.

Mit nur wenigen Zeilen Code können wir mit der Funktion `bar()` aus dem
Plotly-Express-Modul eine Visualisierung erstellen. Zuerst importieren wir das
Modul, dann erzeugen wir das Diagramm mit `bar()` und zuletzt lassen wir das
Diagramm mit `show()` anzeigen.

```{code-cell}
import plotly.express as px

fig = px.bar(anzahl_pro_marke)
fig.show()
```

Obwohl Plotly Express bereits eine ansprechende Visualisierung bietet, könnten
die automatisch generierten Beschriftungen "index", "value" und "variable"
verbessert werden. Außerdem sollte ein Diagrammtitel hinzugefügt werden. Der
Titel kann direkt in der `bar()`-Funktion über das `title=` Argument gesetzt
werden. Für die Achsenbeschriftungen und den Legendentitel verwenden wir die
Funktion `update_layout()`. Die Argumente `xaxis_title=` und `yaxis_title=`
modifizieren die Beschriftung der x- und y-Achse. Mit `legend_title=` wird der
Titel der Legende neu beschriftet.

```{code-cell}
fig = px.bar(anzahl_pro_marke, title='Autoscout24 (Zulassungsjahr 2020)')
fig.update_layout(
    xaxis_title='Marke',
    yaxis_title='Anzahl Autos',
    legend_title='Anzahl Autos pro Marke',
)
fig.show()
```

## Histogramm

Während Barplots in erster Linie kategoriale Daten visualisieren, dienen
Histogramme zur Darstellung numerischer Daten. Ein Barplot zeigt typischerweise
die Anzahl der Werte pro Kategorie. Bei numerischen Daten wäre eine solche
Darstellung oft nicht sinnvoll. Nehmen wir als Beispiel die Kilometerstände von
Autos. Wir lassen zuerst mit der Methode `.unique()` die verschiedenen
Kilometerstände bestimmen. Das Ergebnis ist ein sogenanntes NumPy-Array, das
hier wie eine Liste benutzt werden kann. Mit Hilfe der `len()`-Funktion können
wir die Anzahl der Einträge berechnen.

```{code-cell}
kilometerstaende = data['Kilometerstand (km)'].unique()
anzahl_kilometerstaende = len(kilometerstaende)
print(f'Es gibt {anzahl_kilometerstaende} verschiedene Kilometerstände.')
```

Mit über 10.000 verschiedenen Kilometerständen wäre eine direkte Visualisierung
nicht zielführend. Um dennoch eine sinnvolle Analyse durchzuführen, können wir
die Daten in Kategorien einteilen. Dazu bestimmen wir das Minimum und das
Maximum der Kilometerstände.

```{code-cell}
minimaler_kilometerstand = data['Kilometerstand (km)'].min()
maximaler_kilometerstand = data['Kilometerstand (km)'].max()

print(f'minimaler Kilometerstand: {minimaler_kilometerstand}')
print(f'maximaler Kilometerstand: {maximaler_kilometerstand}')
```

Die Daten reichen von Neuwagen (minimaler Kilometerstand 0 km) bis zu Autos mit
hohem Kilometerstand (maximaler Kilometerstand 435909 km). Wir können diesen
Bereich in gleichmäßige Kategorien unterteilen. Wählen wir beispielsweise 10
Kategorien, so würde die 1. Kategorie alle Autos mit einem Kilometerstand von 0
km bis 50000 km umfassen. Die 2. Kategorie geht dann von 50000 km bis 100000 km
usw. Um jetzt zu ermitteln, wie viele Autos in die jeweilige Kategorie fallen,
könnten wir ein kleines Python-Programm schreiben. Tatsächlich brauchen wir das
nicht, denn diese Funtkionalität ist bereits in der `histogram()`-Funktion
integriert, die auch die Visualisierung übernimmt.

Wir übergeben der Funktion als erstes Argument die Daten und als (optionales)
Argument, wie viele Kategorien wir uns wünschen. Die künstlich erfundenen
Kategorien werden auch als Bins (Tonnen) bezeichnet. Daher lautet das Argument
zum Setzen der Anzahl der Bins `nbins=`, so wie der englische Begriff »number of
bins«.

```{code-cell}
fig = px.histogram(data['Kilometerstand (km)'], nbins=10, 
    title='10 künstlich erzeugte Kategorien bzgl. des Kilometerstandes (km)')
fig.update_layout(
    xaxis_title='Kategorien der Kilometerstände (km)',
    yaxis_title='Anzahl Autos',
    legend_title='Anzahl Autos pro Kategorie',
)
fig.show()
```

Die meisten Autos haben weniger als 200000 km auf dem Kilometerzähler.

Ein charakteristisches Merkmal von Histogrammen ist, dass die Balken ohne Lücke
aneinander liegen, was die kontinuierliche Natur der numerischen Daten
widerspiegelt. Die Anzahl der Kategorien (Bins) beeinflusst die Darstellung
maßgeblich und sollte sorgfältig gewählt werden. Auch können die
Histogramm-Kategorien nicht in eine andere Reihenfolge gebracht werden.

Die Anzahl der Kategorien ist ein sehr wichtiger Faktor bei der Visualisierung.
Werden zu wenige Kategorien gewählt, werden auch nicht die Unterschiede
sichtbar. Werden zu viele Kategorien gewählt, sind ggf. einige Kategorien leer.

```{admonition} Mini-Übung
:class: miniexercise
Wählen Sie verschiedene Werte für die Anzahl der Kategorien aus. Welche Anzahl
an Kategorien ist für diesen Datensatz sinnvoll und warum?
```

Zusammenfassend wird ein Histogramm folgendermaßen beschrieben.

```{admonition} Was ist ... ein Histogramm?
:class: note
Ein Histogramm ist eine grafische Darstellung, bei der numerische Daten in
Kategorien eingeteilt und dann die Anzahl der Werte pro Kategorie durch die Höhe
eines Balkens dargestellt wird
```

## Zusammenfassung und Ausblick

In diesem Kapitel wurden zwei wichtige Diagrammtypen vorgestellt: der Barplot
und das Histogramm. Obwohl beide mit Rechtecken arbeiten, haben sie
unterschiedliche Anwendungsbereiche und sollten nicht verwechselt werden.
Während der Barplot ideal für kategoriale Daten ist, eignet sich das Histogramm
zur Visualisierung numerischer Daten. Im nächsten Kapitel widmen wir uns dem
Thema Datenfilterung.
