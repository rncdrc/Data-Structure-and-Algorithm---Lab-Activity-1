def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


temp = float(input("Enter a temperature:"))

print("\nSelect the conversion type:"
      "\n1. Celsius to Fahrenheit"
      "\n2. Fahrenheit to Celsius")

while True:
    choice = int(input("\nEnter 1 or 2: "))

    if choice == 1 or choice == 2:
        if choice == 1:
            result = celsius_to_fahrenheit(temp)
            print(f"\nResult: {temp}°C is equal to {result:.2f}°F")
        elif choice == 2:
            result = fahrenheit_to_celsius(temp)
            print(f"\nResult: {temp}°F is equal to {result:.2f}°C")
        break
    else:
        print("Invalid choice, please enter 1 or 2.")
