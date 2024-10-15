from app import app_celery

@app_celery.task()
def add(a, b):
    import time
    time.sleep(5)
    return a+b

@app_celery.task()
def hello():
    print("hello_world")
    return "hello"