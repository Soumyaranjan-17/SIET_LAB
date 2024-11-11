import java.io.IOException;
import java.util.Scanner;

public class A32_vote {
    void check(String nm, int age) throws IOException{
        if (age >= 18) {
            System.out.println("Can Vote");
        } else {
            throw new IOException("Cannot vote");
        }
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter the name");
        String nm = sc.nextLine();

        System.out.println("Enter the Age");
        int age = sc.nextInt();        
        
        A32_vote obj = new A32_vote();
        try {
            obj.check(nm, age);
        } catch (Exception e) {
            System.out.println("Can not vote: " + e);
        }
        
        sc.close();    
    }
}
