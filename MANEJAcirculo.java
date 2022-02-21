package MiCodigo;

public class MANEJAcirculo {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Circunferencia circunferencia1;
		Circunferencia circunferencia2;
		circunferencia1=new Circunferencia(7, 9, 4.5);
		System.out.println("CIURCULITO 1:");
		System.out.println("Coordenada X del centro: "+circunferencia1.coordX);
		System.out.println("Coordenada Y del centro: "+circunferencia1.coordY);
		System.out.println("radio: "+circunferencia1.getRadio());
		System.out.println("El area es: "+circunferencia1.getRadio);
		System.out.println("Area: "+circunferencia1.devuelveArea());
		System.out.println("Longitud: "+circunferencia1.devuelveLogitud());
	}

}
