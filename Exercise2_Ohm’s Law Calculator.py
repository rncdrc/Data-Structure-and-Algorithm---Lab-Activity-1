def calculate_voltage(current, resistance):
    return current * resistance


def calculate_current(voltage, resistance):
    try:
        return voltage / resistance
    except ZeroDivisionError:
        return "Error: Resistance cannot be zero."


def calculate_resistance(voltage, current):
    try:
        return voltage / current
    except ZeroDivisionError:
        return "Error: Current cannot be zero."


print("What would you like to calculate?\n"
      "1. Voltage (V)\n"
      "2. Current (I)\n"
      "3. Resistance (R)\n")

while True:
    choice = input("Enter 1, 2, or 3: ")
    if choice == '1':
        current = float(input("\nEnter current (I) in amperes: "))
        resistance = float(input("Enter resistance (R) in ohms: "))
        voltage = calculate_voltage(current, resistance)
        print(f"Voltage (V) = {voltage:.2f} volts")
        break
    elif choice == '2':
        voltage = float(input("\nEnter voltage (V) in volts: "))
        resistance = float(input("Enter resistance (R) in ohms: "))
        current = calculate_current(voltage, resistance)
        print(f"Current (I) = {current:.2f} amperes" if isinstance(current, float) else current)
        break
    elif choice == '3':
        voltage = float(input("\nEnter voltage (V) in volts: "))
        current = float(input("Enter current (I) in amperes: "))
        resistance = calculate_resistance(voltage, current)
        print(f"Resistance (R) = {resistance:.2f} ohms" if isinstance(resistance, float) else resistance)
        break
    else:
        print("Invalid choice, please enter 1, 2, or 3.\n")
