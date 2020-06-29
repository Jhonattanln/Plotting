## Importar as bibliotecas

import pandas as pd
import matplotlib.pyplot as plt

#Dados
prbr = pd.read_excel(r'C:\Users\Jhona\OneDrive\Área de Trabalho\PRBR11.xlsx', index_col='Data')

#Histograma de distribuição


cple = prbr['CPLE6'].loc['2020-01-01':]
percent = cple.pct_change()
plt.hist(percent, bins=30, color='r')
plt.xlabel('Retornos')
plt.ylabel('Frequência')
plt.show()

#Retornos
plt.plot(percent, color='b')
plt.show()

#Scatter plot
plt.scatter(prbr['RAIL3'], prbr['KLBN11'])
plt.xlabel('RAIL3')
plt.ylabel('KLBN11')
plt.show()

#Series
fig, ax = plt.subplots()
ax.plot(prbr.index, prbr['CPLE6'], prbr['KLBN11'])
ax.set_xlabel('Data')
ax.set_ylabel('Preço')
plt.show()