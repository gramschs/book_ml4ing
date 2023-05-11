---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.14.5
  kernelspec:
    display_name: python39
    language: python
    name: python3
---

```python
import pandas as pd 

data = pd.read_csv('data/autokauf.csv')
data.head(12)
```

```python
import plotly.express as px
fig = px.scatter_3d(data, x='Zustand', y='Marke', z='Preis', color=data['Kaufentscheidung'])
fig.show()
```
