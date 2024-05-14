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

# 2.3 Funktionen und Methoden

Sobald die Funktionalitäten komplexer werden, lohnt es sich Code in eigene
Funktionsbausteine auszulagern und vor allem auf Code von anderen
Programmier:innen zurückzugreifen. Code, der eine Teilaufgabe löst und einen
eigenständigen Namen bekommt, wird **Funktion** genannt. Ist die Funktion direkt
an einen Datentyp gekoppelt, wird die Funktion **Methode** genannt. In diesem
Kapitel gehen wir sehr kurz auf die wichtigsten Grundlagen von Funktionen und
Methoden ein.

## Lernziele

```{admonition} Lernziele
:class: goals
* Sie können selbst eine **Funktion** mit Parametern und Rückgabewert
  implementieren.
* Sie kennen das Konzept der **objektorientierten Programmierung**.
* Sie wissen, was **Klassen** und **Methoden** sind.
```


## Funktionen

Eine Funktion ist eine Zusammenfassung von Code, der eine bestimmte Teilaufgabe
löst. Dabei arbeitet die Funktion nach dem EVA-Prinzip (Eingabe, Verarbeitung,
Ausgabe). Die Funktion übernimmt Objekte als Eingabe, verarbeitet diese und
liefert Objekte als Ergebnis zurück. Wie die Funktion dabei im Inneren genau
funktioniert (Verarbeitung), ist unwichtig.

Insbesondere muss die Teilaufgabe, die die Funktion löst, nichts mit Mathematik
zu tun haben. Eine Funktion in der Informatik hat nichts mit einer
mathematischen Funktion zu tun, auch wenn oft mathematische Funktionen als
Beispiel verwendet werden. Ein Beispiel für eine nicht-mathematische Funktion
haben Sie mit `print()` bereits kennengelernt.


### Die Benutzung von Funktionen (oder der Aufruf von Funktionen)

Eine Funktion wird benutzt, indem man den Namen der Funktion hinschreibt und
dann in runden Klammern ihre Argumente. Welche Argumente für eine Funktion
verwendet werden dürfen, hängt von der Implementierung der Funktion ab.

Beispielsweise kann als Argument für die `len()`-Funktion ein String übergeben
werden oder eine Liste. 

```{code-cell} ipython3
len('Hallo')
```

```{code-cell} ipython3
len([1,2,3,4,8,2])
```

In der Regel geben Funktionen wieder Ergebnisse zurück. Diese können einer
Variable zugewiesen werden, um weiter mit dem Ergebnis zu arbeiten.

```{code-cell} ipython3
wort = 'Hallo'
anzahl_zeichen = len(wort)
print(f'Mein Wort {wort} hat {anzahl_zeichen} Zeichen.')
```

### Definition von einfachen Funktionen

Um selbst eine Funktion zu definieren, benutzen wir das Schlüsselwort `def`.
Danach wählen wir einen Funktionsnamen und hängen an den Funktionsnamen runde
Klammern gefolgt von einem Doppelpunkt. Die Anweisungen, die ausgeführt werden
sollen, sobald die Funktion aufgerufen wird, werden eingerückt.

Als erstes Beispiel einer sehr einfachen Funktion betrachten wir die folgende
Funktion:

```{code-cell} ipython3
def gruesse_ausrichten():
    print('Ich grüße Sie!')
```

Die Funktion hat keine Argumente und keine Rückgabe, sondern gibt einfqach nur
einen Text auf dem Bildschirm aus. Nachdem die Funktion `gruesse_ausrichten()`
so implementiert wurde, können wir sie im Folgenden direkt verwenden.

```{code-cell} ipython3
gruesse_ausrichten()
```

Und natürlich kann man sie in Programmverzweigungen und Schleifen einbauen.

```{admonition} Mini-Übung
:class: miniexercise
Schreiben Sie eine Funktion, die den Namen `hallihallo` hat und das Wort Hallihallo ausgibt. Testen Sie Ihre Funktion auch.
```

```{code-cell} ipython3
# Hier Ihr Code:
```

````{admonition} Lösung
:class: minisolution, toggle
```python
def hallihallo():
    print('Hallihallo!')

# Test
hallihallo()
```
````

Das folgende Video zeigt, wie Funktionen selbst definiert werden.

```{dropdown} Video zu "Funktionen selbst definieren" von Programmieren lernen
<iframe width="560" height="315" src="https://www.youtube.com/embed/LQCfN5HS9xI" 
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; 
clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
```

### Funktionen mit Parametern

Meistens haben Funktionen Argumente, um Eingaben/Input entgegennehmen und
verarbeiten zu können. Das Argument wird bei der Implementierung der Funktion
mit einer Variable eingeführt, wie in dem folgenden Beispiel `name`.

```{code-cell} ipython3
def gruesse_ausrichten_mit_parameter(name):
    print(f'Ich grüße {name}')
```

Der Aufruf einer Funktion ohne passende Argumente führt zu einer Fehlermeldung.
Entfernen Sie das Kommentarzeichen `#` und führen Sie die nachfolgende
Code-Zelle aus:

```{code-cell} ipython3
#gruesse_ausrichten_mit_parameter()
```

Daher müssen wir die modifizierte Funktion nun wie folgt aufrufen:

```{code-cell} ipython3
gruesse_ausrichten_mit_parameter('Bob')
```

Die Funktion `gruesse_ausrichten_mit_parameter()` hat aber keinen Rückgabewert.
Das können wir wie folgt testen:

```{code-cell} ipython3
x = gruesse_ausrichten_mit_parameter('Alice')
type(x)
```

`x` ist vom Typ `NoneType` oder anders ausgedrückt, es hat keinen Datentyp. 

Sind Funktionen ohne Rückgabewert sinnvoll? Ja, denn so können Codeblöcke
vereinfacht werden. Sollte in einem Programm Code mehrmals ausgeführt werden,
lohnt es sich, diesen in eine Funktion auszulagern, um diese einfach aufrufen zu
können.


````{admonition} Mini-Übung
:class: miniexercise
Schreiben Sie eine Funktion mit zwei Parametern, nämlich Vor- und Nachname. Wenn 
die Funktion z.B. mit `(Alice, Miller)` aufgerufen wird, soll sie Folgendes auf 
dem Bildschirm ausgeben:

```python
Vorname: Alice
Nachname: Miller
```
````

```{code-cell} ipython3
# Hier Ihr Code:
```

````{admonition} Lösung
:class: minisolution, toggle
```python
def gruesse_ausrichten_mit_parametern(vorname, nachname):
    print(f'Vorname: {vorname}')
    print(f'Nachname: {nachname})

gruesse_ausrichten_mit_parametern('Alice', 'im Wunderland')
```
````

Das folgende Video zeigt, wie Funktionen mit Parametern in Python implementiert
werden.

```{dropdown} Video zu "Funktionen mit Parametern" von Programmieren lernen
<iframe width="560" height="315" src="https://www.youtube.com/embed/af9ORp1Pty0" 
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay;
clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen>
</iframe>
```

### Funktionen mit Rückgabewert

In der Regel jedoch haben Funktionen einen Rückgabewert. Schauen wir uns ein
Beispiel an:

```{code-cell} ipython3
def berechne_quadrat(x):
    return x*x

# Aufruf der Funktion
berechne_quadrat(7)
```

Die Rückgabe wird durch das Schlüsselwort `return` erzeugt. Es ist auch möglich,
mehrere Ergebnisse gleichzeitig zurückzugeben. Diese werden einfach nach dem
Schlüsselwort `return` mit Kommas getrennt gelistet.

````{admonition} Mini-Übung
:class: miniexercise
Schreiben Sie eine Funktion mit zwei Parametern, nämlich den beiden Seitenlängen eines Rechtecks. Lassen Sie die Fläche des Rechtecks berechnen und zurückgeben. Testen Sie Ihr Funktion auch.
````

```{code-cell} ipython3
# Hier Ihr Code:
```

````{admonition} Lösung
:class: minisolution, toggle
```python
def berechne_flaecheninhalt_rechteck(seite1, seite2):
    return seite1 * seite2

# Test der Funktion
A = berechne_flaecheninhalt_rechteck(2,3)
print(A)
```
````

```{dropdown} Video zu "Funktionen mit Rückgabewert" von Programmieren lernen
<iframe width="560" height="315" src="https://www.youtube.com/embed/ehSP-sYoKCY" 
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; 
clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen>
</iframe>
```


## Objektorientierte Programmierung

In den ersten beiden Teilen unseres Crashkurses Python haben wir uns die
Grundlagen der Programmierung erarbeitet:

* Datentypen (Integer, Float, String, List)
* Kontrollstrukturen: for-Schleife
* Funktionen.

In einigen Programmiersprachen wie beispielsweise C hätten wir damit auch alle
Sprachelement kennengelernt. Diese Programmierung nennt man **prozedurale
Programmierung**. Python gehört jedoch zu den objektorientierten
Programmiersprachen, so dass wir uns jetzt noch dem Thema Objektorientierung
widmen.

### Konzept 

Bei der bisherigen prozeduralen Programmierweise haben wir Funktionen und Daten
getrennt. Die Daten werden in Variablen gespeichert. Funktionen funktionieren
nach dem EVA-Prinzip. In der Regel erwartet eine Funktion eine Eingabe von
Daten, verarbeitet diese Daten und gibt Daten zurück. 

Angenommen, wir wollten ein Programm zur Verwaltung von Lottoscheinen schreiben.
Zu einem Lottoschein wollen wir Name, Adresse und die angekreuzten Zahlen
speichern. Dann müssten wir mit unserem bisherigen Wissen folgende Variablen pro
Lottoschein einführen:

* vorname
* nachname
* strasse
* postleitzahl
* stadt
* liste_mit_sechs_zahlen

Wenn jetzt viele Spielerinnen und Spieler Lotto spielen wollen, wie gehen wir
jetzt mit den Daten um? Legen wir eine Liste für die Vornamen und eine Liste für
die Nachnamen usw. an? Und wenn jetzt der 17. Eintrag in der Liste mit den sechs
angekreuzten Lottozahlen sechs Richtige hat, suchen wir dann den 17. Eintrag in
der Liste mit den Vornamen und den 17. Eintrag in der Liste mit den Nachnamen
usw.? Umständlich...

Die Idee der objektorientierten Programmierung ist, für solche Szenarien
**Objekte** einzuführen. Ein Objekt fasst verschiedene Eigenschaften wie hier
Vorname, Nachname, Straße, usw. zu einem Objekt Lottoschein zusammen. In der
Informatik wird eine Eigenschaft eines Objekts **Attribut** genannt. 

Damit hätten wir erst einmal nur einen neuen Datentyp. Ein Objekt macht noch
mehr aus, denn zu dem neuen Datentyp kommen noch Funktionen dazu, die die
Verwaltung des Objektes erleichtern. Funktionen, die zu einem Objekt gehören,
nennt man **Methoden**.

```{dropdown} Video zu "Konzept der Objektorientierung" von Programmieren lernen
<iframe width="560" height="315" src="https://www.youtube.com/embed/46yolPy-2VQ" 
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; 
clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen>
</iframe>
```


### Klassen und Methoden

Im Folgenden sehen Sie, wie ein Objekt in Python definiert wird. Die
Implementierung erfolgt als sogenannte **Klasse**.

```{code-cell}
class Adresse:
    def __init__(self, strasse, hausnummer, plz, stadt):
        self.strasse = strasse
        self.hausnummer = hausnummer
        self.postleitzahl = plz
        self.stadt = stadt
    
    def print(self):
        print('Straße = ', self.strasse)
        print('Hausnummer = ', self.hausnummer)
        print('Postleitzahl = ', self.postleitzahl)
        print('Stadt = ', self.stadt)
```

Eingeleitet wird eine Klasse mit dem Schlüsselwort `class` und dann dem Namen
der Klasse. Da Klassen Objekte sind, ist es Standard, den ersten Buchstaben des
Klassennamens groß zu schreiben. Um Variablen von Objekten leichter zu
unterscheiden, werden Variablennamen klein geschrieben.

Danach folgt ein Abschnitt namens `def __init__(self):`, in dem die
Eigenschaften der Klasse aufgelistet werden. `init` steht dabei für
initialisieren, also den ersten Zustand, den das Objekt später haben wird. 

Wie Sie sehen, können die Eingabe-Parameter der `init()`-Methode die gleichen
Namen tragen wie die Attribute der Klasse, also `self.strasse = strasse`, müssen
sie aber nicht. Das Beispiel `self.postleitzahl = plz` zeigt, dass das Attribut
`self.postleitzahl` einfach den Wert des 4. Parameters bekommt, egal wie der
heißt.

Eine Adresse wird nun folgendermaßen initialisiert:

```{code-cell}
adresse_fra_uas = Adresse('Nibelungenplatz', 1, 60318, 'Frankfurt am Main')
```

Würden wir nun versuchen, mit `print(adresse_fra_uas)` die Adresse am Bildschirm
ausgeben zu lassen, würden wir eine Fehlermeldung erhalten. Die Funktion
`print()` ist nicht für den Datentyp `Adresse` entwickelt worden. Schließlich
können die Python-Entwickler nicht wissen, welche Klassen Sie entwickeln... Wir
müssen also eine eigene Adressen-print()-Funktion implementieren. Da diese
print()-Funktion nicht allgemeingültig sein kann, sondern nur für die Objekte
`Adresse` funktionieren wird, gehört sie auch folgerichtig zur Klasse selbst.
Sie ist also keine Funktion, sondern eine **Methode**. 

Eine Methode wird definiert, indem innerhalb des Anweisungsblocks der Klasse
eine Funktion mit dem Schlüsselwort `def` definiert wird. Der erste Eingabewert
muss zwingend der `self`-Parameter sein. Ansonsten gelten aber die gleichen
Regeln für Methoden wie für Funktionen.

Bleibt nur noch eine Frage? Wie wird nun die Methode ausgeführt? Methoden werden
ausgeführt, indem die Variable hingeschrieben wird, dann ein Punkt gesetzt wird
und dann die Methode mit runden Klammern angefügt wird.

```{code-cell} ipython3
adresse_fra_uas.print()
```

Objektorientierung ist ein sehr detailreiches Thema, das wir in diesem Kapitel
nur streifen konnten. Die folgenden Videos geben einen vertieften Einblick in
die Objektorientierung mit Python.

```{dropdown} Video zu "Klassen und Objekte" von Programmieren lernen
<iframe width="560" height="315" src="https://www.youtube.com/embed/XxCZrT7Z3G4" 
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; 
clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen>
</iframe>
```

```{dropdown} Video zu "Der self Parameter" von Programmieren lernen
<iframe width="560" height="315" src="https://www.youtube.com/embed/CLoK-_qNTnU" 
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; 
clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen>
</iframe>
```

```{dropdown} Video zu "Methoden in Klassen" von Programmieren lernen
<iframe width="560" height="315" src="https://www.youtube.com/embed/58IjjwHs_4A" 
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; 
clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen>
</iframe>
```

## Zusammenfassung und Ausblick

In diesem Kapitel haben wir gelernt, selbst Funktionen und Klassen mit Methoden
zu definieren. Oft ist es aber praktischer, Funktionen und Klassen zu nutzen,
die bereits implementiert sind, anstatt das Rad neu zu erfinden. Vor allem bei
der Datenexploration und den maschinellen Lernalgorithmen benutzen wir die
vorgefertigten Funktionsbausteine eher als eigene zu definieren, wie wir in den
nächsten Kapiteln sehen werden.




