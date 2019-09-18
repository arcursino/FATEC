package br.com.modelo.fatec;

import java.io.Serializable;
import java.util.ArrayList;
import java.util.List;

import br.com.negocio.fatec.Controle;

@SuppressWarnings("serial")
public class Contato implements Serializable, Comparable<Contato> {
	protected String nome;
	protected Telefone tel;
	protected DataNascimento dataNascimento;
	protected String genero;
	public List<Produto> produtos = new ArrayList<Produto>();
	
	public Contato(String nome, String tel, String dataNascimento, String genero) {
		this.nome = new String(nome);
		this.tel = new Telefone(tel);
		this.dataNascimento = new DataNascimento(dataNascimento);
		this.genero = new String(genero);
	}

	public String getNome() {
		return nome;
	}

	public void setNome(String nome) {
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

	public String getGenero() {
		return genero;
	}

	public void setGenero(String genero) {
		this.genero = genero;
	}
	
	public void inserirProduto() {
		System.out.println("Por favor, digite um nome para o produto/servico");
		Controle ctrl = new Controle();
		System.out.println("Nome: ");
		String nome = ctrl.texto();
		System.out.println("valor: ");
		String valor = ctrl.texto();
		Produto c = new Produto(nome, valor);
		
		produtos.add(c);
	}
	
	
	@Override
	public int compareTo(Contato o) {
		return nome.compareTo(o.nome);
	}
	

}















