s1 = {2, 3, 1}
s2 = {'b', 'a', 'c'}
s3 = list(zip(s1, s2))
print(s3,"\n")



list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

for x, y in zip(list1, list2[::-1]):
    print(x, y)
