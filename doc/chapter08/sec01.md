---
jupytext:
  formats: ipynb,md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.13.8
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

# Das Perzeptron

Neuronale Netze sind sehr beliebte maschinelle Lernverfahren. Das einfachste künstliche neuronale Netz ist das **Perzeptron**. In diesem Abschnitt werden wir das Perzeptron vorstellen.

```{admonition} Lernziele
:class: hint
* Sie können das Perzeptron als mathematische Funktion formulieren und in dem Zusammenhang die folgenden Begriffe erklären:
    * gewichtete Summe (Weighted Sum),
    * Bias oder Bias-Einheit (Bias),
    * Schwellenwert (Threshold)  
    * Heaviside-Funktion (Heaviside Function) und
    * Aktivierungsfunktion (Activation Function).
* Sie können das Perzeptron als ein binäres Klassifikationsproblem des überwachten Lernens einordnen.
```

## Die Hirnzelle dient als Vorlage für künstliche Neuronen

1943 haben die Forscher Warren McCulloch und Walter Pitts das erste Modell einer vereinfachten Hirnzelle präsentiert. Zu Ehren der beiden Forscher heißt dieses Modell MCP-Neuron. Darauf aufbauend publizierte Frank Rosenblatt 1957 seine Idee einer Lernregel für das künstliche Neuron. Das sogenannte Perzeptron bildet bis heute die Grundlage der künstlichen neuronalen Netze. Inspiriert wurden die Forscher dabei durch den Aufbau des Gehirns und der Verknüpfung der Nervenzellen.

```{figure} pics/neuron_wikipedia.svg
---
width: 600px
name: fig_neuron_wikipedia
---
Schematische Darstellung einer Nervenzelle 

([Quelle:](https://de.wikipedia.org/wiki/Künstliches_Neuron#/media/Datei:Neuron_(deutsch)-1.svg) "Schematische Darstellung einer Nervenzelle" von Autor unbekannt. Lizenz: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/))
```

Elektrische und chemische Eingabesignale kommen bei den Dendriten an und laufen im Zellkörper zusammen. Sobald ein bestimmter Schwellwert überschritten wird, wird ein Ausgabesignal erzeugt und über das Axon weitergeleitet. Mehr Details zu Nervenzellen finden Sie bei [Wikipedia/Nervenzelle](https://de.wikipedia.org/wiki/Nervenzelle).


+++

(rasen_nass_problem)=
## Eine mathematische Ungleichung ersetzt das logische Oder

Das einfachste künstliche Neuron besteht aus zwei Inputs und einem Output. Dabei sind für die beiden Inputs nur zwei Zustände zugelassen und auch der Output besteht nur aus zwei verschiedenen Zuständen. In der Sprache des maschinellen Lernens liegt also eine **binäre Klassifikationsaufgabe** innerhalb des **Supervised Learnings** vor.

Beispiel:
* Input 1: Es regnet oder es regnet nicht.
* Input 2: Der Rasensprenger ist an oder nicht.
* Output: Der Rasen wird nass oder nicht.

Den Zusammenhang zwischen Regen, Rasensprenger und nassem Rasen können wir in einer Tabelle abbilden:

Regnet es? | Ist Sprenger an? | Wird Rasen nass?
-----------|------------------|-----------------
nein       | nein             | nein
ja         | nein             | ja
nein       | ja               | ja
ja         | ja               | ja

+++

```{admonition} Mini-Übung
:class: miniexercise
Schreiben Sie ein kurzes Python-Programm, das abfragt, ob es regnet und ob der Rasensprenger eingeschaltet ist. Dann soll der Python-Interpreter ausgeben, ob der Rasen nass wird oder nicht. 
```

```{code-cell} ipython3
# Ihr Code:
```
+++

````{admonition} Lösung
:class: minisolution, toggle
```python
# Eingabe
x1 = input('Regnet es (j/n)?')
x2 = input('Ist der Rasensprenger eingeschaltet? (j/n)')

# Verarbeitung
y = (x1 == 'j') or (x2 == 'j')

# Ausgabe
if y == True:
    print('Der Rasen wird nass.')
else:
    print('Der Rasen wird nicht nass.')
```
````

+++

Für das maschinelle Lernen müssen die Daten als Zahlen aufbereitet werde, damit
die maschinellen Lernverfahren in der Lage sind, Muster in den Daten zu
erlernen. Anstatt "Regnet es? Nein." oder Variablen mit True/False setzen wir
jetzt Zahlen ein. Die Inputklassen kürzen wir mit x1 für Regen und x2 für
Rasensprenger ab. Die 1 steht für ja, die 0 für nein. Den Output bezeichnen wir
mit y. Dann lautet die obige Tabelle für das "Ist-der-Rasen-nass-Problem":

x1 | x2 | y
---|----|---
0  | 0  | 0
1  | 0  | 1
0  | 1  | 1
1  | 1  | 1

+++

```{admonition} Mini-Übung
:class: miniexercise
Schreiben Sie Ihren Programm-Code der letzten Mini-Übung um. Verwenden Sie Integer 0 und 1 für die Eingaben.
```

+++

```{code-cell} ipython3
# Ihr Code:
```
+++

````{admonition} Lösung
:class: minisolution, toggle
```python
# Eingabe
x1 = int(input('Regnet es (ja = 1 | nein = 0)?'))
x2 = int(input('Ist der Rasensprenger eingeschaltet? (ja = 1 | nein = 0)'))

# Verarbeitung
y = (x1 == 1) or (x2 == 1)

# Ausgabe
if y == True:
    print('Der Rasen wird nass.')
else:
    print('Der Rasen wird nicht nass.')
```
````

+++

Nun ersetzen wir das logische ODER durch ein mathematisches Konstrukt:
Wenn die Ungleichung 

$$x_1 \omega_1  +  x_2 \omega_2 \geq \theta \strut$$

erfüllt ist, dann ist $y = 1$ oder anders ausgedrückt, der Rasen wird nass. Und
ansonsten ist $y = 0$, der Rasen wird nicht nass. Allerdings müssen wir noch die
**Gewichte** $\omega_1$ und $\omega_2$ (auf Englisch: weights) geschickt wählen.
Die Zahl $\theta$ ist der griechische Buchstabe Theta und steht als Abkürzung
für den sogenannten **Schwellenwert** (auf Englisch: threshold).

Beispielsweise $\omega_1 = 0.3$, $\omega_2=0.3$ und $\theta = 0.2$ passen:
* $0 \cdot 0.3 + 0 \cdot 0.3 = 0.0 \geq 0.2$ nicht erfüllt
* $0 \cdot 0.3 + 1 \cdot 0.3 = 0.3 \geq 0.2$ erfüllt
* $1 \cdot 0.3 + 0 \cdot 0.3 = 0.3 \geq 0.2$ erfüllt
* $1 \cdot 0.3 + 1 \cdot 0.3 = 0.6 \geq 0.2$ erfüllt


+++

```{admonition} Mini-Übung
:class: miniexercise
Schreiben Sie Ihren Programm-Code der letzten Mini-Übung um. Ersetzen Sie das logische ODER durch die linke Seite der Ungleichung und vergleichen Sie anschließend mit $0.2$, um zu entscheiden, ob der Rasen nass wird oder nicht. 
```

```{code-cell} ipython3
# Ihr Code:
```

+++

````{admonition} Lösung
:class: minisolution, toggle
```python
# Eingabe
x1 = int(input('Regnet es (ja = 1 | nein = 0)?'))
x2 = int(input('Ist der Rasensprenger eingeschaltet? (ja = 1 | nein = 0)'))

# Verarbeitung
y = 0.3 * x1 + 0.3 * x2

# Ausgabe
if y >= 0.2:
    print('Der Rasen wird nass.')
else:
    print('Der Rasen wird nicht nass.')
```
````

+++

## Die Heaviside-Funktion ersetzt die Ungleichung 

Noch sind wir aber nicht fertig, denn auch die Frage "Ist die Ungleichung
erfüllt oder nicht?" muss noch in eine mathematische Funktion umgeschrieben
werden. Dazu subtrahieren wir zuerst auf beiden Seiten der Ungleichung den
Schwellenwert $\theta$:

$$-\theta + x_1 \omega_1  +  x_2 \omega_2 \geq 0. \strut$$

Damit haben wir jetzt nicht mehr einen Vergleich mit dem Schwellenwert, sondern
müssen nur noch entscheiden, ob der Ausdruck $-\theta + x_1 \omega_1 + x_2
\omega_2$ negativ oder positiv ist. Bei negativen Werten, soll $y = 0$ sein und
bei positiven Werten (inklusive der Null) soll $y = 1$ sein. Dafür gibt es in
der Mathematik eine passende Funktion, die sogenannte
[Heaviside-Funktion](https://de.wikipedia.org/wiki/Heaviside-Funktion) (manchmal
auch Theta-, Stufen- oder Treppenfunktion genannt).

```{figure} pics/heaviside_wikipedia.svg
---
width: 600px
name: fig_heaviside_wikipedia
---
Schaubild der Heaviside-Funktion

([Quelle:](https://de.wikipedia.org/wiki/Heaviside-Funktion#/media/Datei:Heaviside.svg) "Verlauf der Heaviside-Funktion auf $\mathbb{R}$" von Lennart Kudling. Lizenz: gemeinfrei)
```

+++

Definiert ist die Heaviside-Funktion folgendermaßen:

$$\Phi(x) = \begin{cases}0:&x<0\\1:&x\geq 0\end{cases}$$

In dem Modul NumPy ist die Heaviside-Funktion schon hinterlegt, siehe 
> https://numpy.org/doc/stable/reference/generated/numpy.heaviside.html   

+++

```{admonition} Mini-Übung
:class: miniexercise
Visualisieren Sie die Heaviside-Funktion für das Intervall $[-3,3]$ mit 101 Punkten. Setzen Sie das zweite Argument einmal auf 0 und einmal auf 2. Was bewirkt das zweite Argument? Sehen Sie einen Unterschied in der Visualisierung? Erhöhen Sie auch die Anzahl der Punkte im Intervall. Wählen Sie dabei immer eine ungerade Anzahl, damit die 0 dabei ist.
```

```{code-cell} ipython3
# Ihr Code:
```

+++

````{admonition} Lösung
:class: minisolution, toggle
```python
import matplotlib.pylab as plt
import numpy as np

x = np.linspace(-3,3, 101)
y0 = np.heaviside(x, 0)     # an der Stelle x=0 ist y=0
y1 = np.heaviside(x, 2)     # an der Stelle x=0 ist y=2

fig, ax = plt.subplots()
ax.plot(x,y0)
ax.plot(x,y1)
ax.grid()
ax.set_title('Heaviside-Funktion');
```
````

+++

Mit der Heaviside-Funktion können wir nun den Vergleich in der
Programmverzweigung mit $0.2$ durch eine direkte Berechnung ersetzen. Schauen
Sie sich im folgenden Programm-Code an, wie wir jetzt ohne logisches Oder und
ohne Programmverzweigung if-else auskommen. 

+++

```python
# Import der notwendigen Module
import numpy as np

# Eingabe
x1 = int(input('Regnet es (ja = 1 | nein = 0)?'))
x2 = int(input('Ist der Rasensprenger eingeschaltet? (ja = 1 | nein = 0)'))

# Verarbeitung
y = np.heaviside(0.3 * x1 + 0.3 * x2, 1.0)

# Ausgabe
ergebnis_als_text = ['Der Rasen wird nass.', 'Der Rasen wird nicht nass.']
print(ergebnis_als_text[int(y)])
``` 

+++

## Das Perzeptron mit mehreren Eingabewerten

Das Perzeptron für zwei Eingabewerte lässt sich in sehr natürlicher Weise auf
viele Eingabewerte verallgemeinern, die auch mehrere Zustände annehmen können.
Bei den Outputs bleiben wir jedoch dabei, dass nur zwei Zustände angenommen
werden können, die wir mit 0 und 1 bezeichnen. Wir betrachten also weiterhin
binäre Klassifikationsaufgaben.

Wenn wir nicht nur zwei, sondern $n$ Eingabewerte $x_i$ haben, brauchen wir
entsprechend auch $n$ Gewichte $\omega_i$. Die Eingabewerte können wir in einem
Spaltenvektor zusammenfassen, also

$$\mathbf{x} = \begin{pmatrix} x_1 \\ x_2 \\ \vdots \\ x_n \end{pmatrix}.$$

Auch die Gewichte können wir in einem Spaltenvektor zusammenfassen, also

$$\boldsymbol{\omega} = \begin{pmatrix} \omega_1 \\ \omega_2 \\ \vdots \\
\omega_n\end{pmatrix}$$

schreiben. Nun lässt sich die Ungleichung recht einfach durch das Skalarprodukt
abkürzen:

$$\mathbf{x}^{T}\boldsymbol{\omega} = x_1 \omega_1 +  x_2 \omega_2 + \ldots +
x_n \omega_n \geq \theta.\strut$$

Wie bei dem Perzeptron mit zwei Eingängen wird der Schwellenwert $\theta$ durch
Subtraktion auf die linke Seite gebracht. Wenn wir jetzt bei dem Vektor
$\boldsymbol{\omega}$ mit den Gewichten vorne den Vektor um das Element
$\omega_0 = -\theta$ ergänzen und den Vektor $\mathbf{x}$ mit $x_0 = 1$
erweitern, dann erhalten wir

$$\mathbf{x}^{T}\boldsymbol{\omega} = 1 \cdot (-\theta) + x_1 \omega_1 + x_2
\omega_2 + \ldots + x_n \omega_n \geq 0.\strut$$

Genaugenommen hätten wir jetzt natürlich für die Vektoren $\boldsymbol{\omega}$
und $\mathbf{x}$ neue Bezeichnungen einführen müssen, aber ab sofort gehen wir
immer davon aus, dass die mit dem negativen Schwellenwert $-\theta$ und $1$
erweiterten Vektoren gemeint sind. Der negative Schwellenwert wird übrigens in
der ML-Community **Bias** oder **Bias-Einheit (Bias Unit)** genannt. 

Um jetzt klassfizieren zu können, wird auf die gewichtete Summe
$\mathbf{x}^{T}\boldsymbol{\omega}$ die Heaviside-Funktion angewendet. Manchmal
wird anstatt der Heaviside-Funktion auch die Signum-Funktion verwendet. Im
Folgenden nennen wir die Funktion, die auf die gewichtete Summe angewendet wird,
**Aktivierungsfunktion**.

````{admonition} Was ist ... ein Perzeptron?
:class: note
Das Perzeptron ist ein künstliches Neuron mit Gewichten $\boldsymbol{\omega}$ und einem Schwellenwert $\theta$. Das Perzeptron berechnet eine gewichtete Summe der Inputs $\mathbf{x}\in\mathbb{R}^n$ und wendet dann eine Aktivierungsfunktion $\Phi$ an, um den Output $y$ zu berechnen:

$$y = \Phi(\mathbf{x}^{T}\boldsymbol{\omega}) = \Phi(-\theta + x_1 \omega_1 + \ldots + x_n \omega_n).$$
````

+++

Eine typische Visualisierung des Perzeptrons ist in der folgenden Abbildung
{ref}`fig_perzeptron` gezeigt. Die Inputs und der Bias werden durch Kreise
symbolisiert. Die Multiplikation der Inputs $x_i$ wird durch Kanten dargestellt,
die mit den Gewichten $\omega_i$ beschriftet sind. Die einzelnen Summanden
$x_i \omega_i$ treffen sich sozusagen im mittleren Kreis, wo auf die gewichtete
Summe dann eine Aktivierungsfunktion angewendet wird. Das Ergebnis, der Output
$y$ wird dann berechnet und wiederum als Kreis gezeichnet. 

```{figure} pics/perzeptron.png
---
width: 600px
name: fig_perzeptron
---
Schematische Darstellung eines Perzeptrons
```

## Zusammenfassung und Ausblick

In diesem Abschnitt haben wir gelernt, wie ein Perzeptron aufgebaut ist und wie
aus den Daten mit Hilfe von Gewichten und einer Aktivierungsfunktion der binäre
Zustand prognostiziert wird. Im nächsten Abschnitt beschäftigen wir uns mit der
Frage, wie die Gewichte gefunden werden.
