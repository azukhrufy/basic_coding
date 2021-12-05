def average(array):
    # your code goes here
    result = set(array)
    s = 0.0
    for i in result:
        s += i
    
    result = s / len(result)
    return result

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)