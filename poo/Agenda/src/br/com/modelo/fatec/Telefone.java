package br.com.modelo.fatec;

import java.io.Serializable;

public class Telefone implements Serializable{
	protected String tel;

	public Telefone(String texto) {
		tel = texto;
	}

	public String getTel() {
		return tel;
	}

	public void setTel(String tel) {
		// tratamento
		this.tel = tel;
	}
}
