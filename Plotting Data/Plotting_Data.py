## Importar as bibliotecas

import pandas as pd
import matplotlib.pyplot as plt

#Dados
prbr = pd.read_excel(r'C:\Users\Jhona\OneDrive\Área de Trabalho\PRBR11.xlsx', index_col='Data')

#Histograma de distribuição


cple = prbr['CPLE6'].loc['2020-01-01':]
percent = cple.pct_change()
plt.style.use('ggplot')
plt.hist(percent, bins=30, color='r')
plt.xlabel('Retornos')
plt.ylabel('Frequência')
plt.show()

#Retornos
plt.style.use('ggplot')
plt.plot(percent, color='b')
plt.show()

#Scatter plot
plt.style.use('ggplot')
fig, ax = plt.subplots()
ax.scatter(prbr['CPLE6'], prbr['SAPR11'], c=prbr.index)
ax.set_xlabel('CPLE6')
ax.set_ylabel('SAPR11')
plt.show()

#Series
plt.style.use('ggplot')
fig, ax = plt.subplots()
ax.plot(prbr.index, prbr['CPLE6'], prbr['KLBN11'])
ax.set_xlabel('Data')
ax.set_ylabel('Preço')
plt.show()