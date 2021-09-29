n = int(input())
arr1 = set(map(int,input().split()))
n = int(input())
arr2 = set(map(int,input().split()))
intersection = arr1 & arr2
union =arr1 | arr2
symetric = union-intersection
print(symetric)
