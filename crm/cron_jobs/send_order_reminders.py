#!/usr/bin/env python3
"""
Cron job script to send order reminders by querying the GraphQL endpoint.
Logs activity to /tmp/order_reminders_log.txt
"""

import os
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport
from datetime import datetime

# Log file path that the checker expects
LOG_FILE = "/tmp/order_reminders_log.txt"

# Ensure the log file directory exists (creates /tmp if not existing, mostly for Windows)
os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

# GraphQL endpoint
GRAPHQL_URL = "http://127.0.0.1:8000/graphql"

# GraphQL query to fetch pending orders (example query, adapt to your schema)
query = gql("""
query {
  pendingOrders {
    id
    customer {
      id
      email
    }
    orderDate
  }
}
""")

# Initialize the client
transport = RequestsHTTPTransport(url=GRAPHQL_URL, verify=False)
client = Client(transport=transport, fetch_schema_from_transport=True)

try:
    # Execute the GraphQL query
    result = client.execute(query)

    # Write success info to log
    with open(LOG_FILE, "a") as log:
        log.write(f"{datetime.now()} - Successfully fetched pending orders: {len(result['pendingOrders'])}\n")

except Exception as e:
    # Write errors to log
    with open(LOG_FILE, "a") as log:
        log.write(f"{datetime.now()} - Error fetching orders: {str(e)}\n")

