import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Initialize the Dash app
app = dash.Dash(__name__)

# Load the data
hour_df = pd.read_csv('path_to_your_bike_sharing_data.csv')  # Update with actual path to the dataset
hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])

# Define layout
app.layout = html.Div([
    html.H1("Bike Sharing Dashboard"),
    
    # Dropdown to select the question to visualize
    dcc.Dropdown(
        id='business-question-dropdown',
        options=[
            {'label': 'Distribusi Jumlah Rental Sepeda Berdasarkan Musim', 'value': 'season'},
            {'label': 'Hubungan Antara Jam dan Jumlah Rental Sepeda', 'value': 'hr'},
            {'label': 'Faktor-Faktor yang Mempengaruhi Jumlah Rental Sepeda', 'value': 'factors'}
        ],
        value='season',
        style={'width': '50%'}
    ),
    
    # Graph for the plots
    dcc.Graph(id='bike-rental-graph'),
    
    # Slider for selecting hours (only applicable for hour-based analysis)
    dcc.Slider(
        id='hour-slider',
        min=0,
        max=23,
        step=1,
        value=12,
        marks={i: str(i) for i in range(24)},
        style={'width': '50%'}
    )
])

# Define callback to update graph based on dropdown selection
@app.callback(
    Output('bike-rental-graph', 'figure'),
    [Input('business-question-dropdown', 'value'),
     Input('hour-slider', 'value')]
)
def update_graph(selected_question, selected_hour):
    if selected_question == 'season':
        # Plot distribution based on season
        fig = px.histogram(hour_df, x='season', y='cnt', title="Jumlah Rental Sepeda Berdasarkan Musim")
        return fig
    
    elif selected_question == 'hr':
        # Plot relationship between hour and bike rental count
        filtered_df = hour_df[hour_df['hr'] == selected_hour]
        fig = px.scatter(filtered_df, x='dteday', y='cnt', title=f"Jumlah Rental Sepeda pada Jam {selected_hour}")
        return fig
    
    elif selected_question == 'factors':
        # Plot factors like temperature, humidity, and weather situation affecting rentals
        fig = px.scatter(hour_df, x='temp', y='cnt', color='weathersit', title="Faktor yang Mempengaruhi Jumlah Rental Sepeda")
        return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)

# ================== Footer ==================
st.markdown("---")
st.caption("📌 Dibuat oleh **Rafi Nanda Edtrian** | Proyek Analisis Data Dicoding")
