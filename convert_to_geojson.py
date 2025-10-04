import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
import ast

# Load Excel file
df = pd.read_excel("sentiment_merged.xlsx")

# Clean keywords: convert stringified lists to comma-separated strings
def clean_keywords(val):
    if pd.isna(val):
        return ""
    try:
        parsed = ast.literal_eval(val)  # safely parse "['a','b']" into list
        if isinstance(parsed, list):
            return ", ".join([str(x).strip() for x in parsed])
    except Exception:
        return str(val)
    return str(val)

df["keywords"] = df["keywords"].apply(clean_keywords)

# Normalize category text
if "category" in df.columns:
    df["category"] = df["category"].astype(str).str.strip().str.lower()

# Create geometry from lat/lng
geometry = [Point(xy) for xy in zip(df["lng"], df["lat"])]

# Convert to GeoDataFrame
gdf = gpd.GeoDataFrame(df, geometry=geometry, crs="EPSG:4326")

# Select relevant columns (including top_keywords now)
gdf = gdf[[
    "name", "address", "bert_score", "bert_label",
    "user_ratings_total", "review_count", "keywords", "category", "geometry"
]].rename(columns={
    "name": "place_name",
    "bert_score": "sentiment_score",
    "user_ratings_total": "total_ratings"
})

# Export as GeoJSON
gdf.to_file("shops_sentiment.geojson", driver="GeoJSON")

print("🎉 GeoJSON file created: shops_sentiment.geojson (with top_keywords)")

