import os
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Zomato Recommender", layout="wide", page_icon="🍽️")
st.title("🍽️ Zomato Restaurant Recommender")

# ------------------------------
# Load Dataset
# ------------------------------

file_path = "zomato_sample.csv"

if not os.path.exists(file_path):
    st.error(f"❌ File '{file_path}' not found in the folder.")
    st.stop()

df = pd.read_csv(file_path, encoding='latin-1')


# ------------------------------
# Clean the Data
# ------------------------------

df = df[df['rate'].notnull()]
df = df[~df['rate'].isin(['NEW', '-'])]
df['rate'] = df['rate'].astype(str).apply(lambda x: x.split('/')[0].strip())
df['rate'] = pd.to_numeric(df['rate'], errors='coerce')

df['approx_cost(for two people)'] = df['approx_cost(for two people)'].astype(str).str.replace(',', '', regex=False)
df['approx_cost(for two people)'] = pd.to_numeric(df['approx_cost(for two people)'], errors='coerce')

df.dropna(subset=['rate', 'approx_cost(for two people)', 'location'], inplace=True)
df_clean = df.drop_duplicates(subset=['name', 'location'])

# ------------------------------
# Recommender System UI
# ------------------------------

st.header("🔍 Restaurant Finder")

location = st.selectbox("📍 Select Location", sorted(df_clean['location'].unique()))
max_cost = st.slider("💰 Max Cost (for two)", 100, 2000, 500, step=50)
min_rating = st.slider("⭐ Min Rating", 1.0, 5.0, 4.0, step=0.1)
top_n = st.number_input("📌 Top N Restaurants", min_value=1, max_value=20, value=5)

def recommend(location, max_cost, min_rating, top_n):
    filtered = df_clean[
        (df_clean['location'].str.lower() == location.lower()) &
        (df_clean['approx_cost(for two people)'] <= max_cost) &
        (df_clean['rate'] >= min_rating)
    ]
    return filtered[['name', 'cuisines', 'rate', 'approx_cost(for two people)', 'rest_type']]\
        .sort_values(by='rate', ascending=False).head(top_n)

if st.button("🔎 Show Recommendations"):
    result = recommend(location, max_cost, min_rating, top_n)
    if result.empty:
        st.warning("No matching restaurants found.")
    else:
        st.success(f"Top {top_n} restaurants in {location}")
        st.dataframe(result.reset_index(drop=True))

# ------------------------------
# Visual Insights Section
# ------------------------------

st.markdown("---")
st.header("📊 Data Insights")

col1, col2 = st.columns(2)

# Most Common Cuisines
with col1:
    st.subheader("🍱 Top 10 Cuisines")
    top_cuisines = df['cuisines'].value_counts().head(10)
    st.bar_chart(top_cuisines)

# Ratings Distribution
with col2:
    st.subheader("⭐ Rating Distribution")
    rating_counts = df['rate'].value_counts().sort_index()
    st.bar_chart(rating_counts)

col3, col4 = st.columns(2)

# Cost Distribution
with col3:
    st.subheader("💰 Cost Distribution (Top 20 Values)")
    cost_counts = df['approx_cost(for two people)'].value_counts().sort_index().head(20)
    st.bar_chart(cost_counts)

# Top 5 Cuisine Pie Chart
with col4:
    st.subheader("🥘 Cuisine Share (Top 5)")
    top5 = df['cuisines'].value_counts().head(5)
    fig, ax = plt.subplots()
    ax.pie(top5, labels=top5.index, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')
    st.pyplot(fig)
