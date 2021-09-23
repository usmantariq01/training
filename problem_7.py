# leap year

def is_leap(year):
    leap = False

    if 1900 <= year <= 100000:
        if (year % 4) == 0:
            if (year % 100 == 0):
                leap = False
                if (year % 400) == 0:
                    leap = True
                else:
                    leap = False
            else:
                leap = True
        else:
            leap = False

    # Write your logic here

    return leap


year = int(input())
print(is_leap(year))
