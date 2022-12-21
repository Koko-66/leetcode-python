# # Dictonary with Roman values
roman_values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

s_invalid = True
# # Check if input is valid
while s_invalid:
    s = input("What is the number you want to convert? ").upper()
    if len(s) < 1:
        print("The number cannot be 0. Please try again")
    if len(s) > 15:
        print("The number you provided is too long. Please try again")
    for c in set(s): # check for illegal characters
        if c not in roman_values.keys():
            print(f"The number contains illegal character {c}, please try again")
            break
    else:
        s_invalid = False
        i = -1
        num = 0
        while abs(i) <= len(s):
            if abs(i) != len(s): # prevent index out of range error
                num += roman_values[s[i]]
                if s[i] == "V" and s[i-1] == "I" or s[i] == "X" and s[i-1] == "I":
                    num -= roman_values[s[i-1]]
                    i-=2
                elif s[i] == "L" and s[i-1] == "X" or s[i] == "C" and s[i-1] == "X":
                    num -= roman_values[s[i-1]]
                    i-=2
                elif s[i] == "D" and s[i-1] == "C" or s[i] == "M" and s[i-1] == "C":
                    num -= roman_values[s[i-1]]
                    i-=2
                else:
                    i-=1
            else:
                num += roman_values[s[i]]
                i-=1
        print(num)
