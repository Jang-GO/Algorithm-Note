"""
기준 데이터를 설정하고 그 기준보다
큰 데이터와 작은 데이터의 위치를 바꾸는 방법

일반적인 상황에서 가장 많이 사용되는 정렬 알고리즘

병합 정렬과 더불어 대부분의 프로그래밍 언어의 정렬
라이브러리의 근간이 되는 알고리즘
"""
list = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(list,start,end):
    if start>=end: # 원소가 1개인 경우 종료
        return
    pivot = start #피벗은 첫 번째 원소
    left = start + 1
    right = end
    while(left<=right):
        #피벗보다 큰 데이터를 찾을때 까지 반복
        while(left<=end and list[left]<=list[pivot]):
            left+=1
        #피벗보다 작은 데이터를 찾을때 까지 반복
        while(right>start and  list[right]>= list[pivot]):
            right -=1
        if(left>right):
            list[right],list[pivot] = list[pivot],list[right]
        else:
            list[left],list[right] = list[right],list[left]
        
        quick_sort(list,start,right-1)
        quick_sort(list,right+1,end)
quick_sort(list,0,len(list)-1)
print(list)