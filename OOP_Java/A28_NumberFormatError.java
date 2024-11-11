//  WAP to show NumberFormatError


public class A28_NumberFormatError {
    public static void main(String[] args) {
        String nm = "Soumya";
        try {
            int i = Integer.parseInt(nm);
            System.out.println(i);
        } catch (NumberFormatException e) {
            System.out.println("Cann't convert string to int");
        }
    }
}
// OUTPUT
// Cann't convert string to int