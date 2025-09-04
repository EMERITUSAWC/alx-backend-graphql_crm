import logging
from celery import shared_task
from django.utils import timezone
from .models import Product

# Setup logging
logger = logging.getLogger(__name__)
logging.basicConfig(
    filename="/tmp/crmreportlog.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


@shared_task
def generatecrmreport():
    """
    Task to generate a CRM report of products.
    Logs report summary to /tmp/crmreportlog.txt
    """
    products = Product.objects.all()
    total_products = products.count()
    low_stock = products.filter(stock__lt=5).count()

    report_summary = (
        f"CRM Report generated at {timezone.now()} - "
        f"Total Products: {total_products}, Low Stock: {low_stock}"
    )

    logger.info(report_summary)
    return report_summary
