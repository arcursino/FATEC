package br.com.modelo.fatec;

import java.io.Serializable;
import java.util.ArrayList;
import java.util.List;

import br.com.negocio.fatec.Controle;

@SuppressWarnings("serial")
public class Agenda implements Serializable {
	public List<Contato> contatos = new ArrayList<Contato>();

	public void listarContatos() {
		for (Contato contato : contatos) {
			System.out.println("Nome: " + contato.getNome().getNome());
			System.out.println("tel: " + contato.getTel().getTel());
			System.out.println("Data: " + contato.getDataNascimento().getDt());
			System.out.println("Genero: " + contato.getGenero().getGen());
		}
	}

	public void inserirContato() {
		System.out.println("Por favor, digite um nome para o contato");
		Controle ctrl = new Controle();
		Contato c = new Contato(ctrl.texto(),ctrl.texto(),ctrl.texto(),ctrl.texto());
		
		contatos.add(c);
	}
}





















