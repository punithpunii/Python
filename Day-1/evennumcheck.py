for i in range(100,401):
    if i%2!=0:
        continue
    else:
        x=i
        while x!=0:
            d=x%10
            if d%2!=0:
                break
            x=x//10
        if x==0:
            print(i,end=",")
