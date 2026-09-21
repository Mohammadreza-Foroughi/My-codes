import re
pass_input = input('Enter your password: ')
strenght = 0
level = ''

if len(pass_input) >= 8 :
    strenght += 1

if re.search(r"\d", pass_input) :
    strenght += 1
if re.search(r'[A-Z]', pass_input) :
    strenght += 1
if re.search(r"[a-z]", pass_input) :
    strenght += 1
if re.search (r'[!@#$%^&*(),.?+/_:{}|<>-]', pass_input) : 
    strenght += 1

if strenght <= 2:
    level = "Weak"
elif strenght <= 3:
    level = "Medium"
elif strenght == 4:
    level = "Strong"
else:
    level = "Very Strong"

print(f"Level: {level} ({strenght}/5)")