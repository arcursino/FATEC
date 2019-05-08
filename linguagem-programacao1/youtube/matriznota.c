#include <stdio.h>

int main () {
	float notas [4][4] = {};
	float media [4] = {};
	float mediaAlunos = 0;

	//printf("Digite a nota dos aluno1:\n");

	for (int i = 0; i < 4; i++) {
	    printf("Digite a nota do aluno%i:\n", i + 1);
		for (int j = 0; j < 4; j++){
			scanf("%f", &notas[i][j]);
			mediaAlunos += notas[i][j];
		}
        media[i] = mediaAlunos / 4;
		mediaAlunos = 0;
	}
	for (int i = 0; i < 4; i++)
	printf("A média do aluno(%d) é %.2f\n", i + 1, media[i]);
}
