# 이진 탐색
```
이진 탐색이란 원소가 정렬된 리스트의 양 끝에서 범위를 반씩 좁혀가며 
값을 찾는 알고리즘이다.

원소를 하나씩 탐색하는 순차 탐색은 원소가 정렬되어 있지 않은 리스트에서 사용되지만
만약 정렬되어 있다면 이진 탐색을 사용하는 것이 훨씬 효율적이다.
```

## 재귀를 이용한 이진 탐색 
```python
def binary_search(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2

    if array[mid] == target:
        return mid

    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)

    else:
        return binary_search(array, target, mid+1, end)


if __name__ == "__main__":
    n, target = map(int, input().split())
    array = list(map(int, input().split()))

    result = binary_search(array, target, 0, n-1)
    if result == None:
        print("원소 없다")
    else:
        print(result+1)
```

## 반복문을 이용한 이진 탐색
```python
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

if __name__ == "__main__":
    n, target = list(map(int, input().split()))
    array = list(map(int, input().split()))
    
    result = binary_search(array, target, 0, n-1)
    if result == None:
        print("원소 없음")
    else:
        print(result+1)
```
