import uuid

def generate_primary_key(post_fix):
    """
    Generates a unique primary key by combining a random UUID with a given postfix.

    Parameters:
    post_fix (str): The desired postfix for the primary key.

    Returns:
    str: A unique primary key in the format 'uuid-postfix'.
    """
    return f'{uuid.uuid4()}-{post_fix}'