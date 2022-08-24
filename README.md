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

## 2. 딕셔너리(사전)
{} : key값과 value 값을 지정하여 정리 , {key:value}를 사용
```
cabinet = {3: "유재석", 100: "김태호"}
print(cabinet[3])
print(cabinet[100])
-> 유재석, 김태호
```

- .get() 메소드 : 딕셔너러의 키값에 해당하는 value값을 출력, 해당 키값이 없을 경우 none 출력
```
print(cabinet.get(3)) -> 유재석
print(cabinet.get(5)) -> none
print(cabinet.get(5, "사용 가능")) -> 사용 가능
```
- (키값 in 딕셔너리) : 블리언 타입으로 출력
```
print(3 in cabinet) -> True
print(5 in cabinet) -> False
```
- 키 부분에 문자 또한 넣을 수 있음
```
cabinet = {"A-3": "유재석", "B-100" : "김태호"} 
print(cabinet["A-3"]) 
print(cabinet["B-100"])
-> 유재석, 김태호
```
- 새로운 인덱스 추가 : 딕셔너리 안에 새로운 키값과 value 값을 넣는다.
```
cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호"
print(cabinet)
-> {'A-3': '김종국', 'B-100': '김태호', 'C-20': '조세호'}
```
- del : 딕셔너리에서 삭제할 경우
```
del cabinet["A-3"]
print(cabinet)
-> {'B-100': '김태호', 'C-20': '조세호'}
```
- .keys() : key 들만 출력
```
print(cabinet.keys())
-> dict_keys(['B-100', 'C-20'])
```
- .values() : value 값들만 출력
```
print(cabinet.values())
-> dict_values(['김태호', '조세호'])
```
- .items() : key, value를 쌍으로 출력
```
print(cabinet.items())
-> dict_items([('B-100', '김태호'), ('C-20', '조세호')])
```
- .clear() : 일괄 삭제
```
cabinet.clear()
-> {}
```






