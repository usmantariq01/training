#problem no 1
n = int(input().strip())
if 1 <= n <= 100:
    if (n % 2) == 0 and n == 4:
        print("Not Weird")
    elif (n % 2) and 6 <= n <= 20:
        print("Weird")
    elif (n % 2 == 0) and n > 20:
        print("Not Weird")
    else:
        print("Weird")
