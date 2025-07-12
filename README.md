# 🍽️ Zomato Restaurant Recommender

Discover the best restaurants around you — sorted by rating, price, and location — all in one click.  
This interactive web app recommends top-rated, budget-friendly restaurants using real Zomato data, powered by Python and Streamlit.

👉 **[Try the Live App](https://zomato-recommender.streamlit.app/)**

---

## 🔍 What This App Does

- Recommend restaurants based on your **location**, **budget**, and **preferred rating**
- Show a **filtered list** of top restaurants with name, cuisine, cost, rating, and type
- Visualize insights like:
  - ⭐ Average Rating Distribution
  - 💸 Cost for Two Histogram
  - 🍽️ Most Popular Cuisines

---

## 📂 About the Dataset

- Source: Open Zomato dataset
- Cleaned, transformed, and sampled to optimize speed and performance
- Includes columns like `name`, `location`, `cuisines`, `cost`, `rate`, `rest_type`

---

## 🚀 Tech Stack

- **Python** (Pandas, Matplotlib, Seaborn)
- **Streamlit** (for UI & Deployment)
- **Git & GitHub** (Version control & Hosting)
- **Streamlit Cloud** (Deployed with love 💖)

---

## 🛠️ How to Run Locally

Clone the repository and run:

```bash
git clone https://github.com/your-username/zomato-recommender.git
cd zomato-recommender
pip install -r requirements.txt
streamlit run streamlit_app.py
