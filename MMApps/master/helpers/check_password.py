import re

def is_valid_password(password):
    """
    Validates the password based on the following criteria:
    - Must be at least 8 characters long.
    - Must contain at least one uppercase letter (A-Z).
    - Must contain at least one lowercase letter (a-z).
    - Must contain at least one digit (0-9).
    - Must contain at least one special character from the set "#@._".

    Args:
        password (str): The password to be validated.

    Returns:
        tuple: A tuple where:
               - The first value is a boolean, True if the password is valid, False otherwise.
               - The second value is a message (str) explaining the validation result.
                 If the password is valid, the message will be an empty string.
                 If the password is invalid, the message will explain why.

    Example:
        >>> is_valid_password("Password123#")
        (True, "")
        
        >>> is_valid_password("pass")
        (False, "Password must be at least 8 characters long.")
        
        >>> is_valid_password("password123")
        (False, "Password must contain at least one uppercase letter.")
        
        >>> is_valid_password("Password123")
        (False, "Password must contain at least one special character from '#@._'.")
    """
    # Check if the password has at least 8 characters
    if len(password) < 8:
        return False, "Password must be at least 8 characters long."
    
    # Check for at least one uppercase letter
    if not re.search(r'[A-Z]', password):
        return False, "Password must contain at least one uppercase letter."
    
    # Check for at least one lowercase letter
    if not re.search(r'[a-z]', password):
        return False, "Password must contain at least one lowercase letter."
    
    # Check for at least one digit
    if not re.search(r'\d', password):
        return False, "Password must contain at least one digit."
    
    # Check for at least one special character from "#@._"
    if not re.search(r'[#@._]', password):
        return False, "Password must contain at least one special character from '#@._'."
    
    return True, ""