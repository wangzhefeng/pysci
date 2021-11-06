# -*- coding: utf-8 -*-

"""
# https://mp.weixin.qq.com/s/wlqvAvKvqPCclZm8AvkUSw
# hppts://github.com/miguelgrinberg/merry
pip3 install merry
"""


from merry import Merry
import requests
from requests import ConnectTimeout

# version 1.0
def process_v1_0(num1, num2, file):
    result = num1 / num2
    with open(file, "w", encoding = "utf-8") as f:
        f.write(str(result))

# version 1.1 
def process_v1_1(num1, num2, file):
    try:
        result = num1 / num2
        with open(file, "w", encoding = "utf-8") as f:
            f.write(str(result))
    except ZeroDivisionError:
        print(f"{num2} can not be zero")
    except FileNotFoundError:
        print(f"file {file} not found")
    except Exception as e:
        print(f"exception, {e.args}")

# version 2.0
merry = Merry()
merry.logger.disabled = True

@merry._try
def process_v2_0(num1, num2, file):
    result = num1 / num2
    with open(file, "w", encoding = "utf-8") as f:
        f.write(str(result))

@merry._except(ZeroDivisionError)
def process_zero_division_error(e):
    print("zero_division_error", e)

@merry._except(FileNotFoundError)
def process_file_not_found_error(e):
    print("file_not_found_error", e)

@merry._except(Exception)
def process_exception(e):
    print("exception", type(e), e)


# version 3.0
merry = Merry()
merry.logger.disabled = True
catch = merry._try

class BaseClass(object):
    
    @staticmethod
    @merry._except(ZeroDivisionError)
    def process_zero_division_error(e):
        print("zero_division_error", e)
    
    @staticmethod
    @merry._except(FileNotFoundError)
    def process_file_not_found_error(e):
        print("file_not_found_error", e)

    @staticmethod
    @merry._except(Exception)
    def process_exception(e):
        print("exception", type(e), e)

    @staticmethod
    @merry._except(ConnectTimeout)
    def process_connect_timeout(e):
        print("connect_timeout", e)

class Caculator(BaseClass):
    
    @catch
    def process_v3_0(self, num1, num2, file):
        result = num1 / num2
        with open(file, "w", encoding = "utf-8") as f:
            f.write(str(result))

class Fetcher(BaseClass):
    
    @catch
    def process(self, url):
        response = requests.get(url, timeout = 1)
        if response.status_code == 200:
            print(response.text)



if __name__ == "__main__":
    # process_v1_0(1, 2, "result/result.txt")
    # process_v1_0(1, 0, "result.txt")
    # process_v1_0(1, [2], "result.txt")

    process_v1_1(1, 2, "result/result.txt")
    process_v1_1(1, 0, "result.txt")
    process_v1_1(1, [2], "result.txt")

    process_v2_0(1, 2, "result/result.txt")
    process_v2_0(1, 0, "result.txt")
    process_v2_0(1, 2, "result.txt")
    process_v2_0(1, [1], "result.txt")

    c = Caculator()
    c.process_v3_0(1, 0, "result.txt")

    f = Fetcher()
    f.process("http://notfound.com")
