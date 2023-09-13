# cook your dish here
for t in range(int(input())):
    a1,a2,b1,b2=map(int,input().split())
    neta=a1-a2 
    netb=b1-b2 
    total=neta+netb 
    if(total<0):
        print("YES")
    else:
        print("NO")