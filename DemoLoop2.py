# DemoLoop2.py
# 수열함수
for i in range(5):
    print(i)

years = list(range(2000, 2023))
print(years)
days = list(range(1,32))
print(days)

#리스트 검프리핸즈
lst = list(range(1, 11))
print([i**2 for i in lst if i > 5])

tp = ("apple", "banana", "orange")
print([len(i) for i in tp])

#딕셔너리
d = {100:"apple", 200:"orange"}
print([v.upper() for v in d.values()])

