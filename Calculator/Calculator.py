first = float(input("Enter first operand: "))
second = float(input("Enter second operand: "))

print("\nCalculator Menu")
print("---------------")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Which operation do you want to perform? "))

if choice == 1:
    print(f"The result of the operation is {first + second}. Goodbye!")
elif choice == 2:
    print(f"The result of the operation is {first - second}. Goodbye!")
elif choice == 3:
    print(f"The result of the operation is {first * second}. Goodbye!")
elif choice == 4:
    print(f"The result of the operation is {first / second}. Goodbye!")
elif choice > 4:
    print("Error: Invalid selection! Terminating program.")