#Import the math module
import math

#input

Numerator = int(input("Enter a non-zero positive integer for your numerator: "))
Denominator = int(input("Enter a non-zero positive integer for your denominator: "))

#input validation

while Numerator <= 0:
    print("Numerator value is not accepted as it is less than or equal to 0: ")
    Numerator = int(input("Enter a non-zero positive integer for your numerator: "))
while Denominator <= 0:
    print("Denominator value is not accepted as it is less than or equal to 0: ")
    Denominator = int(input("Enter a non-zero positive integer for your denominator: "))

#Additional Variables

Div = math.gcd(Numerator, Denominator)
NumDiv = Numerator//Div
DenomDiv = Denominator//Div
WholeNum = Numerator//Denominator
RemainNum = Numerator%Denominator

#Improper/proper fraction, and reducing

if Numerator < Denominator:
    if Div == 1:
        print(f"{Numerator}/{Denominator} is a proper fraction that cannot be reduced further")

    else:
        print(f"{Numerator}/{Denominator} is a proper fraction that can be reduced.")
        print(f"{NumDiv}/{DenomDiv} is the reduced form of this fraction.")

if Numerator > Denominator:
    if Div == 1 and Denominator != 1:
        print(f"{Numerator}/{Denominator} is an improper fraction that cannot be reduced.")
        print(f"The mixed number is {WholeNum} and {RemainNum}/{Denominator}")

    elif Denominator == 1:
            print(f"{Numerator}/{Denominator} is an improper fraction that cannot be reduced.")
            print(f"The whole number is {WholeNum}")

    elif Div != 1 and DenomDiv != 1:
        print(f"{Numerator}/{Denominator} is an improper fraction that can be reduced ")
        print(f"{NumDiv}/{DenomDiv} is the reduced form of this fraction.")
        print(f"The mixed number is {WholeNum} and {NumDiv % DenomDiv}/{DenomDiv}")

    elif DenomDiv == 1:
        print(f"{Numerator}/{Denominator} is an improper fraction that can be reduced ")
        print(f"{NumDiv}/{DenomDiv} is the reduced form of this fraction.")
        print(f"The mixed number is {WholeNum}")


