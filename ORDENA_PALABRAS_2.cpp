#include<stdio.h>
#include<string.h>
#include<stdlib.h>
int cuenta_vocales(char *letrita){
        int n_vocales=0;
        int cont;
        int longitud;
        longitud=strlen(letrita);
        for(cont=0;cont<longitud;cont++){
                printf("\nla letra %d es %c",cont,*(letrita+cont));
                if(*(letrita+cont)=='A' || *(letrita+cont)=='a'){
                        n_vocales++;
                }
                if(*(letrita+cont)=='E' || *(letrita+cont)=='e')
                        n_vocales++;
                if(*(letrita+cont)=='I' || *(letrita+cont)=='i')
                        n_vocales++;
                if(*(letrita+cont)=='O' || *(letrita+cont)=='o')
                        n_vocales++;
                if(*(letrita+cont)=='U' || *(letrita+cont)=='u')
                        n_vocales++;        
        }
        return(n_vocales);
}
int main(){
        char provisional[10];
        char *aux;
        int longitud;
        char *mispalabras[5];
        int cont;
        int repetir;
        for(cont=0;cont<5;cont++){
                printf("\nDime la palabra %d: ",cont);
                scanf("%s",provisional);
                printf("\nLa palabra %s tiene %d vocales",provisional,cuenta_vocales(provisional));
                longitud=strlen(provisional);
                printf("\nMIDE %d",longitud);
                mispalabras[cont]=(char *)malloc(longitud*sizeof(char));           
                strcpy(mispalabras[cont],provisional);
        }
        printf("\n LAS CINCO PALABRAS SON: ");
        for(cont=0;cont<5;cont++){
                printf("\n %s",*(mispalabras+cont));
        }
        for(repetir=1;repetir<5;repetir++){
           for(cont=0;cont<=3;cont++){
                   if(cuenta_vocales(mispalabras[cont])>cuenta_vocales(mispalabras[cont+1])){
                          aux=mispalabras[cont];
                          mispalabras[cont]=mispalabras[cont+1];
                          mispalabras[cont+1]=aux;
                        }
                }
        }
        printf("\n LAS CINCO PALABRAS ORDENADAS SON: ");
        for(cont=0;cont<5;cont++){
                printf("\n %s",*(mispalabras+cont));
        }
        return(0);
}
