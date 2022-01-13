#include<stdio.h>
int main(){
	char letras[5];
	int cont;
	for(cont=0;cont<5;cont++){
		printf("DAME UNA LETRA %d: ",cont);
		scanf(" %c",&letras[cont]);
	}
	printf("\nHAS ESCRITO LA PALABRA: ");
	for(cont=0;cont<5;cont++){
		printf("%c",letras[cont]);
	}
	printf("\nLA PALABRA AL REVES ES: ");
	for(cont=4;cont>=0;cont--){
		printf("%c",letras[cont]);
	}
	return 0;
}
