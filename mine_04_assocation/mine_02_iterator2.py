from collections.abc import Iterable
from collections.abc import Iterator


class MyList2:

    def __init__(self):
        self.items = list()
        self.current_num = 0

    def add(self, name):
        self.items.append(name)

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_num < len(self.items):
            item = self.items[self.current_num]
            self.current_num += 1
            return item
        else:
            raise StopIteration


def main():
    my_list = MyList2()
    my_list.add("tom")
    my_list.add("carry")
    print(isinstance(my_list, Iterable))
    print(isinstance(my_list, Iterator))

    for item in my_list:
        print("遍历循环 %s" % item)


if __name__ == '__main__':
    main()
