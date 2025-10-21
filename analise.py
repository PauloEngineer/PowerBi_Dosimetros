# %%
import pandas as pd
import numpy as np
# %%
df = pd.read_excel('Resultados de análises radiométricas - GLP.xlsx')
# %%
df.head()
# %%
df.info()
# %%
colunas_analise = df[['Ano de Geração','Taxa de Dose Máxima (µSv/h)', 'Resultado_ra226']]
print(colunas_analise.describe())
# %%
taxa_dose = df['Taxa de Dose Máxima (µSv/h)']
print(taxa_dose.describe())
# %%
ano = df['Ano de Geração']
print(ano.describe())
# %%  Garantir que a coluna é numérica
df['Resultado_ra226'] = pd.to_numeric(df['Resultado_ra226'], errors='coerce')


# %%
# Contar quantos valores são <= 8
qtd = (df['Resultado_ra226'] <= 8).sum()
# %%
print("Quantidade de valores <= 8:", qtd, "Unidades.")
# %%
Ra226_menor_8 = ((df['Resultado_ra226'] > 1) & (df['Resultado_ra226'] <= 8)).sum()
# %%
Ra226_menor_8
# %%
