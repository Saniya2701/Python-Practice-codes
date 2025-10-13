try:
    num = int(input("Enter a number: "))
    print(10 / num)
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("Please enter a valid number!")
else:
    print("Division successful.")
finally:
    print("Execution complete.")
