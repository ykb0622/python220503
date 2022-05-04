# try1.py
# 함수를 정의
def divide(a,b):
    return a/b

#에러처리
try:
    # 함수 호출
    result = divide(5, 0)
    print("결과:{0}".format(result))
except ZeroDivisionError:
    print("0으로 나누면 안됩니다")
except TypeError:
    print("숫자여야 합니다")
else:
    print("결과:{0}".format(result))
finally:
    print("한번 더 체크")

print("---전체 코드 실행 종료---")
