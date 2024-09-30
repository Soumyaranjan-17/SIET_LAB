// WAP to implement single inheritance on classes initializing on constructor

import java.util.Scanner;

class Father {
    String Fname;
    int age;

    // Constructor to initialize Father's details
    public Father(String fname, int age) {
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

    // Constructor to initialize both Father's and Son's details
    public Son(String fname, int fage, String sname, int sage) {
        super(fname, fage); // Call the Father's constructor
        this.Sname = sname;
        this.Sage = sage;
    }

    // Method to display son's details along with father's details
    void disp() {
        display();  // Calling display method from Father class
        System.out.println("Son's name = " + Sname + ", Son's age = " + Sage);
    }
}

public class SingleInheritanceConstructor {
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

        // Create a Son object using constructor
        Son sonA = new Son(fname, fage, sname, sage);
        
        // Display the details
        sonA.disp();

        sc.close();
    }
}

// OUTPUT

// Enter name of father: Tom  
// Enter age of father: 56 
// Enter name of son: Jonny
// Enter age of son: 45
// Father's name = Tom, Father's age = 56
// Son's name = Jonny, Son's age = 45