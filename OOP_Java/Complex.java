public class Complex {
    int real, imag;
    public Complex(){
        real = 1;
        imag = 2;
    }
    public Complex(int r){
        real = r;
        imag = 3;
    }
    public Complex(int r, int i){
        real = r;
        imag = i;
    }

    public void add(){
        System.out.println("Sum is "+ real+ "j" + imag);
    }

    public static void main(String[] args) {
        Complex A = new Complex();
        Complex B = new Complex(7);
        Complex C = new Complex(7, 23);

        A.add();
        B.add();
        C.add();
    }
}

// OUTPUT
// Sum is 1j2
// Sum is 7j3
// Sum is 7j23
