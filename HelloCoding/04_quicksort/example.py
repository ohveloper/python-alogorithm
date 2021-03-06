# 1. sum 함수를 작성해 보세요
def sum(arr):
    if len(arr) == 0:
        return 0
    return arr[0] + sum(arr[1:])


arr = [1, 2, 3, 4]
sum_result = sum(arr)
print(sum_result)


# 2.리스트에 포함된 원소의 숫자를 세는 재귀 함수를 작성해 보세요
def count(arr):
    if arr == []:
        return 0
    return 1 + count(arr[1:])


count_result = count(arr)
print(count_result)


# 3. 리스트에서 가장 큰 수를 찾는 재귀함수
## 방법 1
def max(a, b):
    return a if a > b else b


def maximum(L):
    if len(L) == 1:
        return L[0]
    else:
        return max(L[0], maximum(L[1:]))


max_result = maximum(arr)
print('max: ', max_result)


## 방법 2
def max2(list):
    if len(list) == 2:
        return list[0] if list[0] > list[1] else list[1]
    # _max2 = max2(list[1:])
    return list[0] if list[0] > max2(list[1:]) else max2(list[1:])


max2_result = max2(arr)
print('max2: ', max2_result)


# 파이선에서 if 문을 사용할때
def test(a, b):
    return a if a > b else b  # 만약 a 가 b보다 크면 a를 리턴하고 그렇지 않으면 b를 리턴하세요


print(test(12, 2))
