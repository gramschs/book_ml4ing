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

# 8.2 Kodierung und Skalierung

```{admonition} Warnung
:class: warning
Warnung: Dieser Abschnitt wird gerade überarbeitet.
```

TODO

## Lernziele

```{admonition} Lernziele
:class: goals
* TODO
```

## Kategoriale Daten müssen numerisch werden

Bei den Beispielen zur linearen Regression und zu Entscheidungsbäumen (Decision
Trees) haben wir zur Prognose des Verkaufspreise nur numreische Daten genutzt.
Beispielsweise haben wir bei der Klassifikation, ob ein Auto bei einer
Verkaufsaktion verkaufbar ist oder nicht, den Preis und den Kilometerstand als
Merkmal zur Prognose genutzt. Bei den linearen Regressionsproblemen ging es
darum, aufgrund des Kilometerstandes des Autos einen Verkaufspreis zu
prognostizieren. Dabei gibt es einige andere Eigenschaften von Autos, die
sicherlich ebenfalls Einfluss auf die Kaufentscheidung haben. Beispielsweise ist
für viele Autofahrer wichtig, ob das Auto mit Diesel oder Benzin fährt und auch
die Marke beinflusst die Kaufentscheidung.

Wir laden einen Datensatz mit Verkaufsdaten der Plattform
[Autoscout24.de](https://www.autoscout24.de). Sie können die csv-Datei hier
herunterladen {download}`Download autoscout24_kodierung.csv
<https://gramschs.github.io/book_ml4ing/data/autoscout24_kodierung.csv>` und in
das Jupyter Notebook importieren. Alternativ können Sie die csv-Datei auch über
die URL importieren, wie es in der folgenden Code-Zelle gemacht wird.

```{code-cell}
import pandas as pd 

url = 'https://gramschs.github.io/book_ml4ing/data/autoscout24_kodierung.csv'
data = pd.read_csv(url)

data.info()
```
