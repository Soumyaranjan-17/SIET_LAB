import java.util.Scanner;
class A14_Number_Task{
    public void palindrome(int n){
        int m = n;
        int rev = 0;
        while(m > 0){
            int R = m % 10;
            rev = (rev*10)+R;
            m = m / 10;
        }
        String Output = (rev == n)? "Palindrome\n" : "Not Palindrome";
        System.out.println(Output);
        // if (n == rev) {
        //     System.out.println("Palindrome");
        // }
        // else{
        //     System.out.println("Not Palindrome");
        // }
    }

    public void Is_Prime(int n){
        if(n < 1){
            System.out.println("!!Only for Positive value!!");
        }
        else if (n == 2 || n == 3) {
            System.out.println("Prime");
        }
        else {
            for(int i = 5; i <= n/2; i+=2){
                if (n % i == 0) {
                    System.err.println("Composite Number");
                    break;
                }
            }
            System.out.println("Prime");
        }
    }

    public void Fibbo(int n){
        int a = 0, b = 1, c, i= 2;
        System.out.print(a+  " ");
        System.out.print(b+  " ");
        do{
            c = a + b;
            System.out.print(c+ " ");
            a = b;
            b = c;
            i ++;
        }while(i < n);
    }

    public void Fact(int n){
        int ans = 1;
        for(int i = 1; i <= n; i++){
            ans *= i;
        }
        System.out.println("Factorial is: "+ ans);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a number to perform Operations: ");
        int n = sc.nextInt();
        A14_Number_Task N = new A14_Number_Task();
        N.palindrome(n);
        N.Is_Prime(n);
        N.Fibbo(n);
        N.Fact(n);
        
        
        
        
        sc.close();
    }
}

// OUTPUT
// Enter a number to perform Operations: 
// 11
// Palindrome
// 
// Prime
// 0 1 1 2 3 5 8 13 21 34 55 Factorial is: 39916800
