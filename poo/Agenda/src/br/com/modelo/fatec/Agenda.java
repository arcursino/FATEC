package br.com.modelo.fatec;

import java.io.Serializable;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

import br.com.negocio.fatec.Controle;

@SuppressWarnings("serial")
public class Agenda implements Serializable {
	public List<Contato> contatos = new ArrayList<Contato>();

	public void listarContatos() {
		for (Contato contato : contatos) {
			System.out.println("Nome: " + contato.getNome());
			System.out.println("tel: " + contato.getTel().getTel());
			System.out.println("Data: " + contato.getDataNascimento().getDt());
			System.out.println("Genero: " + contato.getGenero());
		}
	}

	public void inserirContato() {
		System.out.println("Por favor, digite um nome para o contato");
		Controle ctrl = new Controle();
		System.out.println("Nome: ");
		String nome = ctrl.texto();
		System.out.println("Tel: ");
		String tel = ctrl.texto();
		System.out.println("Data nasciemnto: ");
		String data = ctrl.texto();
		System.out.println("Genero: ");
		String genero = ctrl.texto();
		Contato c = new Contato(nome, tel, data, genero);
		
		contatos.add(c);
	}
	
	public void editarContato() {
		int id;
		Controle ctrl = new Controle();
		System.out.println("Entre com o indice do contato a ser editado");
		id = ctrl.opcao();
		System.out.println("Nome: ");
		String nome = ctrl.texto();
		System.out.println("Tel: ");
		String tel = ctrl.texto();
		System.out.println("Data nasciemnto: ");
		String data = ctrl.texto();
		System.out.println("Genero: ");
		String genero = ctrl.texto();
		Contato c = new Contato(nome, tel, data, genero);
		contatos.set(id,c);
		
	}
	
	public void excluirContato() {
		int id;
		Controle ctrl = new Controle();
		id = ctrl.opcao();
		contatos.remove(id);
	}
	
	public void listarContatosAlfabetica() {
		
		Collections.sort(contatos);
		for (Contato contato : contatos) {
			System.out.println("Nome: " + contato.getNome());
			System.out.println("tel: " + contato.getTel().getTel());
			System.out.println("Data: " + contato.getDataNascimento().getDt());
			System.out.println("Genero: " + contato.getGenero());
			int i = 0;
			if (!contato.produtos.isEmpty()) {
				for(Produto prod :contato.produtos) {
					i = i+1;
					System.out.println("Produto numero: " + i);
					System.out.println(prod.getProduto());
					System.out.println(prod.getValor());
				}
			}
		}
	
	}
	
	public void listarContatosGenero() {
		Controle ctrl = new Controle();
		String genero = ctrl.texto();
		System.out.println("Entre com o genero a ser listado");
		Collections.sort(contatos);
		for (Contato contato : contatos) {
		if(contato.getGenero().equals(genero)) {
			System.out.println("Nome: " + contato.getNome());
			System.out.println("tel: " + contato.getTel().getTel());
			System.out.println("Data: " + contato.getDataNascimento().getDt());
			System.out.println("Genero: " + contato.getGenero());
		}
		}
	}
	
	public void adicionarProduto() {
		int id;
		Controle ctrl = new Controle();
		System.out.println("Entre com o indice do contato");
		id = ctrl.opcao();
		contatos.get(id).inserirProduto();
	}
	
}





















