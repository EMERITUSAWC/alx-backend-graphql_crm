from crm.cron import log_crm_heartbeat


def run():
    """
    Entry point for `python manage.py runscript log_crm_heartbeat`.
    This just calls the log_crm_heartbeat() function.
    """
    log_crm_heartbeat()


