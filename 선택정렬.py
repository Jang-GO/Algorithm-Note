"""
처리되지 않은 데이터 중에서 가장 작은 데이터를 선택해 
맨앞에 있는 데이터와 바꾸는 것을 반복
"""
list = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(list)):
    minimum = i #가장 작은 원소의 인덱스
    for j in range(i+1,len(list)):
        if list[minimum]>list[j]:
            minimum = j
    list[i],list[minimum] = list[minimum],list[i]

print(list)