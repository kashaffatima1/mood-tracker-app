import streamlit as st
import pandas as pd
import datetime
import csv
import os

MOOD_FILE = "mood_log.csv"

def load_mood_data():
    if os.path.exists(MOOD_FILE):
        return pd.read_csv(MOOD_FILE)
    return pd.DataFrame(columns=["Date", "Mood"])
    
    
def save_mood_data(date, mood):
    file_exists = os.path.isfile(MOOD_FILE)

    with open(MOOD_FILE, "a", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([date, mood])

st.title("Mood Tracker")

today = datetime.date.today()

st.subheader("How are you feeling today?")

mood = st.selectbox("Select your mood", ["Happy", "Sad", "Angry", "Neutral"])

if st.button("Log Mood"):
    save_mood_data(today, mood)
    st.success("Mood logged successfully")

data = load_mood_data()

if not data.empty:
    st.subheader("Mood Trends Over Time")

    data["Date"] = pd.to_datetime(data["Date"]) 

    mood_counts = data.groupby("Mood").count()["Date"]

    st.bar_chart(mood_counts)


