def eName(name):
    print(name)


def eSalary(exp):
    if exp >= 5:
        return 3000000
    elif exp >= 3:
        return 1000000
    else:
        return 500000


eName('Rakrank')
a = eSalary(5)
print('Salary of the employee is ', a)
