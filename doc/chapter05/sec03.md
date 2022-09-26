# Histogramm und Kerndichteschätzung

## Histogramme

Das erste Histogramm, das Ihnen wahrscheinlich begegnet ist, ist der
Notenspiegel in der Schule gewesen. Für jedes Merkmal (hier = Note) des
Datensatzes (hier = Klasse) wird die Anzahl der Schülerinnen und Schüler
angegeben, die diese Note erreicht haben. Eine typische Klassenarbeit könnte
beispielsweise so aussehen:

|1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---| --- |
| 2 | 4  | 8  | 6  | 3  | 1 |

Ein Histogramm ist eine Visualisierung einer solchen Tabelle. Dabei werden in
der Regel Balken benutzt. Auf der x-Achse sind also die Merkmale aufgetragen und
auf der y-Achse finden wir die Anzahl der Merkmale in dem Datensatz. Die Anzahl
kann dabei in absoluten Zahlen angegeben werden oder in relativen (Prozent).  

So sieht das Histogramm des Notenspiegels aus:

```{code-cell} ipython3
# data
x = np.arange(1,7)
y = np.array([2,4,8,6,3,1])

# plot
fig, ax = plt.subplots()
ax.bar(x,y)
ax.set_xlabel('Note')
ax.set_ylabel('Anzahl')
ax.set_title('Erdkunde-Test, Klasse 7b');
```

Diese Analysemethode wird sehr häufig eingesetzt. Daher stellen alle drei Module
Matplotlib, Numpy und Pandas Methoden für Histogramme zur Verfügung:

* Matplotlib-Histogramm:
  https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html
* Numpy-Histogramm:
  https://numpy.org/doc/stable/reference/generated/numpy.histogram.html
* Pandas-Histogramm:
  https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.hist.html

Da wir ohnehin das Histogramm visualisieren wollen, überspringen wir das
Numpy-Histogramm und wenden uns gleich dem Matplotlib-Histogramm zu, das auch
die Basis für das Pandas-Histogramm bildet.

Um die Optionen des Histogramms kennenzulernen, erzeugen wir zunächst eine sehr
kleine Klasse mit 10 Schülerinnen und Schülern und würfeln ihre Noten zufällig
aus. Und nein, in der Klausur werde ich nicht würfeln ;-)

```{code-cell} ipython3
# draw randomly grades
from random import randint, seed
seed(3)
grades = [randint(1, 6) for _ in range(10)]

print('gewürfelte Noten: ', grades)
```

Danach verwenden wir die Methode ``.hist()``, um ein Histogramm zu zeichnen.

```{code-cell} ipython3
# plot histogram
fig, ax = plt.subplots()
ax.hist(grades)
ax.set_xlabel('Note')
ax.set_ylabel('Anzahl Schüler:innen')
ax.set_title('Klassenarbeit');
```

Die Darstellung sieht etwas ungewohnt aus. Mit den Optionen ``bins=``,
``align=`` und ``rwidth=`` wirkt das Histogramm gleich ein wenig vertrauter. 

```{code-cell} ipython3
# generate custom bins
my_bins = [1,2,3,4,5,6,7]

# plot improved histogram
fig, ax = plt.subplots()
ax.hist(grades, bins=my_bins, align='left', rwidth=0.8)
ax.set_xlabel('Note')
ax.set_ylabel('Anzahl Schüler:innen')
ax.set_title('Klassenarbeit');
```

**Mini-Übung**   
Lesen Sie die Dokumentation der <a
href="https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html">Matplotlib-hist-Funktion</a>.
Beantworten Sie anschließend folgende Fragen:
<ul>
    <li>Was sind Bins?</li>
    <li>Welche Bins werden von Matplotlib gewählt, wenn die Option bins auf eine Zahl gesetzt wird, also z.B. <kbd>bins=10</kbd>?</li>
    <li>Welche Bins werden von Matplotlib benutzt, wenn die Option bins auf ein Array gesetzt wird, z.B. <kbd>bins=[1,2,3,4,5,6,7]</kbd>?</li>
    <li>Welche drei Einstellmöglichkeiten gibt es für die Option <kbd>align</kbd>? Probieren Sie alle drei in der vorhergehenden Zelle aus. Welche gefällt Ihnen anm besten?</li>
    <li>Welche Werte dürfen für die Option <kbd>rwidth</kbd> eingesetzt werden? Welcher Wert gefällt Ihnen persönlich am besten? Probieren Sie aus.</li> 
</ul>

```{code-cell} ipython3
# Hier Ihr Code

```

Nicht immer ist die Klasseneinteilung, also die Bins, vorher schon klar.
Beispielsweise könnten wir die Körpergröße der teilnehmenden Studierenden dieser
Vorlesung analysieren wollen. Und dabei sind wir bei der Einteilung in Bins
frei. Beispielsweise könnten wir zwei Bins, nämlich $< 120~cm$ und $\geq 120~cm$
wählen. So richtig viel verrät uns diese Aufteilung über die Verteilung der
Körpergröße jedoch nicht, denn wahrscheinlich sind alle in der letzten Bin. Aber
stattdessen Millimeterschrittezu wählen, wäre zuviel des Guten. Daher
beschäftigen wir uns als Nächstes mit der Wahl der Bin-Größe im Verhältnis zu
den gegebenen Daten.

Im Folgenden erzeugen wir zunächst einmal 1000 normalverteilte Zufallszahlen mit
Mittelwert 0 und Standardabweichung 1. Bei (0,1)-normalverteilten Zufallszahlen
wissen wir, dass
* 68.27 % aller Zahlen zwischen -1 und 1 liegen,
* 95.45 % aller Zahlen zwischen -2 und 2 liegen und
* 99.73 % aller Zahlen zwischen -3 und 3 liegen. Wenn wir jetzt 100 Bins wählen,
wird eine Bin ca. 0.06 breit sein. Wir tragen jetzt die Anzahl der x, die in
eine Bin fällt, im Histogram auf:

```{code-cell} ipython3
# fix random seed and draw N = 10000 normally distributed random numbers
N = 10000
rand = np.random.RandomState(0)
x = rand.randn(N)

# plot histogram with 100 bins
fig, ax = plt.subplots()
ax.hist(x, bins=100);
```

Ändern Sie bitte in der folgenden Code-Zelle die Anzahl der Zufallszahlen.
Probieren Sie z.B. N = 10, 100, 1000 oder 100000000 aus. Ab wann erkennen Sie
die Gauß-Kurve? Gibt es eine Anzahl N von Punkten, ab der sich die Kurve nicht
mehr ändert?

```{code-cell} ipython3
# variation of N
N = 10
rand = np.random.RandomState(0)
x = rand.randn(N)

# plot histogram with 100 bins
fig, ax = plt.subplots()
ax.hist(x, bins=100);
```

In der Praxis ist es nicht so einfach, die Anzahl der Daten zu vergrößern. Daher
probieren wir als nächstes das Umgekehrte. Wir bleiben bei $N=1000$
Zufallszahlen, aber spielen mit der Anzahl der Bins und der Bingröße herum.
Verändern Sie die Anzahl der Bins von 6, 10, 50, 100, 250, 1000, 10000. Was
beobachten Sie?

```{code-cell} ipython3
# fixed N = 1000
N = 1000
rand = np.random.RandomState(0)
x = rand.randn(N)

# variation of bins 
number_bins = 6
fig, ax = plt.subplots()
ax.hist(x, bins=number_bins);
```

**Mini-Übung**   
Lesen Sie die mit ausgelieferte Datei <kbd>data_airbnb_berlin.csv</kbd> ein, die
ursprünglich aus dem Kaggle-Datensatz <a
href="https://www.kaggle.com/brittabettendorf/berlin-airbnb-data">https://www.kaggle.com/brittabettendorf/berlin-airbnb-data</a>
stammt.
<ul>
    <li>Verschaffen Sie sich einen ersten Überblick. Was enthält die Datei für Daten?</li>
    <li>In welcher Spalte stehen die Preise?</li>
    <li>Welches ist der minimale Preis, was muss maximal bezahlt werden?</li>
    <li>Erzeugen Sie ein Histogramm der Preise mit der Standardeinstellung <kbd>bins=10</kbd>. Was fällt Ihnen auf?</li>
    <li>Was könnten sinnvolle Intervalle sein? Teilen Sie den Datensatz in zwei Datensätzen bei einer plausiblem Preisgrenze. Visualisieren Sie beide Datensätze getrennt mit einer passenden Bin-Einteilung. Versehen Sie beide Histogramme mit Achsen- und Titelbeschriftungen.</li>
</ul>
</div>

```{code-cell} ipython3
# Hier Ihr Code
```