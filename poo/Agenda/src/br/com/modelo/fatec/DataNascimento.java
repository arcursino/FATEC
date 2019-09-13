package br.com.modelo.fatec;

import java.io.Serializable;
import java.util.Calendar;
import java.util.Date;

@SuppressWarnings("serial")
public class DataNascimento implements Serializable{
	protected String dt;
	protected int idade;

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
	public void setIdade(String dt) {
		String lastFourDigits;
		lastFourDigits = dt.substring(dt.length() - 4);
		idade = Integer.parseInt(lastFourDigits);
		idade = Calendar.YEAR - idade;
	}
	public int getIdade() {
		return idade;
	}
}
