package main;

import model.Avaliacao;
import model.Bimestre;
import model.EstudoDirigido;
import model.Prova;
import model.Seminario;

public class BimestreTesteMain {

	public static void main(String[] args) {
		Avaliacao prova1 = new Prova("Prova Poo", 10d, 3d, 5, true);
		Avaliacao seminario1 = new Seminario("Fisica quantica", 10d, 1d, "espaco tempo");
		EstudoDirigido eD1 = new EstudoDirigido("java", 0d, 10, "classe abstrata");
		Bimestre bimestre1 = new Bimestre();

		bimestre1.setIdBimestre("Bimestre id_3 : ");
		bimestre1.setAv1(prova1);
		bimestre1.setAv2(seminario1);
		bimestre1.setAv3(eD1);
		bimestre1.imprimirAvaliacoes();
		
		if(bimestre1.getAv3().getNota() <=0) {
			bimestre1.getAv3().setNota(10d);
			System.out.println();
			bimestre1.imprimirAvaliacoes();
		}

//		if (seminario1 instanceof Seminario) {
//			System.out.println("e um seminario");
//		}
//
//		Seminario semi1 = (Seminario) seminario1;
//		System.out.println("\n" + semi1.getTema() + semi1.getTempoDuracao());
//		

	}

}
