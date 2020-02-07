temp_list = ["a", "b", "c"]
for temp in temp_list:
    print(temp)

# enumerate()将可遍历对象，以元祖的形式返回
for temp in enumerate(temp_list):
    print(temp)

for i, temp in enumerate(temp_list):
    print(temp)
