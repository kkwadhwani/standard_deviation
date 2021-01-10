# standard deviation without shortcut
import math

a = [9, 2, 5, 4, 12, 7, 8, 11, 9, 3, 7, 4, 12, 5, 4]
b=[]

# mean of the values in a list a
def mean():
    n = 0
    for i in a:
        n+=i
    return n/len(a)


# assigning mean value to the variable "average_num".
average_num= mean()


# Each number from the list minus mean value and square of that value.
def number_minus_mean():
    n=0
    for i in a:
        ans= (i-average_num)*(i-average_num)
        b.append(ans)
    for i in b:
        n+=i
    return n


# square values were appended in list b and then adding them all.
value= number_minus_mean()

# getting Variance
def variance():
    variance = 1 / (len(a)) * value
    return variance


def stdfunc():
    variance = 1 / (len(a)) * value
    std=math.sqrt(variance)

    return std

print(variance())
print(stdfunc())


