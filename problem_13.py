if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        line = input().split()
        name, scores = line[0], line[1:]
        scores = list(map(float, scores))
        student_marks[name] = scores
    query_name = input()

for i in student_marks:
    sum1=sum(student_marks[i])/len(scores)
    student_marks[i]=sum1
print(student_marks[query_name])

