start = 2147483647

for i in range(1,100000):
    result = (start * i)%1500

    if(result)==0:
        print(i)