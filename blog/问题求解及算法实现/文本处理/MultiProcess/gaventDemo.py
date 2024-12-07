# n! 递归

def fact(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * fact(n-1)

def fact_tail(n, rst):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    elif n == 1:
        return rst
    else:
        return fact_tail(n - 1 ,n * rst)
    

def fib(n):
    if n < 0:
        return 0
    if n <= 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fib_tail(n, a, b):
    # print("digui: ", n, rst)
    if n <= 0 :
        return 0 
    elif n < 2:
        return a
    else:
        return fib_tail(n-1, b, a + b)


if __name__ == "__main__":
    print("0 的阶乘： {}，1的阶乘：{}， 10 的阶乘： {}".format(fact(0),fact(1),fact(10)))
    print("0 的阶乘： {}，1的阶乘：{}， 10 的阶乘： {}".format(fact_tail(0,1),fact_tail(1,1),fact_tail(10,1)))
    # print("1 的阶乘： {}，1的阶乘：{}， 10 的阶乘： {}".format(fib(1),fib(2),fib(10)))
    for i in range(1,10+1):
        print(fib(i), end=" ")

    print("\n")
    for i in range(1,10+1):
        print(fib_tail(i, 1, 1), end=" ")   
    
