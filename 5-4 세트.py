# 세트 (집합)
# 중복 안됨, 순서 무작위
my_set = {1, 2, 3, 3 , 3}
print(my_set)  # 중복 안됨

java = { "유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

# 교집합 (둘다 할 수 있는 사람), &로 표기 또는 .intersection()
print(java & python)
print(java.intersection(python))


#합집합 (하나라도 할 수 있는 사람) |로 표기 또는 .union()
print(java | python)
print(java.union(python))


# 차집합 (한 부분만 할 수 있는 것) -로 표기 또는 .difference()
print(java-python)
print(java.difference(python))

# 집합에 원소를 더하는 경우 -> .add() 로 표기
python.add("김태호")
print(python)

# 집합에서 원소를 빼는 경우 -> .remove() 로 표기
python.remove("김태호")
print(python)