"""
처리되지 않은 데이터를 하나씩 골라
적절한 위치에 삽입.
난이도는 선택정렬보다 높고 효율도 선택정렬보다 높음
"""
list = [7,5,9,0,3,1,6,2,4,8]

for i in range(1,len(list)):
    for j in range(i,0,-1):# 인덱스 i부터 인덱스 1까지 1씩 감소하며 반복
        if list[j]<list[j-1]:# 한 칸씩 왼쪽으로 이동
            list[j],list[j-1] = list[j-1],list[j]
        else: # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
            break

print(list)