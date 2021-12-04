import textwrap

def wrap(string, max_width):
    # wrap_string = [string[i : i + max_width] for i in range(0,len(string),max_width)]
    wrap_string = []
    for i in range(0,len(string),max_width):
        wrap_string.append(string[i : i + max_width])
        wrap_string.append("\n")
    wrap_string.pop()
    wrap_string = ''.join(wrap_string)

    return wrap_string

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)