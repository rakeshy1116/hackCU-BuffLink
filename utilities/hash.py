import hashlib

def generate_hash(string_input):
    return hashlib.sha512(string_input.encode()).hexdigest()

