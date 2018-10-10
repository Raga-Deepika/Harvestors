from entrepreneur.base import entre_base
from pymongo import MongoClient
from entrepreneur import logger
import time
client = MongoClient('localhost',27017)
db = client.test
col = db.entrepreneur

from redis import Redis
from rq import Queue


redis_conn = Redis()
q_ma = Queue('entrepreneur_ma', connection=redis_conn, default_timeout=3600)
q_lawsuits = Queue('entrepreneur_lawsuits',connection=redis_conn)
q_patents = Queue('entrepreneur_patents',connection=redis_conn)


def entrepreneur_ma_iterator():
    try:
        page = 1
        resp = entre_base(page=str(page), category='mergers-and-acquisitions')
        if resp['success'] is True:
            for res in resp['data']:
                upsert = col.update({"url": res["url"]},
                                    res,
                                    upsert=True)
                logger.info('data upserted {0}'.format(upsert))
        page = 2
        while page <= int(resp['total_pages']):
            try:
                resp = entre_base(page=str(page),category='mergers-and-acquisitions')
                if resp['success'] is False or len(resp['data']) == 0:
                    continue
                if resp['success'] is True:
                    for res in resp['data']:
                        try:
                            upsert = col.update({"url": res["url"]},
                                    res,
                                    upsert=True)
                            logger.info('data upserted {0}'.format(upsert))
                        except Exception as e:
                            logger.warning('error with upsertion {0}'.format(str(e)))
            except Exception as e:
                logger.warning('error in {0}'.format(str(e)))
            page = page + 1
    except Exception as e:
        logger.error('Error in the iterator function of entrepreneur mergers_and_acquisition {0}'.format(str(e)))
        return None


def entrepreneur_lawsuits_iterator():
    try:
        page = 1
        resp = entre_base(page=str(page), category='class-action-lawsuits')
        if resp['success'] is True:
            for res in resp['data']:
                upsert = col.update({"url": res["url"]},
                                    res,
                                    upsert=True)
                logger.info('data upserted {0}'.format(upsert))
        page = 2
        while page <= int(resp['total_pages']):
            try:
                resp = entre_base(page=str(page),category='class-action-lawsuits')
                if resp['success'] is False or len(resp['data']) == 0:
                    continue
                if resp['success'] is True:
                    for res in resp['data']:
                        try:
                            upsert = col.update({"url": res["url"]},
                                    res,
                                    upsert=True)
                            logger.info('data upserted {0}'.format(upsert))
                        except Exception as e:
                            logger.warning('error with upsertion {0}'.format(str(e)))
            except Exception as e:
                logger.warning('error in {0}'.format(str(e)))
            page = page + 1
    except Exception as e:
        logger.error('Error in the iterator function of entrepreneur lawsuits {0}'.format(str(e)))
        return None


def entrepreneur_patents_iterator():
    try:
        page = 1
        resp = entre_base(page=str(page), category='patents')
        if resp['success'] is True:
            for res in resp['data']:
                upsert = col.update({"url": res["url"]},
                                    res,
                                    upsert=True)
                logger.info('data upserted {0}'.format(upsert))
        page = 2
        while page <= int(resp['total_pages']):
            try:
                resp = entre_base(page=str(page),category='patents')
                if resp['success'] is False or len(resp['data']) == 0:
                    continue
                if resp['success'] is True:
                    for res in resp['data']:
                        try:
                            upsert = col.update({"url": res["url"]},
                                    res,
                                    upsert=True)
                            logger.info('data upserted {0}'.format(upsert))
                        except Exception as e:
                            logger.warning('error with upsertion {0}'.format(str(e)))
            except Exception as e:
                logger.warning('error in {0}'.format(str(e)))
            page = page + 1
    except Exception as e:
        logger.error('Error in the iterator function of entrepreneur patents {0}'.format(str(e)))
        return None


def entrepreneur_ma_jobs():
    job_ma = q_ma.enqueue(entrepreneur_ma_iterator)
    time.sleep(2)
    print(job_ma)


def entrepreneur_lawsuits_jobs():
    job_lawsuits = q_lawsuits.enqueue(entrepreneur_lawsuits_iterator)
    time.sleep(2)
    print(job_lawsuits)


def entrepreneur_patents_jobs():
    job_patents = q_patents.enqueue(entrepreneur_patents_iterator)
    time.sleep(2)
    print(job_patents)