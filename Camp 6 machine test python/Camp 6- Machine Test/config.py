import logging

# Configure Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Email settings
MAX_RETRIES = 3
RATE_LIMIT = 5
CIRCUIT_BREAKER_THRESHOLD = 3
