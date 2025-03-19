import hashlib


def hash_number(number):
    # Use SHA-256 and take the first 10 characters
    return hashlib.sha256(str(number).encode()).hexdigest()[:10]
