def validate_name(name):

    """ Checks that the name is greater than two characters and is a string data type.
    
    Args:
        name(string): Name that we are attempting to validate.

    Returns:
        bool: Returns True if all validation checks pass.
    """

    if name == None or len(name) < 3 or len(name.strip()) < 3 or " " in name.strip() or name[0] == '.' or name[-1] == '.' or name == 'NA':
        return False 
    return True


def validate_email(email):

    """Checks that the email address is in a valid format,has a username greater than 1 character, an only one '@' symbol.
    
    Args:
        email(string): Email that we are attempting to validate.

    Returns:
       
    bool: Returns True if all validation checks pass.
    """

    email_split = email.split("@")
    if len(email_split) < 2:
        return False
    else:
        domain_parts = email_split[1].split(".")
        if (len(domain_parts)) < 2:
            return False
        else:
            for part in domain_parts:
                if part == "":
                    return False

    if email == '' or email.count('@') != 1 or ' ' in email or len(email.split("@")[0]) == 0 or len(email.split("@")[1]) == 0 or len(email.split("@")[1].split(".")[0]) == 0 or len(email.split("@")[1].split(".")[1]) == 0: 
        return False
    return True 

def validate_password(password):
    """Checks that password is valid with length > 8, at least one upper case, one lower case, one number and one special character.
    
    Args:
        password(string): Password that we are attempting to validate.

    Returns:
        bool: Returns True if all validation checks pass.
    """
    