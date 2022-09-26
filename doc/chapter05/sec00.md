---
jupytext:
  cell_metadata_filter: -all
  formats: ipynb,md:myst
  main_language: python
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.0
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

# Daten visualisieren mit Matplotlib

Die Visualisierung der Daten gehört zu den wichtigsten Schritten der
Datenanalyse. Oft vermittelt die Visualisierung bereits wichtige Erkenntnisse
über die Daten. Zu dem Modul Pandas gehören bereits Methoden zur grafischen
Darstellung der Daten, wie z.B. ``.plot(kind='line')`` oder
``.plot(kind='bar')``. 

```{code-cell} ipython3
import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.rand(7), index=['Mo','Di','Mi','Do','Fr','Sa','So'])
df.plot(kind='bar')
```

Diese Methoden basieren auf einem weiteren Python-Modul, nämlich **Matplotlib**.
Matplotlib werden wir immer dann verwenden, wenn Grafiken komplexer werden (z.B.
mehrere Visualisierungen in einer Grafik) oder wir Grafiken ästhetisch
ansprechend für Publikationen oder Präsentationen aufbereiten wollen.
