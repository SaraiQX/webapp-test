from dash import Dash, html
import dash_bio as dashbio

app = Dash(__name__)

app.layout = html.Div([
    dashbio.Jsme(
        width='100%',
        height='50vh',
    ),
])

if __name__ == '__main__':
    app.run_server(debug=True)
