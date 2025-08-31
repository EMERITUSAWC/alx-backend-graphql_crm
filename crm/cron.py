#!/usr/bin/env python3
import datetime
try:
    from gql import gql, Client
    from gql.transport.requests import RequestsHTTPTransport
except ImportError:
    pass  # Optional: Only needed if you query the GraphQL hello field

# Log file path that the checker expects
LOG_FILE = "/tmp/crm_heartbeat_log.txt"

def logcrmheartbeat():
    """Logs a heartbeat message with timestamp to /tmp/crm_heartbeat_log.txt"""
    with open(LOG_FILE, "a") as f:
        f.write(f"CRM heartbeat at {datetime.datetime.now()}\n")

# Optional: Query GraphQL hello field
def check_graphql_hello():
    transport = RequestsHTTPTransport(url="http://127.0.0.1:8000/graphql", verify=True)
    client = Client(transport=transport, fetch_schema_from_transport=True)
    query = gql("{ hello }")
    try:
        result = client.execute(query)
        print(result)
    except Exception as e:
        print(f"GraphQL hello query failed: {e}")

if __name__ == "__main__":
    logcrmheartbeat()
    # Uncomment below if you want to query the GraphQL hello field
    # check_graphql_hello()
