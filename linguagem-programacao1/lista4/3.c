#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main () {
    int matriz[4][4];
    int i,j,linha,coluna,somal, somac;

    linha= 0; 
    coluna= 0; 
    somal = 0;
    somal= 0; 

    for(i=0;i<4;i++){
        for(j=0;j<4;j++){
            printf("Insira Matriz[%d][%d]:",i,j);
            scanf("%d",&matriz[i][j]); 

        
   if (i==3) { 
       linha= linha + matriz[i][j];
    }

    if (j==1) {
        coluna= coluna + matriz[i][j];
    }

    somal = somal + matriz[i][j];
    somac = somac + matriz[i][j];

        }
    }
    
    printf("\n A soma da linha eh: %d",linha);
    printf("\n A soma da coluna eh: %d", coluna);
    printf("\n A soma total da linha eh: %d \n", somal);
    printf("\n A soma total da linha eh: %d \n", somac);

 
    for(i=0;i<4;i++) {
        for(j=0;j<4;j++) {
            printf(" Matriz Transposta[%d][%d]= %d \n", i, j, matriz[i][j]);
        }
    return 0;
}