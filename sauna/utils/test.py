import numpy as np

# Initialize weights
temperature_weight = 0.5
humidity_weight = 0.3
pressure_weight = 0.2

# Test the algorithm with some example data
temperatures = [20, 30, 40, 20, 30, 40]
humidities = [20, 60, 60, 20, 60, 60]
pressures = [1013, 1013, 1013, 800, 800, 800]
actual_mets = [1.29, 1.86, 2.43, 1.42, 2.11, 2.8]

# Initialize error
error = 5


def predict_met(temperature, humidity, pressure):
    # Define the weights for each feature

    # Convert temperatures to a scale of 0 to 1
    normalized_temperature = (temperature - 20) / 20

    # Convert humidity to a scale of 0 to 1
    normalized_humidity = (humidity - 20) / 40

    # Convert pressure to a scale of 0 to 2
    normalized_pressure = (pressure - 800) / 200

    # Calculate the weighted sum of the features
    predicted_met = temperature_weight * normalized_temperature + humidity_weight * normalized_humidity + pressure_weight * normalized_pressure

    # Return the predicted MET value
    return predicted_met


# Iterate until error is less than 0.01
while error > 0.01:
    # Calculate predicted METs
    predicted_mets = []
    for temperature, humidity, pressure in zip(temperatures, humidities, pressures):
        predicted_met = predict_met(temperature, humidity, pressure)
        predicted_mets.append(predicted_met)

    # Calculate error
    error = 0
    for predicted_met, actual_met in zip(predicted_mets, actual_mets):
        error += (predicted_met - actual_met) ** 2
    error = np.sqrt(error / len(predicted_mets))
    print(f"Error :{error}")

    # Adjust weights
    temperature_weight += 0.001 * (np.sum(actual_mets) - np.sum(predicted_mets))
    humidity_weight += 0.001 * (np.sum(actual_mets) - np.sum(predicted_mets))
    pressure_weight += 0.001 * (np.sum(actual_mets) - np.sum(predicted_mets))

print("Final weights:")
print("Temperature weight:", temperature_weight)
print("Humidity weight:", humidity_weight)
print("Pressure weight:", pressure_weight)
