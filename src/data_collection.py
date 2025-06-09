import pandas as pd

def coletar_dados():
    # Caminho do arquivo CSV (corrigido)
    caminho_arquivo = '../data/raw/dados_imobiliarios.csv'
    
    # Leitura do arquivo CSV e retorno como DataFrame
    df = pd.read_csv(caminho_arquivo)
    return df

# Teste (remova em produção)
if __name__ == '__main__':
    df = coletar_dados()
    print(df.head())
