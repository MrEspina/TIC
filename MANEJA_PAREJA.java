package MiCodigo;

public class MANEJA_PAREJA {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int suma;
		int suma2;
		MiParejaNumeros objeto1; 
		objeto1=new MiParejaNumeros(5,8);
		MiParejaNumeros objeto2;
		objeto2=new MiParejaNumeros(1,4);
		objeto1.setNum1(6);
		objeto1.setNum2(4);
		suma=objeto1.devuelveSuma();
		objeto2.setNum1(4);
		objeto2.setNum2(1);
		suma2=objeto2.devuelveSuma();
		System.out.println("La suma de la pareja 1: ");
		System.out.println(suma);
		System.out.println("La suma de la pareja 2: "); 
		System.out.println(suma2);
	}

}
