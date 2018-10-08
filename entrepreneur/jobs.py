from entrepreneur.base import entre_base
from pymongo import MongoClient
client = MongoClient('localhost',27017)
db = client.test
from redis import Redis
from rq import Queue


redis_conn  = Redis()
q = Queue('entrepreneur', connection=redis_conn)

def entrepreneur_iterator():
    col = db.entrepreneur
    page = 0
    while page <= 15 :
        resp = entre_base(page=page,category='mergers-and-acquisitions')
        if resp['success'] is True:
            for d in resp["data"]:
                col.update({"url": d["url"]},
                           d,
                           upsert=True)
        page = page+1

    page=0
    while page <= 15 :
        resp = entre_base(page=page,category='class-action-lawsuits')
        if resp['success'] is True:
            for d in resp["data"]:
                col.update({"url": d["url"]},
                           d,
                           upsert=True)
        page = page+1

    page = 0
    while page <= 15:
        resp = entre_base(page=page, category='patents')
        if resp['success'] is True:
            for d in resp["data"]:
                col.update({"url": d["url"]},
                           d,
                           upsert=True)
        page = page + 1

def entrepreneur_queue():
    job = q.enqueue(entrepreneur_iterator)
    print(job)