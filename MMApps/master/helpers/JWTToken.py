import jwt
import datetime

from django.conf import settings

SECRET_KEY = 'XSpHm2vMMNhcCwxOUGaD9sFtbUYq2VmE'

def create_jwt_token(client_id):
    """
    Create a JWT token for a given customer ID.

    Args:
        client_id (str or int): The ID of the customer for whom the token is being created.

    Returns:
        str: The encoded JWT token as a string.

    Raises:
        ValueError: If the client_id is not provided or is invalid.
    """
    if not client_id:
        raise ValueError("Customer ID must be provided")
        
    payload = {
        'client_id': client_id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30),
        'iat': datetime.datetime.utcnow()
    }

    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token

def decode_jwt_token(token):
    print(f"Decoding token: {token}")  # Debugging line
    print(f"Using SECRET_KEY: {SECRET_KEY}")  # Debugging line
    
    """
    Decode a JWT token and retrieve the payload.

    Args:
        token (str): The JWT token to be decoded.

    Returns:
        dict: The decoded payload if the token is valid.

    Returns:
        str: An error message if the token has expired or is invalid.

    Raises:
        jwt.ExpiredSignatureError: If the token has expired.
        jwt.InvalidTokenError: If the token is invalid.
    """
    try:
        # Decode the token using the same secret key
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        print(f"Decoded payload: {payload}")  # Debugging line
        return payload
    except jwt.ExpiredSignatureError:
        print("Token has expired.")
        return {"error": "Token has expired."}
    except jwt.InvalidTokenError:
        print("Invalid token.")
        return {"error": "Invalid token."}