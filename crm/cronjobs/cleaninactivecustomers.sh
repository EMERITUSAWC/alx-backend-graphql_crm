#!/bin/bash
# Activate virtual environment
source ~/alx-backend-graphql_crm/.venv/Scripts/activate

# Navigate to Django project
cd ~/alx-backend-graphql_crm/

# Run the Django script
python manage.py runscript clean_inactive_customers >> ~/alx-backend-graphql_crm/cronjobs/cleaninactivecustomers.log 2>&1

