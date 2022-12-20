# Dictonary with Roman values
roman_values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
# Ask user to provide number
s = input("What is the number you want to convert? ").upper()
print(len(s))
print(roman_values.keys())

# Check if input is valid
if len(s) < 1:
    print("The number cannot be 0. Please try again")
    s = input("What is the number you want to convert? ").upper()
elif len(s) > 15:
    print("The number you provided is too long. Please try again")
    s = input("What is the number you want to convert? ").upper()
else:
    for c in s:
        if c not in roman_values.keys():
            print("The number contains illegal characters, please try again")
            break
    s = input("What is the number you want to convert? ").upper()
# Once calculated, check if the number is within the range (1, 3999)
