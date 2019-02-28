t=int(input())
while(t):
    n, a, b, k= map(int, input().split())
    c=0
    for i in range(1,n+1):
        if((i%a==0 and i%b!=0) or (i%b==0 and i%a!=0)):
            c=c+1
            # print(c)
            if(c>=k):
                print('Win')
                break
    # This else is for the 'for' statement,will be executed if 'for' does not break and gets executed normally,else is skipped if break occurs
    else:                       
        print('Lose')
    t=t-1