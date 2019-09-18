package br.com.modelo.fatec;

import java.io.Serializable;
import java.util.Calendar;

@SuppressWarnings("serial")
public class DataNascimento implements Serializable{
	protected String dt;
	protected int idade;

	public DataNascimento(String texto) {
		dt = texto;
		setIdade(dt);
	}

	public String getDt() {
		return dt;
	}

	public void setDt(String dt) {
		this.dt = dt;
	}
	
	public void setIdade(String dt) {
		String lastFourDigits;
		Calendar today = Calendar.getInstance();
		lastFourDigits = dt.substring(dt.length() - 4);
		this.idade = Integer.parseInt(lastFourDigits);
		this.idade = today.get(Calendar.YEAR) - this.idade;
		//this.idade = 2019 - this.idade;
	}
	public int getIdade() {
		return idade;
	}
}
