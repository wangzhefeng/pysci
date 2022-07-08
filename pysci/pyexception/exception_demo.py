# -*- coding: utf-8 -*-


# *********************************************
# * Author      : zhefeng wang
# * Email       : wangzhefengr@163.com
# * Date        : 2021.01.01
# * Version     : 1.0.0
# * Description : description
# * Link        : link
# **********************************************


# python libraries
import os
import sys


# global variable
GLOBAL_VARIABLE = None


class raise_error:
    """
    captures specified exception and raise Error Code instead
    """
    def __init__(self, captures, code_name) -> None:
        self.captures = captures
        self.code = getattr(error_codes, code_name)

    def __enter__(self):
        """
        该方法将在进入上下文时调用

        Returns:
            [type]: [description]
        """
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        该方法将在退出上下文时调用

        Args:
            exc_type ([type]): [description]
            exc_val ([type]): [description]
            exc_tb ([type]): [description]

        Raises:
            self.code: [description]

        Returns:
            [type]: [description]
        """
        if exc_type is None:
            return False

        if exc_type == self.captures:
            raise self.code from exc_val
        
        return False




# 测试代码 main 函数
def main():
    pass


if __name__ == "__main__":
    main()

