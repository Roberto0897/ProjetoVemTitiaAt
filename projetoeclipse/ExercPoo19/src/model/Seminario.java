package model;

public class Seminario extends Avaliacao {
	private String tema;
	private Double tempoDuracao;

	public Seminario(String nome, Double nota, Double tempoDuracao, String tema) {
		super(nome, nota);
//		if (this.getNota() <= 0) {
//			throw new IllegalArgumentException("A nota da ultima avaliacao, nao pode ser zero!");
//		}
		this.tema = tema;
		this.tempoDuracao = tempoDuracao;
	}

	public String getTema() {
		return tema;
	}

	public void setTema(String tema) {
		this.tema = tema;
	}

	public Double getTempoDuracao() {
		return tempoDuracao;
	}

	public void setTempoDuracao(Double tempoDuracao) {
		this.tempoDuracao = tempoDuracao;
	}

	@Override
	public String getInfo() {
		return "Tipo de avaliacao: Seminario;  \nNome: " + super.getInfo() + ", tema: " + getTema() + ", Nota: ";
	}

//	@Override
//	public Double getNota() {
//		System.out.println(" ");
//		return super.getNota();
//	}

}