---
jupytext:
  formats: ipynb,md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.7
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

# 3.2 Statistik mit Pandas

Pandas dient nicht nur dazu, Daten zu sammeln, sondern ermöglicht auch statistische Analysen. Die deskriptive Statistik hat zum Ziel, die Daten durch Kennzahlen und Diagramme zu beschreiben. In diesem Kapitel geht es darum, die wichtigsten statistischen Kennzahlen mit Pandas zu ermitteln und zu interpretieren. 


## Lernziele

```{admonition} Lernziele
:class: important
* Sie können sich mit **describe** eine Übersicht über statistische Kennzahlen
  verschaffen.
* Sie wissen, wie Sie die Anzahl der gültigen Einträge mit **count** ermitteln.
* Sie kennen die statistischen Kennzahlen Mittelwert und Standardabweichung und
  wissen, wie diese mit **mean** und **std** berechnet werden.
* Sie können das Minimum und das Maximum mit **min** und **max** bestimmen.
* Sie wissen wie ein Quantil interpretiert wird und wie es mit **quantile**
  berechnet wird.
```


## Schnelle Übersicht mit .describe()

Die Methode `.describe()` aus dem Pandas-Modul liefert eine schnelle Übersicht
über viele statistische Kennzahlen. Vor allem, wenn neue Daten geladen werden,
sollte diese Methode direkt am Anfang angewendet werden. Wir bleiben bei unserem
Beispiel mit den zehn Autos und den Verkaufspreisen.

```{code-cell} ipython3
# Import des Pandas-Moduls 
import pandas as pd

# Erzeugung der Daten als Series-Objekt
preisliste = [1999, 35990, 17850, 46830, 27443, 14240, 19950, 15950, 21990, 12450]
preise = pd.Series(preisliste, index = ['Audi Nr. 1', 'Audi Nr. 2', 'Audi Nr. 3', 'BMW Nr. 1', 'BMW Nr. 2', 
    'Citroen Nr. 1', 'Citroen Nr. 2', 'Citroen Nr. 3', 'Citroen Nr. 4', 'Citroen Nr. 5'])
```

Die Anwendung der `.describe()`-Methode liefert folgende Ausgabe:

```{code-cell} ipython3
preise.describe()
```

Die Methode .describe() liefert acht statistische Kennzahlen, deren Bedeutung in
der
[Pandas-Dokumentation](https://pandas.pydata.org/docs/reference/api/pandas.Series.describe.html)
erläutert wird. Wir gehen dennoch jede Kennzahl einzeln durch. Darüber hinaus
wird der Datentyp (hier `dtype: float64`) angegeben.


## Anzahl count()

Mit `.count()` wird die Anzahl der Einträge bestimmt, die *nicht* 'NA' sind. Der
Begriff 'NA' ist ein Fachbegriff des maschinellen Lernens. Gemeint sind fehlende
Einträge, wobei die fehlenden Einträge verschiedene Ursachen haben können:

* NA = not available (der Messsensor hat versagt)
* NA = not applicable (es ist sinnlos bei einem Mann nachzufragen, ob er
  schwanger ist)
* NA = no answer (eine Person hat bei dem Umfrage nichts angegeben)

```{code-cell} ipython3
anzahl_gueltige_preise = preise.count()
print(f'Im Series-Objekt sind {anzahl_gueltige_preise} nicht NA-Werte, also gültige Datensätze gespeichert.')
```


## Mittelwert mean()

Mittelwert heißt auf Englisch mean. Daher ist es nicht verwunderlich, dass die
Methode `.mean()` den Mittelwert der Einträge in jeder Spalte berechnet.

```{code-cell} ipython3
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

Das 'st' in `.std()` für Standard steht, ist nachvollziehbar. Der dritte
Buchstabe 'd' kommt von 'deviation', also Abweichung. Somit ist wiederum die
Methode nach dem englischen Fachbegriff 'standard deviation' benannt. Welche
Standardabweichung erhalten wir bei den Preisen?

```{code-cell} ipython3
standardabweichung = preise.std()
print(f'Die Standardabweichung bei den Verkaufspreisen beträgt {standardabweichung} Euro.')
```

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

```{code-cell} ipython3
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

```{code-cell} ipython3
quantil50 =preise.quantile(0.5)
print(f'Der Median, d.h. das 50 % Quantil, liegt bei {quantil50} EUR.')
```

Das 50 % -Quantil liegt bei 18900 EUR. 50 % aller Autos werden zu einem Preis
angeboten, der kleiner oder gleich 18900 EUR ist. Und 50 % aller Autos werden
teuer angeboten. Wir schauen uns jetzt das 75 % Quantil an. 

```{code-cell} ipython3
quantil75 = preise.quantile(0.75)
print(f'75 % aller Autos haben einen Preis kleiner gleich {quantil75} EUR.')
```

75 % aller Autos werden günstiger als 26079.75 EUR angeboten. Auch wenn Sie sich
natürlich für jede beliebigen Prozentsatz zwischen 0 % und 100 % das Quantil
ansehen können, interessieren wir uns noch für das 25 % Quantil.

```{code-cell} ipython3
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
