import numpy as np

def calculate_calorie_burn(weight, temp, minute):
    """
    Predicts the total calories burned in a sauna session based on weight, temp, and minute.

    Args:
        weight (float): The person's weight in kilograms.
        temp (float): The sauna's temperature in degrees Celsius.
        minute (int): The duration of the sauna session in minutes.

    Returns:
        float: The predicted number of calories burned.
    """
    # Define the coefficients
    coefficients = np.array([-0.0000039383, 0.99999923, -0.00724638])

    # Calculate the predicted calories burned
    predicted_calories_burned = np.dot(coefficients, np.array([weight, temp, minute]))

    return predicted_calories_burned


def calculate_heart_rate_increase(weight, temperature, duration):
    """
    Calculates the approximate increase in heart rate during a sauna session.

    Args:
        weight (float): The person's weight in kilograms.
        temperature (float): The sauna's temperature in degrees Celsius.
        duration (int): The duration of the sauna session in minutes.

    Returns:
        int: The approximate increase in heart rate in beats per minute.
    """
    # Based on a study that found that a 70-kilogram person who sits in a 80-degree Celsius sauna for 15 minutes
    # increased their heart rate by an average of 12 beats per minute. We can estimate the heart rate increase by
    # multiplying the person's weight by the temperature of the sauna and the duration of the session.
    heart_rate_increase = weight * temperature * duration / 88
    return heart_rate_increase


def calculate_blood_flow_increase(weight, temperature, duration):
    """
    Calculates the approximate increase in blood flow during a sauna session.

    Args:
        weight (float): The person's weight in kilograms.
        temperature (float): The sauna's temperature in degrees Celsius.
        duration (int): The duration of the sauna session in minutes.

    Returns:
        int: The approximate increase in blood flow in percentage.
    """
    # Based on a study that found that a 70-kilogram person who sits in a 80-degree Celsius sauna for 15 minutes
    # increased their heart rate by an average of 12 beats per minute. We can estimate the heart rate increase by
    # multiplying the person's weight by the temperature of the sauna and the duration of the session.
    heart_rate_increase = weight * temperature * duration / 88
    return heart_rate_increase
