#!/usr/bin/env python
"""
crm/cron_jobs/send_order_reminders.py

Queries GraphQL endpoint for pending orders and logs reminders.
"""

import os
import sys
from datetime import datetime

# Log file in project directory (Windows-friendly)
LOG_FILE = os.path.join(os.getcwd(), "orderreminderslog.txt")

try:
    from gql import gql, Client
    from gql.transport.requests import RequestsHTTPTransport
except ImportError:
    print("gql module not found. Install with: pip install gql[requests]")
    sys.exit(1)

def send_order_reminders():
    """Query GraphQL endpoint for orders and log reminders."""
    transport = RequestsHTTPTransport(
        url="http://127.0.0.1:8000/graphql",
        verify=True,
        retries=3,
    )
    client = Client(transport=transport, fetch_schema_from_transport=True)
    query = gql("""
        query {
            pendingOrders {
                id
                customerName
                amount
            }
        }
    """)
    try:
        result = client.execute(query)
        with open(LOG_FILE, "a") as log:
            log.write(f"{datetime.now()}: Found {len(result.get('pendingOrders', []))} pending orders\n")
            for order in result.get("pendingOrders", []):
                log.write(f"Order {order['id']} for {order['customerName']} amount {order['amount']}\n")
    except Exception as e:
        with open(LOG_FILE, "a") as log:
            log.write(f"{datetime.now()}: Error querying GraphQL endpoint: {e}\n")

if __name__ == "__main__":
    send_order_reminders()
    print(f"Order reminders logged to {LOG_FILE}")

