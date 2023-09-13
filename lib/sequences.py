# import ipdb
#!/usr/bin/env python3

def print_fibonacci(length):
    a= 0
    b= 1
    list_fib=[]
    if(length == 0):
        print(list_fib)
    else:
        for i in range(length):
            c= a+b
            list_fib.append(a)
            a=b
            b=c
        print(list_fib)
# ipdb.set_trace()
print_fibonacci(1)


  
