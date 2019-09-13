package br.com.modelo.fatec;

import java.io.Serializable;

public class DataNascimento implements Serializable{
	protected String dt;

	public DataNascimento(String texto) {
		dt = texto;
	}

	public String getDt() {
		return dt;
	}

	public void setDt(String dt) {
		// tratamento
		this.dt = dt;
	}
}
