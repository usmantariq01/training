def count_substring(string, sub_string)
    string.lower()
    count = 0
    for i in range(len(string) + 1):
        if sub_string in string[i:i + 3]:
            count += 1;
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
