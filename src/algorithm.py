# -*- coding: utf-8 -*-


# *********************************************
# * Author      : Zhefeng Wang
# * Email       : wangzhefengr@163.com
# * Date        : 2021.01.01
# * Version     : 1.0.0
# * Description : 图算法
# *               1.最短路径问题(shortest-path problem)
# *                   - 广度优先搜索算法
# *               2.狄克斯特拉算法(Dijkstra's algorithm)
# * Link        : link
# **********************************************


# python libraries
import os
import sys


# global variable
GLOBAL_VARIABLE = None


def breadth_first_search():
    """
    图算法--广度优先搜索算法，算法步骤如下：
        1.创建一个双端队列，用于存储要检查的图节点
        2.从队列中弹出一个图节点
        3.检查这个图节点是否负荷条件
        4.如果负荷条件则停止
        5.如果不符合条件
    Args:
        graph ([type]): [description]
    """
    def get_graph():
        graph = {}
        graph["you"] = ["alice", "bob", "claire"]
        graph["bob"] = ["anuj", "peggy"]
        graph["alice"] = ["peggy"]
        graph["claire"] = ["thom", "jonny"]
        graph["anuj"] = []
        graph["peggy"] = []
        graph["thom"] = []
        graph["jonny"] = []
        return graph
    
    def person_is_seller(name):
        return name[-1] == "m"

    from collections import deque
    
    # 创建一个双端队列
    search_queue = deque()

    # 将你的邻居都加入到这个搜索队列中
    graph = get_graph()
    search_queue += graph["you"]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(f"{person} + is a mango seller!")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False


class DemoClass:
    """
    类说明文档
    """
    _class_config_param = 100  # 类私有不变量
    
    def __init__(self, id_):
        self.id = id_
        self.param_a = None  # 类公开变量
        self._internal_param = None  # 类私有变量
    
    def ClassDemoFunc(self):
        """
        类普通方法
        """
        pass
    
    def _ClassPrivateFunc(self):
        """
        类私有方法
        """
        pass


class _PrivateDemoClass:
    """
    私有类
    """
    
    def __init__(self):
        pass




# 测试代码 main 函数
def main():
    breadth_first_search()


if __name__ == "__main__":
    main()

