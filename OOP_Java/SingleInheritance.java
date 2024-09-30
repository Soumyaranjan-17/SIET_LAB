// WAP to implement single inheritance on two classes, Father & Son

import java.util.Scanner;

class Father {
    String Fname;
    int age;

    // Method to get father's details
    void getData(String fname, int age) {
        this.Fname = fname;
        this.age = age;
    }

    // Method to display father's details
    void display() {
        System.out.println("Father's name = " + Fname + ", Father's age = " + age);
    }
}

class Son extends Father {
    String Sname;
    int Sage;

    // Method to get son's details along with father's details
    void get(String fname, int fage, String sname, int sage) {
        // Using the parent class's getData method for father
        getData(fname, fage);
        this.Sname = sname;
        this.Sage = sage;
    }

    // Method to display son's details along with father's details
    void disp() {
        display();  // Calling display method from Father class
        System.out.println("Son's name = " + Sname + ", Son's age = " + Sage);
    }
}

public class SingleInheritance {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Input for Father
        System.out.print("Enter name of father: ");
        String fname = sc.nextLine();
        System.out.print("Enter age of father: ");
        int fage = sc.nextInt();
        sc.nextLine();  // consume newline

        // Input for Son
        System.out.print("Enter name of son: ");
        String sname = sc.nextLine();
        System.out.print("Enter age of son: ");
        int sage = sc.nextInt();

        // Create a Son object
        Son son = new Son();
        
        // Set and display data
        son.get(fname, fage, sname, sage);
        son.disp();

        sc.close();
    }
}

// OUTPUT

// Enter name of father: John
// Enter age of father: 30
// Enter name of son: Pika      
// Enter age of son: 18
// Father's name = John, Father's age = 30
// Son's name = Pika, Son's age = 18