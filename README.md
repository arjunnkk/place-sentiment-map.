# 🗺️ Explainable Place Sentiment Map (Auckland)

## 🎯 Goal

This project combines **Geospatial Intelligence**, **Natural Language Processing (NLP)**, and **User-Centred Web Design** to extract and visualize **emotional patterns tied to specific locations** in Auckland.  

It uses **sentiment** and **aspect-based opinion mining**, paired with **Explainable AI (XAI)** techniques to improve **trust and transparency** in how people interpret **place-based user feedback**.

## ⚙️ Data Pipeline

### **Data Collection (Arjun)**
- Google Places API (Text Search & Details)  
- **4 categories:** restaurant, shopping mall, tourist attraction, park  
- ≤5 reviews per place (as per API quota)

### **NLP & Explainability (Shubham)**
- Aspect extraction (`aspect` column)  
- Sentiment classification (`sentiment_label`, `confidence`)  
- Explainability layer: key tokens and confidence per aspect

### **Visualization & Interaction (Abhiram)**
- Conversion of cleaned CSV to GeoJSON  
- Web map built with **Leaflet.js**, **MarkerCluster**, and **Heatmap layers**  
- Category-based markers, interactive filters, tooltips, and side panel

## 🧮 Final Integrated Dataset

| Column            | Description                                                 |
| ----------------- | ----------------------------------------------------------- |
| `place_id`        | Unique Google Maps place ID                                 |
| `place_name`      | Name of the place                                           |
| `address`         | Formatted address                                           |
| `lat`, `lng`      | Latitude and longitude                                      |
| `category`        | One of: restaurant, shopping mall, park, tourist attraction |
| `review_count`    | Number of user reviews collected                            |
| `total_ratings`   | Google star ratings                                         |
| `keywords`        | Top aspects/terms mentioned in reviews                      |
| `sentiment_label` | Positive / Neutral / Negative                               |
| `sentiment_score` | Average sentiment score                                     |
| `aspect`          | Extracted aspect terms                                      |
| `confidence`      | Model confidence score                                      |


## 👥 Team Roles

| Member | Role | Key Responsibilities |
|---------|------|----------------------|
| **Arjun Koodathil Kalliyadan** | Data Collection & Preprocessing | Collected and cleaned place and review data using the Google Places API, standardized categories, and prepared final CSVs for NLP and visualization. |
| **Shubham Mohapatra** | NLP & Explainable AI | Built sentiment and aspect-based opinion models using transformers, generated sentiment scores and labels, and implemented explainability (confidence & aspect tokens). |
| **Abhiram Sathyarajan** | Web Design & Visualization | Developed the front-end visualization using Leaflet.js, integrated GeoJSON data, implemented interactive filters, heatmaps, and category-based visual markers. |

---

## 🌐 Project Architecture

1. **Data Collection & Cleaning**  
   - Extracted places and reviews from Google Places API  
   - Cleaned, normalized, and categorized data (restaurant, park, mall, attraction)  
   - Exported as structured CSVs  

2. **NLP & Explainability**  
   - Applied transformer-based sentiment and aspect extraction  
   - Generated `sentiment_label`, `sentiment_score`, and `aspect` outputs  
   - Merged model output into the main dataset  

3. **Visualization & Web Design**  
   - Converted final dataset to GeoJSON (`shops_sentiment.geojson`) using Python (`convert_to_geojson.py`)  
   - Built a single-page **Leaflet** web app (`shops_sentiment_map.html`)  
   - Added filters for sentiment, keywords, category, rating, and reviews  
   - Integrated **heatmaps** and **category-based icons**  
   - Added **dark mode**, **export**, and **shareable link** functionality  

---

## 🧩 Technology Stack

| Layer | Tools Used |
|--------|-------------|
| **Data & Preprocessing** | Python, Pandas, GeoPandas, Google Places API |
| **NLP & Explainable AI** | Transformers (BERT), Scikit-learn, Python |
| **Visualization** | Leaflet.js, HTML, CSS, JavaScript |
| **Data Format** | CSV → GeoJSON |
| **Hosting** | Localhost / GitHub Pages |

# 🧭 B. Data Collection & Preprocessing (Arjun Koodathil Kalliyadan)

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

## Ethics & limits
- Official Google Places API (no scraping), ≤5 reviews/place (API limit).
- Cafés merged into restaurants for simplicity.
- We plan to add explainability (aspect tokens) in the UI.

## Releases
- `data-freeze-v1` — initial data hand-off and final CSVs.

# 🧭 B. Web Design & Visualization (Abhiram Sathyarajan)

## 🌐 Overview

The **Explainable Place Sentiment Map** is a fully interactive single-page web app built using **Leaflet.js** to visualize sentiment and aspect patterns across Auckland.  
It bridges **AI outputs** and **geospatial visualization** for an explainable and intuitive user experience.

## 💻 Components

| File                       | Description                                                                                      |
| -------------------------- | ------------------------------------------------------------------------------------------------ |
| `convert_to_geojson.py`    | Converts cleaned CSV into **GeoJSON** format suitable for web visualization                       |
| `shops_sentiment.geojson`  | Final spatial dataset with place coordinates, **sentiment scores**, and metadata                  |
| `shops_sentiment_map.html` | Interactive **Leaflet** web app (supports heatmaps, filters, side panel, export, sharing, dark mode) |

## ✨ Key Features

- **Dynamic Filters:** by sentiment, keyword, review count, rating, and category

- **Interactive Map:**
  - Hover popups with place details
  - Click sidebar with full info and top keywords
  - Category-based marker shapes (e.g., 🍴 restaurant, 🛍️ shopping mall, 🌳 park, 📸 tourist attraction)
  - Heatmaps: toggleable by sentiment category (positive/neutral/negative)
  - Dark Mode toggle for accessibility

- **Export & Share:**
  - Export filtered data as CSV
  - Generate shareable map links with current filters and zoom level

- **Responsive & Accessible UI** using plain HTML/CSS/JS (no external frameworks)

## 🚀 Hosting

The visualization is hosted via **GitHub Pages**:

**🔗 Live Map:**  
[https://arjunnkk.github.io/place-sentiment-map/](https://arjunnkk.github.io/place-sentiment-map/)

## 📈 Future Enhancements

- Integrate **aspect-level sentiment visualizations**
- Add **time-based trend filtering**
- Include **model explainability overlays** (SHAP/attention heatmaps) in the UI
- Extend map to **other cities beyond Auckland**
