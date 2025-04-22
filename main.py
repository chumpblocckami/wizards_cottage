import streamlit as st
import pandas as pd
import plotly.express as px


# === Data Preprocessing ===
df = pd.read_csv("./assets/metagame.csv")
df['match_winrate'] = df['match_winrate'].str.rstrip('%').astype(float)
df['game_winrate'] = df['game_winrate'].str.rstrip('%').astype(float)
df['percentage'] = df['percentage'].str.rstrip('%').astype(float)

st.title("Pauper Meta Analysis (Past 30 Days)")
min_date = "2025-03-22"
max_date="2025-04-22"
mtg_format="Pauper"

st.caption(f"From {min_date} to {max_date} | Format: {mtg_format}")

# === Match Winrate Bar Chart ===
st.subheader("Top Archetypes by Match Winrate")
top_archetypes = df.sort_values('match_count', ascending=False).head(20)

fig = px.bar(top_archetypes.sort_values('match_winrate'),
             x='match_winrate',
             y='archetype',
             orientation='h',
             labels={'match_winrate': 'Match Winrate (%)', 'archetype': 'Archetype'},
             text='match_winrate')

st.plotly_chart(fig, use_container_width=True)

# === Winrate vs Popularity Scatter Plot ===
st.subheader("Winrate vs Popularity")
fig2 = px.scatter(df,
                  x='percentage',
                  y='match_winrate',
                  size='match_count',
                  hover_name='archetype',
                  labels={'percentage': 'Meta Share (%)', 'match_winrate': 'Match Winrate (%)'},
                  title='Archetype Performance')

st.plotly_chart(fig2, use_container_width=True)

# === Full Data Table ===
st.subheader("Full Archetype Data")
st.dataframe(df[['archetype', 'count', 'percentage', 'match_count', 'match_winrate', 'game_winrate']].sort_values(by='match_count', ascending=False), use_container_width=True)
