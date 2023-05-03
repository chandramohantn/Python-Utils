a = 10
b = 5
try:
    print("Opening resource ... (could be file, database, etc..)")
    c = a / b
    print(c)
except ZeroDivisionError as e:
    print("You cannot divide a number by zero")
finally:
    print("Closing resource")
    print("Finally get executed not matter if there is an error or not")
print('*************************************************************\n')

a = 10
b = 0
try:
    print("Opening resource ... (could be file, database, etc..)")
    c = a / b
    print(c)
except ZeroDivisionError as e:
    print("You cannot divide a number by zero")
finally:
    print("Closing resource")
    print("Finally get executed not matter if there is an error or not")
print('*************************************************************\n')


a = 10
b = 0
try:
    print("Opening resource ... (could be file, database, etc..)")
    c = a / b
    print(c)
    inp = int(input("Enter number: "))
except Exception as e:
    print("Exception Error", e)
finally:
    print("Closing resource")
    print("Finally get executed not matter if there is an error or not")
print('*************************************************************\n')


a = 10
b = 5
try:
    print("Opening resource ... (could be file, database, etc..)")
    c = a / b
    print(c)
    inp = int(input("Enter number: "))
except ZeroDivisionError as e:
    print("You cannot divide a number by zero")
except ValueError as e:
    print("You can input only a number")
finally:
    print("Closing resource")
    print("Finally get executed not matter if there is an error or not")
print('*************************************************************\n')


try:
    f = open('dummyfile.txt', 'r')
except FileNotFoundError as e:
    print('dummyfile.txt is not present')
else:
    print(f.read())
    f.close()
print('*************************************************************\n')


class CustomException(Exception):
    pass

class DOBException(CustomException):
    pass

class AnotherException(CustomException):
    pass

year = int(input("Enter year of birth: "))
valid_age = 2022 - year
try:
    if 20 <= valid_age <= 30:
        print("Valid date of year")
    else:
        raise DOBException
except DOBException:
    print("Not a valid age")

