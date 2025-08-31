#!/usr/bin/env python
"""
crm/cron.py

Logs CRM heartbeat and optionally queries the GraphQL hello field to verify endpoint.
"""

import os
import sys
from datetime import datetime

# Use virtual environment Python when running manually
try:
    from gql import gql, Client
    from gql.transport.requests import RequestsHTTPTransport
except ImportError:
    print("gql module not found. Please install with: pip install gql[requests]")
    sys.exit(1)

# Log file in project directory (Windows-friendly)
LOG_FILE = os.path.join(os.getcwd(), "crmheartbeatlog.txt")

def log_crm_heartbeat():
    """Log the current datetime as a heartbeat."""
    with open(LOG_FILE, "a") as log:
        log.write(f"CRM Heartbeat at {datetime.now()}\n")

def check_graphql_hello():
    """Optionally query the GraphQL 'hello' field."""
    transport = RequestsHTTPTransport(
        url="http://127.0.0.1:8000/graphql",
        verify=True,
        retries=3,
    )

    client = Client(transport=transport, fetch_schema_from_transport=True)
    query = gql("""
        query {
            hello
        }
    """)
    try:
        result = client.execute(query)
        with open(LOG_FILE, "a") as log:
            log.write(f"GraphQL hello: {result.get('hello')}\n")
    except Exception as e:
        with open(LOG_FILE, "a") as log:
            log.write(f"GraphQL query failed: {e}\n")

if __name__ == "__main__":
    log_crm_heartbeat()
    check_graphql_hello()
    print(f"Heartbeat logged to {LOG_FILE}")
