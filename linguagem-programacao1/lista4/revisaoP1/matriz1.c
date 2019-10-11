#include <stdio.h>

void main () {
    int i = 0, j = 0;
    int m1[4][4];
    int m2[4][4];
    
    for (i=0;i<4;i++) {
        for (j=0;j<4;j++) {
            m1[i][j]=i+2;
            m2[i][j]=j+1;

        printf("m1[%d][%d] = %d\n", i, j, m1[i][j]);
        printf("m2[%d][%d] = %d\n", i, j, m2[i][j]);
        }

    printf("proxima linha --------\n");
    }

    printf("segundaparte \n");

    for (i=0;i<4;i++) {
        for (j=0;j<4;j++) {
            if (m1[i][j] == m2[i][j]) {
                m1[i][j]=9;
            }
            else {
                m2[i][j]=0;
            } 
        printf("m1[%d][%d] = %d\n", i, j, m1[i][j]);
        printf("m2[%d][%d] = %d\n", i, j, m2[i][j]);   
        } 
    printf("proxima linha --------\n");   
    }
}   