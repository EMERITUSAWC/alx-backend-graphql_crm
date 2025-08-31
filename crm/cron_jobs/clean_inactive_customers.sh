#!/bin/bash

LOG_FILE="/tmp/customercleanuplog.txt"
echo "Running customer cleanup..." > "$LOG_FILE"

# Use absolute path to Python in venv
"C:/Users/AMBITIOUS AWC/alx-backend-graphql_crm/.venv/Scripts/python.exe" manage.py shell >> "$LOG_FILE" 2>&1 <<EOF
from crm.scripts.clean_inactive_customers import delete_inactive_customers
delete_inactive_customers()
EOF

echo "Customer cleanup finished." >> "$LOG_FILE"



