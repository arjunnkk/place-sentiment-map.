# ------------------------------------------------------------
# Script Name: convert_to_geojson.py
# Purpose:
#   Convert a sentiment-annotated Excel dataset (from AI teammate)
#   into a cleaned, geospatially-enabled GeoJSON file for use in
#   the Explainable Place Sentiment Map web visualization.
#
# Dependencies:
#   pandas, geopandas, shapely, ast (all standard or pip-installable)
# ------------------------------------------------------------

import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
import ast

# ------------------------------------------------------------
# STEP 1: Load sentiment dataset
# ------------------------------------------------------------
# Read the Excel file that contains shop-level sentiment scores,
# model labels, review counts, keywords, and location coordinates.
# This file was produced by the AI component of the project.
df = pd.read_excel("sentiment_merged.xlsx")

# ------------------------------------------------------------
# STEP 2: Clean the 'keywords' field
# ------------------------------------------------------------
# The 'keywords' column often contains stringified Python lists,
# e.g., "['service', 'price', 'staff']".
# The goal is to safely convert them into readable comma-separated strings.
def clean_keywords(val):
    """Convert stringified lists like "['a','b']" into a readable string."""
    if pd.isna(val):  # Handle missing (NaN) values
        return ""
    try:
        # Safely evaluate the string using literal_eval to avoid code execution
        parsed = ast.literal_eval(val)
        if isinstance(parsed, list):
            # Join list elements into a comma-separated string
            return ", ".join([str(x).strip() for x in parsed])
    except Exception:
        # If parsing fails, just return the original value as a string
        return str(val)
    return str(val)

# Apply the cleaning function to the 'keywords' column
df["keywords"] = df["keywords"].apply(clean_keywords)

# ------------------------------------------------------------
# STEP 3: Normalize category names
# ------------------------------------------------------------
# Convert all text in the 'category' column to lowercase
# and remove any leading/trailing whitespace.
# This ensures consistency when grouping or filtering later.
if "category" in df.columns:
    df["category"] = df["category"].astype(str).str.strip().str.lower()

# ------------------------------------------------------------
# STEP 4: Create geometric points from latitude/longitude
# ------------------------------------------------------------
# For each row in the dataset, create a Shapely Point object
# using the 'lng' (longitude) and 'lat' (latitude) columns.
# These will serve as the spatial geometry for mapping.
geometry = [Point(xy) for xy in zip(df["lng"], df["lat"])]

# ------------------------------------------------------------
# STEP 5: Convert to a GeoDataFrame
# ------------------------------------------------------------
# Convert the cleaned pandas DataFrame to a GeoDataFrame
# by assigning the geometry column and specifying the coordinate
# reference system (CRS) as WGS84 (EPSG:4326), which is standard
# for web mapping and GPS coordinates.
gdf = gpd.GeoDataFrame(df, geometry=geometry, crs="EPSG:4326")

# ------------------------------------------------------------
# STEP 6: Select and rename relevant columns
# ------------------------------------------------------------
# Only keep the columns necessary for visualization.
# Rename some fields to more intuitive names used in the map UI.
gdf = gdf[[
    "name", "address", "bert_score", "bert_label",
    "user_ratings_total", "review_count", "keywords", "category", "geometry"
]].rename(columns={
    "name": "place_name",
    "bert_score": "sentiment_score",
    "user_ratings_total": "total_ratings"
})

# ------------------------------------------------------------
# STEP 7: Export as GeoJSON
# ------------------------------------------------------------
# Save the resulting GeoDataFrame to a GeoJSON file that can be
# loaded directly by Leaflet.js on the frontend.
# The driver parameter ensures output in standard GeoJSON format.
output_file = "shops_sentiment.geojson"
gdf.to_file(output_file, driver="GeoJSON")

print(f"🎉 GeoJSON file created: {output_file} (with top_keywords)")
