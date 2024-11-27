package model;

import java.util.Scanner;

public class Pedido {
	public Produto itens;
	public String forPagamento;
	public Cliente cli;
	public int qtdPedido;
	public float total = 0;
	public int digito;
	public float caixa;

	Scanner scan = new Scanner(System.in);

	public Pedido() {

	}

	public Pedido(Produto itens, String pag, Cliente cli, int qtdPedido) {
		this.itens = itens;
		this.cli = cli;
		this.forPagamento = pag;
		this.qtdPedido = qtdPedido;
	}

	public int qtdPedido() {
		System.out.println("Digite a quatidade de " + itens.nome + " desejada!");
		int num = scan.nextInt();
		qtdPedido = num;
		return qtdPedido;
	}

	public String verificaPagamento() {
		System.out.println("Escolha a forma de pagamento");
		System.out.println("(1)CARTAO , (2)PIX, (3)BOLETO");
		digito = scan.nextInt();
		switch (digito) {
		case 1:
			this.forPagamento = "CARTAO";
			break;
		case 2:
			this.forPagamento = "PIX AE";
			break;
		case 3:
			this.forPagamento = "BOLETO";
			break;
		default:
			while (digito > 3 && digito <= 1) {
				System.out.println("Escolha um forma de pagamento valida!");
				digito = scan.nextInt();
			}
		}
		return forPagamento;
	}

	public float total() {
		if (qtdPedido > 0) {
			total = itens.preco * qtdPedido;
//		} else if (qtdPedido > itens.qtdEstoque) {
//			System.out.println("Quantidade indisponivel! compre no maximo " + itens.qtdEstoque);
//			while (qtdPedido > itens.qtdEstoque) {
//				qtdPedido();
//			}
		} else {
			System.out.println("Necessario ao menos um produto para realizar um pedido!");
			while (qtdPedido <= 0) {
				qtdPedido();
			}
		}
		return total;
	}

	public int estoque() {
		itens.qtdEstoque -= qtdPedido;
		return itens.qtdEstoque;
	}

	public String pedidoGerado() {
		return "------PEDIDO GERADO-------";
	}

	public float caixaEmpresa(){
		caixa += total();
		return caixa;
	}
	public void status() {
		System.out.println(pedidoGerado() + "\nProduto = " + itens.produtos() + "\nQuantidade de itens = " + qtdPedido()
				+ "\nTotal pedido = " + total() + " reais" + "\nForma de pagamento = " + verificaPagamento()
				+ "\nCliente= " + cli.nome + cli.lerDados() + "\nEndereco = " + cli.entrega());
		System.out.println("---------------------------\n");
	}
}
