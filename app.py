import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output

# Crear la app Dash
app = dash.Dash(__name__)

# Datos de ejemplo
df = px.data.gapminder()

# Layout del dashboard
app.layout = html.Div([
    html.H1("Dashboard Interactivo con Dash y Plotly"),
    dcc.Dropdown(
        id='dropdown-pais',
        options=[{'label': c, 'value': c} for c in df['country'].unique()],
        value='Canada',
        clearable=False
    ),
    dcc.Graph(id='grafico-lineas')
])

# Callback para actualizar la gráfica
@app.callback(
    Output('grafico-lineas', 'figure'),
    [Input('dropdown-pais', 'value')]
)
def actualizar_grafico(pais):
    df_filtrado = df[df['country'] == pais]
    fig = px.line(df_filtrado, x='year', y='gdpPercap', title=f'PIB per cápita de {pais}')
    return fig

# Ejecutar la app
if __name__ == '__main__':
    app.run_server(debug=True)
