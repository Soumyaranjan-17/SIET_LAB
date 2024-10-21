// WAP to implement multiple inheritance 

import java.util.*;

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
    
    public void area(){
        System.out.println("Area of Circle is " + (Math.PI * Math.pow(rad, 2)));
    }
}

class Square extends Shape{
    public void get(float s){
        side = s;
    }
    public void area(){
        System.out.println("Area of Square is " + (side*side) + "Unit Square");
    }
}
public class Inheritance {
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        Rectangle r = new Rectangle();
        System.out.println("Enter the length and breadth of rectangle: ");
        float l = sc.nextFloat(); 
        float b = sc.nextFloat(); 

        r.get(l, b);
        r.area();
        
        Circle c = new Circle();
        System.out.println("Enter the circle radius: ");
        float rad = sc.nextFloat();

        c.get(rad);
        c.area();

        Square sq = new Square();
        System.out.println("Enter the length of one side of square : ");
        float a = sc.nextFloat();
        sq.get(a);
        sq.area();

        sc.close();
        
    }
}

// OUTPUT

// Enter the length and breadth of rectangle: 
// 12
// 11
// Area of Rectangle is 132.0
// Enter the circle radius: 
// 7
// Area of Circle is 153.93804002589985
// Enter the length of one side of square : 
// 12
// Area of Square is 144.0Unit Square