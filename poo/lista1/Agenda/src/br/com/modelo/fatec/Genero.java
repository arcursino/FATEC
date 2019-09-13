package br.com.modelo.fatec;

import java.io.Serializable;

public class Genero implements Serializable{
	protected String gen;

	public Genero(String texto) {
		gen = texto;
	}

	public String getGen() {
		return gen;
	}

	public void setGen(String gen) {
		// tratamento
		this.gen = gen;
	}
}
