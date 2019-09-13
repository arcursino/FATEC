package br.com.modelo.fatec;

import java.io.Serializable;

@SuppressWarnings("serial")
public class Contato implements Serializable {
	protected Nome nome;
	protected Telefone tel;
	protected DataNascimento dataNascimento;
	protected Genero genero;
	
	public Contato(String nome, String tel, String dataNascimento, String genero) {
		this.nome = new Nome(nome);
		this.tel = new Telefone(tel);
		this.dataNascimento = new DataNascimento(dataNascimento);
		this.genero = new Genero(genero);
	}

	public Nome getNome() {
		return nome;
	}

	public void setNome(Nome nome) {
		this.nome = nome;
	}

	public Telefone getTel() {
		return tel;
	}

	public void setTel(Telefone tel) {
		this.tel = tel;
	}

	public DataNascimento getDataNascimento() {
		return dataNascimento;
	}

	public void setDataNascimento(DataNascimento dataNascimento) {
		this.dataNascimento = dataNascimento;
	}

	public Genero getGenero() {
		return genero;
	}

	public void setGenero(Genero genero) {
		this.genero = genero;
	}
	

}















