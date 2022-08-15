# 사전(dict) -> 해당 값을 찾아주는 함수 , {}를 사용
cabinet = {3: "유재석", 100: "김태호"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3)) # .get() = []
print(cabinet.get(5)) # 값이 없으면 none 으로 출력
print(cabinet.get(5, "사용 가능"))
# print(cabinet[5]) -> 없으면 프로그램 종료
# in으로 참거짓 판별
print(3 in cabinet) # True
print(5 in cabinet) # False

cabinet = {"A-3": "유재석", "B-100" : "김태호"} # 키 부분에 문자 또한 넣을 수 있다.
print(cabinet["A-3"])
print(cabinet["B-100"])

# 새 손님 -> 밑에다가 새로운 값을 넣으면 추가되거나 바뀐다. *
print(cabinet)
cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호"
print(cabinet)


# 간 손님 -> del을 사용하고 출력 시킨다 *
del cabinet["A-3"]
print(cabinet)

# key 들만 출력 -> .keys()로 출력(key는 앞의 값)
print(cabinet.keys())

# value들만 출력 -> .values()로 출력(values는 뒤의 값)
print(cabinet.values())

# key, value를 쌍으로 출력 ->.items()로 출력
print(cabinet.items())

# 목욕탕 폐점 -> .clear()을 입력
cabinet.clear()
print(cabinet)
