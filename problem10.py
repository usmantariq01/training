if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(set(list(arr)))
    ar = len(arr)
    print(ar)
    arr = sorted(arr)
    print(arr[ar-2])
    print(arr[ar-3])
