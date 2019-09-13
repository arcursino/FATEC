package br.com.modelo.fatec;

import java.io.Serializable;

public class Nome implements Serializable{
	protected String nome;

	public Nome(String texto) {
		nome = texto;
	}

	public String getNome() {
		return nome;
	}

	public void setNome(String nome) {
		// tratamento
		this.nome = nome;
	}
}
