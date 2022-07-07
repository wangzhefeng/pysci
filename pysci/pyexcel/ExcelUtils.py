# -*- coding: utf-8 -*-


# ***************************************************
# * File        : utils_xlrd_xlwt.py
# * Author      : Zhefeng Wang
# * Email       : wangzhefengr@163.com
# * Date        : 2022-07-07
# * Version     : 0.1.070722
# * Description : description
# * Link        : link
# * Requirement : 相关模块版本需求(例如: numpy >= 2.1.0)
# ***************************************************


# python libraries
import os
import sys
from typing import Any, List

import numpy as np
import pandas as pd
import xlrd
import xlwt
import win32com


# global variable
LOGGING_LABEL = __file__.split('/')[-1][:-3]
# TODO
FILE_PATH = os.path.split(os.path.realpath(__file__))[0]
DATA_PATH = os.path.join(FILE_PATH, "data")


class Xlrd:
    """
    xlrd 工具类
    """
    
    def __init__(self, read_excel_name: str = None, write_excel_name: str = None, *args):
        """
        :param read_excel_name: 文件名及路径, 如果路径或者文件名中有中文, 前面加一个 r, defaults to None
        :type read_excel_name: str, optional
        :param write_excel_name: 文件名及路径, 如果路径或者文件名中有中文, 前面加一个 r, defaults to None
        :type write_excel_name: str, optional
        """
        self.read_excel_name = read_excel_name
        self.write_excel_name = write_excel_name

    def getData(self):
        """
        打开 Excel 文件读取数据

        :return: _description_
        :rtype: _type_
        """
        excel_data = xlrd.open_workbook(self.read_excel_name)

        return excel_data

    def processSheet(self):
        pass

    def processExcel(self):
        pass

    def saveExcel(self):
        pass 


class Xlwt:
    """
    lwt 工具类
    """

    def __init__(self):
        pass

    def createExcel(self):
        """
        创建 Excel 文件
        """
        workbook = xlwt.Workbook(encoding = "ascii")

        return workbook

    def createSheet(self):
        """
        创建 Excel Sheet 表格
        """
        pass


class ExcelXlutils:
    """
    xlutils可用于拷贝原excel或者在原excel基础上进行修改, 并保存
    
    Links:
        - Doc: https://xlutils.readthedocs.io/en/latest/
    """
    def __init__(self) -> None:
        pass


class ExcelXlwings:
    """
    xlwings:
        - xlwings 能够非常方便的读写 Excel文件中的数据, 并且能够进行单元格格式的修改
        - 可以和 matplotlib 以及 pandas 无缝连接, 支持读写 numpy、pandas数据类型, 
          将 matplotlib 可视化图表导入到excel中
        - 可以调用 Excel文件中 VBA 写好的程序, 也可以让 VBA 调用用 Python 写的程序
        - 开源免费, 一直在更新
    xlwings 安装:
        $ pip install xlwings
    Links:
        - Org: https://www.xlwings.org/
        - Doc: https://docs.xlwings.org/en/stable/api.html
    """
    def __init__(self) -> None:
        pass


class ExcelOpenpyxl:
    """
    openpyxl 概念:
        - 打开 Workbooks
        - 定位 Sheets
        - 操作 Cells

    openpyxl 安装:
        $ pip install openpyxl
    Link: 
        https://openpyxl.readthedocs.io/en/stable/
    """
    def __init__(self) -> None:
        pass


class ExcelXlswriter:
    """
    _summary_

    :return: _description_
    :rtype: _type_
    """
    def __init__(self):
        pass


class ExcelWin32Com:
    """
    win32com 可以操作 com 的目的
    win32com 功能强大, 可以操作 word、调用宏

    win32com 安装:
    $ pip install pypiwin32
    """
    
    def __init__(self) -> None:
        # 创建 win32com 客户端应用
        self.app = win32com.client.Dispatch("Excel.Application")
        # 后台运行, 不显示, 不警告
        self.app.Visible = 0
        self.app.DisplayAlerts = 0

    def createExcel(self):
        self.workbook = self.app.Workbooks.Add()
        return self.workbook
    
    def createSheet(self):
        self.sheet = self.workbook.Worksheets.add()
        return self.sheet
    
    def openExcel(self, excel_name: str = None, sheet_name: str = None):
        self.workbook = self.app.Workbooks.open(os.path.join(DATA_PATH, excel_name))
        self.sheet = self.workbook.Worksheets(sheet_name)

    def getCell(self, row: int, col: int) -> Any:
        cell_content = self.sheet.Cells(row, col).Value
        return cell_content

    def setCell(self, row: int, col: int, cell_content: str = None):
        self.sheet.Cells(row, col).Value = cell_content

    def saveNowExcel(self):
        self.workbook.save()
        self.closeExcel()

    def saveNewExcel(self, excel_name: str = None):
        self.workbook.SaveAs(os.path.join(DATA_PATH, excel_name))
        self.closeExcel()
    
    def closeExcel(self):
        self.workbook.close()
        self.app.Quit()
    

class ExcelPanda:

    def __init__(self):
        pass

    def createExcel(self, excel_path: str = None):
        """
        创建 Excel 表格文件

        :param excel_path: _description_, defaults to None
        :type excel_path: str, optional
        """
        self.data = pd.to_excel(excel_path)

    def readExcel(self, excel_path: str = None, sheet_name: str = None):
        """
        读取 Excel 表格文件

        :param excel_path: _description_, defaults to None
        :type excel_path: str, optional
        :param sheet_name: _description_, defaults to None
        :type sheet_name: str, optional
        :return: _description_
        :rtype: _type_
        """
        self.data = pd.read_excel(excel_path, sheet_name = sheet_name)
        
        return self.data
    
    def saveExcel(self, 
                  data: pd.DataFrame = None, 
                  excel_path: str = None, 
                  sheet_name: str = None):
        """
        保存 Excel 表格文件

        :param data: _description_, defaults to None
        :type data: pd.DataFrame, optional
        :param excel_path: _description_, defaults to None
        :type excel_path: str, optional
        :param sheet_name: _description_, defaults to None
        :type sheet_name: str, optional
        """
        pd.DataFrame(data).to_excel(
            excel_writer = excel_path,
            sheet_name = sheet_name,
            index = False,
            header = True,
        )

    def addRow(self, row_num: int = 0, row_content: List = []):
        """
        新增行数据

        :param data: _description_
        :type data: _type_
        :param row_num: _description_, defaults to 0
        :type row_num: int, optional
        :param row_content: _description_, defaults to []
        :type row_content: List, optional
        """
        self.data.loc[row_num] = row_content
        self.num_row = len(self.data)

    def addCol(self, column_name: str = None):
        """
        新增列数据

        :param data: _description_
        :type data: _type_
        :param column_name: _description_
        :type column_name: _type_
        """
        self.data[column_name] = None  # TODO
        self.num_col = len(self.data.columns)





# 测试代码 main 函数
def main():
    print(FILE_PATH)
    print(DATA_PATH)
    print(os.path.realpath(__file__))


if __name__ == "__main__":
    main()

