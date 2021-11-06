
# -*- coding: utf-8 -*-

__author__ = 'wangzhefeng'


import hashlib
from datetime import datetime


# 摘要算法
# hashlib.md5()
# hashlib.sha1()
# hashlib.sha256()
# hashlib.sha512()

# hashlib.md5()
md5_test1 = hashlib.md5()
md5_test1.update('how to use md5 in python hashlib?'.encode('utf-8'))
md5_test1_hexdigest = md5_test1.hexdigest()
print(md5_test1_hexdigest)

md5_test2 = hashlib.md5()
md5_test2.update('how to use md5 in '.encode('utf-8'))
md5_test2.update('python hashlib?'.encode('utf-8'))
md5_test2_hexdigest = md5_test2.hexdigest()
print(md5_test2_hexdigest)

# hashlib.sha1()
sha1_test1 = hashlib.md5()
sha1_test1.update('how to use md5 in python hashlib?'.encode('utf-8'))
sha1_test1_hexdigest = sha1_test1.hexdigest()
print(sha1_test1_hexdigest)

sha1_test2 = hashlib.md5()
sha1_test2.update('how to use md5 in '.encode('utf-8'))
sha1_test2.update('python hashlib?'.encode('utf-8'))
sha1_test2_hexdigest = sha1_test2.hexdigest()
print(sha1_test2_hexdigest)

print(md5_test1_hexdigest == md5_test2_hexdigest)
print(sha1_test1_hexdigest == sha1_test2_hexdigest)
print(md5_test1_hexdigest== sha1_test1_hexdigest) 




# Example

# db = {}

# def input_md5():
#     print('请注册：')
#     username = input('username:')
#     password = input('password:')
#     register(username,password)

# def get_md5(password):
#     md5 = hashlib.md5()
#     md5.update(password.encode('utf-8'))
#     return md5.hexdigest()

# def register(username,password):
#     db[username] = get_md5(password + username + 'the-Salt')
#     print('Welcom {},please login.'.format(username.title()))
#     login(username,password)

# def login(username,password):
#     print('请登录：')
#     username = input('username:')
#     password = input('password:')
#     p = get_md5(password + username + 'the-Salt')
#     if username in db:
#         while p == db[username]:
#             print('登录成功')
#             break
#         else:
#             print('请输入的的密码有误，请重新输入：')
#             login(username,password)
#     else:
#         print('您输入的账户未注册，请先注册{}'.format(username))
#         input_md5()

# input_md5()
# print('以下为注册用户信息')
# print(db)


# Example
def md5(str):
    m = hashlib.md5()
    m.update(str.encode('utf-8'))
    return m.hexdigest().upper()

def updatescan(trackno):
    timestamp = (datetime.now()).strftime('%Y-%m-%d %H:%M:%S')
    str1 = '''20BC45092988B9AA6D740514060530C0actiontracking.getOrderVerdorTrackingapp_keyken@oigbuy.com''' + \
           '''data{"trackingnos":"''' +\
           trackno + \
           '''"}formatjsonplatformSELLERERPsign_methodmd5timestamp''' + \
           timestamp + \
           '''version1.020BC45092988B9AA6D740514060530C0'''
    sign = md5(str1)
    return sign

trackno = '1ZE356F80337946253'
print(updatescan(trackno))


