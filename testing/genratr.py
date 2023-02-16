def my_genrator(n):
    value = 0
    while(value<n):
        yield value
        value+=1
        


for val in my_genrator(5):
    print(val)        
    