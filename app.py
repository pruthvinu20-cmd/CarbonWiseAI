import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from carbon_calculator import calculate_emissions, TRANSPORT_FACTORS
from ai_recommendations import generate_recommendations


# ---------------- PAGE CONFIGURATION ----------------

st.set_page_config(
    page_title="CarbonWiseAI",
    page_icon="🌍",
    layout="wide"
)


# ---------------- HEADER ----------------

st.title("🌍 CarbonWiseAI")
st.subheader("AI-Powered Carbon Footprint Intelligence")

st.write(
    "Measure your estimated carbon emissions, explore alternative "
    "scenarios, and discover practical ways to protect our planet."
)

st.divider()


# ---------------- SIDEBAR INPUTS ----------------

st.sidebar.title("🌱 Activity Information")
st.sidebar.write("Enter your daily activities below.")

transport = st.sidebar.selectbox(
    "Primary Transport Method",
    list(TRANSPORT_FACTORS.keys())
)

distance = st.sidebar.number_input(
    "Daily Travel Distance (km)",
    min_value=0.0,
    max_value=1000.0,
    value=20.0,
    step=1.0
)

electricity = st.sidebar.number_input(
    "Daily Electricity Consumption (kWh)",
    min_value=0.0,
    max_value=1000.0,
    value=5.0,
    step=0.5
)

cooking_gas = st.sidebar.number_input(
    "LPG Consumed (kg/day)",
    min_value=0.0,
    max_value=100.0,
    value=0.2,
    step=0.1
)

food = st.sidebar.number_input(
    "Food Consumed (kg/day)",
    min_value=0.0,
    max_value=100.0,
    value=1.0,
    step=0.5
)

air_travel = st.sidebar.number_input(
    "Air Travel Distance (passenger-km/day)",
    min_value=0.0,
    max_value=10000.0,
    value=0.0,
    step=10.0
)

waste = st.sidebar.number_input(
    "Waste Generated (kg/day)",
    min_value=0.0,
    max_value=100.0,
    value=0.5,
    step=0.1
)

water = st.sidebar.number_input(
    "Water Used (litres/day)",
    min_value=0.0,
    max_value=10000.0,
    value=100.0,
    step=10.0
)

shopping = st.sidebar.number_input(
    "Shopping Spending (₹/day)",
    min_value=0.0,
    max_value=100000.0,
    value=100.0,
    step=50.0
)


# ---------------- CARBON CALCULATION ----------------

results = calculate_emissions(
    transport=transport,
    distance=distance,
    electricity=electricity,
    cooking_gas=cooking_gas,
    food=food,
    air_travel=air_travel,
    waste=waste,
    water=water,
    shopping=shopping
)

emissions = results["emissions"]
total_emissions = results["total_emissions"]


# ---------------- MAIN METRICS ----------------

st.header("📊 Carbon Footprint Overview")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Daily Emissions",
    f"{total_emissions:.2f} kg CO₂e"
)

col2.metric(
    "Monthly Estimate",
    f"{total_emissions * 30:.2f} kg CO₂e"
)

col3.metric(
    "Yearly Estimate",
    f"{total_emissions * 365 / 1000:.2f} tonnes CO₂e"
)


# ---------------- EMISSIONS TABLE ----------------

st.header("📋 Activity-wise Emissions")

chart_data = pd.DataFrame({
    "Activity": list(emissions.keys()),
    "Emissions (kg CO₂e/day)": list(emissions.values())
})

st.dataframe(
    chart_data.style.format({
        "Emissions (kg CO₂e/day)": "{:.3f}"
    }),
    use_container_width=True,
    hide_index=True
)


# ---------------- BAR CHART ----------------

st.header("📈 Carbon Emissions by Activity")

st.bar_chart(
    chart_data,
    x="Activity",
    y="Emissions (kg CO₂e/day)",
    height=500
)


# ---------------- PIE CHART ----------------

st.header("🥧 Emissions Contribution")

positive_emissions = {
    activity: value
    for activity, value in emissions.items()
    if value > 0
}

if positive_emissions:

    fig, ax = plt.subplots(figsize=(10, 8))

    ax.pie(
        list(positive_emissions.values()),
        labels=list(positive_emissions.keys()),
        autopct="%1.1f%%",
        startangle=90,
        pctdistance=0.75
    )

    ax.set_title("Carbon Footprint by Activity")
    ax.axis("equal")

    st.pyplot(fig)
    plt.close(fig)

else:
    st.info(
        "Enter activity values to display the emissions chart."
    )


# ---------------- DIGITAL TWIN SIMULATOR ----------------

st.divider()
st.header("🌐 Digital Twin Simulator")

st.write(
    "Explore how changing your daily travel distance or transport "
    "method affects your estimated carbon emissions."
)

scenario_col1, scenario_col2 = st.columns(2)

with scenario_col1:

    scenario_transport = st.selectbox(
        "Choose an alternative transport method",
        list(TRANSPORT_FACTORS.keys()),
        index=list(TRANSPORT_FACTORS.keys()).index(transport)
    )

with scenario_col2:

    scenario_distance = st.slider(
        "Simulated daily travel distance (km)",
        min_value=0,
        max_value=200,
        value=min(int(distance), 200)
    )


# Calculate simulated emissions

scenario_results = calculate_emissions(
    transport=scenario_transport,
    distance=scenario_distance,
    electricity=electricity,
    cooking_gas=cooking_gas,
    food=food,
    air_travel=air_travel,
    waste=waste,
    water=water,
    shopping=shopping
)

scenario_total = scenario_results["total_emissions"]

difference = total_emissions - scenario_total


# Display comparison

digital_col1, digital_col2, digital_col3 = st.columns(3)

digital_col1.metric(
    "Current Emissions",
    f"{total_emissions:.2f} kg CO₂e/day"
)

digital_col2.metric(
    "Simulated Emissions",
    f"{scenario_total:.2f} kg CO₂e/day"
)

digital_col3.metric(
    "Estimated Daily Reduction",
    f"{difference:.2f} kg CO₂e",
    delta=f"{difference:.2f} kg CO₂e"
)


# Explain the result

if difference > 0:

    st.success(
        f"The simulated scenario reduces estimated emissions "
        f"by {difference:.2f} kg CO₂e per day."
    )

elif difference < 0:

    st.warning(
        f"The simulated scenario increases estimated emissions "
        f"by {abs(difference):.2f} kg CO₂e per day."
    )

else:

    st.info(
        "The simulated scenario has the same estimated emissions "
        "as your current scenario."
    )


# ---------------- RECOMMENDATIONS ----------------

st.divider()
st.header("🤖 Personalized Recommendations")

recommendations = generate_recommendations(
    transport,
    distance,
    electricity,
    total_emissions
)

for number, recommendation in enumerate(
    recommendations,
    start=1
):
    st.info(f"💡 {number}. {recommendation}")


# ---------------- FOOTER ----------------

st.divider()

st.caption(
    "CarbonWiseAI | Educational prototype. Emission factors are "
    "illustrative placeholders and must be validated before "
    "the results are treated as real-world estimates. Actual "
    "emissions depend on location, technology, and activity."
)