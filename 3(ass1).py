conversion_factors = [12, 1/3, 1/5280, 304.8, 30.48, 0.3048, 0.0003048]
conversion_units = ["Inches", "Yards", "Miles", "Millimeters", "Centimeters", "Meters", "Kilometers"]

print("Choose an option for converting feets:")
options = ["1. Inches", "2. Yards", "3. Miles", "4. Millimeters", "5. Centimeters", "6. Meters", "7. Kilometers"]
for option in options:
    print(option)

feet = float(input("\nEnter length in feet: "))
choice = int(input("Enter your choice (1-7): "))

if 1 <= choice <= 7:
    converted_value = feet * conversion_factors[choice - 1]
    print(f"\n{feet} feet is equal to {converted_value:.4f} {conversion_units[choice - 1]}")
else:
    print("\nInvalid choice! Please enter a number between 1 and 7.")