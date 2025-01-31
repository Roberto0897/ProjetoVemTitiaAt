package model;

public class EstudoDirigido extends Avaliacao {
	private String tema;
	private int numeroPaginas;

	public EstudoDirigido(String nome, Double nota, int numeroPaginas, String tema) {
		super(nome, nota);
//		if (this.getNota() <= 0) {
//			throw new IllegalArgumentException("A nota da ultima avaliacao, nao pode ser zero!");
//		}
		this.numeroPaginas = numeroPaginas;
		this.tema = tema;
	}

	public String getTema() {
		return tema;
	}

	public void setTema(String tema) {
		this.tema = tema;
	}

	public int getNumeroPaginas() {
		return numeroPaginas;
	}

	public void setNumeroPaginas(int numeroPaginas) {
		this.numeroPaginas = numeroPaginas;
	}

	@Override
	public String getInfo() {
		return "Tipo de avaliacao:  Estudo Dirigido;  \nNome: " + super.getInfo() + ", Tema: " + getTema() + ", Nota: ";
	}

//	@Override
//	public Double getNota() {
//		System.out.println();
//		return super.getNota();
//	}
//
//	@Override
//	public void setNota(Double nota) {
//		// TODO Auto-generated method stub
//		super.setNota(nota);
//	}

	
}
