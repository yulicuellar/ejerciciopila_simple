using System;
namespace listasimple
{
    class listasimple{
     private nodo primero= new nodo ();
     private nodo ultimo = new nodo ();

    public listh (){
        primero=null;
        ultimo=null;
    }  
public void insertarnodo()
{
nodo Nuevo = new nodo ();
Console.write("ingresar el dato que contendra el nuevo nodo");
Nuevo.dato = int.Parse(Console.ReadLine());
if (primero== null){
primero = Nuevo;
primero.siguiente = null;
ultimo=Nuevo;
}
else
{
ultimo.siguiente=Nuevo ;
Nuevo.siguiente=null;
ultimo = Nuevo;   
}
Console.WriteLine("\n nodo ingresado \n");
}
public void desplegarlista(){
nodo actual= new nodo();
actual=primero;
if(primero != null )
{
  while (actual != null)
  {
Console.WriteLine("{0}",actual.dato );
actual=actual.siguiente;
  }

}
else{
    Console.WriteLine("\n la lista se encuentra en blanco \n");
}

}

    }

}
