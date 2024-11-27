package model;

import java.util.ArrayList;
import java.util.Scanner;

public class Produto {
	public String nome;
	public float preco;
	public int qtdEstoque;
	public boolean selet;

	Scanner scan = new Scanner(System.in);

	public Produto(String nome, float pc, int et) {
		this.nome = nome;
		this.preco = pc;
		this.qtdEstoque = et;

	}

	ArrayList<Produto> produtos = new ArrayList<>();
	ArrayList<String> guarda = new ArrayList<>();

	public String produtos() {
//		FORMA DE DECLARACAO INSTANCIA COMPLETA
//		Produto pr1 = new Produto("Samsung S24", 7999.54f, 599);
//		produtos.add(pr1);

		produtos.add(new Produto("lapis", 1.5f, 1000));
		produtos.add(new Produto("Samsung S24", 7999.54f, 599));
		produtos.add(new Produto("Fone QCY", 169.99f, 1931));
		produtos.add(new Produto("Caixa de som", 599, 587));
		produtos.add(new Produto("Forno a lenha", 2988.5f, 50));

//		String [] guarda = new String [5];


		System.out.println("Escolha um produto!\n");

		for (Produto pro : produtos) {
			guarda.add(pro.nome);

			System.out.println(String.format("Produto: %s, Preço: %.2f reais, Quantidade: %d", pro.nome, pro.preco,
					pro.qtdEstoque));
		}
		nome = scan.nextLine();

		if (guarda.contains(nome)) {
			selet = true;
			System.out.println("Produto selecionado!");

		} else {
			selet = false;
			throw new RuntimeException("Produto não encontrado. Encerramento controlado.");

		}
		
		for (int i = 0; i < guarda.size(); i++) {
			if (guarda.get(i).equals(nome)) {
				produtos.get(i);
				this.preco = produtos.get(i).preco;
				this.qtdEstoque = produtos.get(i).qtdEstoque;
			}
		}
		return nome;
	}
}
