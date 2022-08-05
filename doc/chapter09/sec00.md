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

# Pandas anstatt Excel

Nachdem wir mit dem Scikit-Learn-Modell Perzeptron kleine, händisch erzeugte
Beispiele klassifiziert haben, werden wir in den nächsten Abschnitten größere
Datensätze klassifizieren. Typischerweise liegen größere Datensätze in Form von
Tabllen vor. Das verwendetet Datenformat variiert dabei. Manchnal liegen die
Daten im Excel-Format vor, sehr oft jedoch auch im CSV-Format. Davei steht CSV
als Abkürzung für Comma Separated Values, also Werte die durch ein Komma
getrennt werden.

Um Daten in Tabellenform einzulesen und leicht zu verabeiten könnnen. gibt es in
Python das Pandas-Modul, das wir uns nun näher ansehen werden.