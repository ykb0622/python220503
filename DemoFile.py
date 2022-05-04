# DemoFile.py
# 문자열 조립(웹서버에 데이터 전송 : QueryString)
url = "http://www.credu.com/?page=" + str(1)
print(url)

import sys

print("welcome to", "python", sep="~", end="!", file=sys.stderr)


f = open("c:\\work\\demo.txt","wt")
print("file write", file=f)
f.close()

#구구단 출력
for x in range(1,6):
    print(x,"*",x,"=",str(x*x))


print("---약간 보정---")
for x in range(1,6):
    print(x,"*",x,"=",str(x*x).rjust(3))

print("---약간 보정---")
for x in range(1,6):
    print(x,"*",x,"=",str(x*x).zfill(3))

# 서식문자를 지정
print("{0:x}".format(10))
print("{0:b}".format(10))
print("{0:c}".format(65))
print("{0:e}".format(4/3))
print("{0:f}".format(4/3))
print("{0:.2f}".format(4/3))
# 화폐 형태로 출력
print("{0:,}".format(150000000))

