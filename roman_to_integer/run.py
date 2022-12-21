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
    for c in set(s):
        if c not in roman_values.keys():
            print(f"The number contains illegal character {c}, please try again")
            break
    else:
        s_invalid = False
        i = 0
        num = 0
        while i < len(s)-1:
            if s[i] == "I" and s[i+1] == "V" or s[i] == "I" and s[i+1] == "X":
                num += roman_values[s[i+1]] - roman_values[s[i]]
                i+=2
            elif s[i] == "X" and s[i+1] == "L" or s[i] == "X" and s[i+1] == "C":
                num += roman_values[s[i+1]] - roman_values[s[i]]
                i+=2
            elif s[i] == "C" and s[i+1] == "D" or s[i] == "C" and s[i+1] == "M":
                num += roman_values[s[i+1]] - roman_values[s[i]]
                i+=2
            else:
                num += roman_values[s[i]]
                i+=1
        print(num)
