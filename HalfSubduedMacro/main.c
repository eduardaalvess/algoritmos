/*      fila.c       */
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include "fila.h"
#include "fila_function.h"
int main (){          
Fila *sequencia;         
char *nome;         
if ((sequencia = (fila *) malloc (sizeof (fila))) == NULL)           
return -1;         
if ((nome = (char *) malloc (50 * sizeof (char))) == NULL)           
return -1;         
inicialização (sequência);         
printf ("Inserir uma palavra:");         
scanf ("%s", nome);         
inserir (sequência, sequência->fim, nome);         
printf ("A fila (%de elementos)\n",sequência->tamanho);         
printf("\nInício de la fila [ ");         
exibir (sequência);     

/*primeiro elemento inserido será exibido */         
printf(" ] fim de la fila\n\n");         
printf ("Inserir uma palavra:");         
scanf ("%s", nome);         
Inserir (sequência, sequência->fim, nome);         
printf ("A fila (%de elementos)\n",sequência->tamanho);         
printf("\nInício da fila [ ");         
exibir (sequência);      

/*primeiro elemento inserido será exibido */         
printf(" ] fim da fila\n\n");         
printf ("Inserir uma palavra:");         
scanf ("%s", nome);         
Inserir (sequência, sequência->fim, nome);         
printf ("A fila (%de elementos)\n",sequência->tamanho);         
printf("\nInício de la fila [ ");         
exibir (sequência);      

/*primeiro elemento inserido será exibido */         
printf(" ] fim da fila\n\n");         
printf ("\nO primeiro elemento inserido (FirstInFirstOut) [ %s ] será removido",
fila_dado(sequência));         
printf ("\nO primeiro elemento inserido é removido\n");         
remover (sequência);              

/*remoção do primeiro elemento inserido*/         
printf ("A fila (%d elementos): \n",sequência->tamanho);         
printf("\nInício da fila [ ");         
exibir (sequência);         
printf(" ] fim da fila\n\n");         
return 0;       
}