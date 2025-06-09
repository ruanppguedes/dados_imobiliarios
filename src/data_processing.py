import pandas as pd
import re
import sys
import os

# Adiciona o caminho do diretório pai para importar data_collection
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from data_collection import coletar_dados

def converter_milhoes(valor):
    """
    Converte valores no formato 'x milhões' para float.
    """
    if isinstance(valor, str) and 'milhões' in valor:
        return float(re.sub(r'[^\d.]', '', valor)) * 1e6
    return valor

def processar_dados():
    df = coletar_dados()

    # Corrige nomes de colunas com espaços
    df.columns = df.columns.str.strip()

    # Verifica nomes das colunas
    print("Colunas disponíveis:", df.columns.tolist())

    # Converte colunas de texto para valores numéricos
    df['População'] = df['População'].apply(converter_milhoes)
    df['Investimento público (R$)'] = df['Investimento público (R$)'].apply(converter_milhoes)

    return df


# Teste (remova em produção)
if __name__ == '__main__':
    df_processado = processar_dados()
    print(df_processado.head())
    

