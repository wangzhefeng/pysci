# -*- coding: utf-8 -*-

def binary_search(List, item):
    # low 和 high 用于跟踪要在其中查找的列表部分
    low = 0
    high = len(List) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = List[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    
    return None


def findSmallest(arr):
    """
    寻找数组中最小元素
    """
    # 存储最小的值
    smallest = arr[0]
    # 存储最小元素的索引
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    
    return smallest_index

def selectionSort(arr):
    """
    选择排序
    """
    newArr = []
    for i in range(len(arr)):
        smallest_index = findSmallest(arr)
        newArr.append(arr.pop(smallest_index))
    
    return newArr


if __name__ == "__main__":
    my_list = [1, 3, 5, 7, 9]
    result1 = binary_search(my_list, 3)
    # print(result1)

    result2 = binary_search(my_list, -1)
    # print(result2)

    my_list2 = [5, 3, 6, 2, 10]
    result3 = selectionSort(my_list2)
    print(result3)
