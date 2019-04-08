#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymysql

# Connection Object
# instance of class pymysql.connection.Connection()
conn = pymysql.connect(host = 'localhost',
                       user = 'root',
                       password = '1234567',
					   # passwd = '',
                       database = 'tinker',
					   db = '',
                       port = '3306',
                       # bind_address = '',
                       # unix_socket = '',
                       charset = 'utf8mb4',
                       # sql_mode = 'SQL_MODE',
                       # read_default_file = 'my_cnf',
                       # conv = '',
                       # use_unicode = True,
                       # client_flag = '',
                       cursorclass = pymysql.cursors.DictCursor,
                       # init_command = '',
                       connect_timeout = 10,
                       # ssl = {},
                       # read_default_group = '',
                       # compress = '',
                       # named_pipe = '',
                       autocommit = False,
                       # local_infile = False,
                       # max_allowed_packet = '16MB',
                       # defer_connect = False,
                       # auth_plugin_map = {},
                       # binary_prefix = False
                       )
conn.cursor(cursor = None)
conn.autocommit_mode        # specified autocommit mode. None means use server default
conn.begin()                # Begin transaction
conn.close()
conn.commit()
conn.rollback()
conn.ping(reconnect = True) # Check if the server is alive
conn.select_db()            # Set current db
conn.show_warings()


# Cursor Objects
# the instance of class pymysql.cursors.Cursor()
cur = conn.cursor()
cur.callproc(procname, args = ())
cur.close()
cur.execute(query, args = None)
cur.executemany(query, args)
cur.fetchone()
cur.fetchmany(size = None)
cur.max_stmt_length
cur.mogrify(query, args = None)
cur.setinputsizes()
cur.setoutputsizes()

# class pymysql.cursors.SSCursor(connection)
cur.fetchall()
cur.fetchall_unbuffered()
cur.fetchmany()
cur.fetchone()
cur.read_next()

# class pymysql.cursors.DictCursor(connection)

# class pymysql.cursors.SSDictCursor(connection)