## Importas as bibliotecas

import pandas as pd
import matplotlib.pyplot as plt

#Dados
prbr = pd.read_excel(r'C:\Users\Jhona\OneDrive\Área de Trabalho\PRBR11.xlsx', index_col='Data')

#Histograma de distribuição


cple = prbr['CPLE6']
percent = cple.pct_change()
plt.hist(percent, bins=25)
plt.xlabel('Retornos')
plt.ylabel('Frequência')
plt.show()

#Retornos
plt.plot(percent, color='b')
plt.show()

