# Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи 
# оно является, то есть выведите такое число n, что φ(n)=A. Если А не является 
# числом Фибоначчи, выведите число -1.
# Input: 5 Output: 6

x = int(input('Введите число: '))

n1 = 0 # 0 1 1 2 3 5
n2 = 1
s = 1

while n2 < x:
    n1,n2 = n2,n1+n2
    # tmp = n2+n1
    # n1 = n2
    # n2 = tmp
    s += 1
if n2 == x:
    print(s)
else:
    print(-1)


# a,b,c = 4,6,1