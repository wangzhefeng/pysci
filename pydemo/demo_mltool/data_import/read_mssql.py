# -*- coding: utf-8 -*-


import os
import pymssql


"""
input:
    server
    port 
    database
    table
output:
"""


from sqlalchemy import create_engine
import pymssql


def get_engine(host, port, user, password, database):
    db_info = {
        "host": host,
        "port": port,
        "user": user,
        "password": password,
        "database": database
    }
    conn_info = "mssql+pymssql://%(user)s:%(password)s@%(host)s:%(port)s/%(database)s" % db_info
    engine = create_engine(conn_info, encoding = "utf-8")

    return engine


def mssql_connect(host, port, user, password, database, charset):
    conn = pymssql.connect(host = host,
                           port = port,
                           user = user,
                           password = password,
                           database = database,
                           charset = charset)
    cur = conn.cursor()

    return conn, cur


