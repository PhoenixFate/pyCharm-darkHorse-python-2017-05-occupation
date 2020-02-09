# fibonacci简单实现
def test01():
    print("--- test01 ----")
    nums = list()
    a = 0
    b = 1
    i = 0
    while i < 10:
        nums.append(a)
        a, b = b, a + b
        i += 1

    for num in nums:
        print(num)
    print("--- test01 ----")


class Fibonacci:

    def __init__(self, count):
        self.count = count
        self.current_number = 0
        self.a = 0
        self.b = 1
        pass

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_number < self.count:
            return_value = self.a
            self.a, self.b = self.b, self.a + self.b
            self.current_number += 1
            return return_value
        else:
            raise StopIteration


def test02():
    print("--- test02 ----")
    # 使用对象封装
    # 迭代器封装生成的方法
    fibonacci = Fibonacci(10)
    for num in fibonacci:
        print(num)
    print("--- test02 ----")


def test03():
    print("--- test03 ----")

    # list()
    # tuple()
    # 也可以接受迭代器对象
    print(list(Fibonacci(5)))
    print(tuple(Fibonacci(10)))

    print("--- test03 ----")


if __name__ == '__main__':
    test01()
    test02()
    test03()
