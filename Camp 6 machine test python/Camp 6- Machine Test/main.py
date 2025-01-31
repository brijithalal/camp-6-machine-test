import logging
from email_service import EmailService
from email_provider import ProviderA, ProviderB
from email_validation import get_valid_email

# Configure Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    # Initialize email service with providers
    email_service = EmailService([ProviderA(), ProviderB()])

    # Get valid email input from the user
    recipient = get_valid_email()

    # Take subject and body input from the user
    subject = input("Enter email subject: ").strip()
    body = input("Enter email body: ").strip()

    # Attempt to send the email
    email_service.send_email(recipient, subject, body)

if __name__ == "__main__":
    main()
