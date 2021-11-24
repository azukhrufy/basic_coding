if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    res = 0
    
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    if query_name in student_marks:
        for i in student_marks[query_name]:
            res += i

    result = res / len(student_marks[query_name])
    print(format(result,'.2f'))