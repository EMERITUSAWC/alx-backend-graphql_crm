# crm/scripts/send_order_reminders.py

from datetime import datetime, timedelta
from crm.models import Customer, Order

def run():
    cutoff_date = datetime.now() - timedelta(days=1)  # Orders older than 1 day
    pending_orders = Order.objects.filter(status='pending', date__lt=cutoff_date)

    for order in pending_orders:
        customer = order.customer
        print(f"Reminder: Customer {customer.name} has pending order {order.id} from {order.date}")
        # Here you can integrate email/SMS sending logic
