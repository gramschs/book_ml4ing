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

# Objektorientierung

In diesem Abbschnitt werden wir den Crashkurs in Python mit einem Ausflug in die
objektorientierte Programmierung abschließen. 

## Lernziele

```{admonition} Lernziele
:class: hint
* Was ist Objektorientierung?
* Klassen definieren: Attribute und Methoden
```


## Objektorientierte Programmierung — Konzept

In den ersten beiden Teilen unseres Crashkurses Python haben wir uns die
Grundlagen der Programmierung erarbeitet:
* Datentypen (Integer, Float, String, Bool, List)
* Kontrollstrukturen 
    * Programmverzweigungen (if - elif - else)
    * Schleifen (while oder for)
* Funktionen.

In einigen Programmiersprachen wie beispielsweise C hätten wir damit auch alle
Sprachelement kennengelernt. Diese Programmierung nennt man **prozedurale
Programmierung**. Python gehört jedoch zu den objektorientierten
Programmiersprachen, so dass wir uns diese Woche dem Thema Objektorientierung
widmen.

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

<iframe width="560" height="315" src="https://www.youtube.com/embed/46yolPy-2VQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


## Klassen und Objekte

Im Folgenden sehen Sie, wie ein Objekt in Python definiert wird. Die
Implementierung erfolgt als sogenannte **Klasse**. 

```{code-cell} ipython3
class Adresse:
    def __init__(self, strasse, hausnummer, plz, stadt, b):
        self.strasse = strasse
        self.hausnummer = hausnummer
        self.postleitzahl = plz
        self.stadt = stadt
        self.bundesland = b
        self.nachname = nachname  
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

Definieren wir jetzt unsere erste Adresse, der Eingabe-Parameter `self` wird
dabei weggelassen (warum kommt später).

```{code-cell} ipython3
adresse_fra_uas = Adresse('Nibelungenplatz', 1, 60318, 'Frankfurt am Main')
```

Geben wir als nächstes aus, was in der Variable `adresse_fra_uas` gespeichert
ist. Probieren wir es mit der `print()`-Funktion:

```{code-cell} ipython3
print(adresse_fra_uas)
```

Wie Sie sehen, wird der Name der Klasse und der Speicherort im Speicher
angegeben, aber nicht der Inhalt. Die Funktion `print()` ist nicht für den
Datentyp `Adresse` entwickelt worden. Schließlich können die Python-Entwickler
nicht wissen, welche Klassen Sie entwickeln... 

Aber wir kommen wir jetzt an den Inhalt des Objektes `adresse_fra_uas`? Mit dem
Punktoperator.

```{code-cell} ipython3
print(adresse_fra_uas.strasse)
```

```{code-cell} ipython3
print(adresse_fra_uas.postleitzahl)
```

Damit können wir auch ganz normal rechnen, wenn das Attribut eine Zahl ist:

```{code-cell} ipython3
adresse_fra_uas.postleitzahl + 11111
```

Mit dem Punktoperator können wir Attribute eines Objektes auch verändern.
Schauen wir uns zunächst an, welchen Inhalt `adress_fra_uas.postleitzahl` hat,
dann setzen wir eine neue Postleitzahl und schauen erneut, welchen Inhalt
`adress_fra_uas.postleitzahl` jetzt hat:

```{code-cell} ipython3
print('davor: ')
print(adresse_fra_uas.postleitzahl)

adresse_fra_uas.postleitzahl = 77777

print('danach: ')
print(adresse_fra_uas.postleitzahl)
```

**Mini-Übung**   

Schreiben Sie eine Klasse, die Studierende mit den Eigenschaften
* Vorname
* Nachname
* Matrikel-Nummer
verwalten kann.

Testen Sie anschließend Ihre Klasse, indem Sie ein Beispiel ausprobieren.

```{code-cell} ipython3
# Hier Ihr Code:

class Studierende:
    def __init__(self, vorname, nachname, matrikelnummer):
        self.vorname = vorname
        self.nachname = nachname
        self.matrikelnummer = matrikelnummer
        
# Test der Klasse
student1 = Studierende('Alice', 'Wunderland', 123456)
student2 = Studierende('Bob', 'Baumeister', 234567)
student3 = Studierende('Charlie', 'Brown', 345678)

print(student1.vorname)
```

<iframe width="560" height="315" src="https://www.youtube.com/embed/XxCZrT7Z3G4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Falls Sie sich näher mit dem self-Operator beschäftigen möchten, empfehle ich
das nachfolgende Video.

<iframe width="560" height="315" src="https://www.youtube.com/embed/CLoK-_qNTnU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


## Methoden

Es ist bedauerlich, dass wir nicht eine `print()`-Funktion für unsere
Adressen-Klasse zur Verfügung haben. Definieren wir uns einfach eine ...

Da diese Funktion nicht allgemeingültig sein kann, sondern nur für die Objekte
`Adresse` funktionieren kann, gehört sie auch folgerichtig zur Klasse selbst.
Sie ist also keine Funktion, sondern eine Methode. 

Eine Methode wird definiert, indem innerhalb des Anweisungsblocks der Klasse
eine Funktion mit dem Schlüsselwort `def` definiert wird. Der erste Eingabewert
muss zwingend der `self`-Parameter sein. Hier ein Beispiel für eine
Print-Methode: 

```{code-cell} ipython3
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

```{code-cell} ipython3
adresse_fra_uas = Adresse('Nibelungenplatz', 1, 60318, 'Frankfurt am Main')
adresse_fra_uas.print()
```

Vielleicht möchten wir die Print-Ausgabe unterschiedlich haben, z.B. alles in
einer Zeile. Wir erweitern unsere Klasse mit einer neuen Methode namens
`print_einzeilig()`:

```{code-cell} ipython3
class Adresse:
    def __init__(self, strasse, hausnummer, plz, stadt):
        self.strasse = strasse
        self.hausnummer = hausnummer
        self.postleitzahl = plz
        self.stadt = stadt
    
    def print(self):
        print('Straße: ', self.strasse)
        print('Hausnummer: ', self.hausnummer)
        print('Postleitzahl: ', self.postleitzahl)
        print('Stadt: ', self.stadt)
        
    def print_einzeilig(self):
        print('{} {}, {} {}'.format(self.strasse, self.hausnummer, self.postleitzahl, self.stadt ))
```

```{code-cell} ipython3
adresse_fra_uas = Adresse('Nibelungenplatz', 1, 60318, 'Frankfurt am Main')

print('zuerst so:')
adresse_fra_uas.print()

print('\n und \ndann einzeilig:')
adresse_fra_uas.print_einzeilig()
```

````{admonition} Mini-Übung
:class: miniexercise
Fügen Sie Ihrer Klasse zum Verwalten von Studierenden zwei Print-Funktionen
hinzu. Die erste Print-Funktion soll in einer Zeile `Vorname Nachname (xxxxxx)`
ausgeben, wobei das xxxxxx für die Matrikel-Nummer steht, also z.B.
```
Alice Wunderland (123456)
```

ausgeben. Die zweite soll `Nachname, Vorname (Matrikel-Nummer: xxxxxx)`
ausgeben, also z.B.

```
Wunderland, Alice (Matrikel-Nummer: 123456)
```
````


```{code-cell} ipython3
# Ihr Code:

class Studierende:
    def __init__(self, vorname, nachname, matrikelnummer):
        self.vorname = vorname
        self.nachname = nachname
        self.matrikelnummer = matrikelnummer
        
    def print_vorname_nachname_matrikelnummer(self):
        print('{} {} ({})'.format(self.vorname, self.nachname, self.matrikelnummer))
        
    def print_nachname_vorname_matrikelnummer(self):
        print('{}, {} (Matrikel-Nummer: {})'.format(self.nachname, self.vorname, self.matrikelnummer))
        
# Test der Klasse
student1 = Studierende('Alice', 'Wunderland', 123456)
student1.print_vorname_nachname_matrikelnummer()
student1.print_nachname_vorname_matrikelnummer()

student2 = Studierende('Bob', 'Baumeister', 234567)
student2.print_vorname_nachname_matrikelnummer()
student2.print_nachname_vorname_matrikelnummer()
```

Bisher hatten wir nur Methoden ohne weitere Eingabe-Parameter (natürlich mit dem
self-Parameter, der gehört zu allen Methoden dazu). Methoden können aber auch
weitere Parameter haben. Beispielsweise könnte man eine Print-Funktion
schreiben, bei der durch einen Parameter gesteuert wird, ob die Adresse in vier
oder in einer Zeile angezeigt wird:

```{code-cell} ipython3
class Adresse:
    def __init__(self, strasse, hausnummer, plz, stadt):
        self.strasse = strasse
        self.hausnummer = hausnummer
        self.postleitzahl = plz
        self.stadt = stadt
    
    def print(self, einzeilig):
        if einzeilig == True:
            print('{} {}, {} {}'.format(self.strasse, self.hausnummer, self.postleitzahl, self.stadt ))
        else:    
            print('Straße: ', self.strasse)
            print('Hausnummer: ', self.hausnummer)
            print('Postleitzahl: ', self.postleitzahl)
            print('Stadt: ', self.stadt)
    
```

Probieren wir es aus:

```{code-cell} ipython3
adresse_fra_uas = Adresse('Nibelungenplatz', 1, 60318, 'Frankfurt am Main')

print('zuerst einzeilig:')
adresse_fra_uas.print(True)

print('\nund dann vierzeilig:')
adresse_fra_uas.print(False)
```

Zuletzt betrachten wir noch Methoden mit Rückgabewert. Wie bei Funktionen auch
genügt es mit dem Schlüsselwort `return` den Rückgabewert zu definieren. Sehr
häufig ist dabei der Fall, dass eine Eigenschaft des Objektes zurückgegeben
wird. Dann wird in der Regel der Methodenname

```
get_attribut()
```

gewählt.

Aber prinzipiell kann der Rückgabewert auch eine Berechnung oder ähnliches
enthalten.

```{code-cell} ipython3
class Adresse:
    def __init__(self, strasse, hausnummer, plz, stadt):
        self.strasse = strasse
        self.hausnummer = hausnummer
        self.postleitzahl = plz
        self.stadt = stadt
    
    def print(self, einzeilig):
        if einzeilig == True:
            print('{} {}, {} {}'.format(self.strasse, self.hausnummer, self.postleitzahl, self.stadt ))
        else:    
            print('Straße: ', self.strasse)
            print('Hausnummer: ', self.hausnummer)
            print('Postleitzahl: ', self.postleitzahl)
            print('Stadt: ', self.stadt)
 
    def get_stadt(self, grossschreibung):
        if grossschreibung == True:
            return self.stadt.upper()
        else:
            return self.stadt
```

Und auch diese Methode probieren wir aus. Je nachdem, ob die Methode mit `True`
oder `False` aufgerufen wird, gibt die Methode den String `self.stadt` zurück,
entweder normal geschrieben oder in Großbuchstaben. Dabei haben wir die Methode
`.upper()` verwendet, die alle Buchstaben eines Strings in Großbuchstaben
verwandelt.

```{code-cell} ipython3
adresse_fra_uas = Adresse('Nibelungenplatz', 1, 60318, 'Frankfurt am Main')

print('zuerst normal:')
s = adresse_fra_uas.get_stadt(False)
print(s)

print('\nund dann groß geschrieben:')
s = adresse_fra_uas.get_stadt(True)
print(s)
```

````{admonition} Mini-Übung
:class: miniexercise 
Erweitern Sie die Klasse zum Verwalten von Studierenden (Vorname, Name, Matrikel-Nummer) um ein Attribut vorleistung_bestanden. Anfangs sollte dieses Attribut auf `False` gesetzt werden. Implementieren Sie eine Methode, die es ermöglicht, dieses Attribut auf `True` zu setzen.

Testen Sie anschließend Ihre erweiterte Klasse.
````

```{code-cell} ipython3
# Hier Ihr Code:

class Studierende:
    def __init__(self, vorname, nachname, matrikelnummer):
        self.vorname = vorname
        self.nachname = nachname
        self.matrikelnummer = matrikelnummer
        self.vorleistung_bestanden = False

    def print_vorname_nachname_matrikelnummer(self):
        print('{} {} (Matrikel-Nummer: {})'.format(self.vorname, self.nachname, self.matrikelnummer))

    def print_nachname_vorname_matrikelnummer(self):
        print('{}, {} (Matrikel-Nummer: {})'.format(self.nachname, self.vorname, self.matrikelnummer))
        
    def setze_vorleistung_bestanden(self):
        self.vorleistung_bestanden = True
        
student = Studierende('Bob', 'Baumeister', 234567)

print('Vorleistung bestanden???')
print(student.vorleistung_bestanden)

student.setze_vorleistung_bestanden()
print('Vorleistung bestanden???')
print(student.vorleistung_bestanden)  
```

<iframe width="560" height="315" src="https://www.youtube.com/embed/58IjjwHs_4A" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>