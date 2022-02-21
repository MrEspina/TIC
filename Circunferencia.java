package MiCodigo;

public class Circunferencia {
	private MiParejaNumeros centroCirculo;
	private double radio;
	public String getRadio;
	public Circunferencia(int coordX, int coordY, double d) {
		super();
		centroCirculo=new MiParejaNumeros(coordX,coordY);
		this.radio = d;
	}
public int getCoordX() {
	return (centroCirculo.getNum1());
}
public void setCoordX(int coordX) {
	centroCirculo.setNum1(coordX);
}
public int getCoordY() {
	return (centroCirculo.getNum2());
}
public void setCoordY(int coordY) {
	centroCirculo.setNum1(coordY);
}
public double getRadio() {
	// TODO Auto-generated method stub
	return radio;
}
public double devuelveArea() {
	double area = 0;
	area=Math.PI*Math.pow(radio, 2);
	//area=Math.PI*(radio)*(radio);
	return area;
}
public double devuelveLogitud() {
	double longitud;
	longitud=2*Math.PI*radio;
	return longitud;
}
}