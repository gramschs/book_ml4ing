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

# 3.1 Pandas Series

Eine **Series** ist eine von zwei grundlegenden Datenstrukturen des
Pandas-Moduls. Die Series dient vor allem dazu, Daten zu verwalten und
statistisch zu erkunden. Bevor wir die neue Datenstruktur näher beleuchten,
machen wir uns aber zuerst mit dem **Modul Pandas** vertraut.

## Lernziele

```{admonition} Lernziele
:class: goals
* Sie können erklären, was ein **Modul** in Python ist.
* Sie kennen das Modul **Pandas** und können es mit seiner üblichen Abkürzung
  **pd** importieren.
* Sie kennen die Pandas-Datenstruktur **Series**.
* Sie wissen, was ein **Index** ist.
* Sie können aus Listen eine Series-Objekt erzeugen und mit einem Index
  versehen.
* Sie können mit Series-Objekten rechnen.
* Sie können die Elemente eines Series-Objektes mit **sort_values()**
  aufsteigend und absteigend sortieren lassen.
```

## Das Modul Pandas

Stellen Sie sich vor, Sie möchten Spaghetti mit Tomatensauce kochen. Am
einfachsten ist es, die Spaghetti-Nudeln und die Tomatensauce im Supermarkt zu
kaufen. Sie können aber auch nur die Nudeln kaufen und die Tomatensauce selbst
aus Tomaten und Basilikum zubereiten. Oder Sie gehen noch einen Schritt weiter
und machen sogar die Nudeln aus Mehl, Eiern, Wasser und Salz selbst.

In der Programmierung verhält es sich ähnlich. Sie können alle Funktionalitäten
(d.h. die Spagehtti oder die Tomatensauce) selbst programmieren. Oder sie
verwenden schon fertige Komponenten und setzen Sie so zusammen, wie Sie es zur
Lösung ihres Problems brauchen. Eine Sammlung von fertigen Python-Komponenten zu
einem bestimmten Thema wird **Modul** genannt. In anderen Programmiersprachen
oder allgemein in der Informatik nennt man eine solche Sammlung auch
**Bibliothek** oder verwendet den englischen Begriff **Library**.

```{admonition} Was ist ... ein Modul?
:class: note
Ein Modul (oder eine Bibliothek oder eine Library) ist eine Sammlung von
Python-Code zu einem bestimmten Thema, der als Werkzeug für eigene Programme
eingesetzt werden kann.
```

Um ein Modul in Python benutzen zu können, muss es zunächst einmal installiert
sein. Um dann die Funktionen, Klassen, Datentypen oder Konstanten benutzen zu
können, die das Modul zur Verfügung stellt, wird es importiert. Wir werden in
dieser Vorlesung sehr intensiv das Modul **Pandas** verwenden. Pandas ist ein
Modul zur Verarbeitung und Analyse von Daten. Es ist üblich, das Modul `pandas`
mit der Abkürzung `pd` zu importieren, damit wir nicht immer `pandas` schreiben
müssen, wenn wir Code aus dem Pandas-Modul benutzen.

```{code-cell}
import pandas as pd
```

Sollten Sie jetzt eine Fehlermeldung erhalten haben, ist das Pandas-Modul nicht
installiert. Installieren Sie zunächst Pandas beispielsweise mit `!conda install
pandas` oder `!pip install pandas`. Mit der Funktion `dir()` werden alle
Funktionalitäten des Moduls aufgelistet.

```{code-cell}
dir(pd)
```

Eine sehr lange Liste.

## Die Datenstruktur Series

Einfache Listen reichen nicht aus, um größere Datenmengen oder Tabellen
effizient zu speichern. Dazu benutzen Data Scientists die Datenstrukturen
`Series` oder `DataFrame` aus dem Pandas-Modul. Dabei wird **Series** für
Datenreihen genommen. Damit sind Vektoren gemeint, wenn alle Elemente der
Datenreihe aus Zahlen bestehen, oder eindimensionale Arrays. Die Datenstruktur
**DataFrame** wiederum dient zum Speichern und Verarbeiten von tabellierten
Daten, also sozusagen Matrizen, wenn alle Elemente Zahlen sind, oder
zweidimensionale Arrays.

Wir starten mit der Datenstruktur Series. Als Beispiel betrachten wir die
Verkaufspreise (in Euro) von zehn Autos. Die Daten stammen von der
Internetplattform [Autoscout24](https://www.autoscout24.de). Die Preise kommen
zunächst in eine Liste (erkennbar an den eckigen Klammern), aus der dann ein
Series-Objekt erzeugt wird.

```{code-cell}
preisliste = [1999, 35990, 17850, 46830, 27443, 14240, 19950, 15950, 21990, 50000]
preise = pd.Series(preisliste)
print(preise)
```

Was ist aber jetzt der Vorteil von Pandas? Warum nicht einfach bei der Liste
bleiben? Der wichtigste Unterschied zwischen Liste und Series ist der **Index**.

Bei einer Liste ist der Index implizit definiert. Damit ist gemeint, dass bei
der Initialisierung einer Liste automatisch ein nummerierter Index 0, 1, 2, 3,
... angelegt wird. Wenn bei einer Liste auf das dritte Element zugegriffen
werden soll, dann verwenden wir den Index 2 (zur Erinnerung: Python zählt ab 0)
und schreiben

```{code-cell}
preis_drittes_auto = preisliste[2]
print(f'Preis des dritten Autos: {preis_drittes_auto} EUR')
```

Die Datenstruktur Series ermöglich es aber, einen *expliziten Index* zu setzen.
Über den optionalen Parameter `index=` speichern wir als Zusatzinformation noch
ab, von welchem Auto der Verkaufspreis erfasst wurde. Wir werden diesen
Datensatz in den folgenden Kapiteln noch weiter vertiefen. An dieser Stelle
halten wir fest, dass die ersten drei Autos von der Marke Audi sind, die
nächsten sind BMWs und die letzten fünf sind von der Marke Citroen.

```{code-cell}
autos = ['Audi Nr. 1', 'Audi Nr. 2', 'Audi Nr. 3', 'BMW Nr. 1', 'BMW Nr. 2', 'Citroen Nr. 1', 'Citroen Nr. 2', 'Citroen Nr. 3', 'Citroen Nr. 4', 'Citroen Nr. 5']
preise = pd.Series(preisliste, index = autos)
print(preise)
```

Jetzt ist auch klar, warum beim ersten Mal, als wir `print(preise)` ausgeführt
haben, die Zahlen 0, 1, 2, usw. ausgegeben wurden. Zu dem Zeitpunkt hatte das
Series-Objekt noch einen impliziten Index wie eine Liste. Den expliziten Index
nutzen wir jetzt, um auf den Verkaufspreis des dritten Autos zuzugreifen. Das
dritte Auto ist `Audi Nr. 3`. Wie bei Listen verwenden wir eckige Klammern:

```{code-cell}
preis_drittes_auto = preise['Audi Nr. 3']
print(f'Preis des dritten Autos: {preis_drittes_auto} EUR')
```

Die Datenstruktur Series hat gegenüber der Liste noch einen weiteren Vorteil. In
der Datenstruktur ist noch eine Zusatzinformation gespeichert, die Eigenschaft
`dtype`. Darin gespeichert ist der Datentyp der Elemente des Series-Objektes.
Auf diese Eigenschaft kann auch direkt mit dem sogenannten Punktoperator
zugegegriffen werden.

```{code-cell}
datentyp_preise = preise.dtype
print(f'Die einzelnen Elemente des Series-Objektes "preise" haben den Datentyp {datentyp_preise}, sind also Integer.')
```

Offensichtlich sind die gespeicherten Werte Integer.

```{admonition} Mini-Übung
:class: miniexercise 
Erzeugen Sie ein Series-Objekt mit den Wochentagen als Index und der Anzahl der
Vorlesungsstunden (SWS) an diesem Wochentag.
```

```{code-cell} ipython3
# Hier Ihr Code:
```

````{admonition} Lösung
:class: minisolution, toggle
```python
stundenplan = pd.Series([4, 0, 4, 6, 8], index=['Montag', 'Dienstag', 'Mittwoch', 'Donnerstag', 'Freitag'])
print(stundenplan)
```
````

## Arbeiten mit Series-Objekten

Falls der Datentyp der einzelnen Elemente eines Series-Objektes ein numerischer
Typ ist (Integer oder Float), können wir mit den Einträgen auch rechnen. So
lassen sich beispielweise die Preise nicht in Euro, sondern als Preis pro
Tausend Euro angeben, wenn wir alle Preise durch 1000 teilen.

```{code-cell}
preise_pro_1000euro = preise / 1000
print(preise_pro_1000euro)
```

Oder Sie könnten auf die Idee kommen, das billigste Auto auf den Preis 0 zu
setzen und sich ausgeben lassen, um wie viel Euro die anderen Autos teuer sind.
Oder anders ausgedrückt, wir subtrahieren von jedem Preis den Wert 1999 EUR:

```{code-cell}
preise_differenz = preise - 1999
print(preise_differenz)
```

Bei zehn Autos war es relativ einfach, das billigste Auto zu ermitteln, indem
wir einfach die Preisliste durchgeschaut haben. Hilfreicher ist es, vorher die
Preise aufsteigend oder absteigend zu sortieren. Dazu nutzen wir die Methode
`.sort_values()`. Der Name lässt vermuten, dass die Methode die Elemente nach
ihrem Wert sortiert.

```{code-cell}
preise_aufsteigend = preise.sort_values()
print(preise_aufsteigend)
```

Jetzt zeigt sich auch der Vorteil des expliziten Index, denn auf die
ursprüngliche Reihenfolge kommt es nicht an. Der explizite Index ermöglicht uns,
jedes Auto auch in der nach Preisen aufsteigend sortierten Liste eindeutig
wiederzufinden. Zum Abschluss sortieren wir noch absteigend. Mit dem optionalen
Argument `ascending` wird gesteuert, ob aufsteigend sortiert werden soll oder
nicht. Fehlt das Argument, so nimmt der Python-Interpreter an, dass `ascending =
True` gewünscht wird, also dass `aufsteigend = wahr` sein soll. Wollen wir
absteigend sortieren, müssen wir `aufsteigend = falsch` setzen, also `ascending
 = False`.

```{code-cell}
preise_absteigend = preise.sort_values(ascending = False)
print(preise_absteigend)
```

Vielleicht ist Ihnen aufgefallen, dass wir das sortierte Series-Objekt gleich in
einer neuen Vaiable abgespeichert haben. Das ist notwendig, wenn die neue
Sortierung erhalten bleiben soll. Standardmäßig wirkt der Sortierungsbefehl
nämlich nur einmalig und ändert die eigentliche Reihenfolge im Original nicht.
Auch das könnte man durch weitere Parameter ändern (`inplace = True`), wie Sie
in der [Pandas-Dokumentation →
sort_values()](https://pandas.pydata.org/docs/reference/api/pandas.Series.sort_values.html)
nachlesen können.

```{admonition} Mini-Übung
:class: miniexercise
Alice, Bob, Charlie und Dora sind 22, 20, 24 und 22 Jahre alt. Speichern Sie
diese Informationen in einem Series-Objekt und sortieren Sie von alt nach jung.
```

```{code-cell} ipython3
# Hier Ihr Code
```

````{admonition} Lösung
:class: minisolution, toggle
```python
# Erzeugung des Series-Objektes
namen = ['Alice', 'Bob', 'Charlie', 'Dora']
alter = [22, 20, 24, 22]
personen = pd.Series(alter, index = namen)

# Sortierung ud Ausgabe
personen_sortiert = personen.sort_values(ascending = False)
print(personen_sortiert)
```
````

## Zusammenfassung und Ausblick

In diesem Kapitel haben wir Pandas und die sehr wichtige Datenstruktur Series
kennengelernt. Im nächsten Kapitel geht es darum, die wichtigsten statistischen
Kennzahlen der Daten zu ermitteln, die in dem Series-Objekt gespeichert sind.
