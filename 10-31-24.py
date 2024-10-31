#even_numbers = [2,4,6,8]
# even = []
# for i in range(1, 10):
#     if i % 2 == 0:
#         even.append(i)


# mixed_list = ['Alice', 25, 200.5]
#print(mixed_list)


# listy_mcgee = [10, 20, 30, 40]
#print(listy_mcgee[0])
#print(listy_mcgee[-1])
#print(listy_mcgee[2])

# listy_mcgee[2]  = 25
# listy_mcgee.append(50)
# listy_mcgee.insert(1, 'pepperoni')
# listy_mcgee.insert(2, 'pizza')
# listy_mcgee.insert(3, 'pizza')
#print(listy_mcgee)
# listy_mcgee.remove('pizza')

# for item in listy_mcgee:
#     print(item)

# index = 0
# while index < len(listy_mcgee):
#     print(listy_mcgee[index])
#     index += 1

# list2 = [1,2,3]
# list3 = [4,5,6]

# print(list2)
# print(list3)

# combo = list2+list3
# print(combo)

# combo = (list2 * 3)
# combo.reverse()
# print(combo)
# combo.sort()
# combo.sort()
# print(combo)

# squares = [x**3 for x in range(14)]
# print(squares)

# tuple_time = (1,2,3)
# print(tuple_time[0])
# print(tuple_time[-1])


array = [1,2,3]
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

# print(array)
# print(matrix)
# print(matrix[1][2])

# for row in matrix:
    # for item in row:
        # print(item, end=' ')
    # print()

# bill = matrix
# print(bill)

numbers = [10,20,30]
print(sum(numbers))
print(min(numbers))
print(max(numbers))
print(len(numbers))

import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [10,20,25,30]
plt.plot(x, y)
plt.title('Demo')
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()




# import pandas as pd

# data = {
#     'apples': [3, 2, 0, 1],
#     'oranges': [0, 3, 7, 2]
# }

# df = pd.DataFrame(data)
# print(df)