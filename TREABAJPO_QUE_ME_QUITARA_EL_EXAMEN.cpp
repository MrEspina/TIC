#include<stdio.h>
#include<string.h>
#include<stdlib.h>
int main(){
	char provisional[100];
    char *aux;
    int longitud;
    char *mispalabras[2];
    int cont;
    int repetir;
    int *palabron;
    char *primera;
    char*segunda;
    for(cont=0;cont<2;cont++){
        printf("Dime la palabra %d: ",cont);
        scanf("%s",provisional);
        longitud=strlen(provisional);
        printf("MIDE %d\n",longitud);
        mispalabras[cont]=(char *)malloc(longitud*sizeof(char));                
        strcpy(mispalabras[cont],provisional);
        palabron=palabron+longitud;
    }
    printf("%d",palabron);
    printf("\n LAS CINCO PALABRAS SON: ");
	for(cont=0;cont<5;cont++){
        printf("\n %s",*(mispalabras+cont));
    }
    for(repetir=1;repetir<5;repetir++){
        for(cont=0;cont<=3;cont++){
            if(strlen(mispalabras[cont])>strlen(mispalabras[cont+1])){
                aux=mispalabras[cont];
                mispalabras[cont]=mispalabras[cont+1];
                mispalabras[cont+1]=aux;
            }
        }
    }
    for(cont=0;cont=5;cont++){
    	strcpy;
	}
	printf("\nLA NUEVA PALABRA ES: %c",palabron);
	return(0);
}
