public class A15_Complex {
    int real, imag;
    public A15_Complex(){
        real = 1;
        imag = 2;
    }
    public A15_Complex(int r){
        real = r;
        imag = 3;
    }
    public A15_Complex(int r, int i){
        real = r;
        imag = i;
    }

    public void add(){
        System.out.println("Sum is "+ real+ "j" + imag);
    }

    public static void main(String[] args) {
        A15_Complex A = new A15_Complex();
        A15_Complex B = new A15_Complex(7);
        A15_Complex C = new A15_Complex(7, 23);

        A.add();
        B.add();
        C.add();
    }
}

// OUTPUT
// Sum is 1j2
// Sum is 7j3
// Sum is 7j23
