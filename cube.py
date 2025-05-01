def cube(num):
    return num*num*num


def div3(num):
    if num % 3 == 0:
        return cube(num)
    else:
        return False


print(div3(9))
print(div3(4))
