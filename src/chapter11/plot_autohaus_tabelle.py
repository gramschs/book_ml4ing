

import pandas as pd 

data = pd.read_csv('autokauf.csv')
data.head(12)


data_numerisch = data.copy()
data_numerisch.replace('neu', 1, inplace=True)
data_numerisch.replace('gebraucht', 0, inplace=True)

data_numerisch.replace('Audi', 0, inplace=True)
data_numerisch.replace('BMW', 1, inplace=True)
data_numerisch.replace('Citroën', 1, inplace=True)

data_numerisch.replace('ja', 1, inplace=True)
data_numerisch.replace('nein', 0, inplace=True)


import plotly.express as px
fig = px.scatter_3d(data_numerisch, x='Zustand', y='Marke', z='Preis', color=data['Kaufentscheidung'],
color_discrete_sequence=['#3b4cc0', '#b40426'])
fig.write_html('autohaus_tabelle_3dscatter.html')