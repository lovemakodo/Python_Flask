from celery import Celery
#from config import CELERY_CONFIG

celery_app = Celery("test_tasks", broker="redis://@127.0.0.1:6379/0")
#celery_app.conf.update(CELERY_CONFIG)

@celery_app.task
def write_mongodb():
    return "write to mongo"

@celery_app.task
def read_from_mongo():
    return "read from mongo"

if __name__ == "__main__":
   res = write_mongodb.delay()