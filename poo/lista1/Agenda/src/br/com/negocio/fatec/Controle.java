package br.com.negocio.fatec;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.util.Scanner;

import br.com.modelo.fatec.Agenda;
import br.com.modelo.fatec.Contato;

public class Controle {
	public Scanner scanner;

	public Controle() {
		scanner = new Scanner(System.in);
	}

	public int opcao() {
		int op = scanner.nextInt();
		return op;
	}

	public String texto() {
		String t = scanner.nextLine();
		return t;
	}
	
	public Agenda carregar() throws Exception {
		FileInputStream entrada = new FileInputStream("C:\\Users\\Marcio\\Desktop\\agenda.txt");
		ObjectInputStream leitor = new ObjectInputStream(entrada);
		Object ob = leitor.readObject();
		Agenda ag = (Agenda) ob;
		leitor.close();
		return ag;
	}
	
	public void salvar(Agenda ag) throws IOException {
		FileOutputStream saida = new FileOutputStream("C:\\Users\\Marcio\\Desktop\\agenda.txt");
		ObjectOutputStream escritor = new ObjectOutputStream(saida);
		escritor.writeObject(ag);
		escritor.close();
	}
	
	/*
	public void salvar(Agenda ag) throws IOException {
		File arq = new File("C:\\Users\\Aluno\\Desktop\\agenda.txt");
		FileWriter wr = new FileWriter(arq);
		BufferedWriter bwr = new BufferedWriter(wr);
		for(Contato c : ag.contatos) {
			System.out.println(c);
			bwr.write(c.getNome().getNome());
			bwr.newLine();
			bwr.write(c.getTel().getTel());
			bwr.newLine();
			bwr.write(c.getDataNascimento().getDt());
			bwr.newLine();
			bwr.write(c.getGenero().getGen());
			bwr.newLine();
		}
		bwr.close();
	}
		public void carregar(Agenda ag) throws Exception {
		File arq = new File("C:\\Users\\Aluno\\Desktop\\agenda.txt");
		FileReader rd = new FileReader(arq);
		BufferedReader brd = new BufferedReader(rd);
		String texto = brd.readLine();
		while(texto != null) {
			Contato c  = new Contato(texto,texto,texto,texto);
			ag.contatos.add(c);
			texto = brd.readLine();
		}
		brd.close();
	}
	*
	*
	*/
	

	
	
	@Override
	protected void finalize() throws Throwable {
		scanner.close();
	}
}


















