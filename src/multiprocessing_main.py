import os
from multiprocessing import Pool
from multiprocessing import Process


def square_f(x):
    return x * x

def name_f(name):
    print("hello", name)

def info(title):
    print(title)
    print("module name:", __name__)
    print("parent process:", os.getppid())
    print("process id:", os.getpid())

def f(name):
    info("function f")
    print("hello", name)




if __name__ == "__main__":
    with Pool(5) as p:
        print(p.map(square_f, [1, 2, 3]))

    # Process class
    p = Process(target = name_f, args = ("bob",))
    p.start()
    p.join()

    # Process class
    info("main line")
    p = Process(target = f, args = ("bob",))
    p.start()
    p.join()
