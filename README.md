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
- Used transformer-based models for sentiment classification and aspect keyword extraction
- Output includes: bert_label, bert_pos, bert_neg, bert_score (scaled from -1 to 1), plus a list of keywords
- Sentiment is computed at review level, then aggregated per place
- Future expansion planned for aspect-wise sentiment and explanation overlays (token-level highlights)

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
| `bert_label`      | Positive / Neutral / Negative                               |
| `bert_pos`        | % of reviews with positive sentiment                        |
| `bert_label`      | % of reviews with negative sentiment                        |
| `bert_score`      | Average sentiment score                                     |
| `aspect`          | Extracted aspect terms                                      |
| `confidence`      | Model confidence score                                      |


## 👥 Team Roles

| Member | Role | Key Responsibilities |
|---------|------|----------------------|
| **Arjun Koodathil Kalliyadan** | Data Collection & Preprocessing | Collected and cleaned place and review data using the Google Places API, standardized categories, and prepared final CSVs for NLP and visualization. |
| **Shubham Mohapatra** | NLP & Explainable AI | Applied transformer models to generate sentiment scores and labels, extracted keywords, and aggregated results by place. |
| **Abhiram Sathyarajan** | Web Design & Visualization | Developed the front-end visualization using Leaflet.js, integrated GeoJSON data, implemented interactive filters, heatmaps, and category-based visual markers. |

---

## 🌐 Project Architecture

1. **Data Collection & Cleaning**  
   - Extracted places and reviews from Google Places API  
   - Cleaned, normalized, and categorized data (restaurant, park, mall, attraction)  
   - Exported as structured CSVs  

2. **NLP & Explainability**  
   - Applied siebert/sentiment-roberta-large-english for binary sentiment classification
   - Computed per-place metrics: proportion of positive/negative reviews, overall label, and average score
   - Extracted relevant keywords (aspects) per place

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
| **NLP & Explainable AI** | Transformers (Huggingface- BERT), Scikit-learn, Pandas, Custom rules |
| **Visualization** | Leaflet.js, HTML, CSS, JavaScript |
| **Data Format** | CSV → GeoJSON |
| **Hosting** | Localhost / GitHub Pages |

# 🧭 A. Data Collection & Preprocessing (Arjun Koodathil Kalliyadan)

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

# 🧭 B. NLP & Sentiment Modeling (Shubham Mohapatra)
## Overview
This stage focused on extracting sentiment from user reviews using three different approaches — VADER, TextBlob, and a Transformer-based BERT model — and selecting the most accurate one through human-annotated evaluation.

The output sentiment metrics were aggregated per place to support geospatial visualization and deeper insight into how people feel about different locations in Auckland..

## 💻 Components

| File                       | Description                                                                                      |
| -------------------------- | ------------------------------------------------------------------------------------------------ |
| `Sent.ipynb`               | Performs sentiment analysis on all the reviews extracted using Google API                       |
| `manual labels for reviews.csv`  | Includes 30 test reviews analysed and labelled bu humans as positive, negative or neutral  |
| `sentiment_merged.csv` | Consists of sentiment labels and scores using the best performing sentiment models. |

## Quick start
1. Use Jupyter Notebook and open `Sent.ipynb`.
2. Import `places.csv` and `reviews.csv` from `data/final/*`.
3. Run all the cell blocks.
4. Extract a sample of 30 reviews to test manually annotated human sentiment against labels from VADER, TextBLOB and BERT.
5. Compare the models using classification report.
6. Get outputs for all categories using the best model.


## Ethics & limits
- Sentiment models applied only after data cleaning and anonymization.
- No personal identifiers from reviewers were stored or processed.
- Keyword extraction avoids brand names or individual user mentions.

# 🧭 C. Web Design & Visualization (Abhiram Sathyarajan)

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

# 🧭 User Manual

The **Explainable Place Sentiment Map** is an interactive web application designed to visualize emotional and opinion-based data tied to urban locations in Auckland. It enables users to explore spatial sentiment patterns derived from user-generated Google Maps reviews analyzed by an AI-based sentiment classifier.  

This section functions as a practical user manual for end-users, researchers, and developers intending to interact with or extend the system.

---

## 🚀 Accessing the Application

The application is publicly accessible at:  
🔗 **[https://arjunnkk.github.io/place-sentiment-map](https://arjunnkk.github.io/place-sentiment-map)**

The source code, GeoJSON dataset, and related documentation are hosted on the GitHub repository:  
🔗 **[https://github.com/arjunnkk/place-sentiment-map](https://github.com/arjunnkk/place-sentiment-map)**

The application runs directly in a web browser with no installation required. It has been tested and optimized for **Google Chrome**, **Mozilla Firefox**, and **Microsoft Edge** on both desktop and laptop environments.

---

## 🗺️ Interface Overview

Upon launching the web page, users are greeted with an interactive **Leaflet map** centered on Auckland City.  
The main components of the interface include:

- **Map View** – Displays clustered emoji markers representing different place categories  
  *(e.g., restaurants 🍴, shopping malls 🛍️, parks 🌳, tourist attractions 📸).*

- **Control Panel (Top-Left)** – A white floating interface panel where users can apply filters, toggle layers, or export data.

- **Sidebar (Right)** – A collapsible information panel displaying details about a selected location, including sentiment score, category, ratings, and aspect keywords.

- **Heatmap Toggle Section** – Located below the main filters; users can activate sentiment heatmaps to observe density-based emotional intensity.

- **Dark/Light Mode Button (🌙)** – Allows switching between light and dark themes for accessibility and user comfort.

The interface is fully responsive and dynamically adjusts to different screen sizes and browser window dimensions.

---

## 🧭 Navigating the Map

Users can **pan and zoom** freely using mouse or touch controls.  
Hovering over a marker reveals a tooltip displaying the **place name and address**.  
Clicking a marker opens the **sidebar** with detailed metadata.

### Map Legend (Bottom-Right)
- 🟩 **Green** = Positive sentiment  
- 🟧 **Orange** = Neutral sentiment  
- 🟥 **Red** = Negative sentiment  

Each emoji marker indicates the place’s category, allowing users to visually distinguish locations even in dense clusters.

---

## 🔍 Filtering Data

The **Control Panel** offers several filters that dynamically refine visible map data.  
These filters can be used independently or in combination.

1. **Sentiment Filter:**  
   Dropdown – *All, Positive, Neutral, Negative*  
   > Selecting “Positive” displays only green markers associated with positive sentiment predictions.

2. **Category Filter:**  
   Dropdown – *All, Restaurant, Shopping Mall, Tourist Attraction, Park*  
   > Enables thematic exploration of sentiment trends per category.

3. **Search Box:**  
   Live autocomplete search to find a specific place name.  
   > Example: Typing “Sky Tower” presents matching entries and re-centers the map.

4. **Minimum Reviews and Ratings:**  
   Numeric inputs restrict results to places meeting given thresholds.  
   > Example: Entering “50” in *Min Reviews* shows only highly reviewed locations.

5. **Keyword Filter:**  
   Text input filter based on aspect keywords (e.g., “coffee”, “service”).  
   > The map updates to show places whose extracted keywords include the input term.

Once filters are applied, press **Apply** to update the map instantly.  
**Reset** clears all filters and restores the default view.  

The map’s state is automatically encoded into the URL, allowing users to **bookmark or share** specific configurations.

---

## 🏷️ Viewing Place Details

When a marker is clicked:
- The **sidebar slides out** from the right.
- It displays:
  - Place name and address  
  - Sentiment label (positive / neutral / negative) with colored text  
  - Sentiment score (numerical value from the BERT model)  
  - Category, total ratings, and review count  
  - Top Keywords as grey pill-shaped tags  

**Example:**
> *The Coffee Club, Britomart*  
> Sentiment: **Positive (0.83)**  
> Keywords: *coffee, service, breakfast, friendly staff*

---

## 🌡️ Heatmap Visualization

The lower part of the Control Panel includes checkboxes for:
- ✅ **Positive Heatmap**
- ⚪ **Neutral Heatmap**
- 🔴 **Negative Heatmap**

Each can be toggled independently. These heatmaps aggregate sentiment intensities spatially, creating smooth gradients of emotional density across Auckland.  

- Positive = shades of **green**  
- Negative = shades of **red and pink**  

Users can overlay multiple heatmaps simultaneously to compare sentiment zones.

---

## 🌙 Dark Mode and Accessibility

Clicking the **moon (🌙) button** toggles **dark mode**, switching to a high-contrast theme using CartoDB’s *Dark Matter* basemap.  

This improves comfort for nighttime viewing and accessibility for users with light sensitivity.  
Both the control panel and sidebar adapt their colors automatically for legibility.

---

## 📤 Exporting and Sharing Data

Users can download filtered map data directly from the interface:

1. Click the **Export (📥)** button.  
2. Choose the desired format:
   - **CSV** – For use in spreadsheets or statistical software.  
   - **GeoJSON** – For GIS tools or other web map applications.

Exports include **only the currently visible (filtered) features**, enabling targeted analysis.

The **Share (🔗)** button generates a sharable URL containing all current filter states and map coordinates.  
Copying and sending this link allows others to load the same filtered view — ideal for collaboration or presentations.

---

## 🌐 Browser Compatibility and Requirements

- Works entirely in the browser using **HTML5**, **JavaScript**, and **CSS3**.  
- **No installation or plugins required.**
- JavaScript must be enabled.
- Recommended minimum screen resolution: **1366×768**.
- Optimized for datasets up to **1,000 features** for smooth performance.

Developers can customize the visualization by editing:
- `shops_sentiment_map.html` (main web app)
- `shops_sentiment.geojson` (spatial dataset)

Both files are open-source and available in the GitHub repository.

---

## 🚀 Hosting

The visualization is hosted via **GitHub Pages**:

**🔗 Live Map:**  
[https://arjunnkk.github.io/place-sentiment-map/](https://arjunnkk.github.io/place-sentiment-map/)

## 📈 Future Enhancements

- Integrate **aspect-level sentiment visualizations**
- Add **time-based trend filtering**
- Include **model explainability overlays** (SHAP/attention heatmaps) in the UI
- Extend map to **other cities beyond Auckland**
