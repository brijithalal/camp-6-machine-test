import re
import logging

# Configure Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Email Validation Function
def is_valid_email(email: str) -> bool:
    """Validate email format using regex."""
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None

# Function to get valid email input
def get_valid_email():
    """Continuously prompt the user until they enter a valid email."""
    while True:
        email = input("Enter recipient email: ").strip()
        if is_valid_email(email):
            return email
        logging.error("Invalid email format. Please enter a valid email (e.g., user@example.com).")
