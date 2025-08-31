import logging
from django.utils import timezone

# Set up logger
logger = logging.getLogger(__name__)


def log_crm_heartbeat():
    """
    Simple cron task that logs a heartbeat message
    to confirm the CRM system is alive.
    """
    now = timezone.now()
    logger.info(f"CRM heartbeat at {now}")
    print(f"CRM heartbeat at {now}")  # Useful for testing in console


def update_low_stock():
    """
    Example cron task for updating low-stock products.
    You can replace this with your own logic later.
    """
    now = timezone.now()
    logger.info(f"Checking low stock products at {now}")
    print(f"Checking low stock products at {now}")
