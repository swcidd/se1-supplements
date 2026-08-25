##Write a function named calculate_bmi(weight_kg, height_m) that takes a person's weight in kilograms and height in meters. The function should calculate and return the BMI as a float. The formula for BMI is weight divided by height squared.

def calculate_bmi(weight_kg, height_m):
    return weight_kg / height_m ** 2

print(calculate_bmi(70, 1.75))  # Expected output: 22.857...
print(calculate_bmi(90, 1.80))  # Expected output: 27.777...