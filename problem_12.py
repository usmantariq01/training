def split_and_join(line):
    # write your code
    split = line.split(" ")
    join = "-".join(split)
    return join

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
