# 자료의 형태 -> {} : 집합(set), [] : 리스트(list), () : 튜플 
# 자료의 형태 변환 -> , type()으로 변경

menu = {"커피", "우유", "주스"}
print(menu)
print(menu, type(menu)) 

# set -> list
menu = list(menu)
print(menu, type(menu))

#list -> tuple
menu = tuple(menu)
print(menu, type(menu))

#tuple -> set
menu = set(menu)
print(menu, type(menu))




