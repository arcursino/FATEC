package br.com.aplicacao.fatec;

import java.io.IOException;

import br.com.modelo.fatec.Agenda;
import br.com.negocio.fatec.Controle;
import br.com.negocio.fatec.Menu;

public class App {
	public static void main(String[] args){
		Agenda ag = new Agenda();
		Controle c = new Controle();
		Menu menu = new Menu();
		try {
			ag = c.carregar();
		} catch (Exception e) {
			ag = new Agenda();
		}
		menu.boasVindas();
		int opcao = 100;
		while(opcao != 0) {
			menu.menu();
			Controle ctrl = new Controle();
			opcao = ctrl.opcao();
			if(opcao == 1) {
				ag.inserirContato();
			}
			if(opcao == 2) {
				ag.listarContatos();
			}
			if(opcao == 3) {
				ag.editarContato();
			}
			if(opcao == 4) {
				ag.excluirContato();
			}
			if(opcao == 5) {
				ag.listarContatosAlfabetica();
			}
			if(opcao == 6) {
				ag.listarContatosGenero();
			}
			if(opcao == 7) {
				ag.adicionarProduto();
			}
		}
		//c = new Controle();
		try {
			c.salvar(ag);
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
			System.out.println("Nao foi possivel salvar sua agenda");
		}
		
	}
}







































