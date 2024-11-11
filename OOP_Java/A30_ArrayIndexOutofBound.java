//  WAP to show Array Index out of Bound Error


public class A30_ArrayIndexOutofBound {
    public static void main(String[] args) {
        int arr[] = {1,2,3,4,5,6,7,8,9,0};
        try {
           System.out.println(arr[11]); 
        } catch (Exception e) {
            System.out.println("Array Index Out of Bound");
        }
    }
}

// Array Index Out of Bound