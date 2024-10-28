import java.util.Scanner;

// Define an interface for Rate with a fixed rate
interface Rate {
    double getRate();
}

// Define SimpleInterestCalculator interface
interface SimpleInterestCalculator {
    double calculateSimpleInterest();
}

// Calculate class demonstrating multiple inheritance
class Calculate implements Rate, SimpleInterestCalculator {
    private double principal;
    private double time;
    private final double RATE = 5.0;  // fixed rate for calculation

    public Calculate(double principal, double time) {
        this.principal = principal;
        this.time = time;
    }

    @Override
    public double getRate() {
        return RATE;
    }

    @Override
    public double calculateSimpleInterest() {
        return (principal * time * RATE) / 100;
    }
}

public class TestSI {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter Principal (P): ");
        double principal = sc.nextDouble();
        System.out.print("Enter Time (T in years): ");
        double time = sc.nextDouble();

        Calculate calc = new Calculate(principal, time);
        double simpleInterest = calc.calculateSimpleInterest();
        System.out.println("Simple Interest (SI): " + simpleInterest);

        sc.close();
    }
}
