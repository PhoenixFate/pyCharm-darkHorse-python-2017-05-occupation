from collections.abc import Iterable
from collections.abc import Iterator


class MyList:

    def __init__(self):
        self.items = list()

    def add(self, name):
        self.items.append(name)

    def __iter__(self):
        """
        如果想让一个对象称为 可迭代对象，
        必须实现__iter__方法
        并且返回一个具有__iter__，__next__方法的对象的引用
        :return:
        """
        return MyIterator(self)


class MyIterator:

    def __init__(self, my_list):
        self.my_list = my_list
        self.current_num = 0

    def __next__(self):
        if self.current_num < len(self.my_list.items):
            item = self.my_list.items[self.current_num]
            self.current_num += 1
            return item
        else:
            raise StopIteration


def main():
    # 判断是否可以迭代，只需要判断，是否是Iterable的子类
    print(isinstance([12, 34, 77], Iterable))
    print(isinstance((32, 56, 23), Iterable))
    print(isinstance("abc", Iterable))
    print(isinstance(100, Iterable))

    my_list = MyList()
    my_list.add("tom")
    my_list.add("carry")
    print(isinstance(my_list, Iterable))
    print(isinstance(my_list, Iterator))

    for item in my_list:
        print("遍历循环 %s" % item)


if __name__ == '__main__':
    main()
