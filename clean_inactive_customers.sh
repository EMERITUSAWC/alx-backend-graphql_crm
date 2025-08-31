#!/bin/bash
LOG_FILE=/tmp/customercleanuplog.txt
echo "Starting cleanup..." >> $LOG_FILE 2>&1

# Activate virtual environment
source $PWD/.venv/Scripts/activate

# Run Django shell commands
$PWD/.venv/Scripts/python.exe manage.py shell >> $LOG_FILE 2>&1 <<EOF
from crm.models import Customer
from datetime import datetime, timedelta

cutoff_date = datetime.now() - timedelta(days=365)
inactive_customers = Customer.objects.filter(order__date__lt=cutoff_date)

print("Found", inactive_customers.count(), "inactive customers")

inactive_customers.delete()
EOF

echo "Cleanup done" >> $LOG_FILE 2>&1

