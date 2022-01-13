#include<stdio.h>
int main(){
	int x[10];
	int cont;
	for(cont=1;cont<=10;cont=cont+1){
		printf("Dame una cifra: ");
		scanf("%d",&x[cont]);
	}
	/*for(cont=0;cont<=10;cont++){
		printf("%d",x[cont]);
	}*/
	for(cont=0;cont<=10;cont++){
		printf("\nx[%d]=%d",cont,x[cont]);
	}
	return(0);
}
