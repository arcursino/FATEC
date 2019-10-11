#include <stdio.h>
main() {
    int x = 0;
	int y = 0;
	int z=0;
	for (z=0; z < 5; z++) {
        if ( (++x > 4) || (++y > 2) ) {
            x++;
        }
    }
    printf("x:%d y:%d \n",x,y) ;             
}