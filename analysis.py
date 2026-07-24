import pandas as pd
import plotly.express as px

df = pd.read_csv("sales_data.csv")

fig = px.scatter_geo(
    df,
    lat="Latitude",
    lon="Longitude",
    size="Sales",
    color="Sales",
    hover_name="City",
    title="Geospatial Data Analysis"
)

fig.show()
