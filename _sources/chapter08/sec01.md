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

# 8.1 Fehlende Daten

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
:class: goals
* Sie können in einem Datensatz mit **isnull()** fehlende Daten aufspüren und
  analysieren.
* Sie kennen die beiden grundlegenen Strategien, mit fehlenden Daten umzugehen:
  * **Elimination** (Löschen) und
  * **Imputation** (Vervollständigen).
* Sie können Daten gezielt mit **drop()** löschen.
* Sie können fehlende Daten mit **fillna()** ersetzen.
```

## Fehlende Daten aufspüren mit isnull()

Wir arbeiten im Folgenden mit einem echten Datensatz der Verkaufsplattform
[Autoscout24.de](https://www.autoscout24.de), der Verkaufsdaten zu 1000 Autos
enthält. Sie können die csv-Datei hier herunterladen {download}`Download
autoscout24_fehlende_daten.csv
<https://gramschs.github.io/book_ml4ing/data/autoscout24_fehlende_daten.csv>`
und in das Jupyter Notebook importieren. Alternativ können Sie die csv-Datei
auch über die URL importieren, wie es in der folgenden Code-Zelle gemacht wird.

```{code-cell}
import pandas as pd

url = 'https://gramschs.github.io/book_ml4ing/data/autoscout24_fehlende_daten.csv'
daten = pd.read_csv(url)

daten.info()
```

Wir hatten bereits festgestellt, dass die Anzahl der `non-null`-Einträge für die
verschiedenen Merkmale unterschiedlich ist. Offensichtlich ist nur bei 963 Autos
eine »Farbe« eingetragen und die »Leistung (PS)« ist nur bei 988 Autos gültig.
Am wenigsten gültige Einträge hat das Merkmal »Verbrauch (l/100 km)«, wohingegen
bei der Eigenschaft »Kilometerstand (km)« nur ein ungültiger Eintrag auftaucht.
Welche Einträge ungültig sind, können wir mit der Methode `isnull()` bestimmen.
Die Methode liefert ein Pandas DataFrame zurück, das True/False-Werte enthält.
True steht dabei dafür, dass ein Wert fehlt bzw. mit dem Eintrag `NaN`
gekennzeichnet ist (= not a number). Weitere Details finden Sie in der
[Pandas-Dokumentation →
isnull()](https://pandas.pydata.org/docs/reference/api/pandas.isnull.html).

```{code-cell}
daten.isnull()
```

Bereits in der zweiten Zeile befindet sich ein Auto, bei dem das Merkmal
»Verbrauch (l/100 km)« nicht gültig ist (ggf. müssen Sie weiter nach rechts
scrollen), den dort steht `True`. Wir betrachten uns diesen Eintrag:

```{code-cell}
daten.loc[1,:]
```

Bei dem Auto handelt es sich um einen Hybrid, vielleicht wurde deshalb der
»Verbrauch (l/100 km)« nicht angegeben. Ist das vielleicht auch bei den anderen
Autos der Grund? Wir speichern zunächst die isnull()-Datenstruktur in einer
eigenen Variable ab und ermitteln zunächst, wie viele Autos keinen gültigen
Eintrag bei diesem Merkmal haben. Dazu nutzen wir aus, dass der boolesche Wert
`False` bei Rechnungen als 0 interpretiert wird und der boolesche Wert `True`
als 1. Die Methode `.sum()` summiert pro Spalte alle Werte, so dass sie direkt
die Anzahl der ungültigen Werte pro Spalte liefert.

```{code-cell}
fehlende_daten = daten.isnull()

fehlende_daten.sum()
```

Jetzt lassen wir uns diese 108 Autos anzeigen, bei denen ungültige Werte beim
»Verbrauch (l/100 km)« angegeben wurden. Dazu nutzen wir die True-Werte in der
Spalte `Verbrauch (l/100 km)` als Filter für den ursprünglichen Datensatz.
Zumindest die ersten 20 Autos lassen wir uns dann mit der `.head(20)`-Methode
anzeigen.

```{code-cell}
autos_mit_fehlendem_verbrauch_pro_100km = daten[ fehlende_daten['Verbrauch (l/100 km)'] == True ]
autos_mit_fehlendem_verbrauch_pro_100km.head(20)
```

Bemerkung: Der Vergleich `== True` ist redundant und kann auch weggelassen werden.

Beim Kraftstoff werden alle möglichen Angaben gemacht: Hybrid, Benzin, Diesel
und Elektro. Wir müssten jetzt systematisch den fehlenden Angaben nachgehen. Für
Elektrofahrzeuge und ggf. Hybridautos ist die Angabe »Verbrauch (l/ 100 km)«
unsinnig. Aber das zweite Auto mit der Nr. 5 wird mit Benzin betrieben, da
scheint Nachlässigkeit beim Ausfüllen der Merkmale vorzuliegen. Beim fünften
Auto mit der Nr. 77 ist zwar der »Verbrauch (l/100 km)« nicht angegeben, aber
dafür der »Verbrauch (g/km)«. Daraus könnten wir den »Verbrauch (l/100 km)«
abschätzen und den fehlenden Wert ergänzen. Es gibt verschiedene Strategien, mit
fehlenden Daten umzugehen. Die beiden wichtigsten Verfahren zum Umgang mit
fehlenden Daten sind

1. Löschen (Elimination) und
2. Vervollständigung (Imputation).

Bei Elimination werden Datenpunkte (Autos) und/oder Merkmale gelöscht. Bei
Imputation (Vervollständigung) werden die fehlenden Werte ergänzt. Beide
Verfahren werden wir nun etwas detaillierter betrachten.

## Löschen (Elimination) mit drop()

Bei der Elimination (Löschen) können wir filigran vorgehen oder die
Holzhammer-Methode verwenden. Beispielsweise könnten wir entscheiden, das
Merkmal »Verbrauch (l/100 km)« komplett zu löschen und einfach nur den
»Verbrauch (g/km)« zu berücksichtigen. Aber ein kurzer Blick auf die Daten hatte
ja bereits gezeigt, dass diese Werte auch nur unzuverlässig gefüllt waren, auch
wenn sie technisch gültig sind. Wir löschen beide Merkmale. Dazu benutzen wir
die Methode `drop()` mit dem zusätzlichen Argument `columns=['Verbrauch (l/
100 km)', 'Verbrauch (g/km)']`. Da wir gleich zwei Spalten aufeinmal eliminieren
möchten, müssen wir die Spalten (Columns) als Liste übergeben. Danach überprüfen
wir mit der Methode `.info()`, ob das Löschen geklappt hat.

```{code-cell}
daten.drop(columns=['Verbrauch (l/100 km)', 'Verbrauch (g/km)'])
daten.info()
```

Leider hat der Befehl `drop()` nicht funktioniert! Was ist da los? Python und
Pandas verfolgen das Programmierparadigma »Explizit ist besser als implizit!«
Daher werden zwar werden durch den `drop()`-Befehl die beiden Spalten gelöscht,
aber der Datensatz `daten` selbst bleibt aus Sicherheitsgründen unverändert.
Möchten wir den Datensatz mit den gelöschten Merkmalen weiter verwenden, müssen
wir ihn in einer neuen Variable speichern oder die alte Variable `daten` damit
überschreiben. Wir nehmen eine neue Variable namens `daten_ohne_verbrauch`.

```{code-cell}
daten_ohne_verbrauch = daten.drop(columns=['Verbrauch (l/100 km)', 'Verbrauch (g/km)'])
daten_ohne_verbrauch.info()
```

Ein weiterer Datenpunkt weist einen ungültigen Eintrag für den »Kilometerstand
(km)« auf. Schauen wir zunächst nach, um welches Auto es sich handelt.

```{code-cell}
daten_ohne_verbrauch[ daten_ohne_verbrauch['Kilometerstand (km)'].isnull() ]
```

Bei den Einträgen des Autos sind noch mehr Probleme ersichtlich. Die
Erstzulassung war sicherlich nicht bei 37.500 km und das Jahr ist nicht 12/2020.
Wir können jetzt diesen Datenpunkt löschen oder den Datenpunkt reparieren.
Zunächst einmal der Code zum Löschen des Datenpunktes. Standardmäßig löscht die
`drop()`-Methode ohnehin Zeilen, also Datenpunkte, so dass wir ohne weitere
Optionen den Index der zu löschenden Datenpunkte angeben. Diesmal verwenden wir
die alte Variable um den reduzierten Datensatz zu speichern.

```{code-cell}
daten_ohne_verbrauch = daten_ohne_verbrauch.drop(708)
daten_ohne_verbrauch.info()
```

Wie Sie in der [Dokumentation Scikit-Learn →
drop()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop.html)
nachlesen können, gibt es zum expliziten Überschreiben der alten Variable auch
die Alternative, die Option `inplace=True` zu setzen. Welche Option Sie nutzen,
ist Geschmackssache.

Ob alle Angaben plausibel sind, ist nicht gesagt. Bei dem Peugeot mit dem Index
708 hatten wir ja gesehen, dass bei der Erstzulassung eine Kilometerangabe
stand. Tatsächlich gab es bereits erste Hinweise darauf, dass manche Werte
technisch gültig, aber nicht plausibel sind. Die Spalte mit dem Jahr
beispielsweise wurde beim Import als Datentyp Object klassifiziert. Zu erwarten
wäre jedoch der Datentyp Integer gewesen. Schauen wir noch einmal in den
ursprünglichen Datensatz hinein.

```{code-cell}
daten['Jahr'].unique()
```

Da bei dem Peugeot mit dem Index 708 das Jahr fälschlicherweise mit `12/2020`
angegeben wurde, hat dieser eine Text-Eintrag dazu geführt, dass die komplette
Spalte als Object klassifiziert wurde und nicht als Integer. Daher müssen stets
weitere Plausibilitätsprüfungen durchgeführt werden, bevor die Daten genutzt
werden, um statistische Aussagen zu treffen oder ein ML-Modell zu trainieren.

## Vervollständigung (Imputation) mit fillna()

Auch bei den Angaben zur Farbe fehlen Einträge. Zum Beispiel die Zeile mit
dem Index 2 ist unvollständig.

```{code-cell}
daten_ohne_verbrauch.loc[2, :]
```

Diesmal entscheiden wir uns dazu, diese Eigenschaft nicht wegzulassen.
ML-Verfahren brauchen aber immer einen gültigen Wert und nicht `NaN`. Wir müssen
daher den fehlenden Wert ersetzen. Eine Möglichkeit ist, eine Farbe zu erfinden,
z.B. 'bunt', oder die fehlenden Werte explizit durch einen Eintrag 'keine
Angabe' zu vervollständigen. Dazu benutzen wir die Methode `fillna()` (siehe
[Pandas-Dokumentation →
fillna](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.fillna.html)).
Die Vervollständigung soll nur die NaN-Werte der Spalte »Farbe« füllen. Daher
filtern wir zuerst diese Spalte und wenden darauf die `fillna()`-Methode an. Das
erste Argument der `fillna()`-Methode ist der Wert, durch den die NaN-Werte
ersetzt werden sollen (hier `'keine Angabe'`). Damit die Verwollständigung
explizit gespeichert wird, überschreiben wir die Spalte.

```{code-cell}
daten_ohne_verbrauch['Farbe'] = daten_ohne_verbrauch['Farbe'].fillna('keine Angabe')

# Kontrolle der Vervollständigung
daten_ohne_verbrauch.isnull().sum()
```

Wenn wir uns jetzt noch einmal die dritte Zeile ansehen, sehen wir, dass
`fillna()` funktioniert hat.

```{code-cell} ipython3
daten_ohne_verbrauch.loc[2,:]
```

Bei den PS-Zahlen haben wir ebenfalls nicht vollständige Daten vorliegen.
Diesmal haben wir nicht kategoriale Daten wie die Farben, sondern numerische
Werte. Daher bietet es sich hier eine zweite Methode der Ersetzung (Imputation)
an. Wenn wir überall da, wo wir keine PS-Zahlen vorliegen haben, den Mittelwert
der vorhandenen PS-Zahlen einsetzen, machen wir zumindest den Mittelwert des
gesamten Datensatzes nicht kaputt. Wir berechnen daher zuerst den Mittelwert mit
der Methode `.mean()` und nutzen dann die `fillna()`-Methode.

```{code-cell}
mittelwert = daten_ohne_verbrauch['Leistung (PS)'].mean()
print(f'Der Mittelwert der vorhandenen Einträge »Leistung (PS)« ist: {mittelwert:.2f}')

daten_ohne_verbrauch['Leistung (PS)'] = daten_ohne_verbrauch['Leistung (PS)'].fillna(mittelwert)

# Kontrolle
daten_ohne_verbrauch.isnull().sum()
```

Besser wäre natürlich zu versuchen, die fehlenden Daten zu recherchieren. Oder
aber mittels linearer Regression die fehlenden Werte zu schätzen und dann zu
ergänzen. Als erste Näherung nehmen wir jetzt den Mittelwert der vorhandenen
Daten.

## Zusammenfassung

Ein wichtiger Teil eines ML-Projektes beschäftigt sich mit der Aufbereitung der
Daten für die ML-Algorithmen. Dabei ist es nicht nur wichtig, in großen
Datensammlungen fehlende Einträge aufspüren zu können, sondern ein Gespür dafür
zu entwickeln, wie mit den fehlenden Daten angesetzt werden sollen. Die
Strategien hängen dabei von der Anzahl der fehlenden Daten und ihrer Bedeutung
ab. Häufig werden unvollständige Daten aus der Datensammlung gelöscht oder
numerische Einträge durch den Mittelwert der vorhandenen Daten ersetzt.
