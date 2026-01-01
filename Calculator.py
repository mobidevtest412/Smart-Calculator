from sympy import sympify
from pint import UnitRegistry

memory = None
last_result = None
history = []

def memory_store():
    global memory, last_result
    if last_result is None:
        print("Nothing to store")
    else:
        memory = last_result
        print(f"Stored {memory} in memory")

def memory_recall():
    if memory is None:
        print("Memory is empty")
        return None
    print(f"Memory value: {memory}")
    return memory

def memory_clear():
    global memory
    memory = None
    print("Memory cleared")

def getnum():
    x = get_number("Enter the first number : ")
    y = get_number("Enter the second number : ")
    return x,y

def Summation(x , y):
    global last_result
    print(f"{x} + {y} = {x+y}")
    last_result = x + y
    history.append(f"{x} + {y} = {x+y}")

def Subtraction(x , y):
    global last_result
    print(f"{x} + {y} = {x-y}")
    last_result = x - y
    history.append(f"{x} - {y} = {x-y}")

def Multiplication(x , y):
    global last_result
    print(f"{x} * {y} = {x*y}")
    last_result = x * y
    history.append(f"{x} * {y} = {x*y}")

def Division(x , y):
    global last_result
    try:
        print(f"{x} / {y} = {x/y}")
        last_result = x / y
        history.append(f"{x} / {y} = {x/y}")    
    except ZeroDivisionError:
        print("Please number other than zero")

def Modulus(x , y):
    global last_result
    try:
        print(f"{x} % {y} = {x%y}")
        last_result = x % y
        history.append(f"{x} % {y} = {x%y}")    
    except ZeroDivisionError:
        print("Please number other than zero")

def Square(x , y):
    global last_result
    print(f"{x} ** {y} = {x**y}")
    last_result = x ** y
    history.append(f"{x} ** {y} = {x**y}")

def Expression():
    exp = input("Enter Expression : ")
    try:
        result = sympify(exp)
        print(f"{exp} = {result}")
        history.append(f"{exp} = {result}")
    except:
        print("please enter valid expression")

def convert_temperature(value, from_unit, to_unit):
    if from_unit == "C":
        c = value
    elif from_unit == "F":
        c = (value - 32) * 5 / 9
    elif from_unit == "K":
        c = value - 273.15
    else:
        raise ValueError("Invalid temperature unit")

    if to_unit == "C":
        return c
    elif to_unit == "F":
        return c * 9 / 5 + 32
    elif to_unit == "K":
        return c + 273.15

def convert_length(value, from_unit, to_unit):
    units = {
        "m": 1,
        "cm": 0.01,
        "km": 1000
    }
    return value * units[from_unit] / units[to_unit]

def convert_weight(value, from_unit, to_unit):
    units = {
        "g": 1,
        "kg": 1000,
        "lb": 453.59237
    }
    return value * units[from_unit] / units[to_unit]

def Conversion():
    print("\nSelect Conversion Type")
    print("1. Temperature")
    print("2. Length")
    print("3. Weight")

    choice = input("Enter choice (1-3): ")

    if choice == "1":
        print("\nTemperature Units: C, F, K")
        from_unit = input("From unit: ").upper()
        to_unit = input("To unit: ").upper()
        value = float(input("Enter value: "))

        result = convert_temperature(value, from_unit, to_unit)
        print(f"Result: {result} {to_unit}")

    elif choice == "2":
        print("\nLength Units: m, cm, km")
        from_unit = input("From unit: ").lower()
        to_unit = input("To unit: ").lower()
        value = float(input("Enter value: "))

        result = convert_length(value, from_unit, to_unit)
        print(f"Result: {result} {to_unit}")

    elif choice == "3":
        print("\nWeight Units: g, kg, lb")
        from_unit = input("From unit: ").lower()
        to_unit = input("To unit: ").lower()
        value = float(input("Enter value: "))

        result = convert_weight(value, from_unit, to_unit)
        print(f"Result: {result} {to_unit}")

    else:
        print("Invalid choice")

def get_number(prompt):
    value = input(prompt)

    if value.lower() == 'm':
        mem = memory_recall()
        if mem is None:
            return get_number(prompt)
        return mem

    return float(value)

while True:
    print("\nOptions:")
    print("+  -  *  / % **")
    print("Expression")
    print("Conversion")
    print("MS (store) | MR (recall) | MC (clear)")
    print("exit")

    choice = input("Choose: ").lower()

    if choice == "exit":
        break

    elif choice in ["+", "-", "*", "/","%", "**"]:
        a,b = getnum()

        if choice == "+":
            Summation(a,b)
        elif choice == "-":
            Subtraction(a,b)
        elif choice == "*":
            Multiplication(a,b)
        elif choice == "/":
            Division(a,b)
        elif choice == "%":
            Modulus(a,b)
        elif choice == "**":
            Square(a,b)

    elif choice == "expression":
        Expression()

    elif choice == "conversion":
        Conversion()

    elif choice == "ms":
        memory_store()

    elif choice == "mr":
        memory_recall()

    elif choice == "mc":
        memory_clear()

    else:
        print("Invalid option")



