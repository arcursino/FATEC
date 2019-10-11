#include<stdio.h>


void func(int *px, int *py)  {   /*A*/ 
    py = px;                     /*B*/
    printf("py = %d\n", py);
    *py = (*py) * (*px)*(*px);   /*C*/
    printf("*py = %d\n", *py);
    *px = *py;                   /*D*/
     printf("*px = %d\n", *px);

} 

void main(void) {
    int x, y;
    scanf("%d",&x);                         /*2*/
    scanf("%d",&y);                         /*1*/
    func(&x,&y);
    printf("x = %d, y = %d\n", x, y);        /*E*/
}
