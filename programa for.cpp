#include<stdio.h>

int main(){
	int x[10];
	int cont;
	for(cont=1;cont<=10;cont=cont+1){
	//cont=cont+1 u otra opción cont++
		printf("Dame una cifra: ");
		scanf("%d",&x[cont]);
	}
	return(0);
}
