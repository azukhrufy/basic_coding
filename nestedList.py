def sorted_list(sub_li):
    l = len(sub_li)
    for i in range(0, l):
        for j in range(0, l-i-1):
            if (sub_li[j][1] > sub_li[j + 1][1]):
                tempo = sub_li[j]
                sub_li[j]= sub_li[j + 1]
                sub_li[j + 1]= tempo
    return sub_li

def counting(li,val):
    l = len(li)
    res = 0
    for i in range(0,l):
        if li[i][1] == val:
            res +=1
    
    return res

if __name__ == '__main__':
    students = []
    lowest = 0
    res = []
    result = []
    
    for _ in range(int(input())):
        student = [0] * 2
        name = input()
        score = float(input())
        
        student[0] = name
        student[1] = score
        students.append(student)
    
    res = sorted_list(students)
    
    #get the lowest
    index = counting(students,students[0][1])
    
    #get val
    index2 = counting(students,students[index][1])
    
    for i in range(index,index+index2):
        result.append(students[i][0])
        
    result.sort(reverse=False) 
    
    for i in result:
        print(i)