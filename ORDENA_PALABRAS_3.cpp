#include<stdio.h>
#include<string.h>
#include<stdlib.h>
int main(){
	char provisional[100];
    char *aux;
    int longitud;
    char *mispalabras[5];
    int cont;
    int repetir;
    for(cont=0;cont<5;cont++){
            printf("Dime la palabra %d: ",cont);
            scanf("%s",provisional);
            longitud=strlen(provisional);
            printf("MIDE %d\n",longitud);
            mispalabras[cont]=(char *)malloc(longitud*sizeof(char));                
            strcpy(mispalabras[cont],provisional);
    }
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
    printf("\n LAS CINCO PALABRAS ORDENADAS POR LONGITUD SON: ");
    for(cont=0;cont<5;cont++){
        printf("\n %s",*(mispalabras+cont));
    }
	return(0);
       
}
