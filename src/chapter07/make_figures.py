#%%
import matplotlib.pylab as plt
plt.style.use('bmh')

import numpy as np



#%%
x = np.linspace(0, 1, 250)
y_test = -(x-0.6)**2 + 4.0
y_train = y_test - 0.3 + np.exp(x-1.0)


#%%
fig, ax = plt.subplots()
ax.plot(x, y_train, label='Score Trainingsdaten', linewidth=2, linestyle='dashed', color='k')
ax.plot(x, y_test, label='Score Testdaten', linewidth=2, linestyle = 'dotted', color='k')

ax.set_xlim([0.0, 1.0])
ax.set_ylim([3.5, 4.8])
ax.set_xticks([0.05, 0.95])
ax.set_xticklabels(['niedrig', 'hoch'])
ax.set_yticks([3.6, 4.5])
ax.set_yticklabels(['schlecht', 'sehr gut'])

ax.set_xlabel('Modellkomplexität', size=14)
ax.set_ylabel('Score', size=14)
ax.set_title('Prinzipielle Validierungskurven')
ax.grid(False)
ax.legend(bbox_to_anchor=(0.0, 1), loc='upper left')
plt.tight_layout()
plt.savefig('validierungskurven_dotted.pdf')
plt.show()
# %%
