import java.util.Scanner;

class A13_Bank {
    String customerName;
    long accountNo;
    long balance = 0; // Initialize balance to 0

    private static final Scanner sc = new Scanner(System.in); // Single Scanner instance

    // Method to create an account
    void create() {
        System.out.println("Enter the name:");
        customerName = sc.nextLine();
        System.out.println("Enter Account Number:");
        accountNo = sc.nextLong();
        // Clear the newline character left by nextLong()
        sc.nextLine(); 
    }

    // Method to deposit money into the account
    long deposit() {
        System.out.println("Enter deposit amount:");
        long depositAmount = sc.nextLong();
        balance += depositAmount;
        return balance;
    }

    // Method to withdraw money from the account
    void withdraw() {
        System.out.println("Enter withdraw amount:");
        long withdrawAmount = sc.nextLong();
        if (withdrawAmount <= balance) {
            balance -= withdrawAmount;
            System.out.println("Withdrawal successful. Current balance: " + balance);
        } else {
            System.out.println("Insufficient balance. Withdrawal failed.");
        }
    }

    // Method to display account details
    void display() {
        System.out.println("Customer Name: " + customerName);
        System.out.println("Account Number: " + accountNo);
        System.out.println("Balance: " + balance);
    }

    public static void main(String[] args) {
        A13_Bank obj = new A13_Bank();
        obj.create();
        obj.deposit();
        obj.withdraw();
        obj.display();
    }
}