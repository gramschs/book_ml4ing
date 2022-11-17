from sklearn.datasets import make_circles

X,y = make_circles(100, random_state=0, factor=0.3, noise=0.1)

import numpy as np

X1 = X[:,0]
X2 = X[:,1]

X3 = np.sqrt( X1**2 + X2**2 )

import plotly.express as px

fig = px.scatter_3d(x=X1, y=X2, z=X3, color=y, color_continuous_scale='rdbu')
fig.write_html("circles_3d.html")