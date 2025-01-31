import time
import logging
from collections import deque
from threading import Lock
from config import MAX_RETRIES, RATE_LIMIT
from email_provider import ProviderA, ProviderB


class EmailService:
    def __init__(self, providers, max_retries=MAX_RETRIES, rate_limit=RATE_LIMIT):
        self.providers = deque(providers)
        self.max_retries = max_retries
        self.rate_limit = rate_limit
        self.sent_emails = set()
        self.email_queue = deque()
        self.lock = Lock()

    def send_email(self, recipient, subject, body):
        """Processes the email and prevents duplicates."""
        email_key = (recipient, subject, body)
        if email_key in self.sent_emails:
            logging.warning("Duplicate email detected. Skipping to avoid multiple sends.")
            return False

        self.email_queue.append(email_key)
        return self.process_queue()

    def process_queue(self):
        """Processes the email queue with retries and provider fallback."""
        while self.email_queue:
            recipient, subject, body = self.email_queue.popleft()
            retries = 0
            while retries < self.max_retries:
                provider = self.providers[0]
                if provider.send_email(recipient, subject, body):
                    self.sent_emails.add((recipient, subject, body))
                    logging.info("Email sent successfully.")
                    return True

                retries += 1
                delay = 2 ** retries  # Exponential Backoff
                logging.warning(f"Retrying in {delay} seconds...")
                time.sleep(delay)

            # Fallback to next provider
            logging.error("Max retries reached. Switching provider.")
            self.providers.rotate(-1)
        return False
