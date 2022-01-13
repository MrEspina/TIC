#include<stdio.h>
#include<string.h>
#include<stdlib.h>
int main(){
	char aux[100];
	int longitud;
	printf("DIME ALGO BONITO ");
	scanf("%s",aux);
	longitud=strlen(aux);
	char *palabra;
	palabra=(char*)malloc(longitud*sizeof(char));
	strcpy(palabra,aux);
	printf("\nRESUTADO: ");
	printf("%s",palabra);
	
	return(0);
}
