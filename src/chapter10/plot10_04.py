from sklearn.datasets import make_blobs
from sklearn.svm import SVC

import matplotlib.pylab as plt; plt.style.use('bmh')

import numpy as np

# Quelle: VanderPlas Data Science mit Python, S. 482
def plot_svc_decision_function(model, ax=None, plot_support=True):
    """Diagramm der Entscheidungsfunktion eines zweidimensionalen SVC erstellen"""
    if ax is None:
        ax = plt.gca()
        xlim = ax.get_xlim()
        ylim = ax.get_ylim()
        # Raster für die Auswertung erstellen
        x = np.linspace(xlim[0], xlim[1], 30)
        y = np.linspace(ylim[0], ylim[1], 30)
        Y, X = np.meshgrid(y, x)
        xy = np.vstack([X.ravel(), Y.ravel()]).T
        P = model.decision_function(xy).reshape(X.shape)
        # Entscheidungsgrenzen und Margins darstellen
        ax.contour(X, Y, P, colors='k', levels=[-1, 0, 1], alpha=0.5, linestyles=['--', '-', '--'])
        # Stützvektoren darstellen
        if plot_support:
            ax.scatter(model.support_vectors_[:, 0], model.support_vectors_[:, 1], s=300, linewidth=1, facecolors='none');
            ax.set_xlim(xlim)
            ax.set_ylim(ylim)

X, y = make_blobs(n_samples=60, centers=2, random_state=0, cluster_std=0.8)

for (C,index) in zip([1e6, 10, 1, 0.1, 0.01], ['a', 'b', 'c', 'd', 'e']):
    fig, ax = plt.subplots()
    ax.scatter(X[:,0], X[:,1], c=y, cmap='coolwarm')
    ax.set_xlabel('Feature 1')
    ax.set_ylabel('Feature 2')
    ax.set_title('SVM mit Soft Margin, C = {}'.format(C));

    model = SVC(kernel='linear', C=C)
    model.fit(X,y)

    plot_svc_decision_function(model, ax=None, plot_support=True)
    filename = 'fig10_04' + index + '.pdf'
    fig.savefig(filename)