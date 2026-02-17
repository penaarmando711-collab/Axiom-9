import hashlib

def generate_axiom_hash(data):
    """
    Creates a unique SHA-256 fingerprint for a specific piece of data.
    This acts as a permanent seal of authenticity.
    """
    # Convert the data to bytes and hash it
    hash_object = hashlib.sha256(data.encode())
    # Return the hexadecimal representation of the hash
    return hash_object.hexdigest()

# Example usage:
raw_data = "Observation 2026-02-17: Logic Node Active"
print(f"Data Fingerprint: {generate_axiom_hash(raw_data)}")
