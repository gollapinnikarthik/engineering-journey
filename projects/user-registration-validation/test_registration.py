from python_functions import validate_name, validate_email,validate_password
"""
This function tests 

"""
test_cases = ["User Name Testing", "Email Validation Testing", "Password Validation Testing"]
print("-------------------------------------------------------------------------------------")
print(test_cases[0])
print("-------------------------------------------------------------------------------------")
names = ['Baby', 'Baby123', "KingLordisbaby", "Baby.123", "Baby_123", "Baby 123", ".Baby", "Baby.", 'ba', '  Baby   12    ', None, "   Baby    "]
for name in names:
    print(name, ":", validate_name(name))
print("-------------------------------------------------------------------------------------")

print(test_cases[1])
print("-------------------------------------------------------------------------------------")
emails = ["baby@gmail.com", "baby@gmail.", "baby@.com", '@gmail.com', "baby@@gmail.com", "baby@mail.google.com", "baby@"]
for email in emails:
    print(email, ":", validate_email(email))
print("-------------------------------------------------------------------------------------")

print(test_cases[2])
print("-------------------------------------------------------------------------------------")
passwords = [""]
for password in passwords:
    print(password, ":", validate_password(password))
print("-------------------------------------------------------------------------------------")