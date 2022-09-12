import numpy as np
import matplotlib.pylab as plt; plt.style.use('bmh')
plt.rcParams['font.family'] = ['TeX Gyre Heros', 'sans-serif']
import pandas as pd


# import data
data_raw = pd.read_csv('/Users/gramschs/lectures/book_ml4ing/doc/chapter10/data/20220801_Marktwert_Bundesliga.csv', skiprows=5, header=0, index_col=0)

# teile die Datensätze nach Ligazugehörigkeit auf
data_liga1 = data_raw[data_raw['Ligazugehörigkeit'] == 'Bundesliga']
data_liga2 = data_raw[data_raw['Ligazugehörigkeit'] == '2. Bundesliga']
data_liga3 = data_raw[data_raw['Ligazugehörigkeit'] == '3. Liga']

# Visualisiere
data_liga2.replace('2. Bundesliga', 1, inplace=True)
data_liga3.replace('3. Liga', 0, inplace=True)

logit_coefficient = 0.73164937  # evaluated by logistic regression
logit_intercept = -7.38380878   # evaluated by logistic regression
x = np.linspace(0, 35).reshape(-1,1)
from scipy.special import expit
y = expit( x * logit_coefficient + logit_intercept)

fig, ax = plt.subplots()
ax.scatter(data_liga3['Wert'], data_liga3['Ligazugehörigkeit'], label='3. Liga')
ax.scatter(data_liga2['Wert'], data_liga2['Ligazugehörigkeit'], label='2. Bundesliga')
ax.plot(x, y, '--', color='k')
ax.set_xlabel('Marktwert in Mio. Euro')
ax.set_title('Marktwerte deutscher Männerfußball am 01.08.2022')
ax.legend()

plt.savefig('/Users/gramschs/lectures/book_ml4ing/src/chapter10_logistic_regression/bundesliga_decision_function.pdf')


