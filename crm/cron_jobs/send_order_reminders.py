import os
import django
from datetime import datetime, timedelta
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

# Setup Django env (if needed)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "crm.settings")
django.setup()

# GraphQL client
transport = RequestsHTTPTransport(url="http://localhost:8000/graphql", verify=False)
client = Client(transport=transport, fetch_schema_from_transport=True)

# Prepare query: last 7 days
query = gql("""
{
  orders(last_days: 7) {
    id
    customer {
      email
    }
  }
}
""")

result = client.execute(query)

# Log reminders
log_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), "order_reminders_log.txt")
with open(log_file, "a") as f:
    now = datetime.now().strftime("%d/%m/%Y-%H:%M:%S")
    for order in result["orders"]:
        email = order["customer"]["email"]
        f.write(f"{now} Reminder sent for Order ID {order['id']} to {email}\n")

print("Order reminders processed!")
