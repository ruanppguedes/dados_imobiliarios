import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_percentage_error, r2_score
import sys
import os
import numpy as np


# Adiciona o caminho do diretório pai para importar data_processing
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), '..', 'src')))
from data_processing import processar_dados

def treinar_modelo():
    # Processar os dados
    df = processar_dados()
    
    # Separar variáveis preditoras e alvo
    X = df[['IPCA (%)', 'SELIC (%)', 'População', 'Renda per capita (R$)', 'Investimento público (R$)']]
    y = df['Preço médio m² (R$)']
    
    # Dividir os dados em treino e teste
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Treinar o modelo de regressão linear
    modelo = LinearRegression()
    modelo.fit(X_train, y_train)
    
    # Fazer previsões no conjunto de teste
    y_pred = modelo.predict(X_test)
    
    # Avaliar o modelo
    
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    mape = mean_absolute_percentage_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    # Imprimir os resultados
    print(f"RMSE: {rmse}")
    print(f"MAPE: {mape}")
    print(f"R²: {r2}")
    
    # Salvar os resultados em um DataFrame
    resultados = pd.DataFrame({
        'RMSE': [rmse],
        'MAPE': [mape],
        'R²': [r2]
    })
    
    # Criar pasta se não existir
    os.makedirs('../data/processed', exist_ok=True)
    
    # Salvar os resultados em um arquivo CSV
    resultados.to_csv('../data/processed/model_evaluation_metrics.csv', index=False)

# Teste (remova em produção)
if __name__ == '__main__':
    treinar_modelo()
