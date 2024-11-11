//  WAP to show Arithmetic error

public class A27_ArithematicError{
    void devide(int a, int b){
        try {
            System.out.println(a + "/" + b + "=" + a/b);
        } catch (ArithmeticException e) {
            System.out.println("Cannot devide by 0");
        }
    }

    public static void main(String[] args) {
        A27_ArithematicError A = new A27_ArithematicError();
        A.devide(5, 2);
        A.devide(25, 0);
        A.devide(45, 4);

    }
}

// 5/2=2
// Cannot devide by 0
// 45/4=11