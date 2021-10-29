/*      fila.h       */
typedef struct elementoLista{         
char *dado;         
struct elementoLista *seguinte;       
} Elemento;       
typedef struct ListaDetectada{         
Elemento *início;  Elemento *fim;  int tamanho;       
} Fila;

/* inicialização */       
void inicialização (fila * sequência);       
/* Inserir*/       
int inserir (fila * sequência, elemento * atual, char *dado);       

/* Remover*/       
int remover (fila * sequência);       

/* FirstInFirstOut */       
#define fila_dado(sequência) 
sequência->início->dado       

/* Exibir a fila */       
void exibir (fila *sequência);