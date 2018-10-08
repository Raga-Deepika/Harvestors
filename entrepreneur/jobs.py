from entrepreneur.base import entre_base
from pymongo import MongoClient
from entrepreneur import logger
client = MongoClient('localhost',27017)
db = client.test
from redis import Redis
from rq import Queue


redis_conn  = Redis()
q_ma = Queue('entrepreneur_ma', connection=redis_conn)
q_lawsuits = Queue('entrepreneur_lawsuits',connection=redis_conn)
q_patents = Queue('entrepreneur_patents',connection=redis_conn)


def entrepreneur_ma__iterator():
    col = db.entrepreneur_ma
    try:
        page = 0
        resp = entre_base(page=page, category='mergers-and-acquisitions')
        while page <= resp['total_pages']:
            if resp['success'] is True:
                try:
                    for d in resp["data"]:
                        col.update({"url": d["url"]},
                                   d,
                                   upsert=True)
                except Exception as e:
                    logger.warning('Error in the iterator function of entrepreneur mergers_and_acquisition page{0} : {1}'.format(page, str(e)))

            page = page+1
    except Exception as e:
        logger.warning('Error in the iterator function of entrepreneur mergers_and_acquisition page {0} : {1}'.format(page, str(e)))
        return None

def entrepreneur_lawsuits_iterator():
    col = db.entrepreneur_lawsuits
    try:
        page=0
        resp = entre_base(page=page, category='class-action-lawsuits')
        while page <= resp['total_pages']:
            if resp['success'] is True:
                try:
                    for d in resp["data"]:
                        col.update({"url": d["url"]},
                                   d,
                                   upsert=True)
                except Exception as e:
                    logger.warning('Error in the iterator function of entrepreneur_lawsuits page{0} : {1}'.format(page, str(e)))

            page = page+1
    except Exception as e:
        logger.warning('Error in the iterator function of entrepreneur_lawsuits page {0}: {1}'.format(page,str(e)))
        return None

def entrepreneur_patents_iterator():
    col = db.entrepreneur_patents
    try:
        page = 0
        resp = entre_base(page=page, category='patents')
        while page <= resp['total_pages']:
            if resp['success'] is True:
                try:
                    for d in resp["data"]:
                        col.update({"url": d["url"]},
                                   d,
                                   upsert=True)
                except Exception as e:
                    logger.warning('Error in the iterator function of entrepreneur_patents page')

            page = page + 1
    except Exception as e:
        logger.warning('Error in the iterator function of entrepreneur_patents page {0}: {1}'.format(page,str(e)))
        return None


def entrepreneur_ma_jobs():
    job_ma = q_ma.enqueue(entrepreneur_ma__iterator)
    print(job_ma)

def entrepreneur_lawsuits_jobs():
    job_lawsuits = q_lawsuits.enqueue(entrepreneur_lawsuits_iterator)
    print(job_lawsuits)

def entreperener_patents_jobs():
    job_patents = q_patents.enqueue(entrepreneur_patents_iterator)
    print(job_patents)