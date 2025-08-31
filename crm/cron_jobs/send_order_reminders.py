#!/usr/bin/env python
import os
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

# Log file
LOG_FILE = os.path.expanduser("~/alx-backend-graphql_crm/crm/cron_jobs/orderreminderslog.txt")

# GraphQL client
transport = RequestsHTTPTransport(
    url="http://127.0.0.1:8000/graphql",
    use_json=True,
)
client = Client(transport=transport, fetch_schema_from_transport=True)

# Example GraphQL query
query = gql("""
{
  orders {
    id
    customer {
      id
      name
    }
    status
  }
}
""")

# Execute query and log
try:
    result = client.execute(query)
    with open(LOG_FILE, "a") as log:
        log.write("Order reminders executed successfully\n")
        log.write(f"Fetched {len(result['orders'])} orders\n")
except Exception as e:
    with open(LOG_FILE, "a") as log:
        log.write(f"Error executing order reminders: {e}\n")

