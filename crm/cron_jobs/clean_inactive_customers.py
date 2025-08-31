import os
import django
from datetime import datetime, timedelta

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "crm.settings")
django.setup()

from core.models import Customer, Order

one_year_ago = datetime.now() - timedelta(days=365)
inactive_customers = Customer.objects.filter(order__created_at__lt=one_year_ago).distinct()

count = inactive_customers.count()
print(f"Deleting {count} inactive customers")
inactive_customers.delete()
print("Deletion complete")
