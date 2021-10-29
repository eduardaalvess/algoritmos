# Implementação da operação 'inserir', 'buscar'
# e 'remover' de uma lista ligada em Python. 

# Classe que representa uma célula de uma
# lista ligada. 
class CelulaLista:
  def __init__(self, dado = 0, prox = None):
    self.dado = dado
    self.prox = prox
  
  def __repr__(self):
    return '%s - %s' % (self.dado, self.prox)

# Classe que representa uma lista
# ligada. 

class ListaLigada:
  def __init__(self):
    self.h = None
  
  def __repr__(self):
    return "[" + str(self.h) + "]"

# Método 'inserir'

def inserir(lista, elemento):

  novo = CelulaLista(elemento)
  novo.prox = lista.h
  lista.h = novo

#Teste do método 'inserir'

lista = ListaLigada()
print("Lista vazia: ", lista)

inserir(lista, 4)
print("Lista com um elemento:", lista)

inserir(lista, 16)
print("Inserindo novo elemento:", lista)

inserir(lista, 47)
print("Inserindo novo elemento:", lista)

# Método 'buscar'

def buscar(lista, valor):
  p = lista.h
  while p and p.dado != valor:
    p = p.prox
  return p

# Teste do método 'buscar'

lista = ListaLigada()
for i in range(8):
  inserir(lista, i)
print("Lista: ", lista)

for i in range(8, -3, -2):
  ob = buscar(lista, i)
  if ob:
    print("Elemento {0} está na lista!" .format(i))
  else:
    print("Elemento {0} não encontrado." .format(i))

# Método 'remover'

def remover(self, valor):
  assert self.h, "Não é posível remover de uma lista vazia."

  if self.h.dado == valor:
    self.h = self.h.prox 
  else:
    a = None
    p = self.h
    while p and p.dado != valor:
      a = p
      p = p.prox
    if p:
      a.prox = p.prox 
    else:
      a.prox = None

# Teste do método 'remover'

lista = ListaLigada()
for i in range(4):
  inserir(lista, i)
print("Lista:", lista)

print("Remover elementos:")
for i in range(4):
  remover(lista, i)
  print("Removendo o elemento {0}: {1}" .format(i, lista))