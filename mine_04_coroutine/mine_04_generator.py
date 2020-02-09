# 生成器
# 生成器是一种特殊的迭代器


def fun1():
    print("--- fun1 ---")
    list1 = range(10)
    print(list1)
    for x in list1:
        print(x, end="\t")
    print()

    list2 = [x for x in range(10)]
    print(list2)

    list3 = (x for x in range(10))
    print(list3)
    for x in list3:
        print(x, end="\t")
    print()
    print("--- fun1 ----")


# 生成器模板和类的地位一样
def create_number(count):
    a, b = 0, 1
    current_number = 0
    while current_number < count:
        # 如果一个函数中有yield，那么这个就不是一个函数，而是一个生成器模板
        result = yield a
        print("result: %s" % result)
        a, b = b, a + b
        current_number += 1
    return "ok.."


def fun2():
    print("--- fun2 ---")

    # 如果在调用create_number，函数里面有yield，此时不是在调用函数，而是在创建生成器
    # 这是不是调用函数，而是创建生成器对象
    obj = create_number(10)
    obj2 = create_number(10)
    print(obj)
    print(next(obj))
    print(next(obj))

    for number in obj:
        print(number, end="\t")
    print()

    while True:
        try:
            print(next(obj2), end=" - ")
        except Exception as e:
            print()
            print(e)
            break

    print("--- fun2 ---")


def fun3():
    print("--- fun3 ---")
    obj = create_number(10)
    # 调用生成器的第二种方式：send()
    # next() 不能传参数，send()可以传参数
    next(obj)
    obj.send("abc")
    print("--- fun3 ---")


if __name__ == '__main__':
    fun1()
    fun2()
    fun3()
