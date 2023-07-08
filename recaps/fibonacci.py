def fib(pos):
    if pos >=3:
        output = fib(pos-1)+fib(pos-2)
    else:
        output = 1
    return output

for i in range(10):
    print(fib(i)) 

def count(num):
    if num > 0:
        count(num-1)
        print(count(num))

count(10)