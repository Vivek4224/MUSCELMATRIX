import random

def generate_otp(length=6):
    """
    Generates a unique one-time password (OTP) of a specified length.
    
    Parameters:
    length (int): The desired length of the OTP. Default is 6.
    
    Returns:
    str: A unique OTP of the specified length.
    """
    characters = "0123456789"
    otp = ""
    
    for _ in range(length):
        otp += random.choice(characters)

    return otp