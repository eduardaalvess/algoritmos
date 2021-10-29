/*      fila_function.h       */
void inicialização (fila * sequência){         
sequência->início = NULL;         
sequência->fim = NULL;         
sequência->tamanho = 0;       }

/* inserir (adicionar) um elemento na fila */       
int inserir (fila * sequência, elemento * atual, char *dado){         
Elemento *novo_elemento;         
if ((novo_elemento = (elemento *) malloc (sizeof (elemento))) == NULL)
return -1;         
if ((novo_elemento->dado = (char *) malloc (50 * sizeof (char))) == NULL)
return -1;         
strcpy (novo_elemento->dado, dado);         
if(atual == NULL){           
if(sequência->tamanho == 0)             
sequência->fim = novo_elemento;           
novo_elemento->seguinte = sequência->início;           
sequência-> início = novo_elemento;         
}
else 
{           
if(atual->seguinte == NULL)             
sequência->fim = novo_elemento;           
novo_elemento->seguinte = atual->seguinte;           
atual-> seguinte = novo_elemento;         }         
sequência->tamanho++;         
return 0;       
}

/* remover (eliminar) elemento da fila */       
int remover (fila * sequência){         
Elemento *remov_elemento;         
if (sequência->tamanho == 0)           
return -1;         
remov_elemento = sequência->início;         
sequência-> início = sequência->início->seguinte;         
free (remov_elemento->dado);         
free (remov_elemento);         
sequência->tamanho--;         
return 0;       
}

/* exibição da fila */       
void exibir (fila *sequência){         
Elemento *atual;         
int i;         
atual = sequência->início;         
for(i=0;i<sequência->tamanho;++i){           
printf(" %s ", atual->dado);           
atual = atual->seguinte;         
}       
}