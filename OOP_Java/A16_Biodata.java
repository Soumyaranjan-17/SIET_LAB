public class A16_Biodata {
    String name;
    int age;
    String branch;

    public A16_Biodata(String n, int a, String b){
        name = n;
        age = a;
        branch = b;
    }

    public void disaplay(){
        System.out.println("Name : " + name);
        System.out.println("Age : " + age);
        System.out.println("Branch : " + branch);
    }

    public static void main(String[] args) {
        A16_Biodata A = new A16_Biodata("SOUMYA", 19, "CSE");
        A16_Biodata B = new A16_Biodata("SATYA", 20, "CIVIL");

        A.disaplay();
        B.disaplay();
    }




}
