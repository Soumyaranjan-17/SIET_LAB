class A extends Thread{
    public void run(){
        System.out.println("Task ! is running...");
    }
}

class B extends Thread{
    public void run(){
        System.out.println("Task 2 is running...");
    }
}

class C extends Thread{
    public void run(){
        System.out.println("Task 3 is running....");
    }
}

public class A33_thread {
    public static void main(String[] args) {
        A t1 = new A();
        B t2 = new B();
        C t3 = new C();

        t1.run();
        t2.run();
        t3.run();
    }
}

// OUTPUT

// Task ! is running...
// Task 2 is running...
// Task 3 is running....