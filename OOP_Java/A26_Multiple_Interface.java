// WAP to implement multiple inheritance through interface

import java.util.Scanner;

// Define an interface for Rate with a fixed rate
interface Rate {
    double RATE = 3.7;
}

// Define SimpleInterestCalculator interface
interface SimpleInterest {
    double calculateSI();
}

// Calculate class demonstrating multiple inheritance
class Calculate implements Rate, SimpleInterest {
    public double principal;
    
    public double time;
    // public final double RATE = 5.0;  // fixed rate for calculation

    public Calculate(double principal, double time) {
        this.principal = principal;
        this.time = time;
    }

    public double calculateSI() {
        return (principal * time * RATE) / 100;
    }
}

public class A26_Multiple_Interface {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter Principal (P): ");
        double principal = sc.nextDouble();
        System.out.print("Enter Time (T in years): ");
        double time = sc.nextDouble();

        Calculate calc = new Calculate(principal, time);
        double simpleInterest = calc.calculateSI();
        System.out.println("Simple Interest (SI): " + simpleInterest);

        sc.close();
    }
}

// OUTPUT

// Enter Principal (P): 100
// Enter Time (T in years): 2
// Simple Interest (SI): 7.4