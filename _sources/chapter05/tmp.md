Die Scatter-Plots bieten die Möglichkeit, zusätzliche Informationen mit zu
visualisieren. Bei einem Liniendiagramm wird jedem x-Wert ein y-Wert zugeordnet.
Problematisch wird es, wenn wir ein Skalarfeld visualisieren wollen.
Beispielsweise möchten wir in einem Raum an jeder x-Koordinate und jeder
y-Koordinate die Temperatur messen. Mit einem Scatterplot können wir jetzt zu
jedem $(x,y)$ die Temperatur über die Farbe des Markers darstellen. 

Dazu gibt es mehrere Möglichkeiten. Zum einen können wir uns ein Array basteln,
dass die Farben enthält. Auf der Seite 

> https://matplotlib.org/stable/gallery/color/named_colors.html

finden Sie die Namen der wichtigsten Farben. Mit ``.scatter(x,y, c='r')`` färben
Sie beispielsweise alle Marker rot ein.

```{code-cell} ipython3
# data
x = np.random.uniform(0, 5, 10)
y = np.random.uniform(0, 2, 10)
T = np.random.uniform(15,23,10)

# scatter plots
fig, ax = plt.subplots()
ax.scatter(x, y, marker='o', c='r');
```

Mit der Option ``c='aqua'`` wird es grell:

```{code-cell} ipython3
# data
x = np.random.uniform(0, 5, 10)
y = np.random.uniform(0, 2, 10)
T = np.random.uniform(15,23,10)

# scatter plots
fig, ax = plt.subplots()
ax.scatter(x, y, marker='o', c='aqua');
```

Die zweite Möglichkeit ist, eine Farbskala zu nehmen. Alle Werte werden dann
dieser Farbskala zugeordnet. Der minimale Wert bekommt den linken Wert der
Farbskala, der maximale Wert den rechten.

Farbskala heißen im Englischen colormaps. Auf der Internetseite 

> https://matplotlib.org/stable/gallery/color/colormap_reference.html

finden Sie eine Übersicht über mögliche Farbskalen. Schauen wir uns an, wie sich
die Farbe der Marker beim Sinus verändert, wenn wir als Farbskala 'viridis'
wählen. Dazu setzen wir die Option ``cmap='viridis'``:

```{code-cell} ipython3
# data
x = np.linspace(-2*np.pi, 2*np.pi, 50)
y = np.sin(x)

# scatter plots
fig, ax = plt.subplots()
ax.scatter(x, y, marker='o', c=y, cmap='viridis');
```

Und im Winter sieht es mit der Farbskala ``cmap='winter'`` so aus:

```{code-cell} ipython3
# data
x = np.linspace(-2*np.pi, 2*np.pi, 50)
y = np.sin(x)

# scatter plots
fig, ax = plt.subplots()
ax.scatter(x, y, marker='o', c=y, cmap='winter');
```

Wenn die Größe der Marker modifiziert werden soll, gibt es die Option ``s`` wie
size. Entweder wird die Größe konstant auf einen Wert gesetzt, also ``s = 50``,
oder die Größe variiert. Dann muss ``s`` ein Array zugewiesen werden. 

```{code-cell} ipython3
# data
x = np.random.uniform(0, 5, 10)
y = np.random.uniform(0, 2, 10)
T = np.random.uniform(5,25,10)
my_size = np.random.uniform(500,2000,10)

# scatter plots
fig, ax = plt.subplots()
ax.scatter(x, y, s=my_size, c=T);
```

In diesem Fall wurde die Farbskala aus den Temperaturwerten erzeugt. Wir können
aber auch händisch eine Farbskala basteln, indem wir ein Array mit den Farben
zusammenstellen. Beispielsweise wollen wir nun die ersten drei Werte rot, die
nächsten drei Werte grün und die letzten vier Werte blau färben.

```{code-cell} ipython3
meine_farben = ['red', 'red', 'red', 'green', 'green', 'green', 'blue', 'blue', 'blue', 'blue']

x = np.linspace(1,10, 10)
y = np.random.uniform(0, 2, 10)

# scatter plots
fig, ax = plt.subplots()
ax.scatter(x, y, s=50, c=meine_farben);
```