package main;

import model.Produto;
import model.Cliente;
import model.Pedido;

public class Main {

	public static void main(String[] args) {
		Produto po1 = new Produto("lapis", 1.5f, 1000);

		Cliente c1 = new Cliente("");

		Pedido pe1 = new Pedido(po1, "cartao", c1, 1);

		pe1.status();

		System.out.println("STATUS EMPRESA");
		System.out.println("Produto = " + po1.nome);
		System.out.println("Estoque atual de = " + pe1.estoque());
		System.out.println("Preco = " + po1.preco);
		System.out.println("Valor caixa " + pe1.caixaEmpresa() + " reais");

	}

}
