import streamlit as st
from datetime import date
from backend.service import get_travel_plan
from backend.model import TravelPlanRequest

st.set_page_config(page_title="Shoreward Travel Assistant", page_icon="✈️", layout="wide")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []


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
        request = TravelPlanRequest(
            current_city=current_city,
            destination_city=destination_city,
            start_date=start_date,
            end_date=end_date,
            budget_level=budget_level
        )

        try:
            with st.spinner("Generating your travel plan..."):
                travel_plan = get_travel_plan(request)
                st.success("Here’s your personalized travel plan:")
                st.markdown(travel_plan)
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")