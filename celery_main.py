import tasks.test_tasks as test_tasks

test_tasks.write_mongodb.delay()

test_tasks.read_from_mongo.delay()