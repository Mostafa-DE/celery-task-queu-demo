from celery import shared_task

@shared_task(queue='reports')
def generate_report():
    # Simulate a slow task
    import time
    time.sleep(10)
    return "Report generated!"
