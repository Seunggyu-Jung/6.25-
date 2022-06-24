# 튜플 -> 괄호로 만들어진 집합체. 항목 추가나 변경이 불가능, 하지만 프로세스 처리 속도가 리스트 보다 빠름

menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

# menu.add("셍선까스") -> 추가, 수정이 불가능 하다

#name = "김종국"
#age = 20 
#hobby = "운동"
#print(name , age , hobby)

(name, age, hobby) = ("김종국", 20, "운동")
print(name, age, hobby)