from __future__ import division

def average(array):
    count=0
    length_of_array=len(array)
    for i in array:
        count+=i
    result1=float(count/length_of_array)
    return round(result1,3)
    # your code goes here

if __name__ == '__main__':
    n = int(input())
    arr = set(map(int, input().split()))
    result = average(arr)
    print(result)
