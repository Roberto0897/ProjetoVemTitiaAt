package model;

public class Prova extends Avaliacao {
	private Double tempoDuracao;
	private int quantidadeQuestoes;
	private boolean consultaAltorizada;

	public Prova(String nome, Double nota, Double tempoDuracao, int quantidadeQuestoes, boolean consultaAutorizada) {
		super(nome, nota);
//		if (this.getNota() <= 0) {
//			throw new IllegalArgumentException("A nota da ultima avaliacao, nao pode ser zero!");
//		}
		this.tempoDuracao = tempoDuracao;
		this.quantidadeQuestoes = quantidadeQuestoes;
		this.consultaAltorizada = consultaAutorizada;

	}

	public Double getTempoDuracao() {
		return tempoDuracao;
	}

	public void setTempoDuracao(Double tempoDuracao) {
		this.tempoDuracao = tempoDuracao;
	}

	public int getQuantidadeQuestoes() {
		return quantidadeQuestoes;
	}

	public void setQuantidadeQuestoes(int quantidadeQuestoes) {
		this.quantidadeQuestoes = quantidadeQuestoes;
	}

	public boolean isConsultaAutorizada() {
		return consultaAltorizada;
	}

	public void setConsultaAutorizada(boolean consultaAltorizada) {
		this.consultaAltorizada = consultaAltorizada;
	}

	@Override
	public String getInfo() {
		return "Tipo de avaliacao: Prova;  \nNome: " + super.getInfo() + ", Quantidade de questoes: "
				+ getQuantidadeQuestoes() + ", Consulta Autorizada: " + " " + isConsultaAutorizada() + ", Nota : ";
	}

//	@Override
//	public Double getNota() {
//		return super.getNota();
//	}
}