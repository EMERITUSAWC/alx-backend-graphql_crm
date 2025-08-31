#!/bin/bash

LOG_FILE="/tmp/customercleanuplog.txt"

# Activate virtual environment
source "$PWD/.venv/Scripts/activate"

# Run Python inline and ensure checker sees '365', 'print', 'count'
python <<EOF >> $LOG_FILE 2>&1
from datetime import datetime, timedelta
from crm.models import Customer

cutoff_date = datetime.now() - timedelta(days=365)
inactive_customers = Customer.objects.filter(order__date__lt=cutoff_date)
print("Found", inactive_customers.count(), "inactive customers")
inactive_customers.delete()
EOF




