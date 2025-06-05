# Asks question
def ohms_law_menu():
    print("Welcome to Ohm’s Law Calculator!")
    print("What would you like to calculate?")
    print(" 1. Voltage (V) \n 2. Current (I) \n 3. Resistance (R) \n 4. Exit")

# Calculates voltage 
def voltage(current, resistance):
    if isinstance(current, (int, float)) and isinstance(resistance, (int, float)):
        voltage = current * resistance  
        print("Voltage: ", voltage, "V") 
    else:
        print("Enter valid numerical values for Current and Resistance")

# Calculates current 
def current(voltage, resistance):
    if isinstance(voltage, (int, float)) and isinstance(resistance, (int, float)) and resistance != 0:
        current = voltage / resistance  
        print("Current: ", current, "A") 
    else:
        print("Enter  numerical values for Voltage and Resistance, Resistance ≠ 0")

# Calculates resistance
def resistance(current, voltage):
    if isinstance(current, (int, float)) and isinstance(voltage, (int, float)) and current != 0:
        resistance = voltage / current  
        print("Resistance: ", resistance, "Ω") 
    else:
        print("Enter  numerical values for Voltage and Current, Current ≠ 0")

# While Loop    
while True:
    ohms_law_menu()
    choice = input("Enter your choice: ")
    
    if choice == '1':
        try:
            c = float(input("Enter Current (I) in Amps: "))
            r = float(input("Enter Resistance (R) in Ohms: "))
            voltage(c, r)
        except ValueError:
            print("Please enter numeric values.")

    elif choice == '2':
        try:
            v = float(input("Enter Voltage (V) in Volts: "))
            r = float(input("Enter Resistance (R) in Ohms: "))
            current(v, r)
        except ValueError:
            print("Please enter numeric values.")

    elif choice == '3':
        try:
            c = float(input("Enter Current (I) in Amps: "))
            v = float(input("Enter Voltage (V) in Volts: "))
            resistance(c, v)
        except ValueError:
            print("Please enter numeric values.")

    elif choice == '4':
        print("Exiting Ohm's Law Calculator. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")

