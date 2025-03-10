DEFAULT_LEVEL = 200
my_level = int(input())


def level():
    ans = " "
    if my_level < 200:
        ans = "not good"
    else:
        ans = "good"
    
    return ans



print(level())



