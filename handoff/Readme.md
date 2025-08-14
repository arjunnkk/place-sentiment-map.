# NLP Hand-off (v1)
File: `nlp_input_reviews.csv`
Columns: `review_id, place_id, text, rating, time, language`

Scope:
- Categories: restaurant, tourist attraction, park, shopping mall (cafés merged into restaurant).
- Reviews per place: up to 5 (Google cap).
- Text normalized to single-line, UTF-8.

Please return:
- `aspect_sentiment.csv` with columns:
  `review_id, aspect, sentiment (positive|negative|neutral), confidence, top_tokens_json`

Starter aspects:
- Food/taste, service, cleanliness, price/value, ambience, wait-time, accessibility/parking,
  facilities (parks/malls), safety, scenery, family-friendly, crowding.
