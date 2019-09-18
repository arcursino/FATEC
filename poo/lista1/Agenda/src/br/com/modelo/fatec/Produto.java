package br.com.modelo.fatec;

import java.io.Serializable;

@SuppressWarnings("serial")
public class Produto implements Serializable {
	protected String produto;
	protected String valor;
	public Produto(String produto, String valor) {
		super();
		this.produto = produto;
		this.valor = valor;
	}
	public String getProduto() {
		return produto;
	}
	public void setProduto(String produto) {
		this.produto = produto;
	}
	public String getValor() {
		return valor;
	}
	public void setValor(String valor) {
		this.valor = valor;
	}
	
	
}
