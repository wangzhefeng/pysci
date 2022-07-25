
# -*- coding: utf-8 -*-


from abc import ABCMeta, abstractmethod
import time


class Observer(metaclass = ABCMeta):
    """
    观察者的基类
    """
    @abstractmethod
    def update(self, observable, object):
        pass


class Observable:
    """
    被观察者的基类
    """
    def __init__(self):
        self.__observers = []

    def addObserver(self, observer):
        self.__observers.append(observer)

    def removeObserber(self, observer):
        self.__observers.remove(observer)

    def notifyObservers(self, object):
        for o in self.__observers:
            o.update(self, object)


class Account(Observable):
    def __init__(self):
        super().__init__()
        self.__lastestIp = {}
        self.__lastestRegion = {}

    def login(self, name, ip, time):
        region = self.__getRegion(ip)
        if self.__isLongDistance(name, region):
            self.notifyObservers({"name": name, "ip": ip, "region": region, "time": time})
        self.__lastestRegion[name] = region
        self.__lastestIp[name] = ip

    def __getRegion(self, ip):
        """
        由IP地址获取地区信息, 这里只是模拟, 真实项目中应该调用IP地址解析服务
        :param ip:
        :return:
        """
        ipRegions = {
            "101.47.18.9": "浙江省杭州市",
            "67.218.147.69": "美国洛杉矶"
        }
        region = ipRegions.get(ip)
        return "" if region is None else region

    def __isLongDistance(self, name, region):
        """
        计算本次登录与最近几次登录的地区差距
        这里只是简单的用字符串匹配来模拟, 真实的项目中应该用地理信息相关的服务
        :param name:
        :param region:
        :return:
        """
        lastestRegion = self.__lastestRegion.get(name)
        return lastestRegion is not None and lastestRegion != region


class SmsSender(Observer):
    """
    短信发送器
    """
    def update(self, observable, object):
        print("[短信发送] " +
              object["name"] + "您好！检测到您的账户可能登录异常. 最近一次登录信息: \n" +
              "登录地区: " + object["region"] +
              " 登录 ip: " + object["ip"],
              "登录时间: " + time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(object["time"])))


class MailSender(Observer):
    """
    邮件发送器
    """
    def update(self, observable, object):
        print("[邮件发送]" +
              object["name"] +
              "您好！检测到您的账户可能登录异常. 最近一次登录信息: \n" +
              "登录地区: " + object["region"] +
              "登录 ip: " + object["ip"] +
              "登录时间: " + time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(object["time"])))


def testLogin():
    accout = Account()
    accout.addObserver(SmsSender())
    accout.addObserver(MailSender())
    accout.login("Tony", "101.47.18.9", time.time())
    accout.login("Tony", "67.218.147.69", time.time())


def main():
    testLogin()

if __name__ == "__main__":
    main()
