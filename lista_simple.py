class nodo:
    def ____int______ (self, nombre=None, cedula=None, sig=None):
         self.nombre=nombre
         self.cedula=cedula
         self.sig=sig

    def _____str_____(self):
      return "%s %s" % (self.nombre, cedula)

class lslista:
    def ___init____(self):
       self.cabeza =None
       self.cola =None

    def agregar(self, elemento):
        if self.cabeza == None:
               self.cabeza == elemento 

        if self.cola != None:
               self.cola.sig = elemento

     self.cola = elemento 
    def listar (self):
            aux = self.cabeza
            while aux != None:
                print(aux)
                aux = aux.sig

if __name__ == "__main__":
    ls = lslista()

    while(True):
      print("---manu..\n"+
      "1. Agregar \n" +
      "2. Listar")
      num = input("ingresar la opcion")
      if num =="1":
          nombre = input("ingrese el nombre: ")
          cedula = input("ingrese la cedula")
          nod = nodo(nombre, cedula) 
          ls.agregar(nod)
      elif num == "2":
           ls.listar()


