
/*List no es un tipo de datos en Java/C/C++, pero tenemos formas alternativas de crear una lista en Java, es decir, usando ArrayList y LinkedList.

El siguiente ejemplo muestra cómo crear una lista en Java. Aquí estamos usando un método de lista enlazada para crear una lista de números.

import java.util.*; 
import java.lang.*; 
import java.io.*;  */


public class HelloWorld { 
   public static void main (String[] args) throws java.lang.Exception { 
      List<String> listStrings = new LinkedList<String>(); 
      listStrings.add("1"); 
      listStrings.add("2"); 
      listStrings.add("3"); 
      listStrings.add("4"); 
      listStrings.add("5"); 
  
      System.out.println(listStrings); 
   } 
} 