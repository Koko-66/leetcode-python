# # Dictonary with Roman values
roman_values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
# # Ask user to provide number
# s = input("What is the number you want to convert? ").upper()
# print(len(s))
# print(roman_values.keys())

# # Check if input is valid
# if len(s) < 1:
#     print("The number cannot be 0. Please try again")
#     s = input("What is the number you want to convert? ").upper()
# elif len(s) > 15:
#     print("The number you provided is too long. Please try again")
#     s = input("What is the number you want to convert? ").upper()
# else:
#     for c in s:
#         if c not in roman_values.keys():
#             print("The number contains illegal characters, please try again")
#             break
    
# Once calculated, check if the number is within the range (1, 3999)
roman_values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
s = input("What is the number you want to convert? ").upper()
print(s)
i = 0
num = 0
while i < len(s)-1:
    if s[i] == "I" and s[i+1] == "V" or s[i] == "I" and s[i+1] == "X":
        num += roman_values[s[i+1]] - roman_values[s[i]]
    elif s[i] == "X" and s[i+1] == "L" or s[i] == "X" and s[i+1] == "C":
        num += roman_values[s[i+1]] - roman_values[s[i]]
    elif s[i] == "C" and s[i+1] == "D" or s[i] == "C" and s[i+1] == "M":
        num += roman_values[s[i+1]] - roman_values[s[i]]
    else:
        num += roman_values[s[i]]
print(num)
