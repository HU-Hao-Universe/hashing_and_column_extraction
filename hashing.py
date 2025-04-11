import pandas as pd
import numpy as np
import hashlib

def hash_email(email):
    """
    Normalizes and hashes an email address using SHA-256.

    Parameters:
    - email: The email address as a string.

    Returns:
    - The hashed email as a hex string or NaN if input is invalid.
    """
    if pd.isnull(email):
        return np.nan
    email = email.strip().lower()
    return hashlib.sha256(email.encode('utf-8')).hexdigest()

# === Tutorial Demo ===

# Sample list of email addresses (including edge cases)
emails = [
    "User@example.com",
    " user@example.com ",
    "USER@EXAMPLE.COM",
    None,
    np.nan,
    "another.email@domain.org"
]

# Apply hash_email function to each email
hashed_emails = [hash_email(email) for email in emails]

# Display original and hashed results
print("Original Email".ljust(30), "Hashed (SHA-256)")
print("-" * 80)
for original, hashed in zip(emails, hashed_emails):
    print(str(original).ljust(30), hashed)
