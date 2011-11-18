# -*- coding: utf-8 -*-

from chameleon import api


@api.register
def producer_add_deliverer(db, delivererid, producerid,
                           userid=None):
    sql = """INSERT INTO producerdeliverer (delivererid, producerid, addid)
VALUES (%(delivererid)s, %(producerid)s, %(addid)s)"""

    data = {}
    data['delivererid'] = delivererid
    data['producerid'] = producerid
    data['addid'] = userid

    cur = db.cursor()
    cur.execute(sql, data)
    db.commit()
