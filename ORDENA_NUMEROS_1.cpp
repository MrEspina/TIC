#include<stdio.h>
int main(){
	int numeros[5];
	int cont;
	int aux;
	int repetir;
	for(cont=0;cont<5;cont++){
		printf("DAME UN NUMERO: ");
		scanf("%d",&numeros[cont]);
	}
	printf("\nLISTA DE NUMEOS: ");
	for(cont=0;cont<5;cont++){
		printf("%d",numeros[cont]);
	}
	for(repetir=0;repetir<5;repetir++){
		for(cont=0;cont<4;cont++){
			if(numeros[cont]>numeros[cont+1]){
				aux=numeros[cont];
				numeros[cont]=numeros[cont+1];
				numeros[cont+1]=aux;
			}	
		}
	}
	printf("\nLISTA ORDENADA: ");
	for(cont=0;cont<5;cont++){
		printf("%d",numeros[cont]);
	}
	
	return(0);
}
