#include<stdio.h>
int main(){
	char palabra[5];
	int cont;
	printf("ESCRIBE UNA PALABRA: ");
	scanf("%s",palabra);
	printf("\nHAS ESCRITO %s",palabra);
	printf("\nVOY A DELETREARLA: ");
	for(cont=0;cont<5;cont++){
		printf("\n%c",palabra[cont]);
	}
	palabra[1]='U';
	printf("\nPALABRA CAMBIADA: %s",palabra);
	printf("\nQUIEN ES QUIEN: ");
	printf("\npalabra[1] = %x",palabra);
	
	return 0;
	
}
