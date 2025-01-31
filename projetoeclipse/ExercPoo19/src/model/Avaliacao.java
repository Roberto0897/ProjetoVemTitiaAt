package model;

public abstract class Avaliacao {
	private String nome;
	private Double nota;

	public Avaliacao(String nome, Double nota) {
		try {
			if (nota <= 0) {
				throw new IllegalArgumentException("Nota não pode ser nula, zero ou negativa!");
			}
			this.nota = nota;
		} catch (IllegalArgumentException e) {
			System.out.println("Erro:  Nota será ajustada para 10");
			System.out.println();
			this.nota = 10.d;
		}

		this.nome = nome;
		this.nota = nota;

	}

	public String getInfo() {
		return nome;
	}

	public void setNota(Double nota) {
		this.nota = nota;
	}

	public Double getNota() {
		return nota;
	}
}
