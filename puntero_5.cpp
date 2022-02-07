#include<stdio.h>
#include<string.h>
#include<stdlib.h>
int main(){
	char aux[100];
	int longitud;
	char*mispalabras[5];
	int cont;
	for(cont=0;cont<5;cont++){
		printf("DIME LA PALABRA %d: ",cont+1);
		scanf("%s",aux);
		longitud=strlen(aux);
		mispalabras[cont]=(char*)malloc(longitud*sizeof(char));
		strcpy(mispalabras[cont],aux);
	}
	printf("\n LAS PALABRAS SON: ");
	for(cont=0;cont<5;cont++){
		printf("\n %s",*(mispalabras+cont));
	}
	
	return(0);
}
