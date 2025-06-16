import os
import sys
import time
import glob
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Caminho da pasta onde está o módulo 'bib.py'
bibliotecas = r'diretorio do arquivo bib.py'

# Adiciona o diretório ao sys.path
sys.path.append(bibliotecas)

# Importa a função enviar_email do módulo 'bib'
from bib import enviar_email

# Geração de dados simulados
start_date = datetime(2025, 1, 1)
dates = [start_date + timedelta(days=i) for i in range(100)]
values = np.round(np.random.uniform(100, 1000, 100), 2)

df = pd.DataFrame({
    'Data': dates,
    'Valor': values
})

# Criação da coluna AnoMes para agrupamento
df['AnoMes'] = df['Data'].dt.to_period('M')

# Agrupamento por Ano/Mês e soma dos valores
df_agrupado = df.groupby('AnoMes')['Valor'].sum().reset_index()

# Conversão para HTML
html = df_agrupado.to_html(index=False)

# Envio do e-mail com o relatório
enviar_email(
    destinatarios=['leonardoberangergomes@gmail.com'],
    assunto='Relatório Mensal',
    texto_html=html
)
