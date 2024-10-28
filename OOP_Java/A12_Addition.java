import java.util.Scanner;

class A12_Addition{
    double a,b;

    void getData(){
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the number");
        a = sc.nextDouble();
        System.out.println("Enter the second number");
        b = sc.nextDouble();

        sc.close();
    }

    double process(){
        return(a+b);
    }

    void display(){
        System.out.println("sum ="+ process());
    }

    public static void main(String[] args) {
        A12_Addition obj= new A12_Addition();
        obj.getData();
        obj.display();
    }

}