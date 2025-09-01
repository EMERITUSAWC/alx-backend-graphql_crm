import os
import datetime

# Use a project-relative folder for logs
LOG_FILE = os.path.join(os.getcwd(), "crmheartbeatlog.txt")
os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

def log_crm_heartbeat():
    now = datetime.datetime.now().isoformat()
    log_line = f"Heartbeat at {now}\n"

    # Optional GraphQL query
    try:
        from gql import gql, Client
        from gql.transport.requests import RequestsHTTPTransport

        transport = RequestsHTTPTransport(url="http://127.0.0.1:8000/graphql", verify=True)
        client = Client(transport=transport, fetch_schema_from_transport=True)
        query = gql("{ hello }")
        result = client.execute(query)
        log_line += f"GraphQL hello: {result['hello']}\n"
    except Exception as e:
        log_line += f"GraphQL query error: {e}\n"

    with open(LOG_FILE, "a") as f:
        f.write(log_line)

if __name__ == "__main__":
    log_crm_heartbeat()



