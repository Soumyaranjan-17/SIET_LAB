import java.util.Scanner;

// Father class
class Father {
    String Fname;
    int age;

    // Constructor to initialize Father's details
    Father(String fname, int age) {
        this.Fname = fname;
        this.age = age;
    }

    // Method to display Father's details
    void display() {
        System.out.println("Father's name = " + Fname + ", Father's age = " + age);
    }
}

// Son class inheriting from Father
class Son extends Father {
    String Sname;
    int Sage;

    // Constructor to initialize both Father and Son's details
    Son(String fname, int fage, String sname, int sage) {
        // Call Father class constructor to initialize Father's details
        super(fname, fage);
        this.Sname = sname;
        this.Sage = sage;
    }

    // Method to display both Father and Son's details
    void displayDetails() {
        // Display father's details using Father's display method
        super.display();
        // Display son's details
        System.out.println("Son's name = " + Sname + ", Son's age = " + Sage);
    }
}

// Main class to run the program
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

        // Create Son object, which also initializes Father's details via inheritance
        Son son = new Son(fname, fage, sname, sage);

        // Display the details of both Father and Son
        son.displayDetails();
    }
}
