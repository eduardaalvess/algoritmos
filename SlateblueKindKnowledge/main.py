class Dados:
  def __init__(self, d = 0, prox = None):
    self.d = d
    self.prox = prox

  def __repr__(self):
    return '%s - %s' % (self.d, self.prox)


class Fila:
  def __init__(self):
    self.first = None
    self.last = None

  def __repr__(self):
    return "[" + str(self.first) + "]"

def inserir(self, new):
  newd = Dados(new)

  if self.first == None:
    self.first = newd 
    self.last = newd 
  else:
    self.last.prox = newd 
    self.last = newd 

fila = Fila()
print("Fila vazia:", fila)
for i in range(5):
  
  print("Inserir valor {0} ao final da fila: {1}" .format(i, fila))

def buscar(fila, valor):
  c = fila.h
  while c and d.prox != valor:
    c = c.prox
  return c

fila = Fila()
for i in range(8):
  inserir(fila, i)
print("Fila:", fila)

for i in range(8, -4, -2):
  elemento = buscar(fila, i)
  if elemento:
    print("Elemento {0} na lista" .format(i))
  else:
    print("Elemento {0} não encontrado" .format(i))

