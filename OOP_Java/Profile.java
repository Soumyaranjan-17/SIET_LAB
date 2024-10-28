// WAP to implement multiple inheritance 

import java.util.Scanner;

abstract class A17_Profile {
    String name;
    int roll, age, mark;

    void display() {
        System.out.println("Name: " + name + "\nRoll: " + roll + "\nAge: " + age + "\nMark: " + mark);
    }

    abstract void show_branch(); // Abstract method
}

class Medical extends A17_Profile {
    Medical(String n, int r, int a, int m) {
        this.name = n;
        this.roll = r;
        this.age = a;
        this.mark = m;
    }

    void show_branch() {
        System.out.println("Branch: Medical");
    }
}

class Engg extends A17_Profile {
    Engg(String n, int r, int a, int m) {
        this.name = n;
        this.roll = r;
        this.age = a;
        this.mark = m;
    }

    void show_branch() {
        System.out.println("Branch: Engg");
    }
}

class Agri extends A17_Profile {
    Agri(String n, int r, int a, int m) {
        this.name = n;
        this.roll = r;
        this.age = a;
        this.mark = m;
    }

    void show_branch() {
        System.out.println("Branch: Agri");
    }
}

class MultipleInheritancePt2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter Name");
        String name = sc.nextLine();

        System.out.println("Enter Roll");
        int roll = sc.nextInt();

        System.out.println("Enter Age");
        int age = sc.nextInt();

        System.out.println("Enter Mark");
        int mark = sc.nextInt();

        A17_Profile student;

        // Determine the branch based on marks
        if (mark > 90) {
            student = new Medical(name, roll, age, mark);
        } else if (mark > 80) {
            student = new Engg(name, roll, age, mark);
        } else {
            student = new Agri(name, roll, age, mark);
        }

        // Display student details and branch
        student.display();
        student.show_branch();

        sc.close();
    }
}


// OUTPUT

// Enter Name
// Soumya
// Enter Roll
// 99
// Enter Age
// 18
// Enter Mark
// 60
// Name: Soumya
// Roll: 99
// Age: 18
// Mark: 60
// Branch: Agri