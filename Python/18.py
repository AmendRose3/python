# 18. Temperature Inside Earth Calculation: Write a program to calculate and display the
# temperature inside the earth at a certain depth, using the formulas provided.


def calculate_temperature(depth):
    geothermal_gradient = 25  # in degrees Celsius per kilometer
    surface_temperature = 15  # in degrees Celsius (average surface temperature)

    # Calculate the temperature at the given depth
    temperature = surface_temperature + (geothermal_gradient * (depth / 1000))  # Convert depth to kilometers

    return temperature

# Main function to get user input and display the calculated temperature
def main():
    depth_km = float(input("Enter the depth inside the Earth (in kilometers): "))
    temperature = calculate_temperature(depth_km)
    print(f"The temperature at a depth of {depth_km} kilometers is {temperature:.2f} degrees Celsius.")

# Call the main function
main()
