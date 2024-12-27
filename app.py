import streamlit as st
from PIL import Image

# Define emission factors (example values, replace with accurate data)
EMISSION_FACTORS = {
    "India": {
        "Transportation": 0.14,  # kgCO2/km
        "Electricity": 0.82,  # kgCO2/kWh
        "Diet": 1.25,  # kgCO2/meal
        "Waste": 0.1  # kgCO2/kg
    }
}

# Set wide layout and page name
st.set_page_config(layout="wide", page_title="Personal Carbon Calculator", page_icon="🌍")

# Add a header image (optional)
st.image("https://via.placeholder.com/1200x300?text=Personal+Carbon+Calculator", use_column_width=True)

# App title
st.markdown(
    """
    <h1 style='text-align: center; color: #1f77b4;'>Personal Carbon Calculator 🌍</h1>
    <p style='text-align: center; color: gray;'>Calculate your yearly carbon footprint and learn how to reduce it!</p>
    <hr style='border: 1px solid #ddd;'>
    """,
    unsafe_allow_html=True
)

# Sidebar for country selection
st.sidebar.markdown(
    """
    <h2 style='color: #ff6600;'>Country Selection</h2>
    """,
    unsafe_allow_html=True
)
country = st.sidebar.selectbox("🌍 Select your country:", ["India"], index=0)

# Main app layout
st.markdown("<h3 style='color: #1f77b4;'>Input Your Details</h3>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("<h4 style='color: #ff6600;'>🚗 Daily Commute Distance (in km):</h4>", unsafe_allow_html=True)
    distance = st.slider("", 0.0, 100.0, value=10.0, key="distance_input")

    st.markdown("<h4 style='color: #ff6600;'>💡 Monthly Electricity Consumption (in kWh):</h4>", unsafe_allow_html=True)
    electricity = st.slider("", 0.0, 1000.0, value=200.0, key="electricity_input")

with col2:
    st.markdown("<h4 style='color: #ff6600;'>🗑️ Weekly Waste Generated (in kg):</h4>", unsafe_allow_html=True)
    waste = st.slider("", 0.0, 100.0, value=5.0, key="waste_input")

    st.markdown("<h4 style='color: #ff6600;'>🍽️ Number of Meals Per Day:</h4>", unsafe_allow_html=True)
    meals = st.number_input("", min_value=1, max_value=10, value=3, step=1, key="meals_input")

# Normalize inputs
distance *= 365  # Daily to yearly
electricity *= 12  # Monthly to yearly
meals *= 365  # Daily to yearly
waste *= 52  # Weekly to yearly

# Calculate carbon emissions
transportation_emissions = EMISSION_FACTORS[country]["Transportation"] * distance
electricity_emissions = EMISSION_FACTORS[country]["Electricity"] * electricity
diet_emissions = EMISSION_FACTORS[country]["Diet"] * meals
waste_emissions = EMISSION_FACTORS[country]["Waste"] * waste

# Convert to tonnes and round
transportation_emissions = round(transportation_emissions / 1000, 2)
electricity_emissions = round(electricity_emissions / 1000, 2)
diet_emissions = round(diet_emissions / 1000, 2)
waste_emissions = round(waste_emissions / 1000, 2)

total_emissions = round(
    transportation_emissions + electricity_emissions + diet_emissions + waste_emissions, 2
)

# Calculate button
if st.button("✨ Calculate My Carbon Footprint ✨"):
    st.markdown("<hr style='border: 1px solid #ddd;'>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: #1f77b4;'>Results</h3>", unsafe_allow_html=True)

    col3, col4 = st.columns(2)

    with col3:
        st.markdown("<h4 style='color: #ff6600;'>Category-wise Breakdown</h4>", unsafe_allow_html=True)
        st.info(f"🚗 **Transportation:** {transportation_emissions} tonnes CO2/year")
        st.info(f"💡 **Electricity:** {electricity_emissions} tonnes CO2/year")
        st.info(f"🍽️ **Diet:** {diet_emissions} tonnes CO2/year")
        st.info(f"🗑️ **Waste:** {waste_emissions} tonnes CO2/year")

    with col4:
        st.markdown("<h4 style='color: #ff6600;'>Your Total Carbon Footprint</h4>", unsafe_allow_html=True)
        st.success(f"🌍 **Total:** {total_emissions} tonnes CO2/year")
        st.warning(
            "India's average CO2 emissions in 2021 were 1.9 tonnes per capita. "
            "Consider reducing your footprint to align with sustainable goals!"
        )

# Footer
st.markdown(
    """
    <hr style='border: 1px solid #ddd;'>
    <p style='text-align: center; color: gray;'>Made with ❤️ using Streamlit</p>
    """,
    unsafe_allow_html=True
)
