from celery import shared_task


@shared_task(queue='default')
def quick_task():
    # Simulate a fast task
    return "Quick task done!"