import random
import logging
from abc import ABC, abstractmethod
from threading import Lock
from config import CIRCUIT_BREAKER_THRESHOLD

# Email Provider Interface
class IEmailProvider(ABC):
    @abstractmethod
    def send_email(self, recipient: str, subject: str, body: str) -> bool:
        pass


# Base Email Provider (Abstract Class)
class BaseEmailProvider(IEmailProvider):
    def __init__(self, name):
        self.name = name
        self.failure_count = 0
        self.circuit_breaker_threshold = CIRCUIT_BREAKER_THRESHOLD
        self.lock = Lock()

    def send_email(self, recipient: str, subject: str, body: str) -> bool:
        with self.lock:
            if self.failure_count >= self.circuit_breaker_threshold:
                logging.warning(f"{self.name} is temporarily disabled due to failures.")
                return False

        success = random.choice([True, False])  # Simulating success/failure
        if success:
            self.failure_count = 0
        else:
            self.failure_count += 1

        logging.info(f"{self.name}: Sending email to {recipient} - {'Success' if success else 'Failed'}")
        return success


# Mock Email Providers
class ProviderA(BaseEmailProvider):
    def __init__(self):
        super().__init__('ProviderA')


class ProviderB(BaseEmailProvider):
    def __init__(self):
        super().__init__('ProviderB')
