# Define the independent variable (temperature in Kelvin)
temperature = [300, 310, 320, 330, 340]  # Temperatures in Kelvin

# Define the constant (k) for the relationship between temperature and pressure
k = 0.5  # This is a simplified constant for the example

# Calculate the dependent variable (pressure) based on temperature
pressure = [k * temp for temp in temperature]

# Display the relationship
for temp, pres in zip(temperature, pressure):
    print(f"Temperature: {temp}K, Pressure: {pres} atm")
