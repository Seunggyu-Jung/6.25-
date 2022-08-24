# 나도 코딩 파이썬: 5강 리스트

# 1. 리스트
[] : 자료를 순서대로 나열시킨다

- 숫자만 나열할 경우 : [10, 20, 30]
```
subway = [10, 20, 30]
print(subway)
-> [10, 20, 30]
```
- 문자열을 나열할 경우 : ["유재석", "조세호", "박명수"]
```
subway = ["유재석", "조세호", "박명수"]
print(subway)
-> ['유재석', '조세호', '박명수']
```
- .index() : 해당 인덱스가 몇번째에 있는지 알기 위해서 사용
```
subway = ["유재석", "조세호", "박명수"]
subway = subway.index("조세호")
print(subway)
-> 1
```
- .append() : 인덱스를 추가하고자 할 경우
```
subway.append("하하") 
print(subway)
-> ['유재석', '조세호', '박명수', '하하']
```
- .insert(,"") : 인덱스를 중간에 추가하고자 할 경우
```
subway.insert(1, "정형돈")
print(subway)
-> ['유재석', '정형돈', '조세호', '박명수', '하하']
```
- .pop() : 맨 뒤에 있는 사람을 빼낼때 사용
```
print(subway.pop())
-> 하하
```
- .count() : 해당 리스트에 동일한 인덱스가 몇개 있는지 알고 싶은 경우
```
subway.append("유재석")
print(subway.count("유재석"))
-> 2
```
- .sort() : 정렬, 숫자를 작은 수부터 일렬로 정리
```
num_list = [5,4,3,2,1]
print(num_list)
-> [1, 2, 3, 4, 5]
```
- .reverse() : 역으로 정렬, 숫자를 큰 수부터 일렬로 정리
```
num_list = [1, 2, 3, 4, 5]
print(num_list)
-> [5, 4, 3, 2, 1]
```
- .clear(): 리스트 안에 있는 인덱스를 전부 지움
```
num_list = [1, 2, 3, 4, 5]
num_list.clear()
print(num_list)
-> []
```
- 다양한 데이터 타입과 함께 사용가능 : 숫자, 문자, 불리안 전부 포함
```
mix_list = ["조세호" , 20, True]
print(mix_list)
-> ['조세호', 20, True]
```
- .extend() : 리스트의 확장
```
num_list = [1,2,3,4,5]
num_list.extend(mix_list)
print(num_list)
-> [1, 2, 3, 4, 5, '조세호', 20, True]
```





