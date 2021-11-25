def count_substring(string, sub_string):
    s = list(sub_string)
    count = 0
    res = 0
    for i in range(0,len(string)):
        if string[i] == s[0]:
            index = i
            count = 0
            for x in range(0,len(sub_string)):
                if string[index] == sub_string[x]:
                    count += 1
                if index < len(string) -1:
                    index += 1
            if count == len(sub_string):
                res += 1
    
    return res

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)