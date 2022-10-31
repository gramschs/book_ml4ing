---
jupytext:
  formats: ipynb,md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.13.8
kernelspec:
  display_name: Python 3.9.13 ('python39')
  language: python
  name: python3
---

# Digitale Logik und Schleife mit Bedingung

## Lernziele

```{admonition} Lernziele
:class: hint
* Sie können Vergleiche kombinieren und dazu digitale Logik verwenden: **and**, **or** und **not**.
* Sie können eine Schleife mit Bedingung **while** programmieren.
```

## Vergleiche kombinieren - digitale Logik

Vorhin haben wir den boolschen Datentyp kennengelernt: wahr oder falsch. Man
kann solche Ausdrücke auch kombinieren, z.B. könnte man fordern, dass zwei
Bedingungen gleichzeitg erfüllt sein sollen. 

Beispiel beim Busfahren: Kinder unter 6 Jahren können kostenlos Bus fahren. Ab 6
Jahren braucht man eine Fahrkarte. Bis 14 Jahre zahlt man den Kinderpreis, ab 15
Jahren den Erwachsenenpreis: 

```{code-cell} ipython3
alter = 12
if (6 <= alter) and (alter <= 14):
    print('Du darfst eine Kinderfahrkarte kaufen.')
```

Im Folgenden beschäftigen wir uns daher mit der Verknüpfung von booleschen
Ausdrücken. Dieses Fachgebiet nennt man auch boolsche Algebra oder digitale
Logik. Wikipedia fasst hier die wichtigsten Regeln zur booleschen Algebra
zusammen: https://de.wikipedia.org/wiki/Boolesche_Algebra 

Wir werden in dieser Vorlesung uns aber auf die logischen Verknüpfungen oder
logischen Operatoren 

* UND
* ODER
* NICHT

beschränken. Nun wenden wir uns der Umsetzung von logischen Verknüpfungen in
Python zu.

Bedingung 1 | Bedingung 2 | Ergebnis mit ```and```
------------|-------------|--------------------------
True | True | True
False | True | False
True | False | False
False | False | False

+++

Beispiel: Zwei Personen wollen einen Kinofilm sehen, der erst ab 18 erlaubt ist. Nur wenn beide volljährig sind, können sie den Film gemeinsam besuchen:

```{code-cell} ipython3
alter_person1 = 19
alter_person2 = 22
if (alter_person1 >= 18) and (alter_person2 >= 18):
    print('Sie duerfen beide den Film sehen.')
else:
    print('Vielleicht darf einer von Ihnen den Film sehen, aber nicht beide.')
```

Die sogenannte Wahrheitstabelle für die OR-Verknüpfung sieht folgendermaßen aus:

Bedingung 1 | Bedingung 2 | Ergebnis mit ```or```
------------|-------------|--------------------------
True | True | True
False | True | True
True | False | True
False | False | False

Beispiel: Zwei Personen wollen ein Auto mieten, dazu muss aber mindestens einer von beiden den Führerschein besitzen.

```{code-cell} ipython3
person1_hat_fuehrerschein = True
person2_hat_fuehrerschein = False

if (person1_hat_fuehrerschein == True) or (person2_hat_fuehrerschein == True):
    print('Sie duerfen das Auto mieten.')
else:
    print('Keiner von beiden hat einen Fuehrerschein, geht nicht.')
```

Übrigens, der Vergleich `person1_hat_fuehrerschein == True` ist eigentlich
doppelt gemoppelt, da ja die Variable bereits den Datentyp bool hat. Wir könnten
also auch kürzer schreiben

```{code-cell} ipython3
person1_hat_fuehrerschein = True
person2_hat_fuehrerschein = False

if person1_hat_fuehrerschein or person2_hat_fuehrerschein :
    print('Sie duerfen das Auto mieten.')
else:
    print('Keiner von beiden hat einen Fuehrerschein, geht nicht.')
```

Die sogenannte Wahrheitstabelle für die NOT-Verknüpfung sieht folgendermaßen aus:

Bedingung 1 | Ergebnis mit ```not```
------------|--------------------------
True | False
False | True 

Beispiel: Wenn eine Person keinen Führerschein hat, muss sie den Bus nehmen.

```{code-cell} ipython3
person_hat_fuehrerschein = False

if not person_hat_fuehrerschein:
    print('Sie muessen Bus fahren.')
else:
    print('Sie duerfen Auto fahren.')
```

<iframe width="560" height="315" src="https://www.youtube.com/embed/075l6R42tkQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

+++

## Schleifen mit Bedingung "while"

Bei einer Wiederholung mit Bedingung wird eine Anweisung solange wiederholt, bis
die Bedingung erfüllt wird. Sie hat folgende Struktur:

```python
 while Bedingung: 
        anweisungsblock
```

Die bedingte Wiederholung wird mit dem Schlüsselwort `while` eingeleitet. Dann
folgt die Bedingung, die mit einem `:` abgeschlossen wird. Alle Anweisungen, die
wiederholt werden sollen, werden eingerückt. Diesen Teil nennt man das
Schleifeninnere, die Zeile `while Bedingung:` nennt man den Schleifenkopf. 

Beispiel: Wir möchten ein Programm schreiben, das von 10 bis 0 herunterzählt.
Für den Countdown benutzen wir eine Variable als Zwischenspeicher. Dies würde in
Python wie folgt umgesetzt:

```{code-cell} ipython3
print('Dieses Programm zählt von 10 runter...')
countdown = 10
while countdown >= 0:
    print(countdown)
    countdown = countdown - 1
print('Jetzt hebt die Rakete ab!')
```

<iframe width="560" height="315" src="https://www.youtube.com/embed/sXLicTuJzB4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
