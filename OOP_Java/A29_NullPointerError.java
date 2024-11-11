//  WAP to show NullPointerError

public class A29_NullPointerError {
    public static void main(String[] args) {
        String a = null;
        try{
            System.out.println("The length of the string is :"+ a.length());
        }catch(NullPointerException e){
            System.out.println("The length can not be found for a null object");
        }
    }
}
// OUTPUT
// The length can not be found for a null object1