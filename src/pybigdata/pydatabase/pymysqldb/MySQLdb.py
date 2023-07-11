# -*- coding: utf-8 -*-


# ***************************************************
# * File        : MySQLdb.py
# * Author      : Zhefeng Wang
# * Email       : wangzhefengr@163.com
# * Date        : 2022-07-26
# * Version     : 0.1.072621
# * Description : description
# * Link        : link
# * Requirement : 相关模块版本需求(例如: numpy >= 2.1.0)
# ***************************************************


from flask import *
import MySQLdb
import MySQLdb.cursors

app = Flask(__name__)
app.config.from_object(__name__)



# 连接数据库
def connectdb():
    db = MySQLdb.connect(
        host = HOST, 
        user = USER, 
        passwd = PASSWORD, 
        db = DATABASE, 
        port = PORT, 
        charset = CHARSET, 
        cursorclass = MySQLdb.cursors.DictCursor
    )
    db.autocommit(True)
    cursor = db.cursor()
    return (db,cursor)


# 关闭数据库
def closedb(db,cursor):
    db.close()
    cursor.close()


# 首页
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug = True)
