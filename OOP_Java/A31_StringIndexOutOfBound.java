//  WAP to show String Index out of Bound Exception


public class A31_StringIndexOutOfBound {
    public static void main(String[] args) {
        String nm = "Alex";
        try {
            System.out.println(nm.charAt(4));       
        } catch (Exception e) {
            System.out.println(e);
        }
    }
}
// OUTPUT
// java.lang.StringIndexOutOfBoundsException: String index out of range: 4