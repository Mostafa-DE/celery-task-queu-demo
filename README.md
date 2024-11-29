# Celery Task Queue Demo

<h3>Demonstrates the use of Celery for task queue management in a Django application, featuring multiple queues, 
dedicated workers, autoscaling, and concurrency.</h3>


## Celery Workers
```sh
# Start worker for default queue
celery -A demo worker --loglevel=info -Q default -n default_worker@%h

# Start worker for reports queue
celery -A demo worker --loglevel=info -Q reports --concurrency=1 --pool=prefork -n reports_worker@%h

# Start worker for other queue
celery -A demo worker --loglevel=info -Q other -n other_worker@%h

# Example worker with autoscaling
celery -A demo worker --autoscale=2,1 --loglevel=info -Q reports -n reports_worker@%h
```

## Testing Tasks
```sh
python manage.py shell
```
```python
from reports.tasks import generate_report
from other.tasks import some_task

for _ in range(10):
    generate_report.delay()

some_task.delay()
```

## Inspecting Workers
```sh
# Inspect active queues
celery -A demo inspect active_queues

# Inspect worker stats
celery -A demo inspect stats
```

## Task Examples
### reports/tasks.py
```python
from celery import shared_task

@shared_task(queue='reports')
def generate_report():
    # Simulate a long running task
    import time
    time.sleep(10)
    return "Report generated!"
```

### other/tasks.py
```python
from celery import shared_task

@shared_task(queue='default')
def quick_task():
    # Simulate a fast task
    return "Quick task done!"
```