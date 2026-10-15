from carbon_calculator import (
    TRANSPORT_FACTORS,
    ELECTRICITY_FACTOR
)


def simulate_scenarios(distance, electricity):

    scenarios = []

    # Current transport and alternative travel methods
    for transport, factor in TRANSPORT_FACTORS.items():

        transport_emissions = distance * factor

        electricity_emissions = (
            electricity * ELECTRICITY_FACTOR
        )

        total = (
            transport_emissions + electricity_emissions
        )

        scenarios.append({
            "Transport Method": transport,
            "Daily Distance (km)": distance,
            "Transport Emissions (kg CO2e)": round(
                transport_emissions, 2
            ),
            "Total Emissions (kg CO2e/day)": round(
                total, 2
            )
        })

    return scenarios