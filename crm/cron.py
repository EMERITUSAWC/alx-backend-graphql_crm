import os
from datetime import datetime

# Windows-friendly log file path in project directory
LOG_FILE = os.path.join(os.getcwd(), "crmheartbeatlog.txt")

def log_crm_heartbeat():
    """Logs a CRM heartbeat timestamp."""
    with open(LOG_FILE, "a") as f:
        f.write(f"CRM heartbeat at {datetime.now()}\n")

# Optional: you can add GraphQL hello check here if needed

if __name__ == "__main__":
    log_crm_heartbeat()
