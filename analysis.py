import pandas as pd
import plotly.express as px

# Load dataset
df = pd.read_csv("sales_data.csv")

print("Sales Data")
print(df)

# Create Geospatial Map
fig = px.scatter_geo(
    df,
    lat="Latitude",
    lon="Longitude",
    hover_name="City",
    size="Sales",
    color="Sales",
    title="Geospatial Sales Analysis"
)

fig.update_layout(
    geo=dict(
        scope="asia",
        showland=True
    )
)

fig.show()

# Best location
best = df.loc[df["Sales"].idxmax()]
print("\nRecommended Expansion Location")
print(best["City"], "-", best["Sales"])
