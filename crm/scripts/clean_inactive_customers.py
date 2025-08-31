from django.utils import timezone
from datetime import timedelta
from crm.models import Customer
from django.db.models import Max

def run():
    # Consider customers inactive if they have no orders in the last 90 days
    cutoff_date = timezone.now() - timedelta(days=90)

    # Annotate customers with their last order date
    inactive_customers = Customer.objects.annotate(
        last_order_date=Max('order__created_at')  # use the correct field name from Order model
    ).filter(last_order_date__lt=cutoff_date)  # filter by last order date

    for customer in inactive_customers:
        print(f"Inactive customer: {customer.name} ({customer.email})")
        # optionally delete
        # customer.delete()

