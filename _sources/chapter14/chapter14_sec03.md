---
jupytext:
  formats: ipynb,md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.4
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Plots mit Karten

Es ist nützlich, Eigenschaften eines Gebietes auf einer Karte zu visualisieren,
da Karten eine räumliche Darstellung der Daten ermöglichen. Im Gegensatz zu
Tabellen zeigen Karten, wo bestimmte Eigenschaften auftreten und wo nicht.
Karten machen es leicht, Muster und Trends auf einen Blick zu erkennen und die
räumliche Beziehung zwischen verschiedenen Eigenschaften zu verstehen.

Zum Beispiel kann eine Karte die Verbreitung von Krankheiten oder die Verteilung
von Ressourcen in einem Gebiet zeigen. Eine Tabelle kann diese Informationen
ebenfalls darstellen, aber eine Karte gibt einen visuellen Überblick über die
räumliche Verteilung. Karten können auch verwendet werden, um Entscheidungen zu
treffen, wie z.B. Standorte für neue Unternehmen oder Infrastrukturprojekte zu
finden.

Darüber hinaus können Karten auch dazu beitragen, komplexe Daten und
Informationen auf eine einfache und verständliche Weise zu kommunizieren, die
für eine breitere Öffentlichkeit zugänglich ist. Karten sind oft intuitiv und
erfordern keine speziellen Fähigkeiten oder Kenntnisse, um sie zu verstehen.
Daher werden wir uns in diesem Abschnitt der Visualisierung von Karten und
Zusatzinformationen mit dem Python-Modul Folium widmen.

## Lernziele

```{admonition} Lernziele
:class: hint
* Sie kennen das Modul **Folium** und können es importieren.
* Sie können eine Basiskarte mit **.Map()** erstellen.
* Sie können Positionen auf dieser Karte mit **.Marker()** markieren.
* Sie wissen, was eine **GeoJSON** Datei istund wie diese erstellt werden kann.
* Sie wissen, was eine **Choroplethenkarte** ist und können diese mit Folium
  visualisieren.
```

## Karte laden und anzeigen mit Folium

Folium ist ein Python-Modul, das es Benutzern ermöglicht, interaktive Karten zu
erstellen und zu visualisieren. Mit Folium können Sie Daten auf einer Karte
darstellen, indem Sie Markierungen, Polygone, Linien oder Heatmaps hinzufügen.
Es basiert auf dem beliebten JavaScript-Modul Leaflet.js, das eine
benutzerfreundliche Schnittstelle für die Erstellung interaktiver Karten bietet.

Als erstes wird das Module Folium importiert.

```{code-cell} ipython3
import folium
```

Als nächstes erstellen wir eine Karte mit der Basiskarte von OpenStreetMap als
Hintergrund. Dazu wird die Funktion `Map()` verwendet. Der `location`-Parameter
gibt die Koordinaten des Startpunkts an, den wir auf das Zentrum der Frankfurt
UAS (50.110880, 8.679490) setzen. Der `zoom_start`-Parameter legt den Zoomfaktor
fest, bei dem die Karte gestartet wird. Damit das Karten-Objekt, das wir in der
Variable `karte` gespeichert haben, auch angezeigt wird, wird `karte` nochmal
aufgerufen.  

```{code-cell} ipython3
# Laden der Karte  
karte = folium.Map(location=[50.110880, 8.679490], zoom_start=13)

# Anzeige der Karte
karte
```

Folium unterstützt auch verschiedene Kartentypen wie OpenStreetMap, Stamen
Terrain und Stamen Toner, die Sie als Basiskarte verwenden können. Der Kartentyp
wird mit ddem Argument `tiles=` gesetzt. Die verfügbaren Kartentypen können
entweder als String (z.B. 'OpenStreetMap', 'Stamen Terrain', 'Stamen Toner')
oder als URL zu einer eigenen Karte angegeben werden. Der Parameter ist
optional, wenn er ausgelassen wird, wird standardmäßig OpenStreetMap als
Basiskarte verwendet.

```{code-cell} ipython3
# Laden der Karte  
karte = folium.Map(location=[50.110880, 8.679490], zoom_start=13, tiles='Stamen Terrain')

# Anzeige der Karte
karte
```

## Karten markieren

Das Hinzufügen von Markierungen (auch "Pins" genannt) auf einer Karte in Folium
ist einfach und flexibel. Um eine Markierung hinzuzufügen, verwenden wir die
`folium.Marker()`-Methode und geben die Koordinaten des Ortes an, an dem wir die
Markierung hinzufügen möchten.

Zusätzlich können wir der Markierung auch eine Beschreibung in Form eines Popups
hinzufügen. Das Popup wird angezeigt, wenn der Benutzer auf die Markierung
klickt.

Hier ist ein Beispiel, das zeigt, wie Sie eine Markierung auf einer Karte
hinzufügen können:

```{code-cell} ipython3
# Erstellen Sie eine Karte mit einem Startpunkt und Zoomfaktor
karte_markiert = folium.Map(location=[50.13085378545699, 8.691700550887166], zoom_start=15)

# Fügen Sie eine Markierung mit einem Popup hinzu
folium.Marker(location=[50.13085378545699, 8.691700550887166], popup='Hier sitzen wir :-)').add_to(karte_markiert)

# Zeigen Sie die Karte an
karte_markiert
```

In diesem Beispiel erstellen wir eine Karte mit dem Startpunkt Frankfurt UAS und
einem Zoomfaktor von 15. Wir fügen dann eine Markierung an der gleichen Position
wie unser Startpunkt hinzu, indem wir die `folium.Marker()`-Methode verwenden.
Der `popup`-Parameter fügt einen Text hinzu, der angezeigt wird, wenn der
Benutzer auf die Markierung klickt. Zoomen Sie doch einmal weiter in die Karte
hinein!

Es ist auch möglich, mehrere Markierungen auf derselben Karte hinzuzufügen,
indem Sie einfach weitere `folium.Marker()`-Aufrufe machen. Sie können die
Markierungen auch anpassen, indem Sie verschiedene Symbole, Farben und Größen
verwenden, um sie leicht unterscheidbar zu machen.

## Choroplethenkarte und GeoJSON

Eine **Choroplethenkarte** ist eine Art von Karte, bei der bestimmte
geografische Gebiete (z.B. Staaten, Länder, Regionen) anhand einer Farbskala
basierend auf einem numerischen Wert oder einer Rate eingefärbt werden. Diese
Art von Karte wird oft verwendet, um räumliche Muster oder Unterschiede in Daten
darzustellen, wie z.B. Bevölkerungsdichte, Kriminalitätsrate oder
Wirtschaftswachstum. Weitere Details finden Sie bei [Wikipedia →
Choroplethenkarte](https://de.wikipedia.org/wiki/Choroplethenkarte).

Folium bietet ebenfalls die Möglichkeit, Choroplethenkarten zu erstellen. Um
eine Choroplethenkarte mit Folium zu erstellen, benötigen wir
**GeoJSON-Dateien**, die die Geometrien der zu färbenden Gebiete enthalten,
sowie Daten, die diesen Gebieten zugeordnet sind. Die GeoJSON-Dateien können aus
verschiedenen Quellen stammen, z.B. von der Regierung, Open Data-Projekten oder
Geodatenbanken.

Eine GeoJSON-Datei ist ein Dateiformat, das Geodaten im JSON-Format enthält. Es
wird häufig verwendet, um geometrische Formen (z.B. Linien, Polygone) und ihre
zugehörigen Eigenschaften (z.B. Name, ID) zu beschreiben. Es gibt verschiedene
Möglichkeiten, eine GeoJSON-Datei zu erstellen, abhängig von den vorhandenen
Daten und Werkzeugen. 

Der folgende Screencast demonstriert, wie eine GeoJSON-Datei mit Hilfe der
Webseite [http://geojson.io/](http://geojson.io/) erstellt wird.

<video controls loop src="../_static/videos/geojson_erzeugen.mp4"></video>

## GeoJSON in Folium

Um GeoJSON in einer mit Folium erstellten Karte zu verwenden, gehen wir folgt
vor. Zuerst wird die Karte wie üblich mit der `.Map()` Funktion erstellt. Danach
wird eine Choroplethenkarte mit `folium.Choroplth()` erzeugt und mit `.add_to()`
zu der ersten Karte hinzugefügt. Bei der Erstellung der Choroplethenkarte muss
der Pfad und der Dateiname der GeoJSON-Datei bei dem Argument `geo_data`
angegeben werden.  

```{code-cell} ipython3
# Erstellen Sie eine Karte Frankfurt UAS als Ausgangspunkt und Zoomfaktor
karte_geojson = folium.Map(location=[50.13085378545699, 8.691700550887166], zoom_start=13)

geojson_datei = "data/geojson_frankfurt_uas.json"

# Erstellen Sie eine Choroplethenkarte und fügen Sie sie zur Karte hinzu
folium.Choropleth(
    geo_data="data/geojson_frankfurt_uas.json",
    name='choropleth'
).add_to(karte_geojson)

# Zeigen Sie die Karte an
karte_geojson
```

Natürlich ist es auch möglich, das Styling der Choroplethenkarte zu ändern. Dies
wird vor allem dazu genutzt, Gebiete einer Karte mit einer Farbe einzufärben,
die beispielsweise Eigenschaften dieses Gebietes repräsentiert. Für mehr Details
können Sie gerne die [Dokumentation von
Folium](https://python-visualization.github.io/folium/quickstart.html)
hinzuziehen.



