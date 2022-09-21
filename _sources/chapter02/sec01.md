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

# Datentypen, Variablen und Vergleiche

## Lernziele

```{admonition} Lernziele
:class: hint
* Sie kennen die einfachen Datentypen:
    * **Integer**
    * **Float**
    * **String**
* Sie wissen, was eine **Variable** ist und kennen den **Zuweisungsoperator**.
* Sie kennen den **print**-Befehl.
```

+++

## Einfache Datentypen

Im datengestützten Prozessmanagement geht es um die Sammlung, Erkundung und
Analyse, um Antworten auf vorgegebene Fragen zu finden. Schematisch stellen wir
datengestütztes Prozessmanagement folgendermaßen dar:

```{figure} pics/fig01_prozess.png
---
width: 600px
name: fig01_prozess
---
Schematische Darstellung der Vorgehensweise im datengestützten Prozessmanagement
```

+++

Der Computer kann Informationen aber nur als 0 und 1 verarbeiten. Auf dem
Speichermedium oder im Speicher selbst werden Daten daher als eine Folge von 0
und 1 gespeichert. Damit es für uns Programmierinnen und Programmier einfacher
wird, Daten zu speichern und zu verarbeiten, wurden Datentypen eingeführt.  

**Datentypen** fassen gleichartige Objekte zusammen und stellen den
Programmiererinnen und Programmieren passende Operationen zur Verfügung. Es
hängt von der Programmiersprache ab, welche Datentypen zur Verfügung stehen, wie
diese im Hintergrund gespeichtert werden und welche Operationen möglich sind.

In diesem Kapitel beschäftigen wir uns mit den einfachen Datentypen
* Integer,
* Float,
* String und
* Bool.

+++

### Integer und Float 

In der Programmierung unterscheidet man grundsätzlich zwischen zwei Zahlenarten,
den Ganzzahlen und den Gleitkommazahlen/Fließkommazahlen. Die Ganzzahlen werden
in der Mathematik als ganze Zahlen bezeichnet. In der Informatik ist der
englische Begriff am gebräuchlisten: Integer. 

Mit Integern können wir ganz normal rechnen, also Operationen ausführen:

```{code-cell} ipython3
2+3
```

```{code-cell} ipython3
2*3
```

```{code-cell} ipython3
6-7
```

```{code-cell} ipython3
3*(4+7)
```

```{code-cell} ipython3
25/5
```

```{code-cell} ipython3
4**2
```

Mit einer Operation verlassen wir aber bereits den Bereich der ganzen Zahlen,
den Bereich der Integers. `25/5` ist wieder eine ganze Zahl, nicht jedoch
`25/3`. Damit sind wir bei den Fließkommazahlen, den sogenannten Floats. Zur
Verfügung stehen auch hier die üblichen Operationen.

Achtung: Verwenden Sie stets einen Punkt als Dezimaltrennzeichen, nicht ein
Komma.

```{code-cell} ipython3
2.3 + 4.5
```

```{code-cell} ipython3
5.6 - 2.1
```

```{code-cell} ipython3
2.1 * 3.5
```

```{code-cell} ipython3
3.4 / 1.7
```

```{code-cell} ipython3
3.4 ** 2
```

```{code-cell} ipython3
3.5 * (2.6 - 3.8 / 1.9)
```

<iframe width="560" height="315" src="https://www.youtube.com/embed/VtiDkRDPA_c" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

+++

### String

Daten sind aber sehr oft keine Zahlen. Beispielsweise könnte man sich
vorstellen, eine Einkaufsliste zu erstellen und diese im Computer oder in einer
Notiz-App auf dem Handy zu speichern. Eine solche Zeichenkette heißt in der
Informatik String. Mit Zeichen meint man dabei Zahlen, Buchstaben oder andere
Zeichen wie beispielsweise !"§$%&/()=?.

Strings werden in Python durch einfache Hochkomma oder Anführungszeichen
definiert.

```{code-cell} ipython3
'Dies ist ein String!'
```

Mit Strings kann man ebenfalls "rechnen", nur ist das Ergebnis vielleicht anders als erwartet.

```{code-cell} ipython3
2 * 'Dies ist ein String!'
```

```{code-cell} ipython3
'String 1 ' + 'String 2' 
```

<iframe width="560" height="315" src="https://www.youtube.com/embed/sTEf4_mrLvw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>




## Variablen 

Variablen sind beschriftete Schubladen. Oder anders formuliert sind Variablen
Objekte, denen man einen Namen gibt. Technisch gesehen sind diese Schubladen ein
kleiner Bereich im Arbeitsspeicher des Computers. Was in diesen Schubladen
aufbewahrt wird, kann sehr unterschiedlich sein. Beispielsweise die
Telefonnummer des ADAC-Pannendienstes, die 10. Nachkommastelle von Pi oder die
aktuelle Position des Mauszeigers können in den Schubladen enthalten sein. 

### Zuweisung

Wir verwenden Variablen, um bestimmte Werte oder ein bestimmtes Objekt zu
speichern. Eine Variable wird durch Zuweisung erzeugt. Damit meinen wir, dass
eine Schublade angelegt wird und die Schublade dann erstmalig gefüllt wird. Das
erstmalige Füllen der Schublade nennt man in der Informatik auch Initialisieren.

```{code-cell} ipython3
x = 0.5
```

Sobald die Variable `x` in diesem Beispiel durch eine Zuweisung von 0.5 erstellt
wurde, können wir sie verwenden:

```{code-cell} ipython3
x * 3
```

```{code-cell} ipython3
x + 17
```

<iframe width="560" height="315" src="https://www.youtube.com/embed/jfOLXKPGXJ0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Wichtig ist, dass das `=` in der Informatik eine andere Bedeutung hat als in der
Mathematik. `=` meint nicht das Gleichheitszeichen, sondern den sogenannten
**Zuweisungsoperator**. Das ist in der Programmierung ein Kommando, das eine
Schublade befüllt oder technischer ausgedrückt, ein Objekt einer Variable
zuweist.

Variablen müssen initalisiert (erstmalig mit einem Wert versehen) werden, bevor
sie verwendet werden können, sonst tritt ein Fehler auf:

Schreiben Sie in die folgende Code-Zelle `n` und lassen Sie sie ausführen. Was
passiert?

```{code-cell} ipython3
# Hier Ihr Code
```

Sehr häufig findet man Code wie

```{code-cell} ipython3
x = x + 1
```

Würden wir dies als Gleichung lesen, wie wir es aus der Mathematik gewohnt sind,
x = x + 1, könnten wir x auf beiden Seiten subtrahieren und erhalten 0 = 1. Wir
wissen, dass dies nicht wahr ist, also stimmt hier etwas nicht.

In Python sind "Gleichungen" keine mathematischen Gleichungen, sondern
Zuweisungen. "=" ist kein Gleichheitszeichen im mathematischen Sinne, sondern
eine Zuweisung. Die Zuweisung muss immer in der folgenden Weise zweistufig
gelesen werden:

1. Berechne den Wert auf der rechten Seite (also x+1).
2. Weise den Wert auf der rechten Seite dem auf der linken Seite stehenden
   Variablennamen zu (in Python-Sprechweise: binde dem Namen auf der linken
   Seite an das auf der rechten Seite angezeigte Objekt).


```{code-cell} ipython3
x = 4     
x = x + 1
x
```

### Richtlinien für Variablennamen:

Früher war der Speicherplatz von Computern klein, daher wurden häufig nur kurze
Variablennamen wie beispielsweise `i` oder `N` verwendet. Heutzutage ist es
Standard, nur in Ausnahmefällen (z.B. in Schleifen, dazu kommen wir noch) kurze
Variablennamen zu nehmen. Stattdessen werden Namen benutzt, bei denen man
erraten kann, was die Variable für einen Einsatzzweck hat. Beispielsweise lässt
der Code

```{code-cell} ipython3
m = 0.19
n = 80
b = n + m*n
print(b)
```

nur schwer vermuten, was damit bezweckt wird. Dagegen erahnt man bei diesem Code
schon eher, was bezweckt wird:

```{code-cell} ipython3
mehrwertsteuersatz = 19/100
nettopreis = 80
bruttopreis = nettopreis + mehrwertsteuersatz * nettopreis
print(bruttopreis)
```

Verwenden Sie für Variablennamen nur ASCII-Zeichen, also keine Umlaute wie ö, ü
oder ß. Zahlen sind erlaubt, aber nicht am Anfang des Namens. Es ist sinnvoll,
lange Variablen durch einen Unterstrich besser lesbar zu gestalten (sogenannte
Snake-Case-Formatierung). Ich empfehle für Variablennamen beispielsweise

`dateiname_alt` oder `dateiname_neu`

wenn beispielsweise eine Datei umbenannt wird. Sie sind frei in der Gestaltung
der Variablennamen, verboten sind nur die sogannnten Schlüsselwörter. 

+++

Bemerkung: Hier kam erstmalig auch eine eingebaute Python-Funktion zum Einsatz,
die `print()`-Anweisung. Mehr Details zur `print()`-Anweisung finden Sie hier:
https://docs.python.org/3/tutorial/inputoutput.html

+++

<iframe width="560" height="315" src="https://www.youtube.com/embed/XKFQ2_et5k8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

+++


### Mischen von Datentypen 

Werden zwei Integer geteilt, so wird das Ergebnis vom Datentyp automatisch in
einen Float umgewandelt. Mit Hilfe der Funktion `type()` können wir den
Python-Interpreter bestimmen lassen, welcher Datentyp in einer Variable
gespeichert ist. 

```{code-cell} ipython3
x = 25 * 5
type(x)
```

```{code-cell} ipython3
x = 25 / 5
type(x)
```
Nicht immer ist es aber möglich, Datentypen zu mischen. Dann meldet Python einen
Fehler.

<iframe width="560" height="315" src="https://www.youtube.com/embed/1WqFJ5wsA4o" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Typumwandlungen (Type Casting)

Es ist aber auch möglich, einen Datentyp explizit in einen anderen Datentyp
umzuwandeln. Informatiker sagen dazu, einen Type Cast vorzunehmen. Soll ein
Datentyp in einen Integer umgewandelt werden, so verwenden wir die Funktion
`int()`. Die Umwandlung in einen Float erfolgt per `float()` und in einen String
wandeln wir mit Hilfe der Funktion `str()` um. Das klappt nicht mit jedem
Variableninhalt, die Umwandlung muss machbar sein, wie die folgenden Beispiele
zeigen.     

```{code-cell} ipython3
x_old = 3
x_new = str(x_old)
type(x_new)
```

```{code-cell} ipython3
x_old = '3'
x_new = int(x_old)
type(x_new)
```

Der folgende Code ist in Markdown geschrieben, da ansonsten eine Fehlermeldung
erzeugt würde:

```python
x_old = 'drei'
x_new = int(x_old)
type(x_new)
```

+++

<iframe width="560" height="315" src="https://www.youtube.com/embed/u_ECGvn1Z2c" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

+++


