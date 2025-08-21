# Explainable Place Sentiment Map (Auckland)

This project builds a city-wide dataset of places in Auckland and visualizes sentiment by location with explainable NLP.

## What’s included
- `notebooks/01_data_collection_clean.ipynb` — data collection & cleaning (guarded; no API calls by default)
- `data/final/places.csv` — final places with lat/lng & metadata
- `data/final/reviews.csv` — final reviews (≤5 per place)
- `handoff/nlp_input_reviews.csv` — hand-off for NLP (24,805 rows)
- `.env.example` — environment variable template
- `requirements.txt` — Python deps

## Categories (final)
- restaurant (includes cafés/coffee shops/takeaways)
- tourist attraction
- park
- shopping mall

## Quick start
1. `python -m venv .venv && source .venv/bin/activate` (or use Anaconda)
2. `pip install -r requirements.txt`
3. Copy `.env.example` → `.env` and set `GOOGLE_MAPS_API_KEY=...`
4. Open `notebooks/01_data_collection_clean.ipynb`
   - `RUN_TEXTSEARCH = False`
   - `RUN_DETAILS = False`
   - Run cells that **load** processed data and produce `data/final/*`

> API calls are guarded so reviewers don’t spend quota.

## Data pipeline (summary)
- Google Places Text Search → de-dup by `place_id`
- Place Details → keep metadata + up to 5 reviews/place
- Clean & normalize → map Google types to 4 categories
- Freeze final CSVs → `data/final/*`
- NLP hand-off → `handoff/nlp_input_reviews.csv`

## Final snapshot (v1)
- Places: **<fill number>**
- Reviews: **24,805**
- By category:
  - restaurant: **<n>**
  - tourist attraction: **<n>**
  - park: **<n>**
  - shopping mall: **<n>**

## Ethics & limits
- Official Google Places API (no scraping), ≤5 reviews/place (API limit).
- Cafés merged into restaurants for simplicity.
- We plan to add explainability (aspect tokens) in the UI.

## Releases
- `data-freeze-v1` — initial data hand-off and final CSVs.
