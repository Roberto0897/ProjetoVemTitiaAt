package model;

import java.util.Scanner;

public class Cliente {
	public String nome;
	public String endereco;

	Scanner scan = new Scanner(System.in);

	public Cliente(String nome) {
		this.nome = nome;

	}

	public String lerDados() {
		while (true) {
			System.out.println("Digite seu nome !");
			nome = scan.nextLine();
			if (validaNome(nome)) {
				break;
			} else {
				System.out.println("Por favor, digite o nome e sobrenome!");
			}
		}
		return nome;
	}

	public String entrega() {
		System.out.println("Retirada em algum ponto de coleta(1) ou entregar no endereco(2)");
		int digito = scan.nextInt();
		if (digito == 1) {
			this.endereco = "Retirada no ponto de coleta";
			return endereco;
		} else {
			System.out.println("Digite seu endereco!");
			endereco = scan.next();
			return endereco;
		}
	}

	public boolean validaNome(String nome) {
		String[] partes = nome.trim().split("\\s+");
		return partes.length >= 2;
	}

}
