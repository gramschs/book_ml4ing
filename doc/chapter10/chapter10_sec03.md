---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.7
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Nichtlineare SVM

```{admonition} Lernziele
:class: important
* Sie kennen den **Kernel-Trick**.
* Sie können mit den **radialen Basisfunktionen** als neue Option für SVM-Verfahren nichtlinear trennbare Daten klassifizieren.
```

+++

## Nichtlineare trennbare Daten

Für die Support Vecror Machines sind wir bisher davon ausgegangen, dass die
Daten -- ggf. bis auf wenige Ausnahmen -- linear getrennt werden können. Im
Folgenden betrachten wir nun einen künstlichen Messdatensatz, bei dem das
offensichtlich nicht geht. Dazu nutzen wir die in Scikit-Learn integrierte
Funktion `make_circles()`.

```{code-cell} ipython3
import matplotlib.pylab as plt
import matplotlib.pylab as plt; plt.style.use('bmh')
from sklearn.datasets import make_circles

# künstliche Messdaten generieren
X,y = make_circles(100, random_state=0, factor=0.3, noise=0.1)

# künstliche Messdaten visualisieren
fig, ax = plt.subplots()
ax.scatter(X[:,0], X[:,1], c=y, cmap='coolwarm')
ax.set_xlabel('Feature 1')
ax.set_ylabel('Feature 2')
ax.set_title('Künstliche Messdaten');
```

Das menschliche Auge erkennt sofort das Muster in den Daten. Ganz offensichtlich
sind die roten und blauen Punkte kreisförmig angeordnet und können
dementsprechend auch durch einen Kreis getrennt werden. Allerdings wird ein
SVM-Klassifikator, so wie wir das SVM-Verfahren bisher kennengelernt haben,
versagen. Eine Gerade zur Klassifikation der roten und blauen Punkte passt
einfach nicht.

+++

## Aus 2 mach 3

Die Idee zur Überwindung dieses Problems klingt zunächst einmal absurd. Wir
machen aus zwei Features drei Features. Als drittes Feature wählen wir das
Quadrat des Abstandes eines Punktes zum Ursprung. 

```{code-cell} ipython3
import numpy as np

# Extraktion der Daten, damit leichter darauf zugegriffen werden kann
X1 = X[:,0]
X2 = X[:,1]

# neues Feature als Quadrat des Abstandes zum Ursprung
X3 = np.sqrt( X1**2 + X2**2 )

# Visualisierung der künstlichen Messdaten mit neuem Feature
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.scatter(X1, X2, X3, c=y, cmap='coolwarm')
ax.set_xlabel('Feature 1')
ax.set_ylabel('Feature 2')
ax.set_zlabel('neues Feature')
ax.set_title('Künstliche Messdaten');
```

Die obige statische Grafik vermittelt nur ansatzweise den Vorteil, den die neue
Dimension bietet. Daher betrachten wir eine dynamische Ansicht der Daten, die
mittels der Python-Bibliothek [Plotly](https://plotly.com/python/) erzeugt
wurde.

Der Code zur Erzeugung lautet:
```python
import plotly.express as px

fig = px.scatter_3d(x=X1, y=X2, z=X3, color=y, color_continuous_scale=['#3b4cc0', '#b40426'])
fig.show()
```

Da aber Jupyter Book momentan mit der Integration von Plotly Probleme hat, wurde
die interaktive Grafik als HTML exportiert (`fig.write_html('circles_3d.html')`)
und wird hier wiederum importiert.

Bitte drehen Sie die Ansicht solange, bis die z-Achse nach oben zeigt. Die
Punkte bilden eine Art Paraboloiden. In dieser neuen Ansicht können wir eine
Ebene finden, die die roten von den blauen Punkten trennt.

```{code-cell} ipython3
:tags: [remove-input]

from IPython.display import HTML
HTML('circles_3d.html')
```

In der folgenden Grafik ist eine Trennebene eingezeichnet. Wenn wir nun den
Schnitt der Trennebene mit dem Paraboloiden bilden, entsteht eine Kreislinie.
Drehen wir wieder unsere Ansicht zurück, so dass wir von oben auf die
X1-X2-Feature-Ebene blicken, so ist dieser Kreis genau das, was wir auch als
Menschen genommen hätten, um die roten von den blauen Punkten zu trennen.

```{figure} pics/fig10_06_with_plane.png
---
width: 600px
name: fig_10_06
---
Schematische Darstellung der Trennebene in 3D
```


```{figure} pics/fig10_07_with_circle.png
---
width: 600px
name: fig_10_07
---
Schematische Darstellung der Rückprojektion: Trennebene geschnitten mit Paraboloid ergibt eine Kreislinie
```

+++

## Kernel-Trick

Bei diesem künstlichen Datensatz hat das Quadrat der Abstände zum Ursprung als
neues Feature sehr gut funktioniert. Das lag aber unter anderem daran, dass die
Punkte tatsächlich in Kreisen um den Ursprung verteilt waren. Was ist, wenn das
nicht der Fall ist? Wenn der Schwerpunkt der Kreise verschoben wäre, müssten wir
auch die Transformationsfunktion zum Erzeugen des dritten Features in diesen
Schwerpunkt verschieben.

Glücklicherweise übernimmt Scikit-Learn für uns die Suche nach einer passenden
Transformationsfunktion automatisch. Das Verfahren, das dazu in die
SVM-Algorithmen eingebaut ist, wird **Kernel-Trick** genannt. Es beruht darauf,
dass manche Funktionen in ein Skalarprodukt umgewandelt werden können. Und dann
wird nicht das dritte Feature mit der Transformationsfunktion aus den ersten
beiden Features berechnet, was sehr zeitaufwendig werden könnte, sondern die
Transformationsfunktion wird direkt in das Lernverfahren eingebaut. Da
Funktionen, die dafür geeignet sind, werden als **Kernel-Funktionen**
bezeichnet.
 
Am häufigsten zum Einsatz kommt dabei die sogenannte **radiale Basisfunktion**.
Die radialen Basisfunktionen werden mit **RBF** abgekürzt. Sie haben die tolle
Eigenschaft, dass sie nur vom Abstand eines Punktes zum Ursprung abhängen; so
wie unser Beispiel oben.

Um nichtlinear trennbare Daten zu klassifizieren, nutzen wir in Scikit-Learn das
SVC-Lernverfahren. Doch diesmal wählen wir als Kern nicht die linearen
Funktionen, sondern die sogenannten radialen Basisfunktionen RBF. 

```{code-cell} ipython3
from sklearn import svm
svm_modell = svm.SVC(kernel='rbf')
```

Danach erfolgt das Training wie gewohnt mit der `fit()`-Methode, die Bewertung
mit der `score()`-Methode.

```{code-cell} ipython3
svm_modell.fit(X,y);
score = svm_modell.score(X,y)

print('Score: {:.2f}'.format(score))
```

Wir können erneut die Funktion `plot_svc_grenze()`aus dem vorherigen Abschnitt
nutzen, um die Stützvektoren mit einem orangefarbenem Kreis zu markieren und die
Entscheidungsgrenze zu visualisieren. Durch die radialen Basisfunktionen
erhalten wir keinen Kreis, sondern ein deformiertes Ei. Dafür brauchen wir uns
aber keine Gedanken über die Wahl der Funktion zu machen, um das neue Feature
aus den bisherigen zu berechnen.

```{code-cell} ipython3
# Quelle: VanderPlas "Data Science mit Python", S. 482
# modified by Simone Gramsch
import numpy as np

def plot_svc_grenze(model):
    # aktuelles Grafik-Fenster auswerten
    ax = plt.gca()
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()
    # Raster für die Auswertung erstellen
    x = np.linspace(xlim[0], xlim[1], 30)
    y = np.linspace(ylim[0], ylim[1], 30)
    Y, X = np.meshgrid(y, x)
    xy = np.vstack([X.ravel(), Y.ravel()]).T
    P = model.decision_function(xy).reshape(X.shape)
    # Entscheidungsgrenzen und Margins darstellen
    ax.contour(X, Y, P, colors='k', levels=[-1, 0, 1], alpha=0.5, linestyles=['--', '-', '--'])
    # Stützvektoren darstellen
    ax.scatter(model.support_vectors_[:, 0], model.support_vectors_[:, 1], s=300, linewidth=1, facecolors='none', edgecolors='orange');
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)
```

```{code-cell} ipython3
fig, ax = plt.subplots()
ax.scatter(X1, X2, c=y, cmap='coolwarm')
ax.set_xlabel('Feature 1')
ax.set_ylabel('Feature 2')
ax.set_title('Künstliche Messdaten');
plot_svc_grenze(svm_modell)
```

## Zusammenfassung

In diesem Abschnitt haben wir uns mit nichtlinearen Support Vector Machines
beschäftigt. Die Idee zur Klassifizierung nichtlinearer Daten ist, ein neues
Feature hinzuzufügen. Mathematisch gesehen projizieren wir also die Daten mit
einer nichtlinearen Transformationsfunktion in einen höherdimensionalen Raum und
trennen sie in dem höherdimensionalen Raum. Dnn kehren wir durch den Schnitt der
Trennebene mit der Transformationsfunktion wieder in den ursprünglichen Raum
zurück. Wenn wir als Transformationsfunktion die sogenannten Kernel-Funktionen
verwenden, können wir auf die Transformation der Daten verzichten und die
Transformation direkt in die SVM einbauen. Das wird Kernel-Trick genannt und
sorgt für die Effizienz und damit Beliebtheit von SVMs.
