# import sys
# t= int(sys.stdin.readline())
t=int(input())
# print(t)
while(t):
    n, a, b, k= map(int, input().split())
    c=0
    # print(n,a,b,k)
    for i in range(1,n+1):
        if((i%a==0 and i%b!=0) or (i%b==0 and i%a!=0)):
            c=c+1
    print("Win") if(c>=k) else print("Lose")
    t=t-1