from random import *
lst = [1, 2, 3, 4 , 5 , 6 , 7 , 8 , 9 , 10, 11 , 12 , 13 , 14 ,15 ,16, 17, 18, 19, 20]
# lst = range(1 , 21) 1부터 21직전까지 숫자를 생성
# range의 타입은 range -> lst = list(lst)로 타입 변경 
shuffle(lst)
winners = sample(lst,4)
print("---당첨자 발표---")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print("---축하합니다---")


