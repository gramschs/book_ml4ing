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

# Wahrscheinlichkeit und die logistische Funktion


## Lernziele

```{admonition} Lernziele
:class: hint
* TODO
```

## Logistische Funktion ersetzt Heaviside-Funktion

Beim Perzeptron wird auf die gewichtete Summe von Inputs die Heaviside-Funktion angewandt. So simpel die Heaviside-Funktion auch ist, sie hat einen entscheidenen Nachteil. Die Heaviside-Funktion ist unstetig, sie springt von Null auf Eins. Diese Sprungstelle hat die **logistische Funktion** nicht. 

Die logistische Funktion ist defininiert als

$$\phi(z) = \frac{1}{1+e^{-z}}.$$




## Chance für Wahrscheinlichkeiten im Alltag

Im Alltag wird die Wahrscheinlichkeit, dass ein Ereignis eintritt, häufig als eine 
**Chance** angegeben. Beispielsweise sagt eine Person beim
Mensch-ärger-dich-nicht vielleicht: "Meine Chance, eine 6 zu würfeln, ist 1:5."
Seltener wird die Wahrscheinlichkeit eines Ereignisses selbst angegeben, oder
wie oft hört man: "Die Wahrscheinlichkeit, eine 6 zu würfeln, ist 1/6."

Die Chance beschreibt das Verhältnis zwischen der Wahrscheinlichkeit,
dass das Ereignis eintritt, und der Wahrscheinlichkeit, dass das Ereignis nicht
eintritt. Wenn wir die Wahrscheinlichkeit, dass ein Ereignis eintritt, mit $p$
abkürzen, so ist die Wahrscheinlichkeit, dass das Ergeignis nicht eintritt,
gerade $1-p$. Die Formel zur Berechnung einer Chance $R$ lautet also

$$R = \frac{p}{1-p}.$$

Die Wahrscheinlichkeit $p$ ist dabei eine Zahl zwischen Null und Eins, also
$p\in (0,1)$. Dadurch kann die Chancen-Funktion Werte zwischen Null und
Unendlich annehmen, also $R\in (0,\infty)$.

Mehr Details finden Sie bei
[Wikipedia/Chance_(Stochastik)](https://de.wikipedia.org/wiki/Chance_(Stochastik)).

