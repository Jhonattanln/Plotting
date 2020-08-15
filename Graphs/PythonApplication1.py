import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn

stocks = pd.read_excel(r'C:\Users\Jhona\OneDrive\Área de Trabalho\prbr11.xlsx', index_col = 0)
etf = pd.read_excel(r'C:\Users\Jhona\OneDrive\Área de Trabalho\ETF.xlsx', index_col= 0)

def vol(ação):
    returns = stocks[ação].pct_change().dropna()
    vol = np.std(returns)*np.sqrt(252)
    return vol*100

def retorno (ação, data = '2019-08-07'):
    ret = stocks[ação][-1]/stocks[ação].loc[data]-1
    return ret*100

carteira = ['KLBN11', 'POSI3', 'RAIL3', 'SAPR11', 'CPLE6']

for i in carteira:
    df = carteira = {'Ação' : i, 'Volatilidade': vol(i), 'Retonos' : retorno(i)}
    list1 = [df]
    ações = pd.DataFrame(list1)
    print(ações)

