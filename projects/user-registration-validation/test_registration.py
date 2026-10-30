from python_functions import validate_name, validate_email,validate_password
"""
This function tests 

"""
test_cases = ["Username Validation Testing", "Email Validation Testing", "Password Validation Testing"]
print("-------------------------------------------------------------------------------------")
print(test_cases[0])
print("-------------------------------------------------------------------------------------")
names = [None, "Baby\t123", 'Baby', 'Baby123', "KingLordisbaby", "Baby.123", "Baby_123", "Baby 123", ".Baby", "Baby.", 'ba', '  Baby   12    ', None, "   Baby    ", "Baby.King", "Baby..King", "Baby.King.Jr"]
for name in names:
    print(name, ":", validate_name(name))
print("-------------------------------------------------------------------------------------")

print(test_cases[1])
print("-------------------------------------------------------------------------------------")
emails = [None, ""," ", "ab@gmail.com", 'a@gmail.com',"baby@gmail.com\t", "baby@gmail.com\n","baby@gmail.com", "baby@gmail.com ","baby@gmail..com", "baby@mail.google.com","baby@gmail.", "baby@.com", '@gmail.com', 'babygmail.com', "baby@@gmail.com", "baby@mail.google.com", "baby@"]
for email in emails:
    print(email, ":", validate_email(email))
print("-------------------------------------------------------------------------------------")

print(test_cases[2])
print("-------------------------------------------------------------------------------------")
passwords = ["Baby12345", "BABY12345", "Baby", "12345", "baby12345", "Baby12345!@", "Baby12345!", "baby1234%", "Baby12345!", "Baby 12345!", "Baby12345! ", "Baby123!", None, 12345]
for password in passwords:
    print(password, ":", validate_password(password))
print("-------------------------------------------------------------------------------------")