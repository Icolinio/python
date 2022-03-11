def parzyste(y):
    print(y[::2])
def ostatni(y, n=1):
    print(y[-n:])
def reverse(y):
    print(y[::-1])
def dluzszy(y,x):
    len1 = len(y)
    len2 = len(x)
    if(len1 > len2):
        print(y)
    elif(len2 > len1):
        print(x)
def imdat(i,d):
    x="My name is {}. My date of birth is {}"
    print(x.format(i, d))
def factorial(k):
    if k > 1:
        return k * factorial(k - 1)
    else:
        return k
def eulers(n):
    s = 1
    i = 1
    while i <= n:
        s += 1 / factorial(i)
        i += 1
    return s
def sumaw():
    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    list2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    list3 = []
    for x in list1:
        for y in list2:
            list3.append([x,y])
    return list3
