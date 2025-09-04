import logging
from .models import Product

# Setup logging
logger = logging.getLogger(__name__)
logging.basicConfig(
    filename="/tmp/lowstockupdates_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def updatelowstock():
    """
    Cron job to check and update low stock products
    """
    threshold = 5
    low_stock_products = Product.objects.filter(stock__lt=threshold)
    count = low_stock_products.count()

    for product in low_stock_products:
        product.stock = threshold
        product.save()
        logger.info(f"[CRON] Updated stock for product {product.name} (ID: {product.id}) to {threshold}")

    logger.info(f"[CRON] Total products updated: {count}")
    return count
