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

# 3.2 Statistik mit Pandas

Pandas dient nicht nur dazu, Daten zu sammeln, sondern ermöglicht auch
statistische Analysen. Die deskriptive Statistik hat zum Ziel, Daten durch
einfache Kennzahlen und Diagramme zu beschreiben. In diesem Kapitel geht es
darum, die wichtigsten statistischen Kennzahlen mit Pandas zu ermitteln und zu
interpretieren.

## Lernziele

```{admonition} Lernziele
:class: goals
* Sie können sich mit **.describe()** eine Übersicht über statistische Kennzahlen
  verschaffen.
* Sie wissen, wie Sie die Anzahl der gültigen Einträge mit **.count()** ermitteln.
* Sie kennen die statistischen Kennzahlen Mittelwert und Standardabweichung und
  wissen, wie diese mit **.mean()** und **.std()** berechnet werden.
* Sie können das Minimum und das Maximum mit **.min()** und **.max()** bestimmen.
* Sie wissen wie ein Quantil interpretiert wird und wie es mit **.quantile()**
  berechnet wird.
```

## Schnelle Übersicht mit .describe()

Die Methode `.describe()` aus dem Pandas-Modul liefert eine schnelle Übersicht
über viele statistische Kennzahlen. Vor allem, wenn neue Daten geladen werden,
sollte diese Methode direkt am Anfang angewendet werden. Wir bleiben bei unserem
Beispiel mit den zehn Autos und deren Verkaufspreisen.

```{code-cell}
# Import des Pandas-Moduls 
import pandas as pd

# Erzeugung der Daten als Series-Objekt
preisliste = [1999, 35990, 17850, 46830, 27443, 14240, 19950, 15950, 21990, 12450]
autos = ['Audi Nr. 1', 'Audi Nr. 2', 'Audi Nr. 3', 'BMW Nr. 1', 'BMW Nr. 2', 'Citroen Nr. 1', 'Citroen Nr. 2', 'Citroen Nr. 3', 'Citroen Nr. 4', 'Citroen Nr. 5']
preise = pd.Series(preisliste, index = autos)
```

Die Anwendung der `.describe()`-Methode liefert folgende Ausgabe:

```{code-cell}
preise.describe()
```

Offensichtlich liefert die Methode `.describe()` acht statistische Kennzahlen,
deren Bedeutung in der
[Pandas-Dokumentation](https://pandas.pydata.org/docs/reference/api/pandas.Series.describe.html)
erläutert wird. Wir gehen im Folgenden jede Kennzahl einzeln durch.

Aber was machen wir, wenn wir die statistischen Kennzahlen erst später verwenden
wollen, können wir sie zwischenspeichern? Probieren wir es aus.

```{code-cell}
statistische_kennzahlen = preise.describe()
```

Es kommt keine Fehlermeldung. Und was ist in der Variable
`statistische_kennzahlen` nun genau gespeichert, welcher Datentyp?

```{code-cell}
type(statistische_kennzahlen)
```

Offensichtlich wird durch das Anwenden der `.describe()`-Methode auf das
Series-Objekt `preise` ein neues Series-Objekt erzeugt, in dem wiederum die
statistischen Kennzahlen von `preise` gespeichert sind. Da wir im letzten
Kapitel schon gelernt haben, dass mit eckigen Klammern und dem Index auf einen
einzelnen Wert zugegriffen werden kann, können wir uns so den minimalen
Verkaufspreis ausgeben lassen:

```{code-cell}
minimaler_preis = statistische_kennzahlen['min']
print(f'Das billigste Auto wird für {minimaler_preis} EUR angeboten.')
```

```{admonition} Mini-Übung
:class: miniexercise
Lassen Sie zuerst die Verkaufspreise aufsteigend sortieren und ausgeben. Lesen
Sie anhand der Ausgabe ab: welches Auto ist am teuersten und für wieviel Euro
wird es bei Autoscout24 angeboten? Lassen Sie dann das Maximum über die
statistischen Kennzahlen, d.h. mit .describe() ermitteln. Vergleichen Sie beide
Werte.
```

```{code-cell}
# Hier Ihr Code
```

````{admonition} Lösung
:class: minisolution, toggle
Der folgende Code sortiert die Preise aufsteigend und lässt sie anzeigen:
```python
preise_aufsteigend = preise.sort_values()
print('Preise aufsteigend sortiert: ')
print(preise_aufsteigend)
```
Das teuerste Auto ist der BMW Nr. 1. Er wird für 46830 EUR angeboten. Jetzt wird der maximale Preise über die .describe()-Methode ermittelt.
```python
statistische_kennzahlen = preise.describe()
maximaler_preis = statistische_kennzahlen['max']
print(f'Maximaler Preis mit .describe() ermittelt: {maximaler_preis}')
```
````

Neben der Möglichkeit, die statistischen Kennzahlen über .describe() berechnen
zu lassen und dann mit dem expliziten Index darauf zuzugreifen, gibt es auch
Methoden, um die statistischen Kennzahlen direkt zu ermitteln.

## Anzahl count()

Mit `.count()` wird die Anzahl der Einträge bestimmt, die *nicht* 'NA' sind. Der
Begriff 'NA' ist ein Fachbegriff des maschinellen Lernens. Gemeint sind fehlende
Einträge, wobei die fehlenden Einträge verschiedene Ursachen haben können:

* NA = not available (der Messsensor hat versagt)
* NA = not applicable (es ist sinnlos bei einem Mann nachzufragen, ob er
  schwanger ist)
* NA = no answer (eine Person hat bei dem Umfrage nichts angegeben)

```{code-cell}
anzahl_gueltige_preise = preise.count()
print(f'Im Series-Objekt sind {anzahl_gueltige_preise} nicht NA-Werte, also gültige Datensätze gespeichert.')
```

## Mittelwert mean()

Der Mittelwert ist die Summe aller Elemente geteilt durch ihre Anzahl. Wie
praktisch, dass wir mit .count() schon die Anzahl der gültigen Werte geliefert
bekommen. Rechnen wir zuerst einmal "händisch" nach, was der durchschnittliche
Verkaufspreis der 10 Autos ist.

```{code-cell}
preisliste = [1999, 35990, 17850, 46830, 27443, 14240, 19950, 15950, 21990, 12450]
summe = 1999 + 35990 + 17850 + 46830 + 27443 + 14240 + 19950 + 15950 + 21990 + 12450
print(f'Die Summe ist {summe} EUR.')
mittelwert = summe / 10
print(f'Der durchschnittliche Verkaufspreis ist {mittelwert} EUR.')
```

Mittelwert heißt auf Englisch mean. Daher ist es nicht verwunderlich, dass die
Methode `.mean()` den Mittelwert der Einträge in jeder Spalte berechnet.

```{code-cell}
mittelwert = preise.mean()
print(f'Der mittlere Verkaufspreis beträgt {mittelwert} Euro.')
```

Falls Sie prinzipiell nochmal die Berechnung des Mittelwertes wiederholen
wollen, können Sie folgendes Video ansehen.

```{dropdown} Video zu "Mittelwert" von Datatab
<iframe width="560" height="315" src="https://www.youtube.com/embed/IKfsGPwACnU" 
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; 
clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
```

## Standardabweichung std()

Der Mittelwert ist eine sehr wichtige statistische Kennzahl. Allerdings verrät
der Mittelwert nicht, wie sich die einzelnen Autopreise relativ zum Mittelwert
verhalten. Bei den 10 Autos sehen wir mit einem Blick, dass einzelne Autos sehr
stark vom Mittelwert abweichen. Audi Nr. 1 kostet nur 1999 EUR und damit nur
circa 10 % vom durchschnittlichen Verkaufspreis. Dafür ist BMW Nr. 1 mehr als
doppelt so teuer. Es ist daher wichtig, sich zusätzlich zum Mittelwert
anzusehen, wie die anderen Datenpunkte vom Mittelwert abweichen. In der
Statistik wird das als **Streuung** bezeichnet. Eine statistische Kennzahl, die
die Streuung von Daten um den Mittelwert angibt, ist die **Standardabweichung**.

Zur Berechnung der Standardabweichung werden zuerst die Abweichungen jedes
Datenpunktes zum Mittelwert berechnet.

```{code-cell}
mittelwert = preise.mean()
differenzen = preise - mittelwert
print(differenzen)
```

Die negativen Vorzeichen stören, wir wollen ja die Abweichung. Daher quadrieren
wir die Differenzen.

```{code-cell}
quadrate = differenzen * differenzen
print(quadrate)
```

Die durchschnittliche Abweichung beschreibt nun, wie weit "weg" die anderen
Verkaufspreise vom Mittelwert sind. Daher bilden wir nun von den Abweichungen
wiederum den Mittelwert. Da Quadrate ein Series-Objekt ist, machen wir das
diesmal nicht händisch, sondern nutzen die Methode `.mean()`.

```{code-cell}
durchschnittliche_abweichungen = quadrate.mean()
print(f'Die durchschnittliche Abweichung ist {durchschnittliche_abweichungen}.')
```

Wenn wir die durchschnittliche Abweichung wiederum als Verkaufspreis gemessen in
Euro interpretieren wollen, gibt es ein Problem. Offensichtlich ist diese Zahl
soviel größer als das teuerste Auto. Das ist nicht verwunderlich, denn wir haben
ja die quadrierten Differenzen genommen. Die Einheit der durchschnittlichen
Abweichung ist also EUR². Das ist aber unpraktisch. Also ziehen wir wieder die
Wurzel, damit wir ein Maß für die durchschnittliche Abweichung haben, das auch
direkt Verkaufspreise widerspiegelt. Das nennen wir dann Standardabweichung.

```{code-cell}
standardabweichung = quadrate.mean()**0.5
print(f'Die Standardabweichung ist {standardabweichung:.2f} EUR.')
```

Benutzen wir Pandas, so liefert die Methode `.std()` die Standardabweichung. Das
'st' in `.std()` für Standard steht, ist nachvollziehbar. Der dritte Buchstabe
'd' kommt von 'deviation', also Abweichung. Somit ist wiederum die Methode nach
dem englischen Fachbegriff 'standard deviation' benannt. Probieren wir die
Methode für die Autopreise aus.

```{code-cell}
standardabweichung = preise.std()
print(f'Die Standardabweichung bei den Verkaufspreisen beträgt {standardabweichung} Euro.')
```

Der Wert, den Pandas berechnet, unterscheidet sich von dem Wert, den wir
"händisch" berechnet haben. Der Unterschied kommt daher, dass es zwei Formeln
zur Berechnung der Standardabweichung gibt. Einmal wird der Durchschnitt über
die Quadrate gebildet, indem die Summe durch die Anzahl aller Elemente geteilt
wird, so wie wir es getan haben. Wir haben durch 10 geteilt. Bei der anderen
Formel wird die Summe der Quadrate durch 9 geteilt.

Was war eigentlich nochmal die Standardabweichung? Falls Sie dazu eine kurze
Wiederholung der Theorie benötigen, empfehle ich Ihnen dieses Video.

```{dropdown} Video zu "Standardabweichung" von Datatab
<iframe width="560" height="315" src="https://www.youtube.com/embed/QNNt7BvmUJM" 
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; 
clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
```

## Minimum und Maximum mit min() und max()

Die Namen der Methoden `.min()` und `max()` sind fast schon wieder
selbsterklärend. Die Methode `.min()` liefert den kleinsten Wert zurück, der
gefunden wird. Umgekehrt liefert `.max()` den größten Eintrag. Wie häufig die
minimalen und maximalen Werte vorkommen, ist dabei egal. Es kann durchaus sein,
dass das Minimum oder das Maximum mehrfach vorkommt.

Schauen wir uns an, was der niedrigste Verkaufspreis ist. Und dann schauen wir
nach, welches Auto am teuersten ist.

```{code-cell}
preis_min = preise.min()
print(f'Das billigste oder die billigsten Autos werden zum Preis von {preis_min} EUR angeboten.')

preis_max = preise.max()
print(f'Das teuerste oder die teuersten Autos werden für {preis_max} EUR angeboten.')
```

## Quantil mit quantile()

Das Quantil $p \%$ ist der Wert, bei dem $p %$ der Einträge kleiner oder gleich
als diese Zahl sind und $100 \% - p \%$ sind größer. Meist werden nicht
Prozentzahlen verwendet, sondern p ist zwischen 0 und 1, wobei die 1 für 100 %
steht.

Angenommen, wir würden gerne das 0.5-Quantil (auch Median genannt) der Preise
wissen. Mit der Methode `.quantile()` können wir diesen Wert leicht aus den
Daten holen.

```{code-cell}
quantil50 =preise.quantile(0.5)
print(f'Der Median, d.h. das 50 % Quantil, liegt bei {quantil50} EUR.')
```

Das 50 % -Quantil liegt bei 18900 EUR. 50 % aller Autos werden zu einem Preis
angeboten, der kleiner oder gleich 18900 EUR ist. Und 50 % aller Autos werden
teuer angeboten. Wir schauen uns jetzt das 75 % Quantil an.

```{code-cell}
quantil75 = preise.quantile(0.75)
print(f'75 % aller Autos haben einen Preis kleiner gleich {quantil75} EUR.')
```

75 % aller Autos werden günstiger als 26079.75 EUR angeboten. Auch wenn Sie sich
natürlich für jede beliebigen Prozentsatz zwischen 0 % und 100 % das Quantil
ansehen können, interessieren wir uns noch für das 25 % Quantil.

```{code-cell}
quantil25 = preise.quantile(0.25)
print(f'25 % aller Autos haben einen Preis kleiner gleich {quantil25} EUR.')
```

## Zusammenfassung und Ausblick

In diesem Abschnitt haben wir uns mit einfachen statistischen Kennzahlen
beschäftigt, die Pandas mit der Methode `.describe()` zusammenfasst, die aber
auch einzeln über

* `.count()`
* `.mean()`
* `.std()`
* `.min()` und `.max()`
* `.quantile()`

berechnet und ausgegeben werden können. Im nächsten Kapitel geht es darum, durch
Diagramme mehr über die Daten zu erfahren.
