# crm/scripts/clean_inactive_customers.py

print("Running clean_inactive_customers script...")

from datetime import datetime, timedelta
from crm.models import Customer, Order  # Adjust if your models are in a different location

# Define cutoff for inactive customers (e.g., 90 days ago)
cutoff_date = datetime.now() - timedelta(days=90)

# Find inactive customers
inactive_customers = Customer.objects.filter(orders__date__lt=cutoff_date)

# Delete them
for customer in inactive_customers:
    print(f"Deleting inactive customer: {customer.name}")
    customer.delete()

print("Finished cleaning inactive customers.")
