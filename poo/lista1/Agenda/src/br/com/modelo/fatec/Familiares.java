package br.com.modelo.fatec;

public class Familiares extends Contato{

	public Familiares(String texto) {
		super(texto, texto, texto, texto); // super -- chamada construtor superior
	}
	
	public void alterarNome() {
		nome = "Novo nome!!";
	}

}
