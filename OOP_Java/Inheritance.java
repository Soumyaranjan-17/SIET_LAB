import java.util.*;
import java.io.*;
/**
 * Inheritance
 */
public class Inheritance {
    class Shape{
        float xco, yco, rad, side;
    }

    class Rectangle extends Shape{
        public void get(float x, float y){
            xco = x;
            yco = y;
        };

        public void area(){
            System.out.println("Area of Rectangle is " + (xco*yco));
        }
    }
    
    class Circle extends Shape{
        public void get(float r){
            rad = r;
        }
        
        public void display(){
            System.out.println("Area of Circle is " + (Math.PI * Math.pow(rad, 2)));
        }
    }
    
    class Square extends Shape{
        public void get(float s){
            side = s;
        }
        public void display(){
            System.out.println("Area of Square is " + (side*side) + "Unit Square");
        }
    }


    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        Rectangle r = new Rectangle();
        System.out.println("Enter the length and breadth: ");
        float l = sc.nextFloat(); 
        float b = sc.nextFloat(); 

        r.get(l, b);
        
        Circle c = new Circle();
        
        
        
        sc.close();
        
    }
}