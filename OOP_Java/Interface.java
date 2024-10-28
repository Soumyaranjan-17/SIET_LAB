import java.util.Scanner;

// Define the Rate interface
interface Rate {
    float getInterestRate();
}

// RBI class implementing Rate interface
class RBI implements Rate {
    @Override
    public float getInterestRate() {
        return 3.0f;
    }
}

// SBI class implementing Rate interface
class SBI implements Rate {
    @Override
    public float getInterestRate() {
        return 3.5f;
    }
}

// HDFC class implementing Rate interface
class HDFC implements Rate {
    @Override
    public float getInterestRate() {
        return 4.0f;
    }
}

public class Test {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter Bank Name (RBI/SBI/HDFC): ");
        String bankName = sc.nextLine().toUpperCase();

        Rate bank;
        switch (bankName) {
            case "RBI":
                bank = new RBI();
                break;
            case "SBI":
                bank = new SBI();
                break;
            case "HDFC":
                bank = new HDFC();
                break;
            default:
                System.out.println("Invalid Bank Name!");
                sc.close();
                return;
        }

        System.out.println("Interest Rate of " + bankName + ": " + bank.getInterestRate() + "%");
        sc.close();
    }
}
