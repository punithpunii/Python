"""bin_num=input("Enter the numbers:")
bin_num_list=[int(num) for num in bin_num.split(',')]
print(bin_num_list)
"""
"""for num in bin_num_list:
    prod=1
    dec=0
    op=num
    while num!=0:
        dec=dec+num%10*prod
        prod*=2
        num=num/10
    if dec%5==0:
        print(op)

"""
num=input("Enter the number:")
def bin_to_dec(num):
    dec=0
    if num in '[2-9]' or num in '[-1 - -9]':
        return "Invalid number"
    else:
        x=int(num)
        
        prod=1
        while x!=0:
            dec=dec+x%10*prod
            prod*=2
            x=x//10
    print(dec)
bin_to_dec(num)
        


