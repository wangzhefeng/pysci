#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
中介模式
"""


class HouseInfo:
    """
    房源信息
    """
    def __init__(self, area, price, hasWindow, hasBathroom, hasKitchen, address, owner):
        self.__area = area
        self.__price = price
        self.__hasWindow = hasWindow
        self.__hasBathroom = hasBathroom
        self.__hasKitchen = hasKitchen
        self.__address = address
        self.__owner = owner

    def getAddress(self):
        return self.__address

    def getOwnerName(self):
        return self.__owner.getName()

    def showInfo(self, isShowOwner = True):
        print("面积：" + str(self.__area) + "平方米",
              "价格：" + str(self.__price) + "元",
              "窗户：" + ("有" if self.__hasWindow else "没有"),
              "卫生间：" + self.__hasBathroom,
              "厨房：" + ("有" if self.__hasKitchen else "没有"),
              "地址：" + self.__address,
              "房东：" + self.getOwnerName() if isShowOwner else "")


class HousingAgency:
    """
    房屋中介
    """
    def __init__(self, name):
        self.__houseInfos = []
        self.__name = name

    def getName(self):
        return self.__name

    def addHouseInfo(self, houseInfo):
        self.__houseInfos.append(houseInfo)

    def removeHouseInfo(self, houseInfo):
        for info in self.__houseInfos:
            if (info == houseInfo):
                self.__houseInfos.remove(info)

    def getSearchCondition(self, description):
        """
        这里有一个将用户描述信息转换为搜索条件的逻辑
        :param description:
        :return:
        """
        return description

    def getMatchInfos(self, searchCondition):
        """
        根据房源信息的各个属性查找最匹配的信息
        :param searchCondition:
        :return:
        """
        print(self.getName(), "为您找到以下最合适的房源：")
        for info in self.__houseInfos:
            info.showInfo(False)

        return self.__houseInfos

    def signContract(self, houseInfo, period):
        """
        与房东签订协议
        :param houseInfo:
        :param period:
        :return:
        """
        print(self.getName(),
              "与房东", houseInfo.getOwnerName(),
              "签订", houseInfo.getAddress(), "的房子的租赁合同，租期",
              period, "年。合同期内", self.getName(),
              "有权对其进行使用和转租！")

    def signContracts(self, period):
        for info in self.__houseInfos:
            self.signContract(info, period)


class HouseOwner:
    """
    房东
    """
    def __init__(self, name):
        self.__name = name
        self.__houseInfo = None

    def getName(self):
        return self.__name

    def setHouseInfo(self, area, price, hasWindow, bathroom, kitchen, address):
        self.__houseInfo = HouseInfo(area, price, hasWindow, bathroom, kitchen, address, self)

    def publishHouseInfo(self, agency):
        agency.addHouseInfo(self.__houseInfo)
        print(self.getName() + "在", agency.getName(), "发布房源出租信息：")
        self.__houseInfo.showInfo()

class Customer:
    """
    用户，租房的贫下中农
    """
    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def findHouse(self, description, agency):
        print("我是" + self.getName() + ", 我想要找一个\"" + description + "\"的房子")
        print()
        return agency.getMatchInfos(agency.getSearchCondition(description))

    def seeHouse(self, houseInfos):
        size = len(houseInfos)
        return houseInfos[size - 1]

    def signContract(self, houseInfo, agency, period):
        print(self.getName(), "与中介", agency.getName(),
              "签订", houseInfo.getAddress(), "的房子的租赁合同，租期",
              period, "年。合同期内", self.__name, "有权对其进行使用！")



def main():
    def testRenting():
        myHome = HousingAgency("我爱我家")

        zhangsan = HouseOwner("张三")
        zhangsan.setHouseInfo(20, 2500, 1, "独立卫生间", 0, "上地西里")
        zhangsan.publishHouseInfo(myHome)

        lisi = HouseOwner("李四")
        lisi.setHouseInfo(16, 1800, 1, "公用卫生间", 0, "当代城市家园")
        lisi.publishHouseInfo(myHome)

        wangwu = HouseOwner("王五")
        wangwu.setHouseInfo(18, 2600, 1, "独立卫生间", 1,  "金隅美和家园")
        wangwu.publishHouseInfo(myHome)
        print()

        myHome.signContracts(3)
        print()

        tony = Customer("Tony")
        houseInfos = tony.findHouse("18 平方米左右，要有独立卫生间，要有窗户，最好朝南，有厨房更好！价位在 2000 元左右", myHome)
        print()
        print("正在看房，寻找最合适的住巢......")
        print()
        AppropriateHouse = tony.seeHouse(houseInfos)
        tony.signContract(AppropriateHouse, myHome, 1)
    testRenting()

if __name__ == "__main__":
    main()







