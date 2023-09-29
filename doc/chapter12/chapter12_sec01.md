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

# Mehrschichtiges Perzeptron

```{admonition} Lernziele
:class: important
* Sie wissen, was ein **Multilayer-Perzeptron** (MLP), also ein mehrschichtiges Perzeptron, ist.
* Sie können den Begriff **Deep Learning** erklären.
* Sie können mit Scikit-Learn ein neuronales Netz trainieren.
```

+++

## Viele Perzeptronen sind ein neuronales Netz

In einem vorhergehenden Kapitel haben wir das Perzeptron, ein künstliches Neuron
kennengelernt. Schematisch können wir es folgendermaßen darstellen:

```{figure} pics/perceptron.svg
---
width: 600px
---
Schematische Darstellung eines Perzeptrons
```

Jedes Eingangssignal wird mit einem Gewicht multipliziert. Anschließend werden
die gewichteten Eingangssignale summiert. Übersteigt die gewichtete Summe einen
Schwellenwert, feuert sozusagen das künstliche Neuron. Das Ausgabesignal wird
aktiviert.

Mathematisch gesehen, wurde nach dem Bilden der gewichteten Summe die
Heaviside-Funktion angewendet. Im Kapitel über die logistische Regression haben
wir bereits gelernt, dass auch andere Funktionen zum Einsatz kommen können. Bei
der logistischen Regression wird beispielsweise die Sigmoid-Funktion verwendet.
Oft werden diese beiden Schritte -- Bilden der gewichteten Summe und Anwenden
der Aktivierungsfunktion -- in einem Symbol gemeinsam dargestellt, wie in der
folgenden Abbildung zu sehen.

```{figure} pics/neuron.svg
---
width: 600px
---
Vereinfachte schematische Darstellung eines Perzeptrons
```

Tatsächlich sind sogar häufig Darstellungen verbreit, bei denen nur noch durch
die Kreise das Perzeptron oder das künstliche Neuron symbolisiert wird.

```{figure} pics/neuron_symbolisch.svg
---
width: 600px
---
Symbolbild eines Perzeptrons bzw. eines künstlichen Neurons
```

Die Idee des mehrschichtigen Perzeptrons ist es, eine oder mehrere
Zwischenschichten einzuführen. In dem folgenden Beispiel wird eine
Zwischenschichtmit zwei Neuronen eingeführt:

```{figure} pics/MLP_1layer_2neurons.svg
---
width: 600px
---
Ein mehrschichtiges Perzeptron (Mulitilayer Perceptron)
```

Es können beliebig viele Zwischenschichten eingeführt werden. Jede neue
Zwischenschicht kann dabei unterschiedliche Anzahlen von Neuronen enthalten.
Insgesamt nennen wir die so entstehende Rechenvorschrift **mehrschichtiges
Perzeptron** oder **Multilayer Perceptron** oder **neuronales Netz**.

Das folgende Video fasst die Struktur eines neuronalen Netzes noch einmal zusammen.

+++

<iframe width="560" height="315" src="https://www.youtube.com/embed/2dBu9wgW2-s" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

+++

## Viele Schichten = Deep Learning

Bei neuronalen Netzen werden viele Schichten mit vielen Neuronen in die
Rechenvorschrift einbezogen. Das führt dazu, dass vor allem sogenannte tiefe
neuronale Netze, also solche mit vielen Schichten, extrem leistungsfähig sind.
Umgekehrt benötigen neuronale Netze aber auch eine große Anzahl an
Trainingsdaten mit guter Qualität. 

Die Firma Linguee verfügte genau über solche Deutsch-Englisch-Übersetzungen.
2017 trainierten Mitarbeiter dieses Unternehmens auf Basis dieser Übersetzungen
ein neuronales Netz, das die bisher dahin existierenden Übersetzungsdienste von
beispielsweise Google Translate bei Weitem übertraf. 2022 wurde das daraus
gegründete Start-Up DeepL zum sogenannten Einhorn, also zu einem Start-Up, das
mit mehr als 1 Milliarde Dollar bewertet wird (siehe
[Artikel](https://www.faz.net/aktuell/wirtschaft/deepl-der-online-uebersetzungsdienst-wird-zum-einhorn-18467883.html)).
