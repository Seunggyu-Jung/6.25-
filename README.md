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

## 3. 튜플 ()
괄호로 만들어진 집합체. 항목 추가나 변경이 불가능, 하지만 프로세스 처리 속도가 리스트 보다 빠름

```
menu = ("돈까스", "치즈까스")
print(menu[0]) -> 돈까스
print(menu[1]) -> 치즈까스
```

```
(name, age, hobby) = ("김종국", 20, "운동")
print(name, age, hobby)
```

## 4. 세트 
집합을 의미, 중복 안됨, 순서 무작위
```
my_set = {1, 2, 3, 3 , 3}
print(my_set) -> {1, 2, 3}  # 중복 안됨
```

- 세트 표현 방식 
```
java = { "유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])
```

- .intersection() or & : 교집합
```
print(java & python)
print(java.intersection(python))
-> {'유재석'}
```

- .union() or | : 합집합
```
print(java | python)
print(java.union(python))
-> {'양세형', '김태호', '박명수', '유재석'}
```

- .diference() or - : 차집합
```
print(java-python)
print(java.difference(python))
-> {'김태호', '양세형'}
```

- .add() : 세트에 새로운 인덱스를 더할 경우
```
python.add("김태호")
print(python)
-> {'박명수', '김태호', '유재석'}
```

- .remove() : 세트에서 원소를 빼고 싶은 경우
```
python.remove("김태호")
print(python)
-> {'박명수', '유재석'}
```

## 5. 자료구조의 변경
자료의 형태 -> {} : 집합(set), [] : 리스트(list), () : 튜플
자료의 형태 출력 -> , type()으로 출력

- menu = {"커피", "우유", "주스"} -> 세트형태

- set -> list
```
menu = list(menu)
print(menu, type(menu))
-> ['주스', '커피', '우유'] <class 'list'>
```

- list -> tuple
```
menu = tuple(menu)
print(menu, type(menu))
-> ('주스', '커피', '우유') <class 'tuple'>
```

- tuple -> set
```
menu = set(menu)
print(menu, type(menu))
-> {'주스', '커피', '우유'} <class 'set'>
```







