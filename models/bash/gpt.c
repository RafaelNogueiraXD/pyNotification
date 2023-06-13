#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int selection_sort(int arr[], int n) {
    int comparisons = 0;
    int i, j, min_idx;
    
    for (i = 0; i < n-1; i++) {
        min_idx = i;
        for (j = i+1; j < n; j++) {
            comparisons++;
            if (arr[j] < arr[min_idx])
                min_idx = j;
        }
        int temp = arr[min_idx];
        arr[min_idx] = arr[i];
        arr[i] = temp;
    }
    
    return comparisons;
}

int main() {
    srand(time(NULL));
    
    int i, j;
    int min_size = 10;
    int max_size = 2500;
    int increment = 1;
    
    FILE *arquivo = fopen("desempenho.txt", "w");
    if (arquivo == NULL) {
        printf("Erro ao abrir o arquivo!\n");
        return 1;
    }
    
    for (i = min_size; i <= max_size; i += increment) {
        int vetor[i];
        
        // Preencher vetor aleatório
        for (j = 0; j < i; j++) {
            vetor[j] = rand() % 10000;
        }
        
        // Ordenar o vetor e obter o número de comparações
        int comparisons = selection_sort(vetor, i);
        
        // Registrar o número de comparações no arquivo de texto
        fprintf(arquivo, "%d, %d\n", i, comparisons);
    }
    printf("\nO programa de Selection Sort foi executado com intervalo de %d e %d \n",min_size, max_size );
    fclose(arquivo);
    
    return 0;
}
