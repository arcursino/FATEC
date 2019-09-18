 #include <stdio.h>


 void main () {
     int i, j;
     int m1[3][3];
     int m2[3][3];

     for (i=0;i<3;i++){
         for (j=0;j<3;j++) {
             m1[i][j]=i+2;
             m2[i][j]=j+2;
             printf("Primeira rodada m1[%d][%d] = %d\n", m1[i][j], i);
             printf("Primeira rodada m2[%d][%d] = %d\n", m2[i][j], j);
         }
     }
     
     for (i=0;i<3;i++) {
         for (j=0;j<3;j++) {
             if (m1[i][j] == m2[i][j]) {
                 m1[i][j]=0;
             } else {
                 m2[i][j]=1;
             }
             printf("Segunda rodada m1[%d][%d] = %d\n", m1[i][j]);
             printf("Segunda rodada m2[%d][%d] = %d\n", m2[i][j]);                   
         }
         
     }
     
 }
     
         
     
           