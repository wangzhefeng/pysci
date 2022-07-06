import typing
from typing import List, Dict, Tuple, Sequence
from typing import NewType
from typing import Callable



# 定义类型别名
Vector = List[float]
ConnectionOptions = Dict[str, str]
Address = Tuple[str, int]
Server = Tuple[Address, ConnectionOptions]

# 创建类型
UserId = NewType("UserId", int)

# 回调函数



def greeting(name: str) -> str:
    return "Hello " + name



def scale(scalar: float, vector: Vector) -> Vector:
    """
    类型别名
    Vector 和 List[float] 是可以互换的同义词

    Args:
        scalar (float): [description]
        vector (Vector): [description]

    Returns:
        Vector: [description]
    """
    return [scalar * num for num in vector]


def broadcast_message(message: str, servers: Sequence[Server]) -> None:
    """
    类型别名

    Args:
        message (str): [description]
        servers (Sequence[Server]): [description]
    """
    pass

def broadcast_message(message: str, servers: Sequence[Tuple[Tuple[str, int], Dict[str, str]]]) -> None:
    """
    类型别名

    Args:
        message (str): [description]
        servers (Sequence[Tuple[Tuple[str, int], Dict[str, str]]]): [description]
    """
    pass


def feeder(get_next_item: Callable[[], str]) -> None:
    """
    回调函数
    Callable[[Arg1Type, Arg2Type], ReturnType]

    Args:
        get_next_item (Callable[[], str]): [description]
    """
    pass

def async_query(on_sucess: Callable[[int], None], on_error: Callable[[int, Exception], None]) -> None:
    """
    回调函数

    Args:
        on_sucess (Callable[[int], None]): [description]
        on_error (Callable[[int, Exception], None]): [description]
    """
    pass




def main():
    new_vector = scale(2.0, [1.0, -4.2, 5.4])
    print(new_vector)
    some_id = UserId(523313)
    print(some_id)


if __name__ == "__main__":
    main()