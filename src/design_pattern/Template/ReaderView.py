from abc import ABCMeta, abstractmethod
# 引入 ABCMeta 和 abstractmethod 来定义抽象类和抽象方法


class ReaderView(metaclass = ABCMeta):
    """
    阅读器视图
    """
    def __init__(self):
        self.__curPageNum = 1

    def getPage(self, pageNum):
        self.__curPageNum = pageNum
        return "第" + str(pageNum) + "页的内容"

    def prePage(self):
        """
        模板方法，往前翻一页
        """
        content = self.getPage(self.__curPageNum - 1)
        self._displayPage(content)

    def nextPage(self):
        """
        模板方法，往后翻一页
        """
        content = self.getPage(self.__curPageNum + 1)
        self._displayPage(content)

    @abstractmethod
    def _displayPage(self, content):
        """翻页效果

        :param content: [description]
        :type content: [type]
        """
        pass


class SmoothView(ReaderView):
    """左右平滑的视图

    :param ReaderView: [description]
    :type ReaderView: [type]
    """
    def _displayPage(self, content):
        print("左右平滑:" + content)


class SimulationView(ReaderView):
    """仿真翻页的视图

    :param ReaderView: [description]
    :type ReaderView: [type]
    """
    def _displayPage(self, content):
        print("仿真翻页:" + content)


def testReader():
    smoothView = SmoothView()
    smoothView.nextPage()
    smoothView.prePage()

    simulationView = SimulationView()
    simulationView.nextPage()
    simulationView.prePage()


if __name__ == "__main__":
    testReader()
