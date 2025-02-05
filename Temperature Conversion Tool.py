def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
def celsius_to_kelvin(celsius):
    kelvin2=celsius + 273.15
    return kelvin2
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9
def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15
def kelvin_to_celsius(kelvin):
    return kelvin - 273.15
def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32
def get_input():
    while True:
        choice = int(input("Enter your choice (1-6): "))
        
        if choice == 1:
            celsius = float(input("Enter temperature in Celsius: "))
            print(f"{celsius} Celsius is equal to {celsius_to_fahrenheit(celsius)} Fahrenheit")
            
        elif choice == 2:
            
            celsius = float(input("Enter temperature in Celsius: "))
            kelvin2=celsius_to_kelvin(celsius)
            print(f"{celsius} Celsius is equal to {kelvin2} Kelvin")
            
        elif choice == 3:
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            print(f"{fahrenheit} Fahrenheit is equal to {fahrenheit_to_celsius(fahrenheit)} Celsius")
            
        elif choice == 4:
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            print(f"{fahrenheit} Fahrenheit is equal to {fahrenheit_to_kelvin(fahrenheit)} Kelvin")
            
        elif choice == 5:
            kelvin = float(input("Enter temperature in Kelvin: "))
            print(f"{kelvin} Kelvin is equal to {kelvin_to_celsius(kelvin)} Celsius")
            
        elif choice == 6:
            kelvin = float(input("Enter temperature in Kelvin: "))
            print(f"{kelvin} Kelvin is equal to {kelvin_to_fahrenheit(kelvin)} Fahrenheit")
            
        else:
            print("Invalid choice. Please select a valid option.")
def main():
    print("Temperature Conversion Tool")
    print("Select the conversion you want to perform:")
    print("1. Celsius to Fahrenheit")
    print("2. Celsius to Kelvin")
    print("3. Fahrenheit to Celsius")
    print("4. Fahrenheit to Kelvin")
    print("5. Kelvin to Celsius")
    print("6. Kelvin to Fahrenheit")
    choice=get_input()
main()
