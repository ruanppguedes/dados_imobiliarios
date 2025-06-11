import dash
from dash import dcc, html, dash_table
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import os

# Caminho absoluto para o CSV, baseado neste arquivo
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(BASE_DIR, 'data', 'raw', 'dados_imobiliarios.csv')

# Carregar os dados
df = pd.read_csv(csv_path)

# Inicializar o app
app = dash.Dash(__name__)
app.title = "Dashboard Imobiliário"

# Layout
app.layout = html.Div(
    style={'backgroundColor': '#f9f9f9', 'fontFamily': 'Arial, sans-serif'},
    children=[
        html.H1(
            'Dashboard de Predição de Preços Imobiliários',
            style={'textAlign': 'center', 'color': '#2c3e50'}
        ),
        html.P(
            'Visualize a valorização do m² por região ao longo dos anos.',
            style={'textAlign': 'center', 'color': '#7f8c8d'}
        ),
        dcc.Dropdown(
            id='regiao-dropdown',
            options=[{'label': r, 'value': r} for r in df['Região'].unique()],
            value='Sudeste',
            style={'width': '50%', 'margin': 'auto'}
        ),
        dcc.Graph(id='line-chart', style={'marginTop': '30px'}),
        dash_table.DataTable(
            id='data-table',
            columns=[{'name': col, 'id': col} for col in df.columns],
            style_table={'width': '90%', 'margin': 'auto', 'marginTop': '30px'},
            style_header={
                'backgroundColor': '#2c3e50',
                'color': 'white',
                'fontWeight': 'bold'
            },
            style_cell={
                'backgroundColor': '#ecf0f1',
                'color': '#2c3e50',
                'textAlign': 'center'
            }
        )
    ]
)

# Callback
@app.callback(
    [Output('line-chart', 'figure'),
     Output('data-table', 'data')],
    [Input('regiao-dropdown', 'value')]
)
def update_dashboard(regiao):
    df_filtrado = df[df['Região'] == regiao]
    fig = px.line(
        df_filtrado,
        x='Ano',
        y='Preço médio m² (R$)',
        title=f'Valorização do m² na região {regiao}',
        markers=True
    )
    fig.update_layout(
        plot_bgcolor='white',
        paper_bgcolor='white',
        title={'x': 0.5},
        font=dict(color='#2c3e50'),
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=True, gridcolor='lightgrey')
    )
    return fig, df_filtrado.to_dict('records')

# Rodar o app
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8050))
    app.run_server(debug=False, host='0.0.0.0', port=port)
