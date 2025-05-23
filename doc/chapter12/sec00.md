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

# 12. Perzeptron

Durch neuronale Netze, die tief verschachtelt sind (= tiefe neuronale Netze =
deep neural network), gab es im Bereich des maschinellen Lernens einen
Durchbruch. Neuronale Netze sind eine Technik aus der Statistik, die bereits in
den 1940er Jahren entwickelt wurde. Seit ca. 10 Jahren erlebt diese Technik
verbunden mit Fortschritten in der Computertechnologie eine Renaissance.

Neuronale Netze bzw. Deep Learning kommen vor allem da zum Einsatz, wo es kaum
systematisches Wissen gibt. Damit neuronale Netze erfolgreich trainiert werden
können, brauchen sie sehr große Datenmengen. Nachdem in den letzten 15 Jahren
mit dem Aufkommen von Smartphones die Daten im Bereich Videos und Fotos massiv
zugenommen haben, lohnt sich der Einsatz der neuronalen Netze für
Spracherkennung, Gesichtserkennung oder Texterkennung besonders.

Beispielsweise hat ein junges deutsches Start-Up-Unternehmen 2017 aus einem
neuronalen Netz zum Übersetzen Englisch <-> Deutsch eine Webanwendung entwickelt
und ins Internet gestellt, die meinen Alltag massiv beeinflusst:

> DeepL.com

Auf der Seite

> [https://www.deepl.com/en/blog/how-does-deepl-work](https://www.deepl.com/en/blog/how-does-deepl-work)

finden Sie einen kurzen Übersichtsartikel dazu, wie DeepL funktioniert.

Die Grundlage der neuronalen Netze ist das Perzeptron, mit dem wir uns in diesem
Kapitel beschäftigen.

Kapitelübersicht:

```{tableofcontents}
```
