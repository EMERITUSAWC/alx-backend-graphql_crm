# crm/scripts/update_low_stock.py

from crm.models import Product
from datetime import datetime

def run():
    low_stock_threshold = 5
    low_stock_items = Product.objects.filter(quantity__lte=low_stock_threshold)

    for product in low_stock_items:
        print(f"Low stock alert: Product {product.name} has only {product.quantity} items left.")
        # You can also trigger email notifications here
