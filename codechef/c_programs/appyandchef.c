#include <stdio.h>
int main(void) {
    int t,n,a,b,k,c,i;
    scanf("%d",&t);
    while(t--){
        scanf("%d%d%d%d",&n,&a,&b,&k);
        c=0;
        for(i=1;i<=n;i++){
            if((i%a==0 && i%b!=0) || (i%b==0 && i%a!=0)){
                c=c+1;
            }
        }
        (c>=k)?printf("Win\n"):printf("Lose\n");
    }
	return 0;
}