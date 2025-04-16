import streamlit as st
import requests
from datetime import date

st.set_page_config(page_title="Shoreward Travel Assistant", page_icon="✈️", layout="wide")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# API configuration
API_URL = "http://localhost:8000/plan"  # Adjust according to your backend

st.title("✈️ Shoreward Travel Planning Assistant")
st.markdown("_Tell us your trip details and get a travel plan powered by AI._")

# Input form
with st.form("travel_form"):
    current_city = st.text_input("Current City", placeholder="e.g., New York")
    destination_city = st.text_input("Destination City", placeholder="e.g., Tokyo")
    start_date = st.date_input("Start Date", min_value=date.today())
    end_date = st.date_input("End Date", min_value=start_date)
    budget_level = st.selectbox(
        "Budget Level",
        options=["super budget", "midclass", "luxury"]
    )
    submitted = st.form_submit_button("Generate Travel Plan")

# Form submission logic
if submitted:
    if not current_city or not destination_city:
        st.error("Please fill in both cities.")
    elif start_date > end_date:
        st.error("Start date must be before or equal to end date.")
    else:
        # Prepare data
        payload = {
            "current_city": current_city,
            "destination_city": destination_city,
            "start_date": str(start_date),
            "end_date": str(end_date),
            "budget_level": budget_level
        }

        try:
            with st.spinner("Generating your travel plan..."):
                response = requests.post(API_URL, json=payload)
                response.raise_for_status()
                travel_plan = response.json().get("plan", "")
                st.success("Here’s your personalized travel plan:")
                st.markdown(travel_plan)
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")