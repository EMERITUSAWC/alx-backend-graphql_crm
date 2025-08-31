#!/bin/bash
# Ensure executable: chmod +x crm/cron_jobs/clean_inactive_customers.sh

LOG_FILE="/tmp/customercleanuplog.txt"

# Activate virtualenv (Windows path inside Git Bash)
source "$PWD/.venv/Scripts/activate"

# Run the Python cleanup script and log output
python "$PWD/crm/cron_jobs/clean_inactive_customers.py" >> "$LOG_FILE" 2>&1