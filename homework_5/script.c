#include <stdio.h>

int main(){

    int  a = 1500;
    
    int b = 0;
    int res;


    do{
        res+=a;
        b++;
    }
    while (res!= -1200);

    printf("b=%d\n", b );

    return 0;
}