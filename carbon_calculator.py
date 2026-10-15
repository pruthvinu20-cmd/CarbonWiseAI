# CarbonWiseAI - Carbon Emission Calculator

# Illustrative emission factors for demonstration.
# Replace these with verified, documented factors before
# presenting results as real-world emissions estimates.

# Transportation emission factors (kg CO2e per km)
TRANSPORT_FACTORS = {
    "Petrol Car": 0.192,
    "Diesel Car": 0.171,
    "Electric Car": 0.050,
    "Bus": 0.080,
    "Bicycle": 0.0,
    "Motorcycle": 0.103,
    "Train": 0.041,
    "Walking": 0.0
}

# Electricity emission factor (kg CO2e per kWh)
ELECTRICITY_FACTOR = 0.70

# Illustrative factors for other activities.
# Units are specified in the comments.

COOKING_GAS_FACTOR = 2.0       # kg CO2e per kg of LPG
FOOD_FACTOR = 2.5              # kg CO2e per kg of food (illustrative)
AIR_TRAVEL_FACTOR = 0.15       # kg CO2e per passenger-km
WASTE_FACTOR = 0.5             # kg CO2e per kg of waste (illustrative)
WATER_FACTOR = 0.0003          # kg CO2e per litre (illustrative)
SHOPPING_FACTOR = 0.5          # kg CO2e per ₹100 spent (illustrative)


def calculate_emissions(
    transport,
    distance,
    electricity,
    cooking_gas=0,
    food=0,
    air_travel=0,
    waste=0,
    water=0,
    shopping=0
):
    """
    Calculate estimated carbon emissions from daily activities.

    Parameters:
        transport: Selected transportation method
        distance: Distance travelled in kilometres
        electricity: Electricity consumed in kWh
        cooking_gas: LPG consumed in kilograms
        food: Food consumed in kilograms
        air_travel: Air travel distance in passenger-km
        waste: Waste generated in kilograms
        water: Water consumed in litres
        shopping: Shopping expenditure in rupees

    Returns:
        Dictionary containing emissions by activity
        and total estimated emissions in kg CO2e.
    """

    # Transportation emissions
    if transport not in TRANSPORT_FACTORS:
        raise ValueError(
            f"Invalid transport method: {transport}"
        )

    transport_emissions = (
        distance * TRANSPORT_FACTORS[transport]
    )

    # Electricity emissions
    electricity_emissions = (
        electricity * ELECTRICITY_FACTOR
    )

    # Cooking gas emissions
    cooking_emissions = (
        cooking_gas * COOKING_GAS_FACTOR
    )

    # Food emissions
    food_emissions = (
        food * FOOD_FACTOR
    )

    # Air travel emissions
    air_emissions = (
        air_travel * AIR_TRAVEL_FACTOR
    )

    # Waste emissions
    waste_emissions = (
        waste * WASTE_FACTOR
    )

    # Water usage emissions
    water_emissions = (
        water * WATER_FACTOR
    )

    # Shopping emissions
    # SHOPPING_FACTOR represents emissions per ₹100 spent.
    shopping_emissions = (
        shopping / 100 * SHOPPING_FACTOR
    )

    # Store emissions by activity
    emissions = {
        "Transportation": transport_emissions,
        "Electricity": electricity_emissions,
        "Cooking Gas": cooking_emissions,
        "Food": food_emissions,
        "Air Travel": air_emissions,
        "Waste": waste_emissions,
        "Water Usage": water_emissions,
        "Shopping": shopping_emissions
    }

    # Calculate total emissions
    total_emissions = sum(emissions.values())

    # Return results
    return {
        "emissions": emissions,
        "transport_emissions": transport_emissions,
        "electricity_emissions": electricity_emissions,
        "total_emissions": total_emissions
    }