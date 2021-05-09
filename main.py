'''
List Comprehension
'''

# x = []
# for n in range(10):
#   x.append(n ** 2)
# print(x)


# print([n ** 2 for n in range(10)])


'''
Comditionals i List Comprehension
'''

# x = []
# for n in [1,2,3]:
#   for y in [4, 6, 8]:
#     if n != y:
#       x.append((n, y))
# print(x)

# print([(n,y) for n in [1,2,3] for y in [4,6,8] if n != y])




'''
Nested List Comprehension
'''

# x = [
#   [1,2,3,4],
#   [5,6,7,8],
#   [9,10,11,12]
# ]

# print(len(x))

# test = [[row[n] for row in x] for n in range(4)] 
# print(test)

# =========================================

# x = [
#   [1,2,3,4],
#   [5,6,7,8],
#   [9,10,11,12]
# ]

# test = []
# for n in range(4):
#   test.append([row[n] for row in test])
#   print(test)

# =========================================


# x = [
#   [1,2,3,4],
#   [5,6,7,8],
#   [9,10,11,12]
# ]


# test = []
# for n in range(4):
#   test_row = []
#   for row in x:
#     test_row.append(row[n])
#   test.append(test_row)
# print(test)