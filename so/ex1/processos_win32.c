#include <stdio.h>
#include <windows.h>

int main (VOID) {
    STARTUPINFO si;
    PROCESS_INFORMATION pi;

    // Alocar a memória
    ZeroMemory(&si, sizeof(si));
    si.cb = sizeof(si);
    ZeroMemory(&pi, sizeof(pi));

    //Criar o processo fork
    if (!CreateProcess(NULL, // Criar o processo
        "C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe",  // localização do programa que desejo abrir
        NULL, // não herda o processo
        NULL, // não herda o processo
        FALSE, // desabilita o processo de herança
        0, // não cria "flags"
        NULL, // usa o bloco de ambiente dos pais
        NULL, // usa o diretório existente do pai
        &si,
        &pi))
        {
            fprintf (stderr, "Creat Process Failed");
            return -1;
        }
        // o processo "pai" espera o processo "filho" acabar
        WaitForSingleObject(pi.hProcess, INFINITE);
        printf("Child Complete");

        // fecha
        CloseHandle(pi.hProcess);
        CloseHandle(pi.hThread);
}
