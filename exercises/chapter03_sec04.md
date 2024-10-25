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

# Übungen

Gegeben sind folgende Daten zu der Verteilung von Studierenden (männlich/weiblich) auf die Hochschularten Universität und Fachhochschulen (Hochschulen für angewandte Wissenschaften), Quelle: [https://www.statistischebibliothek.de/mir/receive/DESerie_mods_00007716]

```python
bundeslaender = ['Baden-Württemberg', 'Bayern', 'Berlin', 'Brandenburg', 
                 'Bremen', 'Hamburg', 'Hessen', 'Mecklenburg-Vorpommern', 
                 'Niedersachsen', 'Nordrhein-Westfalen', 'Rheinland-Pfalz', 'Saarland',
                 'Sachsen', 'Sachsen-Anhalt', 'Schleswig-Holstein', 'Thüringen']
studierende_universitaeten_maennlich = [85183, 118703, 58682, 15845,
                                        9291, 27444, 68753, 10349, 
                                        62192, 235564, 31487, 7806, 
                                        35826, 15847, 16548, 14350]
studierende_universitaeten_weiblich = [82635, 131158, 65587, 18742,
                                       10181, 28438, 75292, 12821,
                                       69866, 246467, 41755, 8391,
                                       37669, 17061, 22760, 17245]
studierende_fachhochschulen_maennlich = [83058, 81163, 34727, 7778,
                                         8299, 26818, 53998, 7120,
                                         33147, 132976, 21759, 7407,
                                         15497, 12023, 14167, 39330]
studierende_fachhochschulen_weiblich = [65332, 63198, 33333, 6323,
                                        8235, 33558, 47600, 6886,
                                        27157, 106755, 18042, 5767,
                                        11087, 11273, 7943, 63669]
```

```{admonition} Übung 3.1
:class: miniexercise
Laden Sie die Daten zu den Studentinnen an Fachhochschulen. Verschaffen Sie sich einen Überblick über die statistischen Kennzahlen. Lesen Sie dann ab: In welchem Bundesland studieren am wenigsten Studentinnen und im welchem Bundesland am meisten?
```

````{admonition} Lösung
:class: miniexercise, toggle
Zuerst laden wir den Datensatz und verschaffen uns einen Überblick über die statistischen Kennzahlen, um Minimum und Maximum zu bestimmen.

```python
import pandas as pd

stud_fh_weiblich = pd.Series(data=studierende_fachhochschulen_weiblich, index=bundeslaender, name='Studentinnen an Fachhochschulen')
stud_fh_weiblich.describe()
```

Die minimale Anzahl an Studentinnen ist 5767, die maximale Anzahl 106755. Mit `print` lassen wir den kompletten Datensatz anzeigen:

```python
print(stud_fh_weiblich)
```

Wir lesen ab: am wenigsten Studentinnen an Fachhochschulen studieren im Saarland und am meisten in Nordrhein-Westfalen.
````

```{admonition} Übung 3.2
:class: tip
Überprüfen Sie für die anderen drei Datensätze, ob auch dort die beiden gleichen Bundesländer herauskommen. Lassen Sie dazu zuerst das Minimum und das Maximum eines jeden Datensatzes direkt mit einer f-print-Anweisung ausgeben und kontrollieren Sie mit der Anzeige des kompletten Datensatzes, welches Bundesland zum Minimum oder Maximum gehört. Fügen Sie Ihre Antwort als Markdown-Zelle ein.
```

````{admonition} Lösung
:class: miniexercise, toggle
```python
stud_uni_maennlich = pd.Series(data= studierende_universitaeten_maennlich, index=bundeslaender, name='Studenten an Universitäten')
stud_uni_weiblich = pd.Series(data=studierende_universitaeten_weiblich, index=bundeslaender, name='Studentinnen an Universitäten')
stud_fh_maennlich = pd.Series(data=studierende_fachhochschulen_maennlich, index=bundeslaender, name='Studenten an Fachhochschulen')
```

```python
print(f'Uni, männlich: minimale Anzahl = {stud_uni_maennlich.min()}, maximale Anzahl = {stud_uni_maennlich.max()}')
print(stud_uni_maennlich)
```

Ergebnis: minimal im Saarland und maximal in Nordrhein-Westfalen

```python
print(f'Uni, weiblich: minimale Anzahl = {stud_uni_weiblich.min()}, maximale Anzahl = {stud_uni_weiblich.max()}')
print(stud_uni_weiblich)
```

Ergebnis: minimal im Saarland und maximal in Nordrhein-Westfalen

```python
print(f'Fachhochschule, männlich: minimale Anzahl = {stud_fh_maennlich.min()}, maximale Anzahl = {stud_fh_maennlich.max()}')
print(stud_fh_maennlich)
```

Ergebnis: minimal in Mecklenburg-Vorpommern und maximal in Nordrhein-Westfalen

Zusammenfassung: bei den Universitäten studieren die wenigsten Studierenden im Saarland und die meisten Studierenden in Nordrhein-Westfalen. An Fachhochschulen studieren die meisten Studierenden (männlich und weiblich) in Nordrhein-Westfalen. Beim Minimum gibt es jedoch einen Unterschied bei den Geschlechtern. Die wenigsten Studenten findet man in Mecklenburg-Vorpommern, die wenigsten Studentinnen erneut im Saarland.
````

```{admonition} Übung 3.3
:class: miniexercise
Lassen Sie jeden der vier Datensätze durch einen Boxplot darstellen. Verwenden Sie dabei unterschiedliche Variablen zum Speichern des Boxplots (also beispielsweise fig1, fig2, fig3 und fig4). Gibt es Ausreißer?
```

````{admonition} Lösung
:class: miniexercise, toggle
```python
import plotly.express as px


fig1 = px.box(stud_uni_maennlich,
             labels={'variable': '', 'value': 'Anzahl'})
fig1.show()
```

```python
fig2 = px.box(stud_uni_weiblich,
             labels={'variable': '', 'value': 'Anzahl'})
fig2.show()
```

```python
fig3 = px.box(stud_fh_maennlich,
             labels={'variable': '', 'value': 'Anzahl'})
fig3.show()
```

```python
fig4 = px.box(stud_fh_weiblich,
             labels={'variable': '', 'value': 'Anzahl'})
fig4.show()
```

Bei den Studierenden an Universitäten und bei den Studenten an Fachhochschulen ist das Bundesland Nordrhein-Westfalen jeweils als Ausreißer markiert. Dies gilt nicht für die Studentinnen an Fachhochschulen.
````

````{admonition} Übung 3.4
:class: miniexercise
Es wäre schön, die Boxplots in einer Grafik nebeneinander zu stellen. Dazu benötigen wir das Untermodul `Graph Objects` von `Plotly`. Danach können die Grafiken wie folgt kombiniert werden. 

```python
import plotly.graph_objects as go

fig = go.Figure(data = fig1.data + fig2.data + fig3.data + fig4.data)
fig.update_layout(title='Verteilung Studierende 2022')

fig.show()
```

Kopieren Sie den oben Code in eine Code-Zelle und führen Sie die Code-Zelle aus. Vergleichen Sie die vier Boxplots miteinander. Wo liegt der Median am ehesten in der Mitte des Interquartilabstandes?
````

````{admonition} Lösung
:class: miniexercise, toggle
```python
import plotly.graph_objects as go

fig = go.Figure(data = fig1.data + fig2.data + fig3.data + fig4.data)
fig.update_layout(title='Verteilung Studierende 2022')
fig.show()
```

Am ehesten liegt der Median bei den Studenten an Fachhochschulen in der Mitte des Interquartilabstandes. Allerdings ist es visuell schwer einzuordnen, die wenigen Ausreißer führen dazu, dass die Boxplots im unteren Drittel der Grafik platziert sind.    
````

```{admonition} Übung 3.5
:class: miniexercise
Recherchieren Sie im Internet (auch Large Language Models wie ChatGPT oder Bard sind erlaubt), wie die y-Achse auf das Intervall [0, 135000] begrenzt wird, damit der Vergleich leichter fällt und die Ausreißer "abgeschnitten" werden. Modifizieren Sie den gemeinsamen Plot der vier Boxplots entsprechend und beurteilen Sie erneut, wo der Median am ehesten in der Mitte des Interquartilabstandes liegt.
```

````{admonition} Lösung
:class: miniexercise, toggle
```python
# gemeinsame Darstellung der vier Boxplots
fig = go.Figure(data = fig1.data + fig2.data + fig3.data + fig4.data)

# Begrenzung der y-Achse auf das Intervall [0, 150000]
fig.update_layout(title='Verteilung Studierende 2022', yaxis_range=[0,135000])

# Anzeige des Plots
fig.show()
```
````
