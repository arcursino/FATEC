#include <stdio.h>
 #include <stdlib.h> 

int primo(n); 

int main() { 
	int n;
	printf ('Digite um número: ');
	scanf('%d', &n); 

	if(primo(n)) {
    printf('%d É primo!\n', n); 
		} else {
      printf('%d não é primo! \n', n);
		}
		return 0; 
	} 

int primo(n) { 
  int cont = 1; 

  while(cont <= n){
    if (n % cont == 0) {
      if(cont == 1 || cont == n) {
        cont ++;
      } else {
        return 0;
      }
    }
  }
  
   
    
