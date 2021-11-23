if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
    second_highest = sorted(set(arr),reverse=True)[1]
    
    print(second_highest)