# crm/cron.py
import datetime
import requests

LOG_FILE = '/tmp/crm_heartbeat_log.txt'

def log_crm_heartbeat():
    timestamp = datetime.datetime.now().strftime("%d/%m/%Y-%H:%M:%S")
    message = f"{timestamp} CRM is alive\n"

    with open(LOG_FILE, 'a') as f:
        f.write(message)

    try:
        response = requests.post(
            'http://localhost:8000/graphql/',
            json={'query': '{ hello }'},
            timeout=5
        )
        if response.status_code == 200:
            data = response.json()
            if data.get("data", {}).get("hello") == "Hello world":
                status_msg = f"{timestamp} GraphQL: OK\n"
            else:
                status_msg = f"{timestamp} GraphQL: Unexpected response\n"
        else:
            status_msg = f"{timestamp} GraphQL: Failed (HTTP {response.status_code})\n"
    except Exception as e:
        error_time = datetime.datetime.now().strftime("%d/%m/%Y-%H:%M:%S")
        status_msg = f"{error_time} GraphQL: Error - {str(e)}\n"

    with open(LOG_FILE, 'a') as f:
        f.write(status_msg)