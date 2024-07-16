def fibbinario(num):
    a,b = 0, 1 
    sum = 0 
    for i in range(1,num+1):
        a = b 
        b = sum 
        sum = a+b
        print(sum,end = " ")
fibbinario(12)