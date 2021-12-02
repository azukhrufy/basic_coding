if __name__ == '__main__':
    N = int(input())
    list_ = []
    for _ in range(N):
        s = input().split()
        command = s[0]
        args = s[1:]
        if command != "print":
            command += "("+ ",".join(args) +")"
            eval("list_."+command)
        else:
            print(list_)