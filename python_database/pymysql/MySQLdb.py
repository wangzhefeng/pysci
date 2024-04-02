# -*- coding: utf-8 -*-

# ***************************************************
# * File        : MySQLdb.py
# * Author      : Zhefeng Wang
# * Email       : wangzhefengr@163.com
# * Date        : 2023-07-30
# * Version     : 0.1.073015
# * Description : description
# * Link        : link
# * Requirement : 相关模块版本需求(例如: numpy >= 2.1.0)
# ***************************************************

# python libraries
import os
import sys
ROOT = os.getcwd()
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))
import warnings

from flask import Flask
import MySQLdb
import MySQLdb.cursors

sys.setdefaultencoding( "utf8" )
warnings.filterwarnings("ignore")

# global variable
LOGGING_LABEL = __file__.split('/')[-1][:-3]

app = Flask(__name__)
app.config.from_object(__name__)

# 连接数据库
def connectdb(HOST, USER, PASSWORD, DATABASE, PORT, CHARSET):
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




# 测试代码 main 函数
def main():
    app.run(debug = True)

if __name__ == "__main__":
    main()
