#!/bin/bash
# A simple cron test script for the CRM project

LOGFILE="$(dirname "$0")/../../clean_inactive_customers.log"
echo "Cron ran at: $(date)" >> "$LOGFILE"

