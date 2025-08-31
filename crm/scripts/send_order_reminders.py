from crm.models import Order
from django.utils import timezone

def run():
    today = timezone.now().date()
    orders = Order.objects.filter(reminder_sent=False, date__lte=today)

    for order in orders:
        print(f"Reminder: Order #{order.id} for customer {order.customer.name} is due.")
        # Mark reminder as sent if you have such a field
        order.reminder_sent = True
        order.save()
