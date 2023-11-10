---
jupytext:
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

# 7.1 Datenvorverarbeitung

Realistische Datensätze sind oft unvollständig. In einer Umfrage hat eine Person
mit einer Frage nichts anfangen können und daher nichts angekreuzt. Ein
Messsensor an der Produktionsanlage ist abends ausgefallen, was erst am nächsten
Morgen bemerkt wurde. Die Mitarbeitenden einer Arztpraxis sind im Urlaub und
lassen die Meldung der verabreichten Impfungen noch bis nach dem Urlaub liegen.
Es gibt viele Gründe, warum Datensätze unvollständig sind. In diesem Abschnitt
beschäftigen eir uns damit, fehlende Daten aufzuspüren und lernen einfache
Methoden kennen, damit umzugehen.

## Lernziele

```{admonition} Lernziele
:class: important
* Sie können in einer großen Datensammlung mit **isnull()** fehlende Daten aufspüren.
* Sie können Daten gezielt mit **drop()** löschen.
* Sie können fehlende Daten mit **fillna()** ersetzen.
* Sie wissen, dass es nicht eine *einzige* Strategie zum Umgang mit fehlenden Daten 
gibt, sondern von Projekt zu Projekt entschieden werden muss.
```

+++

## Fehlende Daten aufspüren mit isnull()

Ein erstes Beispiel eines unvollständigen Datensatzes haben wir bereits im
letzten Kapitel kennengelernt. Wir laden erneut die Tabelle mit den
Gebrauchtwagenpreisen der Jahre 2011 bis 2021.

```{code-cell} ipython3
import pandas as pd

data_raw = pd.read_csv('data/autoscout24-germany-dataset.csv')
data_raw.info()
```

Wir hatten bereits festgestellt, dass die Anzahl der 'non-null'-Einträge für die
verschiedenen Merkmale unterschiedlich ist. Offensichtlich ist bei manchen
Angeboten die Eigenschaft 'model' nicht angegeben worden. Welche das sind,
können wir mit der Methode `isnull()` bestimmen. Die Methode liefert ein Array
zurück, das True/False-Werte enthält. True steht dabei dafür, dass ein Wert
fehlt bzw. mit dem Eintrag 'NaN' gekennzeichnet ist (= not a number). Weitere
Details finden Sie in der [Pandas-Dokumentation →
isnull](https://pandas.pydata.org/docs/reference/api/pandas.isnull.html).

Dieses boolesche Array können wir dann wiederum als Filter einsetzen.

```{code-cell} ipython3
filter = data_raw.loc[:, 'model'].isnull() == True
data_raw.loc[filter, :].head(20)
```

Scheinbar fehlt die Modellangabe häufig, wenn das Fahrzeug mit Gas betrieben
wird. Dem müssten wir systematisch nachgehen. Sind das vielleicht umgebaute
Fahrzeuge und fehlt deshalb die Modellangabe? Wie oft kommen gasbetriebene
Fahrzeuge überhaupt im kompletten Datensatz vor? Und wie häufig in dem Datensatz
mit den unvollständigen Angaben? Wir wenden uns aber zunächst dem Löschen der
Daten zu.

## Löschen mit drop()

Im letzten Kapitel haben wir einfach alle Datensätze gelöscht, in denen Daten
gefehlt haben — sozusagen die Brute-Force-Methode. Wenn wir uns mehr Zeit für
die Datenvorverarbeitung nehmen, können wir aber auch filigraner vorgehen.
Beispielsweise könnten wir beschließen, dass uns das Modell als Eigenschaft
nicht so wichtig ist und somit die Spalte löschen.

Dazu verwenden wir die `drop()`-Methode. Standardmäßig löscht `drop()` jedoch
Zeilen. Mit der Option `columns=` können wir spaltenweise löschen, wie Sie in
der [Pandas-Dokumentation →
drop](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop.html)
nachlesen können.

```{code-cell} ipython3
data_raw = data_raw.drop(columns='model')
```

## Ersetzen mit fillna()

Auch bei den Angaben zur Schaltung fehlen Einträge. Zum Beispiel die Zeile mit
dem Index 243 ist unvollständig.

```{code-cell} ipython3
print(data_raw.loc[243, :])
```

Diesmal entscheiden wir uns dazu, diese Eigenschaft nicht wegzulassen.
ML-Verfahren brauchen aber immer einen gültigen Wert und nicht NaN. Wir ersetzen
die fehlenden Werte durch den Eintrag 'not defined'. Genausogut könnten wir auch
'keine Angabe' oder 'nada' oder was auch immer nehmen. Dazu benutzen wir die
Methode `fillna()` (siehe [Pandas-Dokumentation →
fillna](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.fillna.html)).

```{code-cell} ipython3
data_raw.loc[:, 'gear'] = data_raw.loc[:, 'gear'].fillna(value='not defined')
```

Wenn wir uns jetzt noch einmal Zeile 243 ansehen, sehen wir, dass `fillna()`
funktioniert hat.

```{code-cell} ipython3
print(data_raw.loc[243,:])
```

Bei den PS-Zahlen haben wir ebenfalls nicht vollständige Daten vorliegen.
Diesmal haben wir nicht diskrete Werte wie 'Schaltwagen' oder 'Automatik',
sondern numerische Werte. Daher bietet es sich hier eine zweite Methode der
Ersetzung an. Wenn wir überall da, wo wir keine PS-Zahlen vorliegen haben, den
Mittelwert der vorhandenen PS-Zahlen einsetzen, machen wir zumindest den
Mittelwert des gesamten Datensatzes nicht kaputt. Besser wäre natürlich zu
versuchen, die fehlenden Daten zu recherchieren. Oder aber mittels linearer
Regression die fehlenden Werte zu schätzen und dann zu ergänzen. Als erste
Näherung nehmen wir jetzt den Mittelwert der vorhandenen Daten.

```{code-cell} ipython3
mittelwert = data_raw.loc[: , 'hp'].mean()
print('Der Mittelwert der vorhandenen PS-Zahlen ist: {:.2f}'.format(mittelwert))

data_raw.loc[:, 'hp'] = data_raw.loc[:, 'hp'].fillna(mittelwert)
```

## Zusammenfassung

Ein wichtiger Teil eines ML-Projektes beschäftigt sich mit der Aufbereitung der
Daten für die ML-Algorithmen. Dabei ist es nicht nur wichtig, in großen
Datensammlungen fehlende Einträge aufspüren zu können, sondern ein Gespür dafür
zu entwickeln, wie mit den fehlenden Daten angesetzt werden sollen. Die
Strategien hängen dabei von der Anzahl der fehlenden Daten und ihrer Bedeutung
ab. Häufig werden unvollständige Daten aus der Datensammlung gelöscht oder
numerische Einträge durch den Mittelwert der vorhandenen Daten ersetzt.
