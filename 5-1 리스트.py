# 리스트 [] : 자료를 순서대로 나열시킨다

# 지하철 칸별로 10명, 20명, 30명 -> 숫자만 있는 경우
subway = [10, 20, 30]
print(subway)

# 지하철 칸별로 탄 사람을 나열하는 경우 -> 문자만 있는 경우
subway = ["유재석", "조세호", "박명수"]
print(subway)

# 조세호씨가 몇 번째 칸에 타고 있는가? -> .index()를 사용
# subway = subway.index("조세호")
# print(subway)

# 하하씨가 다음 정류장에서 다음 칸에 탐-> 뒤에 추가하여 입력 .append
subway.append("하하") 
print(subway)

# 정형돈씨가 중간에 끼여드는 경우 -> 중간에 추가함 (위치, 내용) .insert(,"")
subway.insert(1, "정형돈")
print(subway)

# 지하철에 있는 사람을 뒤에서 한 명씩 꺼냄  .pop()
print(subway.pop())
print(subway)

# 같은 이름의 사람이 몇 명 있는지 확인 .count()
subway.append("유재석")
print(subway.count("유재석"))

# 정렬 .sort() -> 숫자를 작은 수부터 일렬로 정리하여 입력
num_list = [5 ,4, 3, 2, 1]
num_list.sort()
print(num_list)

# 순서 뒤집기 .reverse() -> 역순으로 정렬시킴
num_list.reverse()
print(num_list)

# 모두 지우기 .clear() -> 싹 다 지워버림
# num_list.clear()
# print(num_list)

# 다양한 자료와 함께 사용 -> 숫자, 문자, 불리안 전부 포함
mix_list = ["조세호" , 20, True]
print(mix_list)

# 리스트 확장 -> .extend()
num_list.extend(mix_list)
print(num_list)
