#include <stdio.h>
main() {
    int x = 0;
	int y = 0;
	int z=0;
	for(z=0; z < 7; z++){
        if( (++x > 2) && (y++ > 3) ){
            x++;
        }
        printf("x:%d y:%d \n",x,y);
    }
    
}