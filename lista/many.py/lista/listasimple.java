package lista;

public class listasimple {
       
    nodo primero;
    nodo ultimo;
    public listasimple (){
        primero=null;
        ultimo=null;
    
    }
    public void ingresarnodo (int r){
        nodo nodonuevo= new nodo();
        
        nodonuevo.dato=r; 
        if (primero==null){
            primero=nodonuevo;
            primero.siguiente= null;
            ultimo=primero;
            
        } else{
        ultimo.siguiente=nodonuevo;
        nodonuevo.siguiente=null;
        ultimo = nodonuevo;
        }
                
 }
    public void verlista(){
     nodo actual= new nodo();
     actual = primero;
     while(actual != null ){
     System.out.println(actual.dato);
     actual=actual.siguiente;
     }
     
    }
    
}