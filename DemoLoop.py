# DemoLoop.py

lst = [100, "python", 3.14]

for item in lst:
    print(item, type(item))

#구구단
for i in [2,3,4,5,6]:
    print("---{0}단---".format(i))
    for j in [1,2,3,4,5,6,7,8,9]:
        print("{0} * {1} = {2}".format(i, j, i*j))


#삼각형출력
lst = [1,2,3,4,5,6,7,8,9,10]
for i in lst:
    print("*" * i)

print("---break구문---")
for i in lst:
    if i > 5:
        break
    print ("Item:{0}".format(i))

print("---continue구문---")
for i in lst:
    if i % 2 == 0:
        continue
    print ("Item:{0}".format(i))

print("---continue구문---")
for i in lst:
    if i % 2 == 1:
        continue
    print ("Item:{0}".format(i))

