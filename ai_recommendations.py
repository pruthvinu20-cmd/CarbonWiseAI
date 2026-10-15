def generate_recommendations(
    transport,
    distance,
    electricity,
    total_emissions
):

    recommendations = []

    # Transport recommendations
    if transport in ["Petrol Car", "Diesel Car"]:

        recommendations.append(
            "Consider public transport or carpooling "
            "for suitable journeys to reduce travel emissions."
        )

    elif transport == "Electric Car":

        recommendations.append(
            "Consider charging your electric vehicle "
            "when lower-carbon electricity is available."
        )

    elif transport == "Bus":

        recommendations.append(
            "Continue considering public transport for "
            "journeys where it is a practical alternative."
        )

    elif transport == "Bicycle":

        recommendations.append(
            "Cycling has no direct riding emissions. "
            "Continue cycling where it is safe and practical."
        )

    # Distance recommendations
    if distance > 30:

        recommendations.append(
            "Your daily travel distance is relatively high. "
            "Consider combining errands or reducing "
            "unnecessary trips."
        )

    # Electricity recommendations
    if electricity > 5:

        recommendations.append(
            "Review your electricity usage and consider "
            "switching off unused appliances and lights."
        )

    # General recommendation
    if total_emissions > 10:

        recommendations.append(
            "Explore the Digital Twin scenarios to identify "
            "practical changes that may lower your "
            "estimated daily emissions."
        )

    if not recommendations:

        recommendations.append(
            "Explore the alternative scenarios and choose "
            "practical changes that could reduce your "
            "estimated carbon footprint further."
        )

    return recommendations