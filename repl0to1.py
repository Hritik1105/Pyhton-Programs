# Replace 0 to 1


n=int(input('Enter number: '))
n=str(n) 

n=list(n)
r=""
for i in range(len(n)):

    if(n[i]=='0'):
        n[i]='1'
    r=r + n[i]
del n    
print("Converted number is :",int(r))