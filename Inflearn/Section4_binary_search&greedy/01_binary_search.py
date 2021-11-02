'''
## 이분 검색 ##
임의의 N개의 숫자가 입력으로 주어집니다.
N개의 수를 오름차순으로 정렬한 다음 N개의 수 중 한 개의 수인 M이 주어지면
이분검색으로 M이 정렬된 상태에서 몇 번째에 있는지 구하는 프로그램을 작성하세요.
단 중복값은 존재하지 않습니다.
'''
N, M = map(int, input().split())
def bs(N, M):
    arr = list(map(int, input("arr : ").split()))
    arr.sort()
    lt = 0
    rt = len(arr)
    mid = (lt + rt)//2

    while True:
        if arr[mid] == M:
            return mid
# [1,2,3,4,5]
        if arr[mid] > M:
            rt = mid
            mid = (lt + rt) // 2

        if arr[mid] < M:
            lt = mid
            mid = (lt + rt) // 2

print(bs(N,M))








