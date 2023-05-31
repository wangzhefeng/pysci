
"""
``module`` Class

.. math:: 

    a + b = x_{1}
"""

class Message:
    """
    Message class
    """
    def __init__(self, header, data):
        """
        Initialize a Message
        
        :param header:  Header of the message, specify the type of message
        :param data: Message data
        """
        self.header = header
        self.data = data

    def test(self, a, b):
        """test

        Args:
            a (float): 一个浮点数
            b (float): 又一个浮点数
        """
        self.test_value = a + b

    def test_docstring(self, a: int, b: int):
        """test docsting

        :param a: one int number
        :type a: int
        :param b: another int nunber
        :type b: int
        :return: return a int number
        :rtype: int
        """
        self.test_value2 = a + b
        return self.test_value
