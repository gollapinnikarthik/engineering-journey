def validate_name(name):

    """ Checks that the name is greater than two characters and is a string data type.
    
    Args:
        name(string): Name that we are attempting to validate.

    Returns:
        bool: Returns True if all validation checks pass.
    """
    allowed_punctutaion= {".", "_"}
    if not isinstance(name, str):
        return False
    for letter in name:
        if letter.isspace():
            return False
        if not letter.isalnum() and letter not in allowed_punctutaion:
            return False
    if len(name) < 3 or name[0] == '.' or name[-1] == '.' or '..' in name:
        return False 
    return True


def validate_email(email):

    """Checks that the email address is in a valid format,has a username greater than 1 character, an only one '@' symbol.
    
    Args:
        email(string): Email that we are attempting to validate.

    Returns:
       
    bool: Returns True if all validation checks pass.
    """
    if not isinstance(email, str):
        return False
    for letter in email:
        if letter.isspace():
            return False
    email_split = email.split("@")
    if email.count('@') != 1:
        return False
    else:
        domain_parts = email_split[1].split(".")
        if (len(domain_parts)) < 2:
            return False
        for part in domain_parts:
            if part == "":
                return False

    if len(email_split[0]) < 2 or len(email_split[1]) == 0: 
        return False
    return True 

def validate_password(password):
    """Checks that password is valid with length > 8, at least one upper case, one lower case, one number and one special character.
    
    Args:
        password(string): Password that we are attempting to validate.

    Returns:
        bool: Returns True if all validation checks pass.
    """

    special_chars = {"!", "@", "#", "$", "%", "^", "&", "*"}
    has_upper, has_lower, has_digit, has_special = False, False, False, False
    if not isinstance(password, str):
        return False
    if len(password) < 8:
        return False
    for letter in password:
        if letter.isspace():
            return False
        if letter.islower():
            has_lower = True
        if letter.isupper():
            has_upper = True
        if letter.isdigit():
            has_digit = True
        if letter in special_chars:
            has_special = True
    if has_lower == True and has_upper == True and has_digit == True and has_special == True:
        return True
    else:
        return False
